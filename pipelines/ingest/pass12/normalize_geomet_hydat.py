#!/usr/bin/env python3
"""Normalize raw GeoMet HYDAT pages to app-native source observations.
Preserves source record id, quality flags and time. Does not derive engineering values.
"""
from __future__ import annotations
import argparse,json,uuid
from pathlib import Path

def uid(key): return str(uuid.uuid5(uuid.NAMESPACE_URL,'https://kristal.farms/'+key))
def first(props,*names):
    for n in names:
        if props.get(n) is not None: return props[n]
    return None

def normalize_feature(kind,station,subject_id,series_id,feature):
    p=feature.get('properties',{}); dt=p.get('DATE'); srcid=p.get('IDENTIFIER') or feature.get('id')
    out=[]
    def row(metric,val,unit='m3/s',quality=None):
        if val is None: return
        out.append({'id':uid(f'observation:hydat:{kind}:{station}:{srcid}:{metric}'),'subject_id':subject_id,'metric':metric,'value_numeric':float(val),'value_text':None,'unit':unit,'valid_from':dt,'valid_to':dt,'observed_at':None,'source_evidence_id':None,'derivation_type':'evidence','series_id':series_id,'source_record_id':str(srcid) if srcid is not None else None,'quality_code':quality,'is_provisional':None,'metadata':{'station_number':station,'source_collection':kind,'raw_properties':{k:v for k,v in p.items() if k not in {'DISCHARGE','MONTHLY_MEAN_DISCHARGE'}}}})
    if kind=='daily': row('daily_mean_discharge_m3s',p.get('DISCHARGE'),quality=p.get('DISCHARGE_SYMBOL_EN') or p.get('DISCHARGE_SYMBOL_FR'))
    elif kind=='monthly': row('monthly_mean_discharge_m3s',p.get('MONTHLY_MEAN_DISCHARGE'))
    elif kind=='annual':
        # Field names can evolve; discover only explicitly named discharge max/min fields and never guess from level fields.
        for k,v in p.items():
            ku=k.upper()
            if v is None or 'DISCHARGE' not in ku: continue
            if 'MAX' in ku: row('annual_max_daily_mean_discharge_m3s',v)
            elif 'MIN' in ku: row('annual_min_daily_mean_discharge_m3s',v)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--kind',choices=['daily','monthly','annual'],required=True); ap.add_argument('--station',required=True); ap.add_argument('--subject-id',required=True); ap.add_argument('--series-id',required=True); ap.add_argument('--raw-dir',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for pth in sorted(Path(a.raw_dir).glob('page_*.json')):
        obj=json.loads(pth.read_text());
        for ft in obj.get('features',[]): rows += normalize_feature(a.kind,a.station,a.subject_id,a.series_id,ft)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in rows)); print(json.dumps({'rows':len(rows),'kind':a.kind,'station':a.station}))
if __name__=='__main__': main()
