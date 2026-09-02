#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / 'data/fixtures/current'


def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]


def expected_benchmark_value(benchmark, source):
    key = benchmark['benchmark_key']
    meta = source.get('metadata', {})
    if key.startswith('transmission.'):
        return meta['project_cost_cad'] / meta['line_length_km']
    if key == 'road.north_labrador_unpaved_rom_per_km':
        return meta['road_construction_rom_cad'] / meta['new_road_km']
    if key == 'road.north_labrador_paved_total_per_km':
        return (meta['road_construction_rom_cad'] + meta['paving_increment_cad']) / meta['new_road_km']
    if key == 'road.north_labrador_maintenance_per_km_year':
        return meta['annual_maintenance_cad'] / meta['new_road_km']
    if key.startswith('fibre.'):
        return meta['approved_funding_cad'] / meta['fibre_km']
    if key == 'datacenter.pue_new_facility_2025':
        return meta['new_facility_pue_avg']
    if key == 'datacenter.pue_20mw_plus_2025':
        return meta['large_20mw_plus_pue_avg']
    if key == 'regulation.hq_proposed_data_center_energy_price_2026':
        return meta['proposed_average_price_cad_per_kwh']
    return None


errors = []
sources = {row['source_key']: row for row in rows('research_source.jsonl')}
for benchmark in rows('research_economic_benchmark.jsonl'):
    if benchmark['usable_as_site_estimate'] is not False:
        errors.append('benchmark promoted to site estimate')
    source_key = benchmark.get('metadata', {}).get('source_key')
    source = sources.get(source_key)
    if not source:
        errors.append(f"benchmark source missing: {benchmark['benchmark_key']} -> {source_key}")
        continue
    try:
        expected = expected_benchmark_value(benchmark, source)
    except KeyError as exc:
        errors.append(f"benchmark arithmetic metadata missing: {benchmark['benchmark_key']} -> {exc.args[0]}")
        continue
    if expected is not None and not math.isclose(benchmark['value_numeric'], expected, rel_tol=1e-12, abs_tol=1e-6):
        errors.append(
            f"benchmark arithmetic mismatch: {benchmark['benchmark_key']} "
            f"published={benchmark['value_numeric']} expected={expected}"
        )

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

print(json.dumps({
    'ok': not errors,
    'errors': errors,
    'benchmarks': len(rows('research_economic_benchmark.jsonl')),
    'benchmark_arithmetic_checked': len(rows('research_economic_benchmark.jsonl')),
    'scenarios': len(rows('scenario_scenario.jsonl')),
    'sensitivity_cases': len(rows('scenario_sensitivity_case.jsonl')),
}, indent=2))
raise SystemExit(1 if errors else 0)
