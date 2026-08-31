from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "apps" / "web"

RUNTIME_SUFFIXES = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}
FORBIDDEN_PRODUCT_TOKENS = (
    '"research"',
    "'research'",
    '"pipelines"',
    "'pipelines'",
    '"raw"',
    "'raw'",
    '"fixtures"',
    "'fixtures'",
)


def runtime_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in RUNTIME_SUFFIXES:
            yield path


def test_three_logical_workspaces_are_explicit():
    expected = [
        ROOT / "research" / "README.md",
        ROOT / "research" / "hydrology" / "README.md",
        ROOT / "research" / "energy" / "README.md",
        ROOT / "research" / "communities" / "README.md",
        ROOT / "research" / "experiments" / "README.md",
        ROOT / "docs" / "architecture" / "workspace-boundaries.md",
        ROOT / "docs" / "adr" / "0020-one-monorepo-three-logical-systems.md",
    ]
    assert all(path.is_file() for path in expected)


def test_web_runtime_does_not_reach_into_research_pipelines_raw_or_fixtures():
    violations = []
    for path in runtime_files(WEB):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in FORBIDDEN_PRODUCT_TOKENS:
            if token in text:
                violations.append(f"{path.relative_to(ROOT)}: {token}")
    assert not violations, "\n".join(violations)


def test_observatory_file_bridge_reads_publish_and_stable_catalog_only():
    source = (WEB / "lib" / "server" / "public-data.ts").read_text(encoding="utf-8")
    assert '"data", "publish", "current"' in source
    assert '"packages", "catalog", "catalog.json"' in source
    assert '"fixtures"' not in source
    assert '"research"' not in source
    assert '"pipelines"' not in source
    assert '"raw"' not in source


def test_boundary_is_directional_in_agent_contract():
    agent_contract = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "Product runtime code must not import or execute `research/` or `pipelines/`" in agent_contract
