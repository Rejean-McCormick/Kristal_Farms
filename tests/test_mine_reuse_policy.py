import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def text(path):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mine_reuse_docs_and_source_are_present():
    required = [
        "research/mines/README.md",
        "research/mines/northern_mine_reuse_inventory.csv",
        "docs/30-site-screening/mine-reuse/MINE_REUSE_SCREENING_METHOD.md",
        "docs/30-site-screening/mine-reuse/UNDERGROUND_COMPUTE_REUSE.md",
        "docs/30-site-screening/mine-reuse/MINE_RESERVOIR_PUMPED_STORAGE.md",
        "docs/50-research/mines/NORTHERN_MINE_REUSE_INVENTORY.md",
        "sources/user-provided/step_mine_ocean.md",
    ]
    for rel in required:
        assert (ROOT / rel).is_file(), rel


def test_old_open_pits_are_not_excluded_from_reservoir_research():
    policy = text("docs/30-site-screening/mine-reuse/MINE_RESERVOIR_PUMPED_STORAGE.md").lower()
    assert "historical/old open-pit mines are explicitly eligible" in policy
    assert "age of the mine is therefore metadata, not a rejection threshold" in policy


def test_recent_closure_is_only_a_preference_for_infrastructure_reuse():
    policy = text("docs/30-site-screening/mine-reuse/UNDERGROUND_COMPUTE_REUSE.md").lower()
    assert "preferentially identify mines that ceased material operations within approximately five years" in policy
    assert "while still allowing older sites" in policy


def test_bunker_and_power_inferences_are_blocked():
    screening = text("docs/30-site-screening/mine-reuse/MINE_REUSE_SCREENING_METHOD.md").lower()
    assert "historical_power_mw` **is not** `current_available_capacity_mw" in screening
    assert "does not become blast-resistant" not in screening  # statement belongs in the focused underground note
    underground = text("docs/30-site-screening/mine-reuse/UNDERGROUND_COMPUTE_REUSE.md").lower()
    assert "does not become blast-resistant" in underground


def test_mine_reuse_does_not_enable_site_ranking():
    manifest = json.loads(text("RELEASE_MANIFEST.json"))
    assert manifest["ranking_allowed"] is False
    screening = text("docs/30-site-screening/mine-reuse/MINE_REUSE_SCREENING_METHOD.md")
    inventory = text("docs/50-research/mines/NORTHERN_MINE_REUSE_INVENTORY.md")
    assert "ranking_allowed = false" in screening
    assert "Unranked" in inventory or "Unranked" in inventory
