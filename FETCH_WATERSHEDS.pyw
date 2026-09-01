from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import tempfile
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

SOURCE_URL = "https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nhn_rhn/index/nhn_index_geobase.kmz"
SOURCE_TITLE = "Natural Resources Canada — National Hydro Network (NHN) Work Unit Limits"
LICENCE = "Open Government Licence - Canada"
DEFAULT_BBOX = (-83.0, 50.5, -52.5, 65.5)  # Northern Quebec + Labrador fallback


def repo_root() -> Path:
    return Path(__file__).resolve().parent


def output_paths(root: Path) -> tuple[Path, Path]:
    directory = root / "apps" / "web" / "public" / "data" / "watersheds"
    directory.mkdir(parents=True, exist_ok=True)
    return directory / "nhn_workunit_limits.geojson", directory / "manifest.json"


def community_bbox(root: Path) -> tuple[float, float, float, float] | None:
    path = root / "data" / "publish" / "current" / "communities_public.geojson"
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        coords: list[tuple[float, float]] = []
        for feature in payload.get("features", []):
            geometry = feature.get("geometry") or {}
            if geometry.get("type") != "Point":
                continue
            values = geometry.get("coordinates") or []
            if len(values) >= 2:
                coords.append((float(values[0]), float(values[1])))
        if not coords:
            return None
        xs = [p[0] for p in coords]
        ys = [p[1] for p in coords]
        # Broad enough to include upstream drainage divides around current communities.
        return (min(xs) - 4.0, min(ys) - 2.5, max(xs) + 4.0, max(ys) + 2.5)
    except Exception:
        return None


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "KristalFarms-WatershedFetcher/1.0 (+local research tooling)",
            "Accept": "application/vnd.google-earth.kmz,application/zip,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as handle:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            handle.write(chunk)


def text_of(node: ET.Element | None) -> str | None:
    if node is None or node.text is None:
        return None
    value = node.text.strip()
    return value or None


def sanitize_key(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_]+", "_", value.strip()).strip("_").lower()
    return value[:64] or "field"


def extract_properties(placemark: ET.Element) -> dict[str, str]:
    props: dict[str, str] = {}
    name = text_of(placemark.find("./{*}name"))
    if name:
        props["name"] = name

    for data in placemark.findall(".//{*}ExtendedData/{*}Data"):
        raw_name = data.attrib.get("name") or "field"
        value = text_of(data.find("./{*}value"))
        if value:
            props[sanitize_key(raw_name)] = value

    for data in placemark.findall(".//{*}ExtendedData//{*}SimpleData"):
        raw_name = data.attrib.get("name") or "field"
        value = text_of(data)
        if value:
            props[sanitize_key(raw_name)] = value

    # Keep the output compact and predictable. Prefer identifiers/name-like fields.
    priority = []
    for key in props:
        lower = key.lower()
        score = 0
        if key == "name":
            score = 100
        elif any(token in lower for token in ("dataset", "workunit", "work_unit", "drain", "basin", "name", "id", "code")):
            score = 50
        priority.append((score, key))
    priority.sort(reverse=True)
    compact: dict[str, str] = {}
    for _, key in priority[:12]:
        compact[key] = props[key]
    compact["source"] = "NRCan NHN work-unit index"
    compact["boundary_role"] = "sub_sub_drainage_context"
    return compact


def parse_coordinate_text(raw: str | None) -> list[list[float]]:
    if not raw:
        return []
    points: list[list[float]] = []
    for token in raw.replace("\n", " ").replace("\t", " ").split():
        parts = token.split(",")
        if len(parts) < 2:
            continue
        try:
            lon = float(parts[0])
            lat = float(parts[1])
        except ValueError:
            continue
        if math.isfinite(lon) and math.isfinite(lat):
            points.append([lon, lat])
    return points


def perpendicular_distance(point: list[float], start: list[float], end: list[float]) -> float:
    x, y = point
    x1, y1 = start
    x2, y2 = end
    if x1 == x2 and y1 == y2:
        return math.hypot(x - x1, y - y1)
    dx = x2 - x1
    dy = y2 - y1
    t = ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    px = x1 + t * dx
    py = y1 + t * dy
    return math.hypot(x - px, y - py)


def douglas_peucker(points: list[list[float]], tolerance: float) -> list[list[float]]:
    if len(points) <= 2:
        return points
    max_distance = -1.0
    index = 0
    start = points[0]
    end = points[-1]
    for i in range(1, len(points) - 1):
        distance = perpendicular_distance(points[i], start, end)
        if distance > max_distance:
            index = i
            max_distance = distance
    if max_distance > tolerance:
        left = douglas_peucker(points[: index + 1], tolerance)
        right = douglas_peucker(points[index:], tolerance)
        return left[:-1] + right
    return [start, end]


def simplify_ring(ring: list[list[float]], tolerance: float) -> list[list[float]]:
    if len(ring) < 5 or tolerance <= 0:
        return ring
    closed = ring[0] == ring[-1]
    core = ring[:-1] if closed else ring[:]
    if len(core) < 4:
        return ring
    # Rotate so simplification does not use identical first/last endpoints.
    pivot = max(range(len(core)), key=lambda i: core[i][0] + core[i][1] * 1e-4)
    rotated = core[pivot:] + core[:pivot] + [core[pivot]]
    simplified = douglas_peucker(rotated, tolerance)
    if len(simplified) < 4:
        return ring
    if simplified[0] != simplified[-1]:
        simplified.append(simplified[0])
    return simplified


