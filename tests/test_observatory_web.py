import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "apps" / "web"
PUBLISH = ROOT / "data" / "publish" / "current"


def test_observatory_web_vertical_slice_exists():
    expected = [
        WEB / "app" / "page.tsx",
        WEB / "components" / "explorer" / "ObservatoryMap.tsx",
        WEB / "components" / "explorer" / "HoverCard.tsx",
        WEB / "components" / "explorer" / "EntityInspector.tsx",
        WEB / "app" / "api" / "explorer" / "bootstrap" / "route.ts",
        WEB / "app" / "api" / "explorer" / "entity" / "[id]" / "route.ts",
    ]
    assert all(path.is_file() for path in expected)


def test_web_reads_current_public_release_server_side():
    server_source = (WEB / "lib" / "server" / "public-data.ts").read_text(encoding="utf-8")
    assert '"data", "publish", "current"' in server_source
    assert "communities_public.geojson" in server_source
    assert "hydrometric_stations_public.geojson" in server_source
    assert "hydro_evidence_matrix_public.json" in server_source
    assert "community_context_public.json" in server_source
    assert "evidence_panel_summary_public.json" in server_source
    assert "evidence_records_public.json" in server_source


def test_observatory_v02_public_evidence_is_declared_in_release_manifest():
    manifest = json.loads((PUBLISH / "release_manifest.json").read_text(encoding="utf-8"))
    assert "evidence_records_public.json" in manifest["public_outputs"]


def test_observatory_v02_public_evidence_records_are_human_readable():
    payload = json.loads((PUBLISH / "evidence_records_public.json").read_text(encoding="utf-8"))
    assert payload["items"]
    record = payload["items"][0]
    assert record["claim"]
    assert record["evidence_type"]
    assert isinstance(record["sources"], list)
    assert any(source.get("title") for source in record["sources"])


def test_observatory_v02_river_references_and_context_hydrography_exist():
    server_source = (WEB / "lib" / "server" / "public-data.ts").read_text(encoding="utf-8")
    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")
    style_source = (WEB / "lib" / "map-style.ts").read_text(encoding="utf-8")

    assert "buildRiverReferences" in server_source
    assert "matchRiverReference" in map_source
    assert "contextual-waterway-hover" in map_source
    assert "https://tiles.openfreemap.org/styles/liberty" in style_source


def test_map_does_not_render_conceptual_corridor_geometry():
    semantics = json.loads((ROOT / "packages" / "shared" / "visual_semantics.json").read_text())
    assert semantics["rules"]["role_styles"]["conceptual_corridor"] == "panel_only"

    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")
    forbidden_layer_ids = ["corridor-line", "conceptual-corridor", "research-corridor-line"]
    assert not any(layer_id in map_source for layer_id in forbidden_layer_ids)


def test_web_dependency_versions_are_explicit_and_secure_next_patch():
    package = json.loads((WEB / "package.json").read_text(encoding="utf-8"))
    assert package["dependencies"]["next"] == "16.3.3"
    assert package["dependencies"]["maplibre-gl"] == "6.6.0"


def test_observatory_publication_helper_is_data_platform_code():
    helper = ROOT / "pipelines" / "publish" / "build_observatory_public.py"
    assert helper.is_file()
    source = helper.read_text(encoding="utf-8")
    assert '"data" / "fixtures" / "current"' in source
    assert '"data" / "publish" / "current"' in source


def test_observatory_v024_uses_local_static_satellite_assets():
    style_source = (WEB / "lib" / "map-style.ts").read_text(encoding="utf-8")
    explorer_source = (WEB / "components" / "explorer" / "ObservatoryExplorer.tsx").read_text(encoding="utf-8")

    assert "addLocalSatelliteImagery" in style_source
    assert "/imagery/local-satellite.json" in explorer_source
    assert "api.maptiler.com" not in style_source
    assert "NEXT_PUBLIC_MAPTILER_KEY" not in style_source


def test_observatory_v024_imagery_manifest_is_static_and_local():
    manifest = json.loads((WEB / "public" / "imagery" / "local-satellite.json").read_text(encoding="utf-8"))
    assert manifest["schema"] == "kristal-local-imagery/v1"
    assert manifest["tile_template"].startswith("/imagery/")
    assert "://" not in manifest["tile_template"]


def test_observatory_v024_has_manual_imagery_pipeline_no_downloader():
    helper = ROOT / "pipelines" / "imagery" / "build_local_satellite.py"
    assert helper.is_file()
    source = helper.read_text(encoding="utf-8")
    assert "gdal2tiles" in source
    assert "urllib" not in source
    assert "requests.get" not in source


def test_observatory_v024_clean_basemap_and_fade_are_present():
    style_source = (WEB / "lib" / "map-style.ts").read_text(encoding="utf-8")
    assert 'background-color", "#131b20"' in style_source
    assert "setLayerZoomRange" in style_source
    assert "isPark" in style_source
    assert "isLandTheme" in style_source


def test_root_layout_tolerates_extension_body_attributes():
    source = (WEB / "app" / "layout.tsx").read_text(encoding="utf-8")
    assert "<body suppressHydrationWarning>" in source


def test_observatory_v024_has_reset_and_auto_fit():
    explorer_source = (WEB / "components" / "explorer" / "ObservatoryExplorer.tsx").read_text(encoding="utf-8")
    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")
    assert "Reset view" in explorer_source
    assert "fitToObservatoryExtent" in map_source
    assert "autoFitOnLoad" in map_source
