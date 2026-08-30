#!/usr/bin/env python3
"""Fetch station-filtered HYDAT OGC API collections with paging and immutable raw-page manifests.
No hydrology engineering values are derived here.
"""
from __future__ import annotations
import argparse, hashlib, json, time, urllib.parse, urllib.request
from pathlib import Path
COLLECTIONS={'daily':'hydrometric-daily-mean','monthly':'hydrometric-monthly-mean','annual':'hydrometric-annual-statistics'}

def build_url(kind,station,offset=0,limit=5000,start=None,end=None):
    q={'STATION_NUMBER':station,'offset':offset,'limit':limit,'sortby':'DATE','f':'json'}
    if start or end: q['datetime']=f'{start or ".."}/{end or ".."}'
    return 'https://api.weather.gc.ca/collections/'+COLLECTIONS[kind]+'/items?'+urllib.parse.urlencode(q)

def fetch_json(url,retries=3,timeout=90):
    last=None
    for n in range(retries):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'KristalFarms-Hydrology-Pipeline/1.0'})
            with urllib.request.urlopen(req,timeout=timeout) as r: return json.loads(r.read().decode('utf-8'))
        except Exception as e:
            last=e
            if n+1<retries: time.sleep(2**n)
    raise last

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--kind',choices=COLLECTIONS,required=True); ap.add_argument('--station',required=True); ap.add_argument('--out',required=True); ap.add_argument('--start'); ap.add_argument('--end'); ap.add_argument('--limit',type=int,default=5000); ap.add_argument('--release',default='HYDAT_20260717'); ap.add_argument('--execute',action='store_true'); a=ap.parse_args()
    root=Path(a.out); root.mkdir(parents=True,exist_ok=True)
    manifest={'station_number':a.station,'kind':a.kind,'collection':COLLECTIONS[a.kind],'source_release':a.release,'start':a.start,'end':a.end,'limit':a.limit,'executed':False,'row_count':0,'pages':[],'semantic_guard':'source hydrometric observations only; never design flow or MW'}
    if not a.execute:
        manifest['dry_run_url']=build_url(a.kind,a.station,0,a.limit,a.start,a.end); (root/'manifest.job.json').write_text(json.dumps(manifest,indent=2)+'\n'); print(manifest['dry_run_url']); return
    offset=0
    while True:
        url=build_url(a.kind,a.station,offset,a.limit,a.start,a.end); obj=fetch_json(url); feats=obj.get('features',[])
        raw=json.dumps(obj,ensure_ascii=False,separators=(',',':')).encode(); sha=hashlib.sha256(raw).hexdigest(); page=root/f'page_{offset:08d}.json'; page.write_bytes(raw)
        manifest['pages'].append({'offset':offset,'feature_count':len(feats),'sha256':sha,'file':page.name,'url':url}); manifest['row_count']+=len(feats)
        if len(feats)<a.limit: break
        offset += a.limit
    manifest['executed']=True; (root/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
if __name__=='__main__': main()
