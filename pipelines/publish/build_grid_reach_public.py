#!/usr/bin/env python3
"""Publish the lightweight Côte-Nord electrical grid-reach context.

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


def build(repo_root: Path) -> dict:
    source_path = repo_root / "research/grid/cote_nord_grid_reach.yaml"
    raw = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    anchors = raw["anchors"]
    source_by_id = {item["id"]: item for item in raw["sources"]}

    features = []
    for item in raw["connections"]:
        coordinates = [anchors[anchor_id]["coordinates"] for anchor_id in item["anchor_ids"]]
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
        "title": "Côte-Nord electrical grid reach",
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
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {output} ({len(payload['features'])} features)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
