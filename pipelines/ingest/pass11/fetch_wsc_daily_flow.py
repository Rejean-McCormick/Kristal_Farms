#!/usr/bin/env python3
"""Build/execute WSC historical-flow jobs without deriving project design flow.
Network execution is optional; raw responses belong in raw/staging, never directly in core.
"""
from __future__ import annotations
import argparse,csv,io,json,urllib.parse,urllib.request
from pathlib import Path

def daily_url(station,start,end):
    q=[('stations[]',station),('parameters[]','flow'),('start_date',start),('end_date',end)]
    return 'https://wateroffice.ec.gc.ca/services/daily_data/csv/inline?'+urllib.parse.urlencode(q)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--station',required=True); ap.add_argument('--start',required=True); ap.add_argument('--end',required=True); ap.add_argument('--out',required=True); ap.add_argument('--execute',action='store_true'); a=ap.parse_args()
    url=daily_url(a.station,a.start,a.end); out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    manifest={'station_number':a.station,'start_date':a.start,'end_date':a.end,'endpoint':url,'metric_semantics':'daily mean discharge source observations only; not design flow','executed':False}
    if a.execute:
        with urllib.request.urlopen(url,timeout=60) as r: data=r.read()
        out.write_bytes(data); manifest['executed']=True; manifest['bytes']=len(data)
    else:
        out.with_suffix(out.suffix+'.job.json').write_text(json.dumps(manifest,indent=2)+'\n')
        print(url)

if __name__=='__main__': main()
