#!/usr/bin/env python3
"""Build human-readable Observatory public evidence records.

This is a publication step: product code consumes only the generated artifact in
``data/publish/current`` and never reads canonical fixtures directly.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "data" / "fixtures" / "current"
PUBLISH = ROOT / "data" / "publish" / "current"


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main() -> None:
    manifest = json.loads((PUBLISH / "release_manifest.json").read_text(encoding="utf-8"))
    summaries = json.loads((PUBLISH / "evidence_panel_summary_public.json").read_text(encoding="utf-8"))

    evidence = {row["id"]: row for row in read_jsonl(FIXTURES / "research_evidence.jsonl")}
    sources = {row["id"]: row for row in read_jsonl(FIXTURES / "research_source.jsonl")}
    links = read_jsonl(FIXTURES / "research_evidence_source.jsonl")

    referenced_ids = {
        evidence_id
        for item in summaries.get("items", [])
        for evidence_id in item.get("evidence_ids", [])
    }

    sources_by_evidence: dict[str, list[dict]] = {}
    for link in links:
        evidence_id = link.get("evidence_id")
        source = sources.get(link.get("source_id"))
        if not evidence_id or not source:
            continue
        sources_by_evidence.setdefault(evidence_id, []).append(
            {
                "id": source["id"],
                "title": source.get("title") or source.get("source_key") or "Untitled source",
                "publisher": source.get("publisher"),
                "source_type": source.get("source_type") or "source",
                "url": source.get("url"),
                "role": link.get("source_role") or "supports",
            }
        )

    items = []
    for evidence_id in sorted(referenced_ids):
        row = evidence.get(evidence_id)
        if not row:
            continue
        items.append(
            {
                "id": evidence_id,
                "evidence_type": row.get("evidence_type") or "evidence",
                "claim": row.get("claim") or "",
                "status": row.get("status") or "unknown",
                "confidence": row.get("confidence"),
                "retrieved_at": row.get("retrieved_at"),
                "sources": sources_by_evidence.get(evidence_id, []),
            }
        )

    output = {
        "release": manifest["release_id"],
        "immutable": True,
        "items": items,
    }
    destination = PUBLISH / "evidence_records_public.json"
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} public evidence records to {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
