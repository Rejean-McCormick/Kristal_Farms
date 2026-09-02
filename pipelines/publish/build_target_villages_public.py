#!/usr/bin/env python3
"""Publish governed target-village dossiers for read-only product use.

Research YAML remains outside the product runtime. This promotion step joins target-village
research with already governed community infrastructure/context artifacts and publishes a
single read-only portfolio for the Villages workspace and full-page village dossiers.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

import yaml

SCHEMA = "kristal-target-villages/v1"
RESEARCH_SCHEMA = "kristal-target-village-research/v1"
PORTFOLIO_SCHEMA = "kristal-target-village-portfolio/v1"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_research_dossier(dossier: dict[str, Any], path: Path) -> None:
    if dossier.get("schema") != RESEARCH_SCHEMA:
        raise ValueError(f"{path}: invalid research schema")
    required = {
        "slug", "community_name", "kf_status", "screening_role", "reviewed_at",
        "development_thesis", "air", "marine", "logistics_envelope", "open_gates", "sources",
    }
    missing = sorted(required - dossier.keys())
    if missing:
        raise ValueError(f"{path}: missing required keys {missing}")

    marine = dossier["marine"]
    if marine["load_limits"]["status"] == "not_verified":
        numeric_limits = [
            marine["load_limits"].get("deck_load_t_m2"),
            marine["load_limits"].get("axle_load_t"),
            marine["load_limits"].get("max_unit_mass_t"),
            marine["load_limits"].get("crane_swl_t"),
        ]
        if any(value is not None for value in numeric_limits):
            raise ValueError(f"{path}: unverified marine load limits must remain null")

    if dossier["air"]["load_status"] == "not_verified":
        if dossier["air"].get("max_aircraft_mass_kg") is not None:
            raise ValueError(f"{path}: unverified aircraft mass limit must remain null")

    source_ids = {source["id"] for source in dossier["sources"]}
    missing_sources = sorted(set(marine.get("source_ids", [])) - source_ids)
    if missing_sources:
        raise ValueError(f"{path}: marine source ids not declared in sources: {missing_sources}")


def build(repo_root: Path) -> dict[str, Any]:
    research_root = repo_root / "research" / "communities" / "targets"
    portfolio = read_yaml(research_root / "portfolio.yaml")
    if portfolio.get("schema") != PORTFOLIO_SCHEMA:
        raise ValueError("Invalid target-village portfolio schema")
    if portfolio.get("ranking_allowed") is not False:
        raise ValueError("Target-village portfolio must remain unranked")

    publish_root = repo_root / "data" / "publish" / "current"
    infrastructure = read_json(publish_root / "community_infrastructure_public.json")
    communities = read_json(publish_root / "communities_public.geojson")
    community_context = read_json(publish_root / "community_context_public.json")
    external_energy = read_json(publish_root / "external_reference_energy_public.json")

    infrastructure_by_name = {item["name"]: item for item in infrastructure["items"]}
    feature_by_entity = {feature["properties"]["entity_id"]: feature for feature in communities["features"]}
    context_by_entity = {item["entity_id"]: item for item in community_context["items"]}

    targets = portfolio.get("targets", [])
    if not targets:
        raise ValueError("Target-village portfolio is empty")
    slugs = [row["slug"] for row in targets]
    names = [row["community_name"] for row in targets]
    if len(slugs) != len(set(slugs)) or len(names) != len(set(names)):
        raise ValueError("Target-village slugs and community names must be unique")

    items: list[dict[str, Any]] = []
    for order, target in enumerate(targets, start=1):
        slug = target["slug"]
        name = target["community_name"]
        source_path = research_root / f"{slug}.yaml"
        if not source_path.is_file():
            raise ValueError(f"Missing target-village dossier: {source_path}")
        research = read_yaml(source_path)
        validate_research_dossier(research, source_path)
        if research["slug"] != slug or research["community_name"] != name:
            raise ValueError(f"{source_path}: portfolio identity mismatch")

        base = infrastructure_by_name.get(name)
        if base is None:
            raise ValueError(f"{name}: no governed community infrastructure record")
        entity_id = base["entity_id"]
        feature = feature_by_entity.get(entity_id)
        if feature is None:
            raise ValueError(f"{name}: no governed community geometry")
        coordinates = feature.get("geometry", {}).get("coordinates")
        if not isinstance(coordinates, list) or len(coordinates) < 2:
            raise ValueError(f"{name}: invalid community geometry")
        context = context_by_entity.get(entity_id, {})
        energy_projects = []
        for reference in external_energy.get("items", []):
            if reference.get("entity_type") != "project" or reference.get("project_type") == "telecom":
                continue
            related_ids = {row.get("entity_id") for row in reference.get("community_relations", [])}
            related_names = set(reference.get("communities", []))
            if entity_id not in related_ids and name not in related_names:
                continue
            energy_projects.append({
                "entity_id": reference["entity_id"],
                "canonical_key": reference.get("canonical_key"),
                "name": reference["name"],
                "project_type": reference.get("project_type"),
                "status": reference.get("status"),
                "technology": reference.get("technology"),
                "capacity_mw": reference.get("capacity_mw"),
                "developer": reference.get("developer"),
                "metadata": reference.get("metadata", {}),
                "sources": reference.get("sources", []),
            })
        status_order = {
            "operating": 0,
            "operating_reference": 1,
            "active_2026": 2,
            "procurement_and_preconstruction_2026": 3,
            "funded_2025": 4,
            "feasibility_study": 5,
            "feasibility_completed_2025": 6,
            "not_approved_2025_appeal_context": 7,
        }
        energy_projects.sort(key=lambda row: (status_order.get(row.get("status"), 50), row["name"].casefold()))

        research_air = research["air"]
        research_marine = research["marine"]
        public_air = {
            "access_known": base["airport"]["access_known"],
            "code": base["airport"]["code"],
            "name": base["airport"]["name"],
            "runway_length_m": base["airport"]["runway_length_m"],
            "runway_surface": base["airport"]["runway_surface"],
            "dimension_status": base["airport"]["dimension_status"],
            "access_pattern": research_air["access_pattern"],
            "load_status": research_air["load_status"],
            "pavement_strength": research_air["pavement_strength"],
            "max_aircraft_mass_kg": research_air["max_aircraft_mass_kg"],
            "operational_constraints": research_air["operational_constraints"],
            "presence_source": base["airport"]["presence_source"],
            "dimension_source": base["airport"]["dimension_source"],
            "note": base["airport"]["note"],
        }
        public_marine = {
            "access_known": base["marine"]["access_known"],
            **research_marine,
            "baseline_context": base["marine"]["context"],
            "baseline_source": base["marine"]["source"],
            "baseline_note": base["marine"]["note"],
        }

        item = {
            "order": order,
            "slug": slug,
            "entity_id": entity_id,
            "name": name,
            "region": base["region"],
            "kf_status": research["kf_status"],
            "screening_role": research["screening_role"],
            "ranking_allowed": False,
            "reviewed_at": research["reviewed_at"],
            "development_thesis": research["development_thesis"],
            "coordinates": {
                "longitude": coordinates[0],
                "latitude": coordinates[1],
                "geometry_status": feature["properties"].get("geometry_precision", "approximate_reference"),
                "not_facility_coordinate": bool(feature["properties"].get("not_facility_coordinate", True)),
            },
            "population": base["population"],
            "air": public_air,
            "marine": public_marine,
            "logistics_envelope": research["logistics_envelope"],
            "system_context": {
                "marine": context.get("marine_context"),
                "telecom": context.get("telecom_context"),
                "road": context.get("road_context"),
                "energy": context.get("energy_context"),
            },
            "energy_projects": energy_projects,
            "open_gates": research["open_gates"],
            "sources": research["sources"],
        }
        items.append(item)

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "schema": SCHEMA,
        "generated_at": generated_at,
        "portfolio_version": portfolio["portfolio_version"],
        "status": portfolio["status"],
        "ranking_allowed": False,
        "target_count": len(items),
        "selection_note": portfolio["selection_note"],
        "semantics": {
            "target": "Portfolio inclusion means evidence deepening only; it is not ranking or site selection.",
            "depth": "Approach and anchorage depths are not berth depths. Null depth means not verified.",
            "load": "Null load limits mean not verified. Runway length or water depth alone never establishes cargo capacity.",
            "seasonality": "Published/general service windows are planning context and remain weather/ice/operator dependent.",
            "coordinates": "Village coordinates are approximate community references, not facility coordinates.",
            "energy_projects": "External energy projects are source-backed context only. Study, funded, active, rejected and operating statuses remain distinct; null geometry never becomes a synthetic route.",
        },
        "items": items,
    }


def write_audit(payload: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for item in payload["items"]:
        load_limits = item["marine"]["load_limits"]
        rows.append({
            "slug": item["slug"],
            "community": item["name"],
            "entity_id": item["entity_id"],
            "kf_status": item["kf_status"],
            "runway_length_m": item["air"]["runway_length_m"] if item["air"]["runway_length_m"] is not None else "",
            "air_load_status": item["air"]["load_status"],
            "marine_access_mode": item["marine"]["access_mode"],
            "marine_depth_status": item["marine"]["depth_status"],
            "marine_load_status": load_limits["status"],
            "open_gate_count": len(item["open_gates"]),
            "reviewed_at": item["reviewed_at"],
        })
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--audit", type=Path)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    output = args.output or repo_root / "data" / "publish" / "current" / "target_villages_public.json"
    audit = args.audit or repo_root / "data" / "processed" / "current" / "target_villages_audit.csv"
    payload = build(repo_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_audit(payload, audit)
    print(f"Published {payload['target_count']} target village dossiers")
    print(f"Output: {output}")
    print(f"Audit: {audit}")


if __name__ == "__main__":
    main()
