#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / 'data/fixtures/current'

def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]

errors = []
obs = rows('research_observation.jsonl')
forbidden = {'project_gross_head_m', 'project_net_head_m', 'design_flow_m3s', 'capacity_mw', 'validated_hosting_capacity_kw'}
if forbidden.intersection({x['metric'] for x in obs}):
    errors.append('forbidden engineering/hosting metric in observations')

series = rows('research_observation_series.jsonl')
if series:
    errors.append('real hydrology series unexpectedly materialized in the current fixture')

jobs = rows('system_ingestion_job.jsonl')
hyd = [j for j in jobs if j['job_type'] in {'ingest_hydat_daily_flow', 'ingest_hydat_monthly_flow', 'ingest_hydat_annual_statistics'}]
if len(hyd) != 72:
    errors.append(f'expected 72 HYDAT station/collection jobs, got {len(hyd)}')

states = [s for s in rows('research_screening_dimension_state.jsonl') if s['dimension'] == 'hydrology']
if len(states) != 24:
    errors.append('expected 24 hydrology screening states')
if any(s.get('metadata', {}).get('ranking_allowed') is not False for s in states):
    errors.append('ranking allowed in hydrology screening')

print(json.dumps({'ok': not errors, 'errors': errors, 'hydat_jobs': len(hyd), 'observation_series': len(series), 'hydrology_states': len(states)}, indent=2))
raise SystemExit(1 if errors else 0)
