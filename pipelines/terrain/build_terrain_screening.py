#!/usr/bin/env python3
"""Build local HRDEM-derived terrain screening cells for Observatory.

The output supports two map views:
1. hypsometric relief from DTM elevation;
2. terrain-connected potential-basin depth for an exploratory water-level rise.

This is screening geometry only. Hydro reference points may be proxies and are
not engineered dam locations. No hydraulic head or reservoir design is inferred.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import rasterio
from pyproj import CRS, Transformer
from rasterio.enums import Resampling
from rasterio.transform import rowcol, xy
from rasterio.windows import Window, from_bounds


def clamp_window(window: Window, width: int, height: int) -> Window:
    col0 = max(0, int(math.floor(window.col_off)))
    row0 = max(0, int(math.floor(window.row_off)))
    col1 = min(width, int(math.ceil(window.col_off + window.width)))
    row1 = min(height, int(math.ceil(window.row_off + window.height)))
    return Window(col0, row0, max(0, col1 - col0), max(0, row1 - row0))


def nearest_valid_cell(mask: np.ndarray, row: int, col: int, max_radius: int = 8) -> tuple[int, int] | None:
    h, w = mask.shape
    if 0 <= row < h and 0 <= col < w and mask[row, col]:
        return row, col
    for radius in range(1, max_radius + 1):
        r0, r1 = max(0, row - radius), min(h - 1, row + radius)
        c0, c1 = max(0, col - radius), min(w - 1, col + radius)
        candidates: list[tuple[float, int, int]] = []
        for rr in range(r0, r1 + 1):
            for cc in range(c0, c1 + 1):
                if mask[rr, cc]:
                    candidates.append(((rr - row) ** 2 + (cc - col) ** 2, rr, cc))
        if candidates:
            _, rr, cc = min(candidates)
            return rr, cc
    return None


def minimax_spill(elevation: np.ndarray, valid: np.ndarray, seed: tuple[int, int], max_level: float) -> np.ndarray:
    """Minimum terrain level needed to connect each cell to the seed.

    For a path P, its required level is max(elevation(cell) for cell in P).
    We minimize that maximum using a Dijkstra-style minimax pass.
    """
    h, w = elevation.shape
    inf = np.float64(np.inf)
    spill = np.full((h, w), inf, dtype=np.float64)
    sr, sc = seed
    spill[sr, sc] = float(elevation[sr, sc])
    heap: list[tuple[float, int, int]] = [(spill[sr, sc], sr, sc)]
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while heap:
        cost, r, c = heapq.heappop(heap)
        if cost != spill[r, c]:
            continue
        if cost > max_level:
            continue
        for dr, dc in neighbors:
            rr, cc = r + dr, c + dc
            if rr < 0 or rr >= h or cc < 0 or cc >= w or not valid[rr, cc]:
                continue
            next_cost = max(cost, float(elevation[rr, cc]))
            if next_cost <= max_level and next_cost < spill[rr, cc]:
                spill[rr, cc] = next_cost
                heapq.heappush(heap, (next_cost, rr, cc))
    return spill


def cell_polygon_wgs84(transform, r: int, c: int, to_wgs84: Transformer) -> list[list[float]]:
    x0, y0 = xy(transform, r, c, offset="ul")
    x1, y1 = xy(transform, r, c, offset="lr")
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
    return [[float(lon), float(lat)] for lon, lat in (to_wgs84.transform(x, y) for x, y in corners)]


def build_site(
    src: rasterio.io.DatasetReader,
    site: dict[str, Any],
    radius_m: float,
    cell_size_m: float,
    max_rise_m: float,
    rise_step_m: float,
) -> tuple[list[dict[str, Any]], dict[str, Any], list[float]] | None:
    lon, lat = map(float, site["coordinates"])
    to_src = Transformer.from_crs("EPSG:4326", src.crs, always_xy=True)
    to_wgs84 = Transformer.from_crs(src.crs, "EPSG:4326", always_xy=True)
    x, y = to_src.transform(lon, lat)

    raw_window = from_bounds(x - radius_m, y - radius_m, x + radius_m, y + radius_m, src.transform)
    window = clamp_window(raw_window, src.width, src.height)
    if window.width <= 1 or window.height <= 1:
        return None

    target_w = max(2, int(math.ceil((window.width * abs(src.transform.a)) / cell_size_m)))
    target_h = max(2, int(math.ceil((window.height * abs(src.transform.e)) / cell_size_m)))
    target_w = min(target_w, 300)
    target_h = min(target_h, 300)

    band = src.read(
        1,
        window=window,
        out_shape=(target_h, target_w),
        masked=True,
        resampling=Resampling.average,
    )
    valid = ~np.ma.getmaskarray(band)
    elevation = np.asarray(band.filled(np.nan), dtype=np.float64)
    valid &= np.isfinite(elevation)
    if not valid.any():
        return None

    base_transform = rasterio.windows.transform(window, src.transform)
    scale_x = window.width / target_w
    scale_y = window.height / target_h
    transform = base_transform * rasterio.Affine.scale(scale_x, scale_y)

    seed_r, seed_c = rowcol(transform, x, y)
    seed = nearest_valid_cell(valid, int(seed_r), int(seed_c))
    if seed is None:
        return None
    seed_elev = float(elevation[seed])
    spill = minimax_spill(elevation, valid, seed, seed_elev + max_rise_m)

    reachable = valid & np.isfinite(spill) & (spill <= seed_elev + max_rise_m)
    rows, cols = np.where(reachable)
    if not len(rows):
        return None

    features: list[dict[str, Any]] = []
    bounds = [180.0, 90.0, -180.0, -90.0]
    for r, c in zip(rows.tolist(), cols.tolist()):
        elev = float(elevation[r, c])
        spill_elev = float(spill[r, c])
        polygon = cell_polygon_wgs84(transform, r, c, to_wgs84)
        for px, py in polygon:
            bounds[0] = min(bounds[0], px)
            bounds[1] = min(bounds[1], py)
            bounds[2] = max(bounds[2], px)
            bounds[3] = max(bounds[3], py)
        features.append(
            {
                "type": "Feature",
                "properties": {
                    "site_id": str(site["id"]),
                    "site_name": str(site.get("name") or site["id"]),
                    "screening_scope": str(site.get("screening_scope") or "unknown"),
                    "elevation_m": round(elev, 2),
                    "seed_elevation_m": round(seed_elev, 2),
                    "relative_elevation_m": round(elev - seed_elev, 2),
                    "spill_elevation_m": round(spill_elev, 2),
                    "spill_rise_m": round(max(0.0, spill_elev - seed_elev), 2),
                },
                "geometry": {"type": "Polygon", "coordinates": [polygon]},
            }
        )

    cell_area_m2 = abs(transform.a * transform.e)
    rel = elevation - seed_elev
    spill_rise = spill - seed_elev
    summaries: list[dict[str, Any]] = []
    rise = 0.0
    while rise <= max_rise_m + 1e-9:
        wet = reachable & (spill_rise <= rise) & (rel <= rise)
        depth = np.where(wet, np.maximum(0.0, rise - rel), 0.0)
        summaries.append(
            {
                "rise_m": int(round(rise)),
                "area_km2": round(float(wet.sum() * cell_area_m2 / 1_000_000.0), 3),
                "volume_m3": round(float(depth.sum() * cell_area_m2), 0),
                "max_depth_m": round(float(depth.max()) if wet.any() else 0.0, 1),
            }
        )
        rise += rise_step_m

    default_rise = min(50.0, max_rise_m)
    default_rise = round(default_rise / rise_step_m) * rise_step_m
    profile = {
        "site_id": str(site["id"]),
        "site_name": str(site.get("name") or site["id"]),
        "seed_elevation_m": round(seed_elev, 2),
        "min_rise_m": 0,
        "max_rise_m": int(round(max_rise_m)),
        "default_rise_m": int(round(default_rise)),
        "feature_count": len(features),
        "rise_summaries": summaries,
    }
    return features, profile, bounds


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dtm", required=True, help="Local HRDEM DTM GeoTIFF/mosaic")
    parser.add_argument("--hydro-scope", required=True, help="Published hydro screening scope JSON")
    parser.add_argument("--public-dir", required=True, help="apps/web/public/terrain")
    parser.add_argument("--radius-km", type=float, default=25.0)
    parser.add_argument("--cell-size-m", type=float, default=500.0)
    parser.add_argument("--max-rise-m", type=float, default=150.0)
    parser.add_argument("--rise-step-m", type=float, default=5.0)
    parser.add_argument("--minzoom", type=int, default=5)
    parser.add_argument("--maxzoom", type=int, default=13)
    args = parser.parse_args()

    if args.radius_km <= 0 or args.cell_size_m <= 0 or args.max_rise_m <= 0 or args.rise_step_m <= 0:
        raise SystemExit("radius, cell size, max rise and rise step must be positive")

    dtm_path = Path(args.dtm)
    scope_path = Path(args.hydro_scope)
    public_dir = Path(args.public_dir)
    public_dir.mkdir(parents=True, exist_ok=True)

    scope = json.loads(scope_path.read_text(encoding="utf-8"))
    sites = [*(scope.get("sites") or []), *(scope.get("review_sites") or [])]
    if not sites:
        raise SystemExit("No sites/review_sites found in hydro scope")

    features: list[dict[str, Any]] = []
    profiles: list[dict[str, Any]] = []
    overall_bounds = [180.0, 90.0, -180.0, -90.0]

    with rasterio.open(dtm_path) as src:
        if src.crs is None or CRS(src.crs).is_geographic:
            raise SystemExit("Terrain build requires a projected metre-based DTM CRS")
        for site in sites:
            result = build_site(
                src,
                site,
                radius_m=args.radius_km * 1000.0,
                cell_size_m=args.cell_size_m,
                max_rise_m=args.max_rise_m,
                rise_step_m=args.rise_step_m,
            )
            if result is None:
                continue
            site_features, profile, bounds = result
            features.extend(site_features)
            profiles.append(profile)
            overall_bounds[0] = min(overall_bounds[0], bounds[0])
            overall_bounds[1] = min(overall_bounds[1], bounds[1])
            overall_bounds[2] = max(overall_bounds[2], bounds[2])
            overall_bounds[3] = max(overall_bounds[3], bounds[3])

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    geojson_path = public_dir / "terrain-screening.geojson"
    manifest_path = public_dir / "terrain-manifest.json"

    geojson_path.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": features,
                "metadata": {
                    "schema": "kristal-terrain-screening/v1",
                    "generated_at": generated_at,
                    "cell_size_m": args.cell_size_m,
                    "radius_km": args.radius_km,
                    "max_rise_m": args.max_rise_m,
                    "source": "Natural Resources Canada HRDEM DTM",
                    "vertical_datum": "CGVD2013",
                    "screening_only": True,
                },
            },
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )

    available = bool(features and profiles)
    manifest = {
        "schema": "kristal-local-terrain/v1",
        "id": "hrdem-terrain-screening",
        "title": "HRDEM terrain relief",
        "available": available,
        "geojson_url": "/terrain/terrain-screening.geojson",
        "minzoom": args.minzoom,
        "maxzoom": args.maxzoom,
        "bounds": overall_bounds if available else None,
        "source": "Natural Resources Canada HRDEM DTM",
        "vertical_datum": "CGVD2013",
        "cell_size_m": args.cell_size_m,
        "generated_at": generated_at,
        "note": "Terrain-connected screening only; hydro reference seeds may be proxies and are not engineered dam locations.",
        "site_profiles": profiles,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"published {len(features)} terrain cells for {len(profiles)} hydro references")
    print(f"geojson:  {geojson_path}")
    print(f"manifest: {manifest_path}")


if __name__ == "__main__":
    main()
