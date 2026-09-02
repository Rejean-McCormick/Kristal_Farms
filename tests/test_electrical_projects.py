import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "data/fixtures/current"
PUBLIC = ROOT / "data/publish/current/external_reference_energy_public.json"
REGISTRY = ROOT / "research/grid/electrical_projects.yaml"


def rows(name):
    return [json.loads(line) for line in (FIX / name).read_text(encoding="utf-8").splitlines() if line.strip()]


def test_registry_is_unranked_and_keeps_non_operating_projects_out_of_geometry():
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    assert data["schema"] == "kristal-electrical-projects-research/v1"
    assert data["ranking_allowed"] is False
    assert len(data["projects"]) >= 19
    for project in data["projects"]:
        assert project["canonical_key"].startswith("project:external:")
        assert project["geometry"] is None
        assert project["source_keys"]
        assert project["evidence"]["claim"]


def test_nain_collector_is_local_34_5kv_context_not_main_grid_interconnection():
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    projects = {row["canonical_key"]: row for row in data["projects"]}
    collector = projects["project:external:nl:nain-wind-collector"]
    assert collector["metadata"]["voltage_kv"] == 34.5
    assert collector["metadata"]["not_main_grid_interconnection"] is True
    assert collector["metadata"]["exact_route_geometry_ingested"] is False
    assert collector["metadata"]["route_length_km"] is None
    assert collector["geometry"] is None


def test_key_project_statuses_do_not_overstate_commitment():
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    projects = {row["canonical_key"]: row for row in data["projects"]}
    assert projects["project:external:nl:nain-wind-microgrid"]["project_status"] == "active_2026"
    assert projects["project:external:nl:rigolet-tidal-study"]["project_status"] == "feasibility_study"
    assert projects["project:external:nl:labrador-isolated-interconnection-options-study"]["project_status"] == "feasibility_study"
    south = projects["project:external:nl:southern-labrador-regional-interconnection"]
    assert south["project_status"] == "not_approved_2025_appeal_context"
    assert south["metadata"]["pub_approval_declined"] is True
    assert south["geometry"] is None


def test_governed_project_rows_are_external_references_and_not_candidates():
    entities = {row["canonical_key"]: row for row in rows("core_entity.jsonl")}
    project_rows = {row["entity_id"]: row for row in rows("core_project.jsonl")}
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    for item in data["projects"]:
        entity = entities[item["canonical_key"]]
        project = project_rows[entity["id"]]
        assert project["role"] == "external_reference"
        assert project["geometry"] is None
        assert project["metadata"]["not_kristal_farms_candidate"] is True
        assert project["metadata"].get("kristal_farms_candidate") is not True


def test_public_external_energy_contains_sources_and_community_relations():
    public = json.loads(PUBLIC.read_text(encoding="utf-8"))
    assert public["schema"] == "kristal-external-reference-energy/v2"
    assert public["ranking_allowed"] is False
    items = {row["canonical_key"]: row for row in public["items"]}
    nain = items["project:external:nl:nain-wind-microgrid"]
    assert nain["capacity_mw"] == 3.0
    assert nain["status"] == "active_2026"
    assert "Nain" in nain["communities"]
    assert nain["sources"]
    assert all(source["url"].startswith("https://") for source in nain["sources"])
    rejected = items["project:external:nl:southern-labrador-regional-interconnection"]
    assert rejected["geometry"] is None
    assert rejected["status"].startswith("not_approved")


def test_external_energy_publisher_is_reproducible_except_generated_at(tmp_path):
    output = tmp_path / "external.json"
    subprocess.run([
        sys.executable,
        str(ROOT / "pipelines/publish/build_external_reference_energy_public.py"),
        "--repo-root", str(ROOT),
        "--output", str(output),
    ], check=True)
    generated = json.loads(output.read_text(encoding="utf-8"))
    current = json.loads(PUBLIC.read_text(encoding="utf-8"))
    generated.pop("generated_at", None)
    current.pop("generated_at", None)
    assert generated == current


def test_road_to_north_is_conceptual_non_electrical_enabling_context():
    entities = {row["canonical_key"]: row for row in rows("core_entity.jsonl")}
    corridors = {row["entity_id"]: row for row in rows("core_corridor.jsonl")}
    entity = entities["corridor:road:nl:road-to-the-north"]
    corridor = corridors[entity["id"]]
    assert corridor["corridor_type"] == "conceptual"
    assert corridor["geometry"] is None
    assert corridor["metadata"]["not_route"] is True
    assert corridor["metadata"]["electrical_commitment"] is False
