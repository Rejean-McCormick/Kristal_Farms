#!/usr/bin/env python3
"""Publish the lightweight Northern Atlas electrical grid-reach context.

The source research records document connectivity and voltage. The geometry in this
public artifact is explicitly schematic: straight/piecewise connections between named
anchors, not surveyed conductor/right-of-way geometry. This keeps the web layer tiny
and prevents contextual power infrastructure from becoming an engineering claim.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def _trim_point_toward(point: list[float], neighbor: list[float], gap_degrees: float) -> list[float]:
    dx = neighbor[0] - point[0]
    dy = neighbor[1] - point[1]
    distance = (dx * dx + dy * dy) ** 0.5
    if distance <= 0:
        return list(point)
    # Keep the gap visually useful without removing a material share of short schematic links.
    fraction = min(gap_degrees / distance, 0.12)
    return [point[0] + dx * fraction, point[1] + dy * fraction]


def _trim_terminal_gaps(coordinates: list[list[float]], terminal_coordinates: set[tuple[float, float]], gap_degrees: float) -> list[list[float]]:
    trimmed = [list(point) for point in coordinates]
    if len(trimmed) < 2:
        return trimmed
    if tuple(trimmed[0]) in terminal_coordinates:
        trimmed[0] = _trim_point_toward(trimmed[0], trimmed[1], gap_degrees)
    if tuple(trimmed[-1]) in terminal_coordinates:
        trimmed[-1] = _trim_point_toward(trimmed[-1], trimmed[-2], gap_degrees)
    return trimmed


def build(repo_root: Path) -> dict:
    source_path = repo_root / "research/grid/cote_nord_grid_reach.yaml"
    raw = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    anchors = raw["anchors"]
    source_by_id = {item["id"]: item for item in raw["sources"]}
    terminal_coordinates = {tuple(anchors[item["anchor_id"]]["coordinates"]) for item in raw["reach_markers"]}
    gap_degrees = float(raw["map_policy"].get("terminal_gap_degrees", 0.18))

    features = []
    for item in raw["connections"]:
        coordinates = [anchors[anchor_id]["coordinates"] for anchor_id in item["anchor_ids"]]
        coordinates = _trim_terminal_gaps(coordinates, terminal_coordinates, gap_degrees)
        features.append({
            "type": "Feature",
            "id": item["id"],
            "geometry": {"type": "LineString", "coordinates": coordinates},
            "properties": {
                "feature_role": "grid_connection",
                "name": item["name"],
                "voltage_kv": item["voltage_kv"],
                "design_voltage_kv": item.get("design_voltage_kv"),
                "voltage_class": item["voltage_class"],
                "status": item["status"],
                "endpoint_semantics": item["endpoint_semantics"],
                "geometry_role": "schematic_connectivity_not_engineering_geometry",
                "measurement_allowed": False,
                "source_ids": item["source_ids"],
                "display_terminal_gap": True,
                "note": item["note"],
            },
        })

    for item in raw["reach_markers"]:
        anchor = anchors[item["anchor_id"]]
        features.append({
            "type": "Feature",
            "id": item["id"],
            "geometry": {"type": "Point", "coordinates": anchor["coordinates"]},
            "properties": {
                "feature_role": "reach_marker",
                "name": item["label"],
                "detail": item["detail"],
                "anchor_name": anchor["name"],
                "geometry_precision": anchor["geometry_precision"],
                "geometry_role": "reach_reference_not_grid_terminal_survey",
                "terminal_kind": item.get("terminal_kind", "transmission_end"),
                "voltage_kv": item.get("voltage_kv"),
                "measurement_allowed": False,
                "source_ids": item["source_ids"],
            },
        })

    return {
        "type": "FeatureCollection",
        "schema": "kristal-grid-reach/v1",
        "version": raw["version"],
        "status": raw["status"],
        "ranking_allowed": False,
        "default_visible": bool(raw["map_policy"]["default_visible"]),
        "measurement_allowed": False,
        "local_distribution_network_included": False,
        "title": "Northern Atlas electrical grid reach",
        "note": raw["map_policy"]["note"],
        "sources": [
            {
                "id": sid,
                "publisher": src["publisher"],
                "title": src["title"],
                "url": src["url"],
                "reference_date": src.get("reference_date"),
            }
            for sid, src in source_by_id.items()
        ],
        "features": features,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    output = args.output or repo_root / "data/publish/current/grid_reach_public.geojson"
    payload = build(repo_root)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(serialized, encoding="utf-8")
    print(f"Wrote {output} ({len(payload['features'])} features)")

    # Normal repo rebuilds also keep the static Web asset synchronized.
    # Explicit --output calls (e.g. reproducibility tests) do not mutate the app tree.
    if args.output is None:
        static_output = repo_root / "apps/web/public/grid/grid-reach.geojson"
        static_output.parent.mkdir(parents=True, exist_ok=True)
        static_output.write_text(serialized, encoding="utf-8")
        print(f"Wrote {static_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
