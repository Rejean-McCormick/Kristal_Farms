#!/usr/bin/env python3
"""Query GRHQ layer 15 by fixed request windows and write CANDIDATE segments only."""
import argparse, json, pathlib, requests, geopandas as gpd, pandas as pd
from common import normalized
URL='https://servicescarto.mern.gouv.qc.ca/pes/rest/services/Territoire/GRHQ_WMS/MapServer/15/query'
FIELDS='UDH,TYPECE,PERENNITE,FONCTION,ISOLE,O_STRAHLER,O_HORTON,LONGUEUR_M,DIST_DE_M,TOPONYME,CODE_SOURC_DONNE,DATE_SOURCE,DATE_MAJ,OBJECTID'

def query_bbox(bounds):
    xmin,ymin,xmax,ymax=bounds; rows=[]; offset=0
    while True:
        params={'where':'1=1','geometry':f'{xmin},{ymin},{xmax},{ymax}','geometryType':'esriGeometryEnvelope','inSR':'4326','spatialRel':'esriSpatialRelIntersects','outFields':FIELDS,'returnGeometry':'true','outSR':'4326','f':'geojson','resultOffset':offset,'resultRecordCount':2000}
        r=requests.get(URL,params=params,timeout=90); r.raise_for_status(); js=r.json(); feats=js.get('features',[]); rows.extend(feats)
        if len(feats)<2000: break
        offset += len(feats)
    return {'type':'FeatureCollection','features':rows}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--windows',required=True); ap.add_argument('--out-dir',required=True); a=ap.parse_args(); pathlib.Path(a.out_dir).mkdir(parents=True,exist_ok=True)
    wins=gpd.read_file(a.windows)
    for _,w in wins.iterrows():
        st=w['station_number']; river=w.get('river_name',''); js=query_bbox(w.geometry.bounds)
        g=gpd.GeoDataFrame.from_features(js['features'],crs=4326) if js['features'] else gpd.GeoDataFrame(geometry=[],crs=4326)
        if len(g):
            rn=normalized(river).replace(' RIVER','').replace(' RIVIERE','')
            g['candidate_name_hint']=g.get('TOPONYME','').fillna('').map(lambda x: rn and (rn.split('/')[0].strip() in normalized(str(x)) or normalized(str(x)) in rn))
            g['acceptance_status']='candidate_requires_manual_connected_reach_review'; g['geometry_role']='authoritative_GRHQ_candidate_segment_not_accepted_reach'
        g.to_file(pathlib.Path(a.out_dir,f'{st}_grhq_candidates.geojson'),driver='GeoJSON')
if __name__=='__main__': main()
