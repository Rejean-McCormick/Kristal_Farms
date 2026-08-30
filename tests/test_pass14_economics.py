import json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'pipelines/economics'))
from compare_architectures import reference_frontier,complete_project_economics
P=ROOT/'data/fixtures/pass14'
def jl(n): return [json.loads(x) for x in (P/n).read_text().splitlines() if x.strip()]
def test_benchmarks_never_site_estimates():
    assert jl('research_economic_benchmark.jsonl')
    assert all(x['usable_as_site_estimate'] is False for x in jl('research_economic_benchmark.jsonl'))
def test_fibre_benchmarks_are_proxy_only():
    fb=[x for x in jl('research_economic_benchmark.jsonl') if x['category']=='fibre_funding_intensity']
    assert len(fb)==2 and all(x['benchmark_role']=='proxy_only' for x in fb)
def test_sensitivity_has_64_non_site_cases():
    c=jl('scenario_sensitivity_case.jsonl')
    assert len(c)==64 and all(x['metadata']['not_site_case'] for x in c)
def test_no_sensitivity_calls_result_savings():
    for c in jl('scenario_sensitivity_case.jsonl'):
        assert c['metadata']['not_net_savings'] is True
        assert 'net_savings_cad' not in c['results']
def test_four_conservative_nonpositive_cases_expected():
    c=jl('scenario_sensitivity_case.jsonl')
    n=sum(x['results']['remaining_unpriced_kristal_budget_conservative_cad']<=0 for x in c)
    assert n==4
def test_all_optimistic_reference_cases_positive():
    c=jl('scenario_sensitivity_case.jsonl')
    assert all(x['results']['remaining_unpriced_kristal_budget_optimistic_cad']>0 for x in c)
def test_engine_reference_case():
    x=reference_frontier(25,10,933,tx_low=1300000000/439,tx_high=1271000000/262,road_low=2100000000/809,road_high=2700000000/809,fibre_low_proxy=79419117/933,fibre_high_proxy=271937242/1300)
    assert x['not_net_savings'] is True and x['remaining_unpriced_kristal_budget_conservative_cad']<0
def test_complete_project_economics_is_blocked():
    try: complete_project_economics()
    except RuntimeError: pass
    else: raise AssertionError('bankable economics must be blocked')
def test_unpriced_kristal_items_explicit():
    a=jl('scenario_assumption.jsonl')
    u=[x for x in a if x['scenario_id']==str(__import__('uuid').uuid5(__import__('uuid').NAMESPACE_URL,'https://kristal.farms/scenario:kristal-local-compute-template')) and x['value_text']=='UNPRICED']
    assert len(u)>=7
def test_scenarios_are_not_site_specific():
    assert all(x['metadata'].get('site_specific') is False for x in jl('scenario_scenario.jsonl'))
def test_pass14_catalog_fixture_synced():
    catalog=json.loads((ROOT/'packages/catalog/catalog.pass14.json').read_text())
    fixture=jl('system_layer_catalog.jsonl')
    assert {x['id'] for x in fixture}=={x['id'] for x in catalog['layers']}
    assert len(fixture)==15

def test_pass14_release_is_immutable_and_unranked():
    r=jl('system_release.jsonl')[0]
    assert r['release_key']=='2026.08.30-pass14'
    assert r['immutable'] is True and r['ranking_allowed'] is False
