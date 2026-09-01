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
    tile_template = manifest["tile_template"]
    is_repo_static = tile_template.startswith("/imagery/") and "://" not in tile_template
    is_loopback_static = tile_template.startswith(("http://127.0.0.1:", "http://localhost:"))
    assert is_repo_static or is_loopback_static


def test_observatory_v024_has_manual_imagery_pipeline_no_downloader():
    helper = ROOT / "pipelines" / "imagery" / "build_local_satellite.py"
    assert helper.is_file()
    source = helper.read_text(encoding="utf-8")
    assert "gdal2tiles" in source
    assert "urllib" not in source
    assert "requests.get" not in source


def test_observatory_v024_clean_basemap_and_fade_are_present():
    style_source = (WEB / "lib" / "map-style.ts").read_text(encoding="utf-8")
    assert 'background-color", "#1E6864"' in style_source
    assert "isParkOrLandTheme" in style_source
    assert 'safeLayout(map, layer.id, "visibility", "none")' in style_source
    assert 'layer.type === "raster" || layer.type === "hillshade"' in style_source


def test_root_layout_tolerates_extension_body_attributes():
    source = (WEB / "app" / "layout.tsx").read_text(encoding="utf-8")
    assert "<body suppressHydrationWarning>" in source


def test_observatory_v024_has_reset_and_auto_fit():
    explorer_source = (WEB / "components" / "explorer" / "ObservatoryExplorer.tsx").read_text(encoding="utf-8")
    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")
    assert "Reset view" in explorer_source
    assert "fitToObservatoryExtent" in map_source
    assert "autoFitOnLoad" in map_source


def test_observatory_v041_displaces_village_callouts_and_keeps_house_on_coordinate():
    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")
    css_source = (WEB / "app" / "globals.css").read_text(encoding="utf-8")

    assert "getCommunityCalloutPlacement" in map_source
    assert "community-house-marker" in map_source
    assert "community-callout__leader" in map_source
    assert 'new maplibregl.Marker({ element, anchor: "center" })' in map_source
    assert ".community-map-marker" in css_source
    assert ".community-callout__leader::after" in css_source


def test_observatory_v042_moves_aupaluk_up_and_publishes_extended_hydro_review_sites():
    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")
    public_data_source = (WEB / "lib" / "server" / "public-data.ts").read_text(encoding="utf-8")

    assert 'normalizePlaceName(feature.properties.name) === "aupaluk"' in map_source
    assert 'return { x: 0, y: -74 };' in map_source
    assert 'hydroSites: [...hydroScope.sites, ...hydroScope.review_sites]' in public_data_source


def test_observatory_v043_leaders_use_nearest_panel_edge_geometry():
    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")

    assert "updateCommunityLeaderGeometry" in map_source
    assert "panel.offsetWidth" in map_source
    assert "panel.offsetHeight" in map_source
    assert "const targetX = clamp" not in map_source  # target remains mutable for the defensive fallback
    assert "let targetX = clamp(0, left, right);" in map_source
    assert "let targetY = clamp(0, top, bottom);" in map_source
    assert "const houseRadius = 13;" in map_source
    assert "distance - 26" not in map_source


def test_observatory_v044_declares_local_terrain_and_basin_layers():
    explorer_source = (WEB / "components" / "explorer" / "ObservatoryExplorer.tsx").read_text(encoding="utf-8")
    map_source = (WEB / "components" / "explorer" / "ObservatoryMap.tsx").read_text(encoding="utf-8")
    style_source = (WEB / "lib" / "map-style.ts").read_text(encoding="utf-8")

    assert 'fetch("/terrain/terrain-manifest.json"' in explorer_source
    assert 'id="terrain_relief"' in explorer_source
    assert 'id="terrain_basins"' in explorer_source
    assert "addLocalTerrainScreening" in map_source
    assert "Exploratory retention rise" in map_source
    assert '"fill-color": basinDepthColorExpression(50)' in style_source
    assert '"spill_rise_m"' in style_source


def test_observatory_v044_terrain_manifest_is_local_and_non_fabricated_by_default():
    manifest = json.loads((WEB / "public" / "terrain" / "terrain-manifest.json").read_text(encoding="utf-8"))
    assert manifest["schema"] == "kristal-local-terrain/v1"
    assert manifest["available"] is False
    assert manifest["geojson_url"].startswith("/terrain/")
    assert "://" not in manifest["geojson_url"]
    assert manifest["source"] == "Natural Resources Canada HRDEM DTM"
    assert manifest["vertical_datum"] == "CGVD2013"


def test_observatory_v044_terrain_pipeline_computes_connectivity_offline():
    helper = ROOT / "pipelines" / "terrain" / "build_terrain_screening.py"
    assert helper.is_file()
    source = helper.read_text(encoding="utf-8")
    assert "minimax_spill" in source
    assert "spill_rise_m" in source
    assert "volume_m3" in source
    assert "requests" not in source
    assert "urllib" not in source
