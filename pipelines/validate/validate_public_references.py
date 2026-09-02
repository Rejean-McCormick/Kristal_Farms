#!/usr/bin/env python3
"""Validate provenance links on governed fixtures and public factual surfaces."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def require_https(url: str | None, label: str) -> None:
    if not url or not url.startswith("https://"):
        raise SystemExit(f"{label} requires an HTTPS source URL")


def validate(repo_root: Path) -> dict[str, int]:
    fixtures = repo_root / "data/fixtures/current"
    published = repo_root / "data/publish/current"

    sources = load_jsonl(fixtures / "research_source.jsonl")
    evidence = load_jsonl(fixtures / "research_evidence.jsonl")
    evidence_source = load_jsonl(fixtures / "research_evidence_source.jsonl")
    observations = load_jsonl(fixtures / "research_observation.jsonl")
    benchmarks = load_jsonl(fixtures / "research_economic_benchmark.jsonl")

    source_ids = {row["id"] for row in sources}
    evidence_ids = {row["id"] for row in evidence}
    evidence_with_source: set[str] = set()
    for link in evidence_source:
        if link["evidence_id"] not in evidence_ids:
            raise SystemExit(f"Broken evidence reference: {link['evidence_id']}")
        if link["source_id"] not in source_ids:
            raise SystemExit(f"Broken source reference: {link['source_id']}")
        evidence_with_source.add(link["evidence_id"])
    orphan_evidence = sorted(evidence_ids - evidence_with_source)
    if orphan_evidence:
        raise SystemExit(f"Evidence without source links: {orphan_evidence[:5]}")

    for row in observations:
        evidence_id = row.get("source_evidence_id")
        if not evidence_id or evidence_id not in evidence_ids:
            raise SystemExit(f"Observation missing valid source_evidence_id: {row.get('id')}")
    for row in benchmarks:
        evidence_id = row.get("source_evidence_id")
        if not evidence_id or evidence_id not in evidence_ids:
            raise SystemExit(f"Benchmark missing valid source_evidence_id: {row.get('id')}")

    international = load_json(published / "international_portfolio_public.json")
    if len(international["candidates"]) != 12:
        raise SystemExit("International public portfolio must contain 12 candidates")
    for candidate in international["candidates"]:
        if not candidate.get("sources"):
            raise SystemExit(f"International candidate lacks references: {candidate['organization']}")
        for source in candidate["sources"]:
            require_https(source.get("url"), f"International source {source.get('id')}")
    for source in international["policy_summary"].get("legal_reference_sources", []):
        require_https(source.get("url"), f"Policy source {source.get('id')}")

    community = load_json(published / "community_infrastructure_public.json")
    for item in community["items"]:
        population_source = item.get("population", {}).get("source")
        if population_source:
            require_https(population_source.get("url"), f"Population source for {item['name']}")
        airport = item.get("airport", {})
        for key in ("presence_source", "dimension_source"):
            source = airport.get(key)
            if source:
                require_https(source.get("url"), f"Airport {key} for {item['name']}")
        marine_source = item.get("marine", {}).get("source")
        if marine_source:
            require_https(marine_source.get("url"), f"Marine source for {item['name']}")

    grid = load_json(published / "grid_reach_public.geojson")
    grid_source_ids = {row["id"] for row in grid.get("sources", [])}
    for source in grid.get("sources", []):
        require_https(source.get("url"), f"Grid source {source.get('id')}")
    for feature in grid["features"]:
        refs = feature.get("properties", {}).get("source_ids", [])
        if not refs:
            raise SystemExit(f"Grid feature lacks source_ids: {feature.get('id')}")
        unknown = [ref for ref in refs if ref not in grid_source_ids]
        if unknown:
            raise SystemExit(f"Grid feature {feature.get('id')} has unknown source_ids: {unknown}")

    public_evidence = load_json(published / "evidence_records_public.json")
    public_evidence_ids = {row["id"] for row in public_evidence["items"]}
    for row in public_evidence["items"]:
        if not row.get("sources"):
            raise SystemExit(f"Published evidence lacks source records: {row['id']}")
        for source in row["sources"]:
            # Legacy internal sources are allowed to be non-linkable, but must remain explicitly typed.
            if not source.get("url") and source.get("source_type") != "internal_legacy_research":
                raise SystemExit(f"Published evidence source has no URL and is not explicitly internal legacy: {source.get('id')}")

    public_benchmarks = load_json(published / "economic_benchmarks_public.json")
    for row in public_benchmarks["benchmarks"]:
        if row.get("source_evidence_id") not in public_evidence_ids:
            raise SystemExit(f"Published benchmark lacks resolvable evidence: {row['benchmark_key']}")

    return {
        "fixture_sources": len(sources),
        "fixture_evidence": len(evidence),
        "fixture_observations": len(observations),
        "fixture_benchmarks": len(benchmarks),
        "international_candidates": len(international["candidates"]),
        "community_items": len(community["items"]),
        "grid_features": len(grid["features"]),
        "public_evidence": len(public_evidence["items"]),
        "public_benchmarks": len(public_benchmarks["benchmarks"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    counts = validate(args.repo_root.resolve())
    print(json.dumps({"status": "ok", "counts": counts}, indent=2))


if __name__ == "__main__":
    main()
