#!/usr/bin/env python3
"""Research hydrology derivations with explicit completeness and lineage gates.
Never emits design_flow_m3s, project head, MW or ranking.
"""
from __future__ import annotations
import argparse,calendar,json,statistics,uuid
from collections import defaultdict
from datetime import date
from pathlib import Path
ALGO='hydrology.climatological_monthly_mean'; VERSION='1.0.0'
FORBIDDEN={'design_flow_m3s','capacity_mw','project_gross_head_m','project_net_head_m','validated_hosting_capacity_kw'}
def uid(k): return str(uuid.uuid5(uuid.NAMESPACE_URL,'https://kristal.farms/'+k))
def expected_days(y,m): return calendar.monthrange(y,m)[1]
def derive(rows,subject_id,source_series_id,min_years=10,min_year_fraction=.90,min_month_fraction=.80):
    daily=[]
    for r in rows:
        if r.get('metric')!='daily_mean_discharge_m3s' or r.get('value_numeric') is None: continue
        d=date.fromisoformat(r['valid_from']); daily.append((d,float(r['value_numeric'])))
    if not daily: return {'status':'insufficient','reason':'no_daily_values','observations':[],'derivations':[]}
    by_year=defaultdict(list)
    for d,v in daily: by_year[d.year].append((d,v))
    complete_years=[]
    for y,vals in by_year.items():
        exp=366 if calendar.isleap(y) else 365
        if len({d for d,_ in vals})/exp>=min_year_fraction: complete_years.append(y)
    if len(complete_years)<min_years: return {'status':'insufficient','reason':'minimum_complete_years_not_met','complete_years':complete_years,'observations':[],'derivations':[]}
    monthly_year=defaultdict(list)
    for d,v in daily:
        if d.year in complete_years: monthly_year[(d.year,d.month)].append(v)
    month_means=defaultdict(list)
    for (y,m),vals in monthly_year.items():
        if len(vals)/expected_days(y,m)>=min_month_fraction: month_means[m].append(statistics.fmean(vals))
    if any(len(month_means[m])<min_years for m in range(1,13)):
        return {'status':'insufficient','reason':'monthly_coverage_gate_not_met','complete_years':complete_years,'observations':[],'derivations':[]}
    start=min(d for d,_ in daily); end=max(d for d,_ in daily); expected=(end-start).days+1; completeness=len({d for d,_ in daily})/expected
    observations=[]; derivations=[]
    for m in range(1,13):
        oid=uid(f'observation:derived:{ALGO}:{VERSION}:{subject_id}:month-{m:02d}')
        observations.append({'id':oid,'subject_id':subject_id,'metric':'climatological_monthly_mean_discharge_m3s','value_numeric':statistics.fmean(month_means[m]),'value_text':None,'unit':'m3/s','valid_from':None,'valid_to':None,'observed_at':None,'source_evidence_id':None,'derivation_type':'derived','series_id':None,'source_record_id':None,'quality_code':None,'is_provisional':False,'metadata':{'calendar_month':m,'algorithm_key':ALGO,'algorithm_version':VERSION,'complete_years':len(complete_years),'research_statistic_not_design_flow':True}})
        derivations.append({'observation_id':oid,'algorithm_key':ALGO,'algorithm_version':VERSION,'source_series_ids':[source_series_id],'coverage_start':start.isoformat(),'coverage_end':end.isoformat(),'raw_value_count':len(daily),'completeness_fraction':completeness,'parameters':{'min_complete_years':min_years,'min_year_completeness_fraction':min_year_fraction,'min_month_completeness_fraction':min_month_fraction},'metadata':{'complete_years':complete_years}})
    assert not FORBIDDEN.intersection({o['metric'] for o in observations})
    return {'status':'derived','observations':observations,'derivations':derivations,'complete_years':complete_years,'completeness_fraction':completeness}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--infile',required=True); ap.add_argument('--subject-id',required=True); ap.add_argument('--source-series-id',required=True); ap.add_argument('--out-observations',required=True); ap.add_argument('--out-derivations',required=True); ap.add_argument('--min-years',type=int,default=10); a=ap.parse_args()
    rows=[json.loads(x) for x in Path(a.infile).read_text().splitlines() if x.strip()]; res=derive(rows,a.subject_id,a.source_series_id,a.min_years)
    Path(a.out_observations).parent.mkdir(parents=True,exist_ok=True); Path(a.out_observations).write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in res['observations'])); Path(a.out_derivations).write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in res['derivations'])); print(json.dumps({k:v for k,v in res.items() if k not in {'observations','derivations'}},indent=2))
if __name__=='__main__': main()
