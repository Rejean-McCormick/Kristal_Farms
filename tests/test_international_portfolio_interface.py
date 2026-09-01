import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_international_publication_has_exactly_12_slots():
    payload = json.loads((ROOT / "data/publish/current/international_portfolio_public.json").read_text())
    assert payload["schema"] == "kristal-international-portfolio/v1"
    assert payload["planning_slots"] == 12
    assert [item["slot"] for item in payload["candidates"]] == list(range(1, 13))
    assert len({item["slug"] for item in payload["candidates"]}) == 12
    assert payload["commitments_claimed"] is False


def test_publication_matches_research_portfolio_names_and_roles():
    research = yaml.safe_load((ROOT / "research/commercial/international_portfolio_12.yaml").read_text())
    public = json.loads((ROOT / "data/publish/current/international_portfolio_public.json").read_text())
    expected = [(item["slot"], item["organization"], item["target_role"]) for item in research["candidates"]]
    actual = [(item["slot"], item["organization"], item["target_role"]) for item in public["candidates"]]
    assert actual == expected


def test_publication_uses_jurisdiction_default_and_ring_fence():
    public = json.loads((ROOT / "data/publish/current/international_portfolio_public.json").read_text())
    assert all(item["jurisdiction_state"] == "ENHANCED_DUE_DILIGENCE" for item in public["candidates"])
    nebius = next(item for item in public["candidates"] if item["organization"] == "Nebius")
    assert nebius["ring_fencing_required"] is True
    assert nebius["outreach_state"] == "CONDITIONAL_RING_FENCE"


def test_web_international_surface_reads_only_published_artifact():
    server = (ROOT / "apps/web/lib/server/international-portfolio.ts").read_text()
    component = (ROOT / "apps/web/components/international/InternationalPortfolioExplorer.tsx").read_text()
    assert "data\",\n  \"publish\",\n  \"current" in server
    assert "research/" not in server
    assert "contracts/policy" not in server
    assert 'fetch("/api/international/portfolio"' in component
    assert "research/commercial" not in component


def test_observatory_shell_unifies_atlas_and_international_portfolio():
    shell_path = ROOT / "apps/web/components/shell/KristalObservatoryShell.tsx"
    assert shell_path.exists()
    shell = shell_path.read_text()
    assert "<ObservatoryExplorer embedded />" in shell
    assert "<InternationalPortfolioExplorer embedded />" in shell
    assert 'searchParams.set("section", "international")' in shell
    assert 'searchParams.delete("section")' in shell


def test_root_uses_shell_and_legacy_international_route_redirects():
    page = (ROOT / "apps/web/app/page.tsx").read_text()
    legacy = (ROOT / "apps/web/app/international/page.tsx").read_text()
    assert "KristalObservatoryShell" in page
    assert 'redirect("/?section=international")' in legacy


def test_shell_query_does_not_collide_with_atlas_camera_view_parameter():
    shell = (ROOT / "apps/web/components/shell/KristalObservatoryShell.tsx").read_text()
    observatory = (ROOT / "apps/web/components/explorer/ObservatoryExplorer.tsx").read_text()
    assert 'get("section")' in shell
    assert 'searchParams.set("section", "international")' in shell
    assert 'url.searchParams.set(' in observatory
    assert '"view"' in observatory
