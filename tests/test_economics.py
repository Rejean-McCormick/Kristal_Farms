import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'pipelines/economics'))
from compare_architectures import reference_frontier, complete_project_economics

FIX = ROOT / 'data/fixtures/current'

def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]


def test_benchmarks_never_site_estimates():
    benchmarks = rows('research_economic_benchmark.jsonl')
    assert benchmarks and all(x['usable_as_site_estimate'] is False for x in benchmarks)


def test_fibre_benchmarks_are_proxy_only():
    fibre = [x for x in rows('research_economic_benchmark.jsonl') if x['category'] == 'fibre_funding_intensity']
    assert len(fibre) == 2 and all(x['benchmark_role'] == 'proxy_only' for x in fibre)


def test_sensitivity_has_64_non_site_cases():
    cases = rows('scenario_sensitivity_case.jsonl')
    assert len(cases) == 64 and all(x['metadata']['not_site_case'] for x in cases)


def test_no_sensitivity_result_is_labelled_savings():
    for case in rows('scenario_sensitivity_case.jsonl'):
        assert case['metadata']['not_net_savings'] is True
        assert 'net_savings_cad' not in case['results']


def test_conservative_frontier_has_expected_nonpositive_cases():
    cases = rows('scenario_sensitivity_case.jsonl')
    assert sum(x['results']['remaining_unpriced_kristal_farms_budget_conservative_cad'] <= 0 for x in cases) == 4


def test_complete_project_economics_is_blocked():
    try:
        complete_project_economics()
    except RuntimeError:
        pass
    else:
        raise AssertionError('bankable economics must remain blocked')


def test_current_catalog_fixture_synced():
    catalog = json.loads((ROOT / 'packages/catalog/catalog.json').read_text())
    fixture = rows('system_layer_catalog.jsonl')
    assert {x['id'] for x in fixture} == {x['id'] for x in catalog['layers']}
    assert len(fixture) == 15


def test_current_release_is_immutable_and_unranked():
    release = rows('system_release.jsonl')[0]
    assert release['release_key'] == '2026.08.30'
    assert release['immutable'] is True and release['ranking_allowed'] is False
