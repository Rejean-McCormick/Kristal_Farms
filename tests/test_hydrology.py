import json, sys, importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'packages/schemas/python'))
from kristal_farms_models import Observation

spec = importlib.util.spec_from_file_location('derive', ROOT / 'pipelines/ingest/hydrology/derive_hydrology_statistics.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
FIX = ROOT / 'data/fixtures/current'

def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]


def test_real_observations_have_no_engineering_outputs():
    obs = rows('research_observation.jsonl')
    for item in obs:
        Observation.model_validate({k: v for k, v in item.items() if k in Observation.model_fields})
    forbidden = {'project_gross_head_m', 'project_net_head_m', 'design_flow_m3s', 'capacity_mw', 'validated_hosting_capacity_kw'}
    assert not forbidden.intersection({x['metric'] for x in obs})


def test_hydrology_series_not_faked_when_source_runtime_was_blocked():
    assert rows('research_observation_series.jsonl') == []
    jobs = rows('system_ingestion_job.jsonl')
    hyd = [j for j in jobs if j['job_type'] in {'ingest_hydat_daily_flow', 'ingest_hydat_monthly_flow', 'ingest_hydat_annual_statistics'}]
    assert len(hyd) == 72
    assert all(j['status'].startswith('blocked_runtime_dns') for j in hyd)


def test_natashquan_preserves_two_area_observations():
    obs = rows('research_observation.jsonl')
    station = next(x for x in rows('core_asset.jsonl') if x['metadata'].get('station_number') == '02WB003')['entity_id']
    values = {x['metric']: x for x in obs if x['subject_id'] == station}
    assert values['gross_drainage_area_km2']['value_numeric'] == 15400
    assert values['station_basin_area_km2']['value_numeric'] == 15693


def test_derived_statistics_require_coverage():
    tiny = [{'metric': 'daily_mean_discharge_m3s', 'value_numeric': 1.0, 'valid_from': '2020-01-01'}]
    result = mod.derive(tiny, '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002')
    assert result['status'] == 'insufficient'
    assert result['observations'] == []


def test_synthetic_derivation_has_lineage_and_no_design_flow():
    synthetic = [json.loads(x) for x in (ROOT / 'data/examples/hydrology/synthetic_daily_flow_12y.jsonl').read_text().splitlines() if x.strip()]
    result = mod.derive(synthetic, synthetic[0]['subject_id'], synthetic[0]['series_id'])
    assert result['status'] == 'derived'
    assert len(result['observations']) == 12
    assert len(result['derivations']) == 12
    assert all(d['algorithm_version'] == '1.0.0' and d['raw_value_count'] > 0 and d['source_series_ids'] for d in result['derivations'])
    assert not {'design_flow_m3s', 'capacity_mw', 'project_gross_head_m'}.intersection({o['metric'] for o in result['observations']})


def test_hydrology_screening_remains_unranked():
    hyd = [s for s in rows('research_screening_dimension_state.jsonl') if s['dimension'] == 'hydrology']
    assert len(hyd) == 24
    assert all(s['metadata']['ranking_allowed'] is False for s in hyd)
