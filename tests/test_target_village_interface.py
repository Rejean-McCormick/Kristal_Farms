import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLISH = ROOT / "data" / "publish" / "current"
WEB = ROOT / "apps" / "web"
TARGETS = ROOT / "research" / "communities" / "targets"


def test_target_village_portfolio_publishes_all_12_unranked_targets():
    portfolio = yaml.safe_load((TARGETS / "portfolio.yaml").read_text())
    public = json.loads((PUBLISH / "target_villages_public.json").read_text())
    expected = [(row["slug"], row["community_name"]) for row in portfolio["targets"]]
    actual = [(row["slug"], row["name"]) for row in public["items"]]
    assert public["schema"] == "kristal-target-villages/v1"
    assert public["ranking_allowed"] is False
    assert public["target_count"] == 12
    assert actual == expected
    assert len({row["entity_id"] for row in public["items"]}) == 12


def test_target_village_publication_reuses_governed_community_identity_and_airport_facts():
    public = json.loads((PUBLISH / "target_villages_public.json").read_text())
    infrastructure = json.loads((PUBLISH / "community_infrastructure_public.json").read_text())
    infra_by_name = {row["name"]: row for row in infrastructure["items"]}
    for village in public["items"]:
        base = infra_by_name[village["name"]]
        assert village["entity_id"] == base["entity_id"]
        assert village["population"] == base["population"]
        assert village["air"]["runway_length_m"] == base["airport"]["runway_length_m"]
        assert village["air"]["runway_surface"] == base["airport"]["runway_surface"]


def test_unverified_load_capacity_is_never_manufactured():
    public = json.loads((PUBLISH / "target_villages_public.json").read_text())
    for village in public["items"]:
        if village["air"]["load_status"] == "not_verified":
            assert village["air"]["max_aircraft_mass_kg"] is None
        loads = village["marine"]["load_limits"]
        if loads["status"] == "not_verified":
            assert loads["deck_load_t_m2"] is None
            assert loads["axle_load_t"] is None
            assert loads["max_unit_mass_t"] is None
            assert loads["crane_swl_t"] is None


def test_marine_depth_contract_separates_approach_anchorage_and_berth():
    public = json.loads((PUBLISH / "target_villages_public.json").read_text())
    for village in public["items"]:
        marine = village["marine"]
        assert "approach_depth_m" in marine
        assert "anchorage_depth_m" in marine
        assert "berth_depth_range_m" in marine
        assert "depth_status" in marine
    puvirnituq = next(row for row in public["items"] if row["slug"] == "puvirnituq")
    assert puvirnituq["marine"]["approach_depth_m"] == 8.0
    assert puvirnituq["marine"]["berth_depth_range_m"] == [0.9, 1.5]


def test_target_village_research_inputs_have_schema_and_open_gates():
    portfolio = yaml.safe_load((TARGETS / "portfolio.yaml").read_text())
    assert (ROOT / "contracts" / "schemas" / "target-village-dossier.schema.json").is_file()
    for target in portfolio["targets"]:
        dossier = yaml.safe_load((TARGETS / f"{target['slug']}.yaml").read_text())
        assert dossier["schema"] == "kristal-target-village-research/v1"
        assert dossier["community_name"] == target["community_name"]
        assert dossier["open_gates"]
        assert dossier["marine"]["load_limits"]["status"] == "not_verified"


def test_labrador_target_villages_join_governed_external_energy_projects():
    public = json.loads((PUBLISH / "target_villages_public.json").read_text())
    by_name = {row["name"]: row for row in public["items"]}
    assert any(p["canonical_key"] == "project:external:nl:nain-wind-microgrid" for p in by_name["Nain"]["energy_projects"])
    assert any(p["canonical_key"] == "project:external:nl:rigolet-tidal-study" for p in by_name["Rigolet"]["energy_projects"])
    assert any(p["canonical_key"] == "project:external:nl:makkovik-arena-solar" for p in by_name["Makkovik"]["energy_projects"])
    for name in ("Nain", "Hopedale", "Makkovik", "Postville", "Rigolet"):
        for project in by_name[name]["energy_projects"]:
            assert project["sources"]
            assert all(source["url"].startswith("https://") for source in project["sources"])


def test_village_web_runtime_reads_only_published_artifact():
    server = (WEB / "lib" / "server" / "villages.ts").read_text()
    portfolio_component = (WEB / "components" / "villages" / "VillagePortfolioExplorer.tsx").read_text()
    assert '"data",\n  "publish",\n  "current"' in server
    assert "research/" not in server
    assert "pipelines/" not in server
    assert 'fetch("/api/villages"' in portfolio_component
    assert 'href={`/villages/${village.slug}`}' in portfolio_component


def test_village_routes_and_full_dossier_exist():
    assert (WEB / "app" / "villages" / "page.tsx").is_file()
    assert (WEB / "app" / "villages" / "[slug]" / "page.tsx").is_file()
    assert (WEB / "app" / "api" / "villages" / "route.ts").is_file()
    assert (WEB / "app" / "api" / "villages" / "[slug]" / "route.ts").is_file()
    dossier = (WEB / "components" / "villages" / "VillageDossier.tsx").read_text()
    assert "Air logistics" in dossier
    assert "Marine logistics" in dossier
    assert "Logistics envelope" in dossier
    assert "OPEN LOGISTICS GATES" in dossier
    assert "Electrical system & projects" in dossier
    assert "Evidence & sources" in dossier


def test_atlas_inspector_links_target_communities_to_full_village_dossier():
    inspector = (WEB / "components" / "explorer" / "EntityInspector.tsx").read_text()
    public_data = (WEB / "lib" / "server" / "public-data.ts").read_text()
    assert "targetVillageSlug" in inspector
    assert 'href={`/villages/${detail.targetVillageSlug}`}' in inspector
    assert "target_villages_public.json" in public_data


def test_rebuild_and_release_manifest_include_target_village_publication():
    rebuild = (ROOT / "REBUILD_OBSERVATORY.pyw").read_text()
    manifest = json.loads((PUBLISH / "release_manifest.json").read_text())
    assert "pipelines/publish/build_target_villages_public.py" in rebuild
    assert "target_villages_public.json" in manifest["public_outputs"]
    assert (ROOT / "data" / "processed" / "current" / "target_villages_audit.csv").is_file()
