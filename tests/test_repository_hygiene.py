import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ACTIVE_TEXT_ROOTS = [
    ROOT / "docs",
    ROOT / "contracts",
    ROOT / "packages",
    ROOT / "pipelines",
    ROOT / "database",
    ROOT / "data" / "fixtures" / "current",
    ROOT / "data" / "processed" / "current",
    ROOT / "data" / "publish" / "current",
]
ACTIVE_ROOT_FILES = [
    ROOT / "README.md",
    ROOT / "CHANGELOG.md",
    ROOT / "AGENTS.md",
    ROOT / "ORCHESTRATION.md",
    ROOT / "GITHUB_SETUP.md",
    ROOT / "mkdocs.yml",
]
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".jsonl", ".csv", ".py", ".sql", ".bat"}

FORBIDDEN_ACTIVE_PATTERNS = {
    "internal pass numbering": re.compile(r"\bpasses?\s*[-_ ]?\d+\b|\bpass\d+\b", re.I),
    "retired product name": re.compile(r"Kristal[ _-]?Platform|Kristal Geospatial Platform|platform-native", re.I),
    "separate Kristals project": re.compile(r"\bKristals\b|\bKristALL\b", re.I),
    "superseded siting rule": re.compile(r"\bNain[- ]first\b|\bheat[- ]first\b|\bvillage[- ]first\b", re.I),
}


def active_files():
    for p in ACTIVE_ROOT_FILES:
        if p.exists():
            yield p
    for root in ACTIVE_TEXT_ROOTS:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
                continue
            # Historical/application-source material belongs in archive, not active docs.
            if "archive" in p.parts or ".git" in p.parts:
                continue
            yield p


def test_active_surfaces_do_not_expose_internal_build_history_or_retired_names():
    violations = []
    for p in active_files():
        text = p.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in FORBIDDEN_ACTIVE_PATTERNS.items():
            if pattern.search(text):
                violations.append(f"{label}: {p.relative_to(ROOT)}")
        if re.search(r"\bpass\d+\b", p.name, re.I):
            violations.append(f"internal pass filename: {p.relative_to(ROOT)}")
    assert not violations, "\n".join(sorted(set(violations)))


def test_public_release_manifest_lists_only_existing_outputs():
    release_dir = ROOT / "data" / "publish" / "current"
    manifest = json.loads((release_dir / "release_manifest.json").read_text(encoding="utf-8"))
    missing = [name for name in manifest["public_outputs"] if not (release_dir / name).is_file()]
    assert not missing, missing


def test_public_release_does_not_expose_legacy_ranking_fields():
    publish_dir = ROOT / "data" / "publish" / "current"
    forbidden = ("legacy_tier", "legacy_category", "legacy_decision_use", "priority_rank", "site_score")
    hits = []
    for p in publish_dir.iterdir():
        if not p.is_file() or p.suffix.lower() not in {".json", ".geojson", ".csv"}:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for token in forbidden:
            if token in text:
                hits.append(f"{p.name}: {token}")
    assert not hits, hits

def test_information_architecture_has_single_active_application_doc_axis():
    assert not (ROOT / "docs/60-application-data").exists()
    assert (ROOT / "docs/architecture/information-architecture.md").is_file()
    assert (ROOT / "docs/data/application-data-model.md").is_file()
    assert (ROOT / "docs/product/explorer-data-contract.md").is_file()
    assert (ROOT / "docs/scenarios/economic-method.md").is_file()


def test_root_keeps_specialist_tools_out_of_primary_entry_surface():
    retired_root_tools = [
        "DIAG_OBSERVATORY.pyw",
        "FETCH_SENTINEL2.pyw",
        "FETCH_WATERSHEDS.pyw",
        "INSTALL_PMTILES.pyw",
        "REGISTER_LOCAL_IMAGERY.ps1",
        "START_IMAGERY_SERVER.ps1",
        "KF_target_villages.patch",
        "CHANGED_FILES.txt",
    ]
    assert not [name for name in retired_root_tools if (ROOT / name).exists()]
    assert (ROOT / "tools/observatory/DIAG_OBSERVATORY.pyw").is_file()
    assert (ROOT / "tools/imagery/START_IMAGERY_SERVER.ps1").is_file()
    assert (ROOT / "tools/geospatial/FETCH_WATERSHEDS.pyw").is_file()


def test_archive_is_excluded_from_default_local_search_context():
    ignore = (ROOT / ".ignore").read_text(encoding="utf-8")
    assert "archive/" in ignore
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "historical provenance" in agents

