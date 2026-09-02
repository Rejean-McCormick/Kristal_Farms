import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research/grid/cote_nord_grid_reach.yaml"
ASSETS = ROOT / "research/grid/electrical_assets.yaml"
SOURCES = ROOT / "research/grid/electrical_sources.yaml"
PUBLIC = ROOT / "data/publish/current/grid_reach_public.geojson"
STATIC = ROOT / "apps/web/public/grid/grid-reach.geojson"


def _yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _public():
    return json.loads(PUBLIC.read_text(encoding="utf-8"))


def test_grid_reach_research_is_non_ranked_and_has_no_terminal_model():
    data = _yaml(RESEARCH)
    assert data["schema"] == "kristal-grid-reach-research/v2"
    assert data["ranking_allowed"] is False
    assert data["map_policy"]["measurement_allowed"] is False
    assert data["map_policy"]["local_distribution_network_included"] is False
    assert "terminal_gap_degrees" not in data["map_policy"]
    assert "reach_markers" not in data
    assert len(data["connections"]) >= 13


def test_electrical_asset_registry_contains_real_remote_nodes_and_separate_size_semantics():
    data = _yaml(ASSETS)
    nodes = {item["id"]: item for item in data["grid_nodes"]}

    assert nodes["node_romaine_1"]["installed_capacity_mw"] == 270
    assert nodes["node_romaine_2"]["installed_capacity_mw"] == 640
    assert nodes["node_romaine_3"]["installed_capacity_mw"] == 395
    assert nodes["node_romaine_4"]["installed_capacity_mw"] == 245
    assert nodes["node_churchill_falls"]["installed_capacity_mw"] == 5428
    assert nodes["node_muskrat_falls"]["installed_capacity_mw"] == 824

    assert nodes["node_menihek"]["network_mode"] == "isolated"
    assert nodes["node_menihek"]["installed_capacity_mw"] == 18
    assert nodes["node_lac_robertson"]["network_mode"] == "isolated"
    assert nodes["node_lac_robertson"]["installed_capacity_mw"] == 21
    assert nodes["node_lac_robertson"]["backup_capacity_mw"] == 4.8
    assert nodes["node_innavik"]["network_mode"] == "isolated"
    assert nodes["node_innavik"]["installed_capacity_mw"] == 7.5

    fermont_capacity = nodes["node_fermont"]["available_capacity"]
    assert fermont_capacity["operator"] == "<"
    assert fermont_capacity["value_mw"] == 10
    assert fermont_capacity["as_of"] == "2025-12"
    assert "installed_capacity_mw" not in nodes["node_fermont"]


def test_grid_reach_contains_documented_voltage_classes_and_romaine_labrador_links():
    data = _yaml(RESEARCH)
    connections = {item["id"]: item for item in data["connections"]}
    voltages = {float(item["voltage_kv"]) for item in data["connections"]}

    assert {735.0, 315.0, 230.0, 161.0, 34.5}.issubset(voltages)
    assert connections["montagnais_churchill_falls_735"]["voltage_kv"] == 735
    assert connections["churchill_labrador_west_230"]["voltage_kv"] == 230
    assert connections["churchill_muskrat_315"]["circuit_count"] == 2

    assert connections["romaine_1_romaine_2_315"]["voltage_kv"] == 315
    assert connections["romaine_2_arnaud_315_design_735"]["design_voltage_kv"] == 735
    assert connections["romaine_3_romaine_4_315_design_735"]["design_voltage_kv"] == 735
    assert connections["romaine_4_montagnais_315_design_735"]["design_voltage_kv"] == 735

    extension = connections["natashquan_la_romaine_34_5"]
    assert extension["design_voltage_kv"] == 161
    assert extension["status"] == "existing"


def test_source_registry_is_https_and_all_references_resolve():
    source_data = _yaml(SOURCES)
    source_ids = {item["id"] for item in source_data["sources"]}
    assert source_ids
    assert all(item["url"].startswith("https://") for item in source_data["sources"])

    used = set()
    for item in _yaml(RESEARCH)["connections"]:
        used.update(item["source_ids"])
    for item in _yaml(ASSETS)["grid_nodes"]:
        used.update(item["source_ids"])
    assert used <= source_ids


def test_public_has_grid_nodes_and_no_reach_markers_or_display_gaps():
    payload = _public()
    roles = {feature["properties"]["feature_role"] for feature in payload["features"]}
    assert "grid_connection" in roles
    assert "grid_node" in roles
    assert "reach_marker" not in roles

    nodes = {
        feature["id"]: feature
        for feature in payload["features"]
        if feature["properties"]["feature_role"] == "grid_node"
    }
    assert nodes["node_churchill_falls"]["properties"]["installed_capacity_mw"] == 5428
    assert nodes["node_romaine_2"]["properties"]["installed_capacity_mw"] == 640
    assert nodes["node_menihek"]["properties"]["network_mode"] == "isolated"

    for feature in payload["features"]:
        assert "display_terminal_gap" not in feature["properties"]


def test_schematic_connections_reach_their_declared_anchor_coordinates():
    research = _yaml(RESEARCH)
    assets = _yaml(ASSETS)
    anchors = assets["anchors"]
    public_connections = {
        feature["id"]: feature
        for feature in _public()["features"]
        if feature["properties"]["feature_role"] == "grid_connection"
    }

    for connection in research["connections"]:
        coordinates = public_connections[connection["id"]]["geometry"]["coordinates"]
        expected = [anchors[anchor_id]["coordinates"] for anchor_id in connection["anchor_ids"]]
        assert coordinates == expected


def test_public_geometry_is_explicitly_schematic_and_not_measurable():
    payload = _public()
    assert payload["measurement_allowed"] is False
    assert payload["ranking_allowed"] is False
    for feature in payload["features"]:
        assert feature["properties"]["measurement_allowed"] is False
        assert "geometry_role" in feature["properties"]


def test_publication_is_reproducible(tmp_path):
    output = tmp_path / "grid.geojson"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "pipelines/publish/build_grid_reach_public.py"),
            "--repo-root",
            str(ROOT),
            "--output",
            str(output),
        ],
        check=True,
    )
    generated = json.loads(output.read_text(encoding="utf-8"))
    current = _public()
    assert generated == current
    assert json.loads(STATIC.read_text(encoding="utf-8")) == current


def test_web_layer_uses_asset_nodes_not_terminal_markers():
    explorer = (ROOT / "apps/web/components/explorer/ObservatoryExplorer.tsx").read_text(encoding="utf-8")
    map_code = (ROOT / "apps/web/components/explorer/ObservatoryMap.tsx").read_text(encoding="utf-8")
    map_style = (ROOT / "apps/web/lib/map-style.ts").read_text(encoding="utf-8")
    readme = (ROOT / "apps/web/README.md").read_text(encoding="utf-8")

    assert 'fetch("/grid/grid-reach.geojson"' in explorer
    assert "grid_reach: true" in explorer
    assert "Focus electrical network · Québec / Côte-Nord / Labrador" in explorer
    assert "addGridReach" in map_code
    assert "setGridReachVisible" in map_code
    assert "kristal-grid-reach-source" in map_style
    assert "kristal-grid-reach-generation" in map_style
    assert "kristal-grid-reach-nodes" in map_style
    assert "reach_marker" not in map_style
    assert "terminal-halo" not in map_style
    assert "terminal-core" not in map_style
    assert "terminal markers" not in readme.lower()
    assert STATIC.stat().st_size < 150_000
