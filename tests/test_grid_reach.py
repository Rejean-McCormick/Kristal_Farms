import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research/grid/cote_nord_grid_reach.yaml"
PUBLIC = ROOT / "data/publish/current/grid_reach_public.geojson"
STATIC = ROOT / "apps/web/public/grid/grid-reach.geojson"


def test_grid_reach_research_is_non_ranked_and_lightweight():
    data = yaml.safe_load(RESEARCH.read_text(encoding="utf-8"))
    assert data["ranking_allowed"] is False
    assert data["map_policy"]["measurement_allowed"] is False
    assert data["map_policy"]["local_distribution_network_included"] is False
    assert len(data["connections"]) == 4
    assert len(data["reach_markers"]) == 3


def test_grid_reach_contains_documented_voltage_classes():
    data = yaml.safe_load(RESEARCH.read_text(encoding="utf-8"))
    voltages = {float(item["voltage_kv"]) for item in data["connections"]}
    assert {735.0, 315.0, 161.0, 34.5}.issubset(voltages)
    extension = next(item for item in data["connections"] if item["id"] == "natashquan_la_romaine_34_5")
    assert extension["design_voltage_kv"] == 161
    assert extension["status"] == "existing"


def test_grid_reach_emphasizes_north_and_east_reach():
    payload = json.loads(PUBLIC.read_text(encoding="utf-8"))
    markers = {f["id"]: f for f in payload["features"] if f["properties"]["feature_role"] == "reach_marker"}
    assert set(markers) == {"north_735_reach", "east_161_reach", "east_main_grid_extension"}
    assert markers["east_161_reach"]["properties"]["anchor_name"] == "Natashquan"
    assert "La Romaine" in markers["east_main_grid_extension"]["properties"]["anchor_name"]


def test_public_geometry_is_explicitly_schematic_and_not_measurable():
    payload = json.loads(PUBLIC.read_text(encoding="utf-8"))
    assert payload["measurement_allowed"] is False
    assert payload["ranking_allowed"] is False
    for feature in payload["features"]:
        assert feature["properties"]["measurement_allowed"] is False
        assert "geometry_role" in feature["properties"]


def test_publication_is_reproducible(tmp_path):
    output = tmp_path / "grid.geojson"
    subprocess.run(
        [sys.executable, str(ROOT / "pipelines/publish/build_grid_reach_public.py"), "--repo-root", str(ROOT), "--output", str(output)],
        check=True,
    )
    generated = json.loads(output.read_text(encoding="utf-8"))
    current = json.loads(PUBLIC.read_text(encoding="utf-8"))
    assert generated == current
    assert json.loads(STATIC.read_text(encoding="utf-8")) == current


def test_web_layer_is_static_lightweight_and_not_distribution_dump():
    explorer = (ROOT / "apps/web/components/explorer/ObservatoryExplorer.tsx").read_text(encoding="utf-8")
    map_code = (ROOT / "apps/web/components/explorer/ObservatoryMap.tsx").read_text(encoding="utf-8")
    map_style = (ROOT / "apps/web/lib/map-style.ts").read_text(encoding="utf-8")
    assert 'fetch("/grid/grid-reach.geojson"' in explorer
    assert "grid_reach: true" in explorer
    assert "addGridReach" in map_code
    assert "setGridReachVisible" in map_code
    assert "kristal-grid-reach-source" in map_style
    assert STATIC.stat().st_size < 100_000
