#!/usr/bin/env python3
"""Publish governed external energy/electrical references.

Only canonical fixture rows are read. Research YAML is never consumed by the runtime.
Projects keep their governed status and null geometry unless a separately governed
geometry exists. Rejected/study projects therefore remain panel/context records.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def rows(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def build(root: Path) -> dict[str, Any]:
    fix = root / "data/fixtures/current"
    entities = rows(fix / "core_entity.jsonl")
    projects = rows(fix / "core_project.jsonl")
    assets = rows(fix / "core_asset.jsonl")
    relations = rows(fix / "core_entity_relation.jsonl")
    evidence = rows(fix / "research_evidence.jsonl")
    evidence_relations = rows(fix / "research_evidence_relation.jsonl")
    evidence_sources = rows(fix / "research_evidence_source.jsonl")
    sources = rows(fix / "research_source.jsonl")

    entity_by_id = {row["id"]: row for row in entities}
    source_by_id = {row["id"]: row for row in sources}
    evidence_by_id = {row["id"]: row for row in evidence}

    evidence_ids_by_entity: dict[str, list[str]] = {}
    for link in evidence_relations:
        evidence_ids_by_entity.setdefault(link["entity_id"], []).append(link["evidence_id"])
    source_ids_by_evidence: dict[str, list[str]] = {}
    for link in evidence_sources:
        source_ids_by_evidence.setdefault(link["evidence_id"], []).append(link["source_id"])

    community_relations: dict[str, list[dict[str, Any]]] = {}
    for rel in relations:
        target = entity_by_id.get(rel["to_entity_id"])
        if not target or target.get("entity_type") != "place" or not target.get("canonical_key", "").startswith("place:community:"):
            continue
        community_relations.setdefault(rel["from_entity_id"], []).append({
            "entity_id": target["id"],
            "name": target["name"],
            "relation_type": rel["relation_type"],
        })

    def provenance(entity_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        evs = []
        source_ids: list[str] = []
        for evidence_id in evidence_ids_by_entity.get(entity_id, []):
            ev = evidence_by_id.get(evidence_id)
            if not ev:
                continue
            evs.append({
                "id": ev["id"],
                "evidence_type": ev["evidence_type"],
                "claim": ev["claim"],
                "status": ev["status"],
                "confidence": ev["confidence"],
                "published_at": ev.get("published_at"),
            })
            source_ids.extend(source_ids_by_evidence.get(evidence_id, []))
        unique_source_ids = list(dict.fromkeys(source_ids))
        public_sources = []
        for source_id in unique_source_ids:
            src = source_by_id.get(source_id)
            if not src:
                continue
            public_sources.append({
                "id": src["id"],
                "source_key": src["source_key"],
                "title": src["title"],
                "publisher": src["publisher"],
                "source_type": src["source_type"],
                "url": src["url"],
                "publication_date": src.get("publication_date"),
            })
        return evs, public_sources

    items: list[dict[str, Any]] = []
    for project in projects:
        if project.get("role") != "external_reference":
            continue
        entity = entity_by_id[project["entity_id"]]
        evs, public_sources = provenance(entity["id"])
        related = community_relations.get(entity["id"], [])
        names = [row["name"] for row in related]
        for name in project.get("metadata", {}).get("communities", []):
            if name not in names:
                names.append(name)
        items.append({
            "entity_id": entity["id"],
            "canonical_key": entity["canonical_key"],
            "name": entity["name"],
            "entity_type": "project",
            "role": "external_reference",
            "project_type": project["project_type"],
            "status": project["project_status"],
            "technology": project["technology"],
            "capacity_mw": project.get("capacity_mw"),
            "developer": project.get("developer"),
            "operator": project.get("operator"),
            "geometry": project.get("geometry"),
            "communities": names,
            "community_relations": related,
            "metadata": project.get("metadata", {}),
            "evidence": evs,
            "sources": public_sources,
        })

    for asset in assets:
        entity = entity_by_id[asset["entity_id"]]
        if not entity.get("metadata", {}).get("not_kristal_farms_candidate"):
            continue
        evs, public_sources = provenance(entity["id"])
        items.append({
            "entity_id": entity["id"],
            "canonical_key": entity["canonical_key"],
            "name": entity["name"],
            "entity_type": "asset",
            "role": "external_reference",
            "project_type": None,
            "status": asset.get("operational_status"),
            "technology": asset.get("technology"),
            "capacity_mw": asset.get("capacity_value") if asset.get("capacity_unit") == "MW" else None,
            "capacity_value": asset.get("capacity_value"),
            "capacity_unit": asset.get("capacity_unit"),
            "developer": None,
            "operator": asset.get("operator"),
            "geometry": asset.get("geometry"),
            "communities": [],
            "community_relations": [],
            "metadata": asset.get("metadata", {}),
            "evidence": evs,
            "sources": public_sources,
        })

    items.sort(key=lambda row: (row["entity_type"], row["name"].casefold()))
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "schema": "kristal-external-reference-energy/v2",
        "release": "2026.09.01",
        "generated_at": generated_at,
        "immutable": True,
        "ranking_allowed": False,
        "semantics": {
            "external_reference": "External projects and assets are context only and are not Kristal Farms candidates.",
            "geometry": "Null geometry means no governed route/site geometry is published; do not synthesize one.",
            "status": "Study, funded, rejected and active statuses must not be interpreted as operating infrastructure.",
        },
        "items": items,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    output = args.output or root / "data/publish/current/external_reference_energy_public.json"
    payload = build(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Published {len(payload['items'])} external energy/electrical references")
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
