#!/usr/bin/env python3
"""Sample an HRDEM DTM along a manually accepted, flow-oriented LineString.
Outputs terrain evidence only; project_gross_head_m/project_net_head_m are always null.
"""
import argparse,json,math,pathlib
import geopandas as gpd
import rasterio
from shapely.geometry import LineString
from pyproj import CRS

def sample_line(line, raster, step_m=100.0):
    n=max(2,int(math.ceil(line.length/step_m))+1)
    ds=[min(i*step_m,line.length) for i in range(n-1)]+[line.length]
    pts=[line.interpolate(d) for d in ds]
    vals=[v[0] for v in raster.sample([(p.x,p.y) for p in pts])]
    nodata=raster.nodata
    samples=[(d,None if (nodata is not None and v==nodata) else float(v)) for d,v in zip(ds,vals)]
    return samples

def val_at(samples,dist):
    valid=[x for x in samples if x[1] is not None]
    return min(valid,key=lambda x:abs(x[0]-dist))[1] if valid else None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--reach',required=True); ap.add_argument('--dtm',required=True); ap.add_argument('--out',required=True); ap.add_argument('--step-m',type=float,default=100.0); a=ap.parse_args()
    g=gpd.read_file(a.reach)
    if len(g)!=1 or g.geometry.iloc[0].geom_type!='LineString': raise RuntimeError('Exactly one accepted LineString required')
    row=g.iloc[0]
    if not bool(row.get('connected_reach_manually_accepted',False)) or not bool(row.get('flow_direction_verified',False)):
        raise RuntimeError('Manual acceptance and flow-direction verification are mandatory')
    with rasterio.open(a.dtm) as r:
        gg=g.to_crs(r.crs); line=gg.geometry.iloc[0]
        if r.crs is None or CRS(r.crs).is_geographic: raise RuntimeError('Terrain computation requires projected raster CRS in metre-scale units')
        samples=sample_line(line,r,a.step_m)
        e0=val_at(samples,0); e10=val_at(samples,min(10000,line.length)); e25=val_at(samples,min(25000,line.length)); eend=val_at(samples,line.length)
        def drop(a,b): return None if a is None or b is None else a-b
        out={'source_reach':str(a.reach),'source_dtm':str(a.dtm),'raster_crs':str(r.crs),'sample_step_m':a.step_m,'reach_length_m':line.length,
             'upstream_elevation_m':e0,'downstream_elevation_m':eend,'terrain_drop_10km_m':drop(e0,e10),'terrain_drop_25km_m':drop(e0,e25),'terrain_drop_full_reach_m':drop(e0,eend),
             'terrain_metric_only':True,'project_gross_head_m':None,'project_net_head_m':None,'design_flow_m3s':None,'capacity_mw':None}
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__': main()