def ring_bbox(ring: list[list[float]]) -> tuple[float, float, float, float] | None:
    if not ring:
        return None
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return (min(xs), min(ys), max(xs), max(ys))


def intersects(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])


def polygon_from_node(polygon: ET.Element, tolerance: float) -> list[list[list[float]]] | None:
    outer_node = polygon.find("./{*}outerBoundaryIs/{*}LinearRing/{*}coordinates")
    outer = simplify_ring(parse_coordinate_text(text_of(outer_node)), tolerance)
    if len(outer) < 4:
        return None
    rings: list[list[list[float]]] = [outer]
    for inner_node in polygon.findall("./{*}innerBoundaryIs/{*}LinearRing/{*}coordinates"):
        inner = simplify_ring(parse_coordinate_text(text_of(inner_node)), tolerance)
        if len(inner) >= 4:
            rings.append(inner)
    return rings


def find_kml(kmz_path: Path, workdir: Path) -> Path:
    with zipfile.ZipFile(kmz_path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".kml")]
        if not names:
            raise RuntimeError("The NRCan KMZ did not contain a KML document.")
        preferred = next((name for name in names if Path(name).name.lower() == "doc.kml"), names[0])
        target = workdir / "source.kml"
        target.write_bytes(archive.read(preferred))
        return target


def convert_kml(kml_path: Path, bbox: tuple[float, float, float, float] | None, tolerance: float) -> dict:
    tree = ET.parse(kml_path)
    root = tree.getroot()
    features: list[dict] = []

    for placemark in root.findall(".//{*}Placemark"):
        polygons: list[list[list[list[float]]]] = []
        for polygon in placemark.findall(".//{*}Polygon"):
            rings = polygon_from_node(polygon, tolerance)
            if not rings:
                continue
            bounds = ring_bbox(rings[0])
            if bbox is not None and bounds is not None and not intersects(bounds, bbox):
                continue
            polygons.append(rings)
        if not polygons:
            continue

        geometry: dict
        if len(polygons) == 1:
            geometry = {"type": "Polygon", "coordinates": polygons[0]}
        else:
            geometry = {"type": "MultiPolygon", "coordinates": polygons}
        features.append(
            {
                "type": "Feature",
                "properties": extract_properties(placemark),
                "geometry": geometry,
            }
        )

    if not features:
        raise RuntimeError(
            "No watershed/work-unit polygons were found in the NRCan KML for the selected coverage. "
            "The source format may have changed."
        )

    return {
        "type": "FeatureCollection",
        "name": "NRCan NHN work-unit / sub-sub-drainage boundaries",
        "features": features,
    }


def run(args: argparse.Namespace) -> tuple[Path, int, tuple[float, float, float, float] | None]:
    root = repo_root()
    geojson_path, manifest_path = output_paths(root)

    if args.all_canada:
        bbox = None
        coverage_label = "Canada"
        tolerance = 0.004 if args.tolerance is None else args.tolerance
    else:
        bbox = community_bbox(root) or DEFAULT_BBOX
        coverage_label = "Northern Atlas community envelope"
        tolerance = 0.002 if args.tolerance is None else args.tolerance

    with tempfile.TemporaryDirectory(prefix="kristal-watersheds-") as temp:
        tempdir = Path(temp)
        kmz_path = tempdir / "nhn_index_geobase.kmz"
        download(SOURCE_URL, kmz_path)
        kml_path = find_kml(kmz_path, tempdir)
        payload = convert_kml(kml_path, bbox, tolerance)

    temp_geojson = geojson_path.with_suffix(".geojson.tmp")
    temp_geojson.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    os.replace(temp_geojson, geojson_path)

    manifest = {
        "schema": "kristal-watershed-boundaries/v1",
        "status": "ready",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": SOURCE_TITLE,
        "source_url": SOURCE_URL,
        "licence": LICENCE,
        "coverage": coverage_label,
        "bbox": list(bbox) if bbox else None,
        "feature_count": len(payload["features"]),
        "simplification_tolerance_degrees": tolerance,
        "file": "/data/watersheds/nhn_workunit_limits.geojson",
        "note": (
            "NHN work-unit limits were created based on Water Survey of Canada sub-sub-drainage areas. "
            "They are contextual drainage divides, not exact upstream catchments for individual Kristal sites."
        ),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return geojson_path, len(payload["features"]), bbox


def show_message(title: str, message: str, error: bool = False) -> None:
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        if error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)
        root.destroy()
    except Exception:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(add_help=True)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all-canada", action="store_true", help="Keep all Canadian NHN work-unit boundaries.")
    group.add_argument("--northern-atlas", action="store_true", help="Use the current community envelope (default).")
    parser.add_argument("--tolerance", type=float, default=None, help="GeoJSON simplification tolerance in degrees.")
    parser.add_argument("--silent", action="store_true", help="Do not show a GUI completion dialog.")
    args = parser.parse_args()

    try:
        path, count, bbox = run(args)
        message = f"Watershed boundaries ready.\n\n{count} polygon feature(s)\n{path}"
        if bbox:
            message += f"\n\nCoverage bbox: {bbox}"
        if not args.silent:
            show_message("Kristal Watersheds", message)
        return 0
    except Exception as exc:
        if not args.silent:
            show_message("Kristal Watersheds — error", str(exc), error=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
