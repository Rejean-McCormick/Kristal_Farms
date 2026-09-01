import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "data" / "publish" / "current" / "community_infrastructure_public.json"
AUDIT = ROOT / "data" / "processed" / "current" / "community_infrastructure_audit.csv"
SOURCE = ROOT / "data" / "raw" / "community_infrastructure_source_snapshot.csv"


def test_community_infrastructure_has_one_record_per_published_community():
    payload = json.loads(PUBLISHED.read_text(encoding="utf-8"))
    assert payload["schema"] == "kristal-community-infrastructure/v1"
    assert payload["ranking_allowed"] is False
    assert len(payload["items"]) == 20
    assert len({item["entity_id"] for item in payload["items"]}) == 20
    assert all(item["ranking_allowed"] is False for item in payload["items"])


def test_population_and_airport_values_are_explicitly_sourced():
    payload = json.loads(PUBLISHED.read_text(encoding="utf-8"))
    assert sum(item["population"]["value"] is not None for item in payload["items"]) == 20
    assert all(item["population"]["year"] == 2021 for item in payload["items"])
    assert all(item["population"]["source"] for item in payload["items"])

    runway_refs = [item for item in payload["items"] if item["airport"]["runway_length_m"] is not None]
    assert len(runway_refs) == 19
    assert all(item["airport"]["dimension_source"] for item in runway_refs)

    chisasibi = next(item for item in payload["items"] if item["name"] == "Chisasibi")
    assert chisasibi["airport"]["access_known"] is True
    assert chisasibi["airport"]["runway_length_m"] is None
    assert chisasibi["airport"]["dimension_status"] == "runtime_basemap_or_unknown"
    assert chisasibi["marine"]["access_known"] is False


def test_unverified_port_dimensions_stay_null_instead_of_being_invented():
    payload = json.loads(PUBLISHED.read_text(encoding="utf-8"))
    assert all(item["marine"]["dock_length_m"] is None for item in payload["items"])
    assert all(item["marine"]["max_draft_m"] is None for item in payload["items"])
    assert all(item["marine"]["heavy_lift_status"] != "confirmed" for item in payload["items"])
    assert all(item["runtime_enrichment"]["basemap_population_fallback_allowed"] is False for item in payload["items"])


def test_audit_and_source_snapshot_cover_same_communities():
    with SOURCE.open("r", encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    with AUDIT.open("r", encoding="utf-8-sig", newline="") as handle:
        audit_rows = list(csv.DictReader(handle))

    assert len(source_rows) == len(audit_rows) == 20
    assert {row["community"] for row in source_rows} == {row["community"] for row in audit_rows}
