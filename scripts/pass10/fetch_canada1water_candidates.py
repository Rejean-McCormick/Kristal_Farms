#!/usr/bin/env python3
"""Query registered Canada1Water service by fixed windows; output candidates, never accepted reaches."""
import argparse, pathlib, requests, geopandas as gpd
URL='https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/c1w_stream_index_en/MapServer/0/query'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--windows',required=True); ap.add_argument('--out-dir',required=True); a=ap.parse_args(); pathlib.Path(a.out_dir).mkdir(parents=True,exist_ok=True)
    wins=gpd.read_file(a.windows)
    for _,w in wins.iterrows():
        if str(w.get('jurisdiction','')) != 'Newfoundland and Labrador': continue
        xmin,ymin,xmax,ymax=w.geometry.bounds
        params={'where':'1=1','geometry':f'{xmin},{ymin},{xmax},{ymax}','geometryType':'esriGeometryEnvelope','inSR':'4326','spatialRel':'esriSpatialRelIntersects','outFields':'*','returnGeometry':'true','outSR':'4326','f':'geojson'}
        r=requests.get(URL,params=params,timeout=90); r.raise_for_status(); js=r.json()
        g=gpd.GeoDataFrame.from_features(js.get('features',[]),crs=4326)
        if len(g): g['acceptance_status']='candidate_requires_manual_connected_reach_review'; g['geometry_role']='authoritative_Canada1Water_candidate_segment_not_accepted_reach'
        g.to_file(pathlib.Path(a.out_dir,f"{w['station_number']}_canada1water_candidates.geojson"),driver='GeoJSON')
if __name__=='__main__': main()
