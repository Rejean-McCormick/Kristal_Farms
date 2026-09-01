#!/usr/bin/env python3
"""Publish normalized community population / air / marine access context.

This publisher intentionally separates three levels of information:
1. governed/published community identifiers from data/publish/current;
2. a curated source snapshot with explicit provenance;
3. runtime basemap geometry (handled by apps/web) for mapped airport/dock extents.

Missing facility dimensions remain null. This script never fabricates runway, dock,
draft, heavy-lift, or population values.
"""
from __future__ import annotations

import csv
import json
import os
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve()
DEFAULT_REPO_ROOT = HERE.parents[2]
REPO_ROOT = Path(os.environ.get("KRISTAL_REPO_ROOT", DEFAULT_REPO_ROOT)).resolve()
PUBLISH_ROOT = REPO_ROOT / "data" / "publish" / "current"
RAW_ROOT = REPO_ROOT / "data" / "raw"
PROCESSED_ROOT = REPO_ROOT / "data" / "processed" / "current"

COMMUNITIES_PATH = PUBLISH_ROOT / "communities_public.geojson"
COMMUNITY_CONTEXT_PATH = PUBLISH_ROOT / "community_context_public.json"
SOURCE_PATH = RAW_ROOT / "community_infrastructure_source_snapshot.csv"
OUTPUT_PATH = PUBLISH_ROOT / "community_infrastructure_public.json"
AUDIT_PATH = PROCESSED_ROOT / "community_infrastructure_audit.csv"


def normalize_name(value: str) -> str:
    text = unicodedata.normalize("NFD", value)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return re.sub(r"[^a-z0-9]+", "", text.lower()).strip()


def nullable_int(value: str | None) -> int | None:
    if value is None or not str(value).strip():
        return None
    return int(float(str(value).strip()))


def nullable_float(value: str | None) -> float | None:
    if value is None or not str(value).strip():
        return None
    return float(str(value).strip())


