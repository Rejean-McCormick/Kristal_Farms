import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "apps" / "web"


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
    assert "community_context_public.json" in server_source
    assert "evidence_panel_summary_public.json" in server_source


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
