#!/usr/bin/env python3
"""Build a static local satellite tile pyramid for Kristal Observatory.

This script NEVER downloads imagery. It consumes a GeoTIFF already reviewed
and placed under repository control, then creates XYZ PNG tiles served by
Next.js from apps/web/public/imagery/.

Requirements:
- GDAL command-line tools available on PATH:
    gdal2tiles.py (or gdal2tiles)
    gdalinfo
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[2]
PUBLIC_IMAGERY = ROOT / "apps" / "web" / "public" / "imagery"
PUBLISH_MANIFEST = ROOT / "data" / "publish" / "imagery" / "current" / "imagery_manifest.json"


def command(*names: str) -> str:
    for name in names:
        resolved = shutil.which(name)
        if resolved:
            return resolved
    raise SystemExit(
        "Missing GDAL tooling. Install GDAL/OSGeo4W and ensure "
        f"{', '.join(names)} is available on PATH."
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def wgs84_bounds(gdalinfo: str, source: Path) -> list[float] | None:
    result = subprocess.run(
        [gdalinfo, "-json", str(source)],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    extent = payload.get("wgs84Extent")
    if not extent or not extent.get("coordinates"):
        return None

    points = extent["coordinates"][0]
    xs = [float(point[0]) for point in points]
    ys = [float(point[1]) for point in points]
    return [min(xs), min(ys), max(xs), max(ys)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Georeferenced source GeoTIFF")
    parser.add_argument("--id", default="local-satellite", help="Published tile directory id")
    parser.add_argument("--title", default="Local satellite imagery")
    parser.add_argument("--source-label", default="Locally archived satellite snapshot")
    parser.add_argument("--acquired", default=None, help="Acquisition/mosaic date or period")
    parser.add_argument("--license", default=None, help="Reviewed imagery license identifier")
    parser.add_argument("--attribution", default=None, help="Required display attribution")
    parser.add_argument("--minzoom", type=int, default=7)
    parser.add_argument("--maxzoom", type=int, default=13)
    parser.add_argument("--processes", type=int, default=max(1, min(8, os.cpu_count() or 1)))
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve()
    if not source.is_file():
        raise SystemExit(f"Source file not found: {source}")
    if args.minzoom < 0 or args.maxzoom < args.minzoom:
        raise SystemExit("Invalid zoom range.")

    safe_id = "".join(char for char in args.id.lower() if char.isalnum() or char in "-_")
    if not safe_id or safe_id != args.id:
        raise SystemExit("--id may contain only lowercase letters, digits, '-' and '_'.")

    gdal2tiles = command("gdal2tiles.py", "gdal2tiles")
    gdalinfo = command("gdalinfo")

    output = PUBLIC_IMAGERY / safe_id
    if output.exists():
        if not args.replace:
            raise SystemExit(f"{output} already exists. Use --replace to rebuild it.")
        shutil.rmtree(output)

    output.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            gdal2tiles,
            "--xyz",
            "--webviewer=none",
            "--processes",
            str(args.processes),
            "--zoom",
            f"{args.minzoom}-{args.maxzoom}",
            str(source),
            str(output),
        ],
        check=True,
    )

    bounds = wgs84_bounds(gdalinfo, source)
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

    manifest = {
        "schema": "kristal-local-imagery/v1",
        "id": safe_id,
        "title": args.title,
        "available": True,
        "tile_template": f"/imagery/{safe_id}/{{z}}/{{x}}/{{y}}.png",
        "tile_size": 256,
        "minzoom": args.minzoom,
        "maxzoom": args.maxzoom,
        "bounds": bounds,
        "source": args.source_label,
        "acquired": args.acquired,
        "license": args.license,
        "attribution": args.attribution or args.source_label,
        "source_sha256": sha256_file(source),
        "generated_at": generated_at,
    }

    public_manifest = PUBLIC_IMAGERY / "local-satellite.json"
    public_manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    PUBLISH_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    PUBLISH_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"Published {safe_id} -> {output}")
    print(f"Manifest -> {public_manifest}")
    print(f"Release manifest copy -> {PUBLISH_MANIFEST}")
    if bounds:
        print(f"Bounds: {bounds}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
