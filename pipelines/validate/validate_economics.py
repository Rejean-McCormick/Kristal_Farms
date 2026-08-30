#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / 'data/fixtures/current'

def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]

errors = []
for benchmark in rows('research_economic_benchmark.jsonl'):
    if benchmark['usable_as_site_estimate'] is not False:
        errors.append('benchmark promoted to site estimate')
for case in rows('scenario_sensitivity_case.jsonl'):
    if not case['metadata'].get('not_site_case'):
        errors.append('sensitivity case looks site-specific')
    if not case['metadata'].get('not_net_savings'):
        errors.append('sensitivity case permits savings interpretation')
    if any(k in case['results'] for k in ['net_savings_cad', 'project_npv_cad', 'project_irr', 'site_score', 'priority_rank']):
        errors.append('forbidden economic output')
for scenario in rows('scenario_scenario.jsonl'):
    if scenario['metadata'].get('ranking_allowed') is not False:
        errors.append('scenario ranking enabled')

catalog = json.loads((ROOT / 'packages/catalog/catalog.json').read_text())
if catalog.get('ranking_allowed') is not False:
    errors.append('catalog ranking enabled')

print(json.dumps({'ok': not errors, 'errors': errors, 'benchmarks': len(rows('research_economic_benchmark.jsonl')), 'scenarios': len(rows('scenario_scenario.jsonl')), 'sensitivity_cases': len(rows('scenario_sensitivity_case.jsonl'))}, indent=2))
raise SystemExit(1 if errors else 0)
