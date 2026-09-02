#!/usr/bin/env python3
"""Publish the lightweight Northern Atlas electrical-network context.

The research layer documents real electrical assets and source-backed connectivity.
Public geometry remains explicitly schematic: straight/piecewise connections between
named anchors, not surveyed conductor/right-of-way geometry. Node coordinates are
named-facility or area anchors and are not engineering interconnection points.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def _load_yaml(repo_root: Path, relative_path: str) -> dict:
    path = repo_root / relative_path
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _format_capacity(value: float | int) -> str:
    numeric = float(value)
    if numeric.is_integer():
        return f"{int(numeric):,}"
    return f"{numeric:g}"


def _node_label(item: dict) -> str:
    name = item["name"]
    if item.get("installed_capacity_mw") is not None:
        return f"{name} · {_format_capacity(item['installed_capacity_mw'])} MW"
    available = item.get("available_capacity")
    if isinstance(available, dict) and available.get("value_mw") is not None:
        operator = available.get("operator", "")
        return f"{name} · {operator}{_format_capacity(available['value_mw'])} MW available"
    if item.get("voltage_kv") is not None:
        return f"{name} · {item['voltage_kv']:g} kV"
    return name


def build(repo_root: Path) -> dict:
    network = _load_yaml(repo_root, "research/grid/cote_nord_grid_reach.yaml")
    source_registry = _load_yaml(repo_root, network["source_registry"])
    asset_registry = _load_yaml(repo_root, network["asset_registry"])

    anchors = asset_registry["anchors"]
    source_by_id = {item["id"]: item for item in source_registry["sources"]}

    features: list[dict] = []
    for item in network["connections"]:
        coordinates = [anchors[anchor_id]["coordinates"] for anchor_id in item["anchor_ids"]]
        features.append({
            "type": "Feature",
            "id": item["id"],
            "geometry": {"type": "LineString", "coordinates": coordinates},
            "properties": {
                "feature_role": "grid_connection",
                "name": item["name"],
                "voltage_kv": item.get("voltage_kv"),
                "design_voltage_kv": item.get("design_voltage_kv"),
                "voltage_class": item["voltage_class"],
                "network_mode": item.get("network_mode", "integrated"),
                "status": item["status"],
                "circuit_count": item.get("circuit_count"),
                "endpoint_semantics": item["endpoint_semantics"],
                "geometry_role": "schematic_connectivity_not_engineering_geometry",
                "measurement_allowed": False,
                "source_ids": item["source_ids"],
                "note": item["note"],
            },
        })

    for item in asset_registry["grid_nodes"]:
        anchor = anchors[item["anchor_id"]]
        features.append({
            "type": "Feature",
            "id": item["id"],
            "geometry": {"type": "Point", "coordinates": anchor["coordinates"]},
            "properties": {
                "feature_role": "grid_node",
                "name": item["name"],
                "display_label": _node_label(item),
                "node_kind": item["node_kind"],
                "network_mode": item["network_mode"],
                "installed_capacity_mw": item.get("installed_capacity_mw"),
                "backup_capacity_mw": item.get("backup_capacity_mw"),
                "available_capacity": item.get("available_capacity"),
                "voltage_kv": item.get("voltage_kv"),
                "design_voltage_kv": item.get("design_voltage_kv"),
                "secondary_voltage_kv": item.get("secondary_voltage_kv"),
                "anchor_name": anchor["name"],
                "geometry_precision": anchor["geometry_precision"],
                "geometry_role": "named_asset_or_area_anchor_not_engineering_geometry",
                "measurement_allowed": False,
                "source_ids": item["source_ids"],
            },
        })

    referenced_source_ids = {
        source_id
        for feature in features
        for source_id in feature["properties"].get("source_ids", [])
    }
    unknown_source_ids = sorted(referenced_source_ids.difference(source_by_id))
    if unknown_source_ids:
        raise ValueError(f"Unknown electrical source ids: {unknown_source_ids}")

    return {
        "type": "FeatureCollection",
        "schema": "kristal-grid-reach/v1",
        "version": network["version"],
        "status": network["status"],
        "ranking_allowed": False,
        "default_visible": bool(network["map_policy"]["default_visible"]),
        "measurement_allowed": False,
        "local_distribution_network_included": False,
        "title": "Northern Atlas electrical network context",
        "note": network["map_policy"]["note"],
        "sources": [
            {
                "id": source_id,
                "publisher": source_by_id[source_id]["publisher"],
                "title": source_by_id[source_id]["title"],
                "url": source_by_id[source_id]["url"],
                "reference_date": source_by_id[source_id].get("reference_date"),
            }
            for source_id in sorted(referenced_source_ids)
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