def as_bool(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def clean(value: str | None) -> str | None:
    text = str(value or "").strip()
    return text or None


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def source_rows() -> dict[str, dict[str, str]]:
    with SOURCE_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        name = clean(row.get("community"))
        if not name:
            continue
        key = normalize_name(name)
        if key in result:
            raise ValueError(f"Duplicate infrastructure source row: {name}")
        result[key] = row
    return result


def make_source(name: str | None, url: str | None, reference_date: str | None = None) -> dict[str, Any] | None:
    name = clean(name)
    url = clean(url)
    reference_date = clean(reference_date)
    if not name and not url and not reference_date:
        return None
    return {"name": name, "url": url, "reference_date": reference_date}


def build() -> dict[str, Any]:
    for path in (COMMUNITIES_PATH, COMMUNITY_CONTEXT_PATH, SOURCE_PATH):
        if not path.exists():
            raise FileNotFoundError(path)

    communities = read_json(COMMUNITIES_PATH)
    context_payload = read_json(COMMUNITY_CONTEXT_PATH)
    context_by_id = {str(item["entity_id"]): item for item in context_payload.get("items", [])}
    sources = source_rows()

    items: list[dict[str, Any]] = []
    audits: list[dict[str, Any]] = []
    used_source_keys: set[str] = set()

    for feature in communities.get("features", []):
        props = feature.get("properties", {})
        entity_id = str(props.get("entity_id") or feature.get("id") or "")
        name = str(props.get("name") or "Unnamed community")
        key = normalize_name(name)
        row = sources.get(key)
        if row:
            used_source_keys.add(key)
        context = context_by_id.get(entity_id, {})

        population = nullable_int(row.get("population_2021")) if row else None
        population_year = nullable_int(row.get("population_year")) if row else None
        runway_length_m = nullable_float(row.get("runway_length_m")) if row else None
        dock_length_m = nullable_float(row.get("dock_length_m")) if row else None
        max_draft_m = nullable_float(row.get("max_draft_m")) if row else None

        airport_access_known = as_bool(row.get("airport_access_known")) if row else False
        marine_from_row = as_bool(row.get("marine_access_known")) if row else False
        published_marine_context = clean(context.get("marine_context") or props.get("marine_context"))
        # The curated snapshot is authoritative when a row exists. Legacy marine_context
        # is preserved only as background metadata; it must not create a facility badge by itself.
        marine_access_known = marine_from_row if row else bool(published_marine_context)

        runway_source = (
            make_source(
                row.get("runway_dimension_source"),
                row.get("runway_dimension_source_url"),
                row.get("runway_reference_date"),
            )
            if row
            else None
        )
        airport_presence_source = (
            make_source(row.get("airport_presence_source"), row.get("airport_presence_source_url"))
            if row
            else None
        )
        marine_source = (
            make_source(row.get("marine_context_source"), row.get("marine_context_source_url"))
            if row
            else None
        )

        item = {
            "entity_id": entity_id,
            "name": name,
            "region": props.get("region"),
            "ranking_allowed": False,
            "population": {
                "value": population,
                "year": population_year,
                "geography": clean(row.get("population_geography")) if row else None,
                "source": make_source(
                    row.get("population_source") if row else None,
                    row.get("population_source_url") if row else None,
                ),
                "note": clean(row.get("population_note")) if row else None,
            },
            "airport": {
                "access_known": airport_access_known,
                "code": clean(row.get("airport_code")) if row else None,
                "name": clean(row.get("airport_name")) if row else None,
                "runway_length_m": runway_length_m,
                "runway_surface": clean(row.get("runway_surface")) if row else None,
                "dimension_status": "published_reference" if runway_length_m is not None else "runtime_basemap_or_unknown",
                "presence_source": airport_presence_source,
                "dimension_source": runway_source,
                "note": clean(row.get("airport_note")) if row else None,
            },
            "marine": {
                "access_known": marine_access_known,
                "context": published_marine_context if marine_access_known else None,
                "facility_name": None,
                "dock_length_m": dock_length_m,
                "max_draft_m": max_draft_m,
                "heavy_lift_status": clean(row.get("heavy_lift_status")) if row else "unknown",
                "size_status": clean(row.get("marine_size_status")) if row else "unknown",
                "source": marine_source,
                "note": clean(row.get("marine_note")) if row else None,
            },
            "runtime_enrichment": {
                "basemap_facility_geometry_allowed": True,
                "basemap_population_fallback_allowed": False,
                "note": "Mapped airport/dock geometry may enrich display dimensions at runtime, but never overrides published population or provenance.",
            },
        }
        items.append(item)
        audits.append(
            {
                "entity_id": entity_id,
                "community": name,
                "population": population if population is not None else "",
                "population_year": population_year if population_year is not None else "",
                "airport_access_known": airport_access_known,
                "runway_length_m": runway_length_m if runway_length_m is not None else "",
                "runway_dimension_status": item["airport"]["dimension_status"],
                "marine_access_known": marine_access_known,
                "dock_length_m": dock_length_m if dock_length_m is not None else "",
                "max_draft_m": max_draft_m if max_draft_m is not None else "",
                "heavy_lift_status": item["marine"]["heavy_lift_status"],
                "source_row_present": bool(row),
            }
        )

    extras = sorted(set(sources) - used_source_keys)
    if extras:
        raise ValueError(f"Source snapshot contains communities not in published map: {extras}")

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    payload = {
        "schema": "kristal-community-infrastructure/v1",
        "generated_at": generated_at,
        "ranking_allowed": False,
        "semantics": {
            "population": "Published census/context fact with explicit year and provenance.",
            "airport": "Community access context; published runway dimensions are references, not operational flight-planning data.",
            "marine": "Access/port context; null berth/dock/draft fields mean not verified, not zero.",
            "runtime_basemap": "OpenMapTiles/OpenStreetMap may add mapped geometry/extent for display only and is not Kristal evidence.",
        },
        "items": items,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    PROCESSED_ROOT.mkdir(parents=True, exist_ok=True)
    with AUDIT_PATH.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = list(audits[0].keys()) if audits else []
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(audits)

    return payload


def main() -> int:
    payload = build()
    populated = sum(1 for item in payload["items"] if item["population"]["value"] is not None)
    runway_refs = sum(1 for item in payload["items"] if item["airport"]["runway_length_m"] is not None)
    marine_known = sum(1 for item in payload["items"] if item["marine"]["access_known"])
    print(f"Published {len(payload['items'])} community infrastructure records")
    print(f"Population facts: {populated}")
    print(f"Published runway references: {runway_refs}")
    print(f"Marine-access records: {marine_known}")
    print(f"Output: {OUTPUT_PATH}")
    print(f"Audit: {AUDIT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
