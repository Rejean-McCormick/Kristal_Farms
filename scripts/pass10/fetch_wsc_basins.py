#!/usr/bin/env python3
"""Download/read official WSC MDA packages and extract only target station polygons.
Fails closed: no matching station -> no substitute geometry.
"""
import argparse, io, json, re, zipfile, tempfile, pathlib
import requests, geopandas as gpd, pandas as pd
from common import load_targets
URL='https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/HydrometricNetworkBasinPolygons/geojson/MDA_ADP_{mda}.zip'

def discover_station_col(gdf, targets):
    targetset=set(targets)
    preferred=['STATION_NUMBER','STATION_NUM','STATION','STATION_ID','STN_NUM','STN_NUMBER','HYD_STN_N']
    for c in preferred:
        if c in gdf.columns and set(gdf[c].astype(str)).intersection(targetset): return c
    for c in gdf.columns:
        if c=='geometry': continue
        vals=set(gdf[c].dropna().astype(str).str.strip())
        if len(vals.intersection(targetset))>=max(1,min(3,len(targetset))): return c
    raise RuntimeError('Could not identify WSC station-number property. Inspect package schema manually.')

def read_zip(path_or_bytes):
    td=tempfile.TemporaryDirectory(); root=pathlib.Path(td.name)
    z=zipfile.ZipFile(io.BytesIO(path_or_bytes) if isinstance(path_or_bytes,bytes) else path_or_bytes)
    z.extractall(root)
    files=list(root.rglob('*.geojson'))+list(root.rglob('*.json'))+list(root.rglob('*.gpkg'))+list(root.rglob('*.shp'))
    if not files: raise RuntimeError('No supported geospatial file found in WSC package')
    frames=[]
    for p in files:
        try: frames.append(gpd.read_file(p))
        except Exception: pass
    if not frames: raise RuntimeError('No geospatial layer could be read from WSC package')
    out=pd.concat(frames,ignore_index=True)
    return gpd.GeoDataFrame(out,geometry='geometry',crs=frames[0].crs),td

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--targets',required=True); ap.add_argument('--out',required=True); ap.add_argument('--cache-dir'); a=ap.parse_args()
    targets=load_targets(a.targets); by_mda={}
    for t in targets: by_mda.setdefault(t['station_number'][:2],[]).append(t['station_number'])
    pieces=[]; source_meta=[]
    for mda,stations in by_mda.items():
        local=pathlib.Path(a.cache_dir,f'MDA_ADP_{mda}.zip') if a.cache_dir else None
        if local and local.exists(): payload=str(local); origin=str(local)
        else:
            url=URL.format(mda=mda); r=requests.get(url,timeout=120); r.raise_for_status(); payload=r.content; origin=url
            if local: local.parent.mkdir(parents=True,exist_ok=True); local.write_bytes(r.content)
        gdf,tmp=read_zip(payload); col=discover_station_col(gdf,stations); gdf[col]=gdf[col].astype(str).str.strip()
        sel=gdf[gdf[col].isin(stations)].copy(); found=set(sel[col]); missing=sorted(set(stations)-found)
        if missing: raise RuntimeError(f'Missing target WSC polygons in MDA {mda}: {missing}')
        sel['station_number']=sel[col]; sel['geometry_role']='official_wsc_station_basin_polygon'; sel['source_package']=f'MDA_ADP_{mda}'
        pieces.append(sel); source_meta.append({'mda':mda,'origin':origin,'station_field':col,'count':len(sel)})
    out=gpd.GeoDataFrame(pd.concat(pieces,ignore_index=True),crs=pieces[0].crs).to_crs(4326)
    out.to_file(a.out,driver='GeoJSON')
    pathlib.Path(a.out+'.metadata.json').write_text(json.dumps({'sources':source_meta,'count':len(out)},indent=2)+'\n')
if __name__=='__main__': main()
