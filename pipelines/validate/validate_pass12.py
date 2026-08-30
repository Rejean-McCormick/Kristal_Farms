#!/usr/bin/env python3
import json,sys
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[2]; FIX=ROOT/'data/fixtures/pass12'
def rows(n): return [json.loads(x) for x in (FIX/n).read_text().splitlines() if x.strip()]
errors=[]
ents=rows('core_entity.jsonl'); eids={x['id'] for x in ents}
if len(eids)!=len(ents): errors.append('duplicate entity UUID')
src=rows('research_source.jsonl'); srcids={x['id'] for x in src}
ev=rows('research_evidence.jsonl'); evids={x['id'] for x in ev}
obs=rows('research_observation.jsonl'); forbidden={'project_gross_head_m','project_net_head_m','design_flow_m3s','capacity_mw','validated_hosting_capacity_kw'}
if forbidden.intersection({x['metric'] for x in obs}): errors.append('forbidden engineering/hosting metric in pass12 observations')
for x in obs:
    if x.get('source_evidence_id') and x['source_evidence_id'] not in evids: errors.append('orphan observation evidence '+x['id'])
for x in rows('research_evidence_source.jsonl'):
    if x['source_id'] not in srcids: errors.append('orphan source '+x['source_id'])
    if x['evidence_id'] not in evids: errors.append('orphan evidence-source '+x['evidence_id'])
series=rows('research_observation_series.jsonl')
if series: errors.append('real hydrology series unexpectedly materialized in blocked runtime')
jobs=rows('system_ingestion_job.jsonl'); hyd=[j for j in jobs if j['job_type'] in {'ingest_hydat_daily_flow','ingest_hydat_monthly_flow','ingest_hydat_annual_statistics'}]
if len(hyd)!=72: errors.append(f'expected 72 station HYDAT jobs, got {len(hyd)}')
if any(not j['status'].startswith('blocked_runtime_dns') for j in hyd): errors.append('HYDAT job status not blocked-runtime-DNS')
states=rows('research_screening_dimension_state.jsonl')
if any(s.get('metadata',{}).get('ranking_allowed') is not False for s in states): errors.append('ranking allowed flag detected')
if len([s for s in states if s['dimension']=='hydrology'])!=24: errors.append('expected 24 hydrology states')
# Source discrepancy must be explicit.
if not any(e['evidence_key']=='evidence:drainage-area-source-discrepancy:02wb003' and e['status']=='conflicting' for e in ev): errors.append('Natashquan source discrepancy missing')
res={'pass':not errors,'errors':errors,'counts':{'entities':len(ents),'sources':len(src),'evidence':len(ev),'observations':len(obs),'observation_series':len(series),'screening_states':len(states),'ingestion_jobs':len(jobs),'hydat_station_collection_jobs':len(hyd)}}
print(json.dumps(res,indent=2)); raise SystemExit(1 if errors else 0)
