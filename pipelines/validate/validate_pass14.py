import json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[2]; P=ROOT/'data/fixtures/pass14'
def jl(n): return [json.loads(x) for x in (P/n).read_text().splitlines() if x.strip()]
errors=[]
for b in jl('research_economic_benchmark.jsonl'):
    if b['usable_as_site_estimate'] is not False: errors.append('benchmark promoted to site estimate')
for c in jl('scenario_sensitivity_case.jsonl'):
    if not c['metadata'].get('not_site_case'): errors.append('sensitivity case looks site-specific')
    if not c['metadata'].get('not_net_savings'): errors.append('sensitivity case permits savings interpretation')
    if any(k in c['results'] for k in ['net_savings_cad','project_npv_cad','project_irr','site_score','priority_rank']): errors.append('forbidden economic output')
for s in jl('scenario_scenario.jsonl'):
    if s['metadata'].get('ranking_allowed') is not False: errors.append('scenario ranking enabled')
for a in jl('scenario_assumption.jsonl'):
    if a['parameter'].endswith('_capex_cad') and a['scenario_id'].endswith(''): pass
cat=json.loads((ROOT/'packages/catalog/catalog.pass14.json').read_text())
if cat.get('ranking_allowed') is not False: errors.append('catalog ranking allowed')
print(json.dumps({'pass':not errors,'errors':errors,'benchmarks':len(jl('research_economic_benchmark.jsonl')),'scenarios':len(jl('scenario_scenario.jsonl')),'sensitivity_cases':len(jl('scenario_sensitivity_case.jsonl'))},indent=2))
sys.exit(0 if not errors else 1)
