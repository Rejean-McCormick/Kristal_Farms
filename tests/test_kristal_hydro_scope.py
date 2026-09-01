import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "data" / "publish" / "current" / "kristal_hydro_screening_scope_public.json"
AUDIT = ROOT / "data" / "processed" / "current" / "kristal_hydro_screening_scope_audit.csv"


def test_public_hydro_scope_obeys_core_coastal_model():
    payload = json.loads(PUBLISHED.read_text(encoding="utf-8"))
    core = payload["model_scope"]["core"]
    max_community = float(core["max_distance_to_active_community_km"])
    max_coast = float(core["max_distance_to_mouth_or_coast_proxy_km"])

    assert payload["schema"] == "kristal-hydro-screening-scope/v2"
    assert payload["ranking_allowed"] is False
    assert payload["sites"]

    excluded_names = (
        "churchill falls",
        "muskrat falls",
        "gull island",
        "lower churchill",
        "twin falls",
        "menihek",
    )

    for site in payload["sites"]:
        text = f"{site['name']} {site.get('river_name') or ''}".lower()
        assert not any(token in text for token in excluded_names)
        assert site["screening_scope"] == "coastal_core"
        assert site["distance_to_active_community_km"] <= max_community
        assert site["distance_to_mouth_or_coast_proxy_km"] <= max_coast
        assert site["geometry_role"] == "screening_reference_not_engineered_dam_site"
        assert site["ranking_allowed"] is False


def test_review_sites_stay_out_of_default_core():
    payload = json.loads(PUBLISHED.read_text(encoding="utf-8"))
    core_ids = {site["id"] for site in payload["sites"]}
    review_ids = {site["id"] for site in payload["review_sites"]}
    assert core_ids.isdisjoint(review_ids)
    assert review_ids == {"NOT-L-SITE", "NOT-U-SITE", "KIN-01-SITE"}


def test_audit_preserves_grid_exclusion_reasons():
    with AUDIT.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 43
    by_id = {row["feature_id"]: row for row in rows}

    for feature_id in ("CHU-01-SITE", "CHU-02-SITE", "CHU-03-SITE"):
        row = by_id[feature_id]
        assert row["scope_class"] == "excluded"
        assert "known_large_grid_hydro_context" in row["reason_codes"]
