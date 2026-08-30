#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[2]
FIX=ROOT/'data/fixtures/pass11'

def rows(name):
    return [json.loads(x) for x in (FIX/name).read_text().splitlines() if x.strip()]
errors=[]
entities=rows('core_entity.jsonl'); eids={x['id'] for x in entities}
if len(eids)!=len(entities): errors.append('duplicate entity UUID')
if any(('rank' in x.get('metadata',{}) or 'score' in x.get('metadata',{})) for x in entities): errors.append('implicit ranking metadata')
obs=rows('research_observation.jsonl')
if any(x['metric']=='project_gross_head_m' for x in obs): errors.append('project head present in pass11 observations')
if any(x['metric']=='design_flow_m3s' for x in obs): errors.append('design flow present in pass11 observations')
if any(x['metric']=='capacity_mw' for x in obs): errors.append('capacity MW present in pass11 observations')
states=rows('research_screening_dimension_state.jsonl')
schemas=rows('system_dataset_schema.jsonl')
jobs=rows('system_ingestion_job.jsonl')
if any(x.get('metadata',{}).get('ranking_allowed') is not False for x in states): errors.append('ranking_allowed not false')
assets=rows('core_asset.jsonl')
if any(x.get('metadata',{}).get('geometry_role')!='official_hydrometric_station_position' for x in assets): errors.append('station geometry role mismatch')

if len(schemas)!=3: errors.append('expected 3 migrated dataset schema records')
if len(jobs)!=125: errors.append(f'expected 125 ingestion jobs, found {len(jobs)}')
print(json.dumps({'pass':not errors,'errors':errors,'counts':{'entities':len(entities),'assets':len(assets),'observations':len(obs),'screening_states':len(states),'dataset_schemas':len(schemas),'ingestion_jobs':len(jobs)}},indent=2))
raise SystemExit(1 if errors else 0)
