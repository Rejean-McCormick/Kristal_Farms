#!/usr/bin/env python3
"""Discover HRDEM DTM COG assets for an ACCEPTED connected reach/window. Does not calculate project head."""
import argparse,json,pathlib,requests,geopandas as gpd
URL='https://datacube.services.geo.ca/stac/api/search'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--accepted-reach',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    g=gpd.read_file(a.accepted_reach)
    if len(g)!=1: raise RuntimeError('Provide exactly one manually accepted reach')
    pr=g.iloc[0]
    if not bool(pr.get('connected_reach_manually_accepted',False)) or not bool(pr.get('flow_direction_verified',False)):
        raise RuntimeError('Reach must carry connected_reach_manually_accepted=true and flow_direction_verified=true')
    bbox=list(g.to_crs(4326).total_bounds)
    body={'collections':['hrdem-mosaic-1m','hrdem-mosaic-2m'],'bbox':bbox,'limit':100}
    r=requests.post(URL,json=body,timeout=90); r.raise_for_status(); js=r.json()
    items=[]
    for it in js.get('features',[]):
        assets=it.get('assets',{}); dtm=assets.get('dtm') or assets.get('DTM')
        items.append({'id':it.get('id'),'collection':it.get('collection'),'bbox':it.get('bbox'),'dtm':dtm})
    pathlib.Path(a.out).write_text(json.dumps({'bbox':bbox,'items':items},indent=2)+'\n')
if __name__=='__main__': main()
