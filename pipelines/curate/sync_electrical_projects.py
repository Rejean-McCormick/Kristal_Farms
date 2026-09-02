#!/usr/bin/env python3
"""Sync source-backed external electrical projects into governed fixture tables.

This is a curation bridge, not a publisher. It keeps future/studied/rejected
projects out of grid_reach while giving them canonical entity, project,
relation and provenance records. All generated IDs are deterministic UUIDv5.
"""
from __future__ import annotations

import argparse
import csv
import json
import uuid
from pathlib import Path
from typing import Any

import yaml


BASE = "https://kristal.farms/"


def uid(key: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, BASE + key))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")


def upsert(rows: list[dict[str, Any]], new_rows: list[dict[str, Any]], key) -> list[dict[str, Any]]:
    replacement = {key(row): row for row in new_rows}
    out: list[dict[str, Any]] = []
    seen = set()
    for row in rows:
        row_key = key(row)
        if row_key in replacement:
            out.append(replacement[row_key])
            seen.add(row_key)
        else:
            out.append(row)
    for row in new_rows:
        row_key = key(row)
        if row_key not in seen and all(key(existing) != row_key for existing in rows):
            out.append(row)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.repo_root.resolve()
    registry_path = root / "research/grid/electrical_projects.yaml"
    registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    if registry.get("schema") != "kristal-electrical-projects-research/v1":
        raise SystemExit("Unexpected electrical-projects schema")
    if registry.get("ranking_allowed") is not False:
        raise SystemExit("Electrical external references must remain unranked")

    fix = root / "data/fixtures/current"
    entities = load_jsonl(fix / "core_entity.jsonl")
    projects = load_jsonl(fix / "core_project.jsonl")
    relations = load_jsonl(fix / "core_entity_relation.jsonl")
    sources = load_jsonl(fix / "research_source.jsonl")
    evidence = load_jsonl(fix / "research_evidence.jsonl")
    evidence_sources = load_jsonl(fix / "research_evidence_source.jsonl")
    evidence_relations = load_jsonl(fix / "research_evidence_relation.jsonl")

    entity_by_key = {row["canonical_key"]: row for row in entities}
    source_defs = {row["source_key"]: row for row in registry["sources"]}

    source_rows = []
    source_id_by_key: dict[str, str] = {}
    for item in registry["sources"]:
        source_id = uid(f"research-source:{item['source_key']}")
        source_id_by_key[item["source_key"]] = source_id
        source_rows.append({
            "id": source_id,
            "source_key": item["source_key"],
            "title": item["title"],
            "publisher": item["publisher"],
            "source_type": item["source_type"],
            "url": item["url"],
            "publication_date": item.get("publication_date"),
            "retrieved_at": item["retrieved_at"],
            "document_reference": item.get("document_reference"),
            "license": None,
            "metadata": item.get("metadata", {}),
        })

    entity_rows = []
    project_rows = []
    relation_rows = []
    evidence_rows = []
    evidence_source_rows = []
    evidence_relation_rows = []
    canonical_rows = []

    for item in registry["projects"]:
        canonical_key = item["canonical_key"]
        project_id = uid(canonical_key)
        project_metadata = dict(item.get("metadata", {}))
        project_metadata.update({
            "communities": [community["name"] for community in item.get("communities", [])],
            "not_kristal_farms_candidate": True,
            "research_registry": "research/grid/electrical_projects.yaml",
        })
        entity_rows.append({
            "id": project_id,
            "canonical_key": canonical_key,
            "entity_type": "project",
            "name": item["name"],
            "status": item["project_status"],
            "visibility": "PUBLIC",
            "metadata": {
                "role": "external_reference",
                "region": "Labrador",
                "not_kristal_farms_candidate": True,
            },
        })
        project_rows.append({
            "entity_id": project_id,
            "project_type": item["project_type"],
            "role": "external_reference",
            "project_status": item["project_status"],
            "geometry": None,
            "developer": item.get("developer"),
            "operator": item.get("operator"),
            "technology": item["technology"],
            "capacity_mw": item.get("capacity_mw"),
            "metadata": project_metadata,
        })
        canonical_rows.append({
            "legacy_id": "",
            "canonical_entity_id": project_id,
            "canonical_key": canonical_key,
            "entity_type": "project",
            "mapping_role": "integrated_atlas_context",
            "source_context": "electrical_projects_registry",
        })

        for community in item.get("communities", []):
            entity_key = community.get("entity_key")
            relation_type = community.get("relation_type")
            if not entity_key or not relation_type:
                continue
            target = entity_by_key.get(entity_key)
            if target is None:
                raise SystemExit(f"Missing canonical community entity for {entity_key}")
            relation_rows.append({
                "id": uid(f"entity-relation:{canonical_key}:{relation_type}:{entity_key}"),
                "from_entity_id": project_id,
                "to_entity_id": target["id"],
                "relation_type": relation_type,
                "valid_from": None,
                "valid_to": None,
                "metadata": {"external_reference": True, "operation_not_inferred": item["project_status"] != "operating"},
            })

        ev = item["evidence"]
        evidence_id = uid(f"evidence:electrical-project:{canonical_key}")
        evidence_rows.append({
            "id": evidence_id,
            "evidence_key": f"evidence:electrical-project:{canonical_key}",
            "evidence_type": ev["evidence_type"],
            "claim": ev["claim"],
            "status": "verified",
            "confidence": ev["confidence"],
            "valid_from": None,
            "valid_to": None,
            "observed_at": None,
            "published_at": ev.get("published_at"),
            "retrieved_at": "2026-09-01",
            "metadata": {**ev.get("metadata", {}), "external_reference": True},
        })
        evidence_relation_rows.append({"evidence_id": evidence_id, "entity_id": project_id, "relation_type": "describes"})
        for source_key in item["source_keys"]:
            if source_key not in source_defs:
                raise SystemExit(f"Unknown electrical project source key: {source_key}")
            evidence_source_rows.append({"evidence_id": evidence_id, "source_id": source_id_by_key[source_key], "source_role": "supports"})

    entities = upsert(entities, entity_rows, lambda r: r["id"])
    projects = upsert(projects, project_rows, lambda r: r["entity_id"])
    relations = upsert(relations, relation_rows, lambda r: r["id"])
    sources = upsert(sources, source_rows, lambda r: r["id"])
    evidence = upsert(evidence, evidence_rows, lambda r: r["id"])
    evidence_sources = upsert(evidence_sources, evidence_source_rows, lambda r: (r["evidence_id"], r["source_id"], r["source_role"]))
    evidence_relations = upsert(evidence_relations, evidence_relation_rows, lambda r: (r["evidence_id"], r["entity_id"], r["relation_type"]))

    write_jsonl(fix / "core_entity.jsonl", entities)
    write_jsonl(fix / "core_project.jsonl", projects)
    write_jsonl(fix / "core_entity_relation.jsonl", relations)
    write_jsonl(fix / "research_source.jsonl", sources)
    write_jsonl(fix / "research_evidence.jsonl", evidence)
    write_jsonl(fix / "research_evidence_source.jsonl", evidence_sources)
    write_jsonl(fix / "research_evidence_relation.jsonl", evidence_relations)

    registry_csv = fix / "canonical_id_registry.csv"
    with registry_csv.open(encoding="utf-8", newline="") as handle:
        old_rows = list(csv.DictReader(handle))
    merged = upsert(old_rows, canonical_rows, lambda r: r["canonical_entity_id"])
    with registry_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["legacy_id", "canonical_entity_id", "canonical_key", "entity_type", "mapping_role", "source_context"])
        writer.writeheader()
        writer.writerows(merged)

    print(json.dumps({
        "status": "ok",
        "projects_synced": len(project_rows),
        "sources_synced": len(source_rows),
        "entity_relations_synced": len(relation_rows),
        "evidence_synced": len(evidence_rows),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
