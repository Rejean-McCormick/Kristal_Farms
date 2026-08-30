import json, subprocess, sys, tempfile
from pathlib import Path
import numpy as np, rasterio, geopandas as gpd
from rasterio.transform import from_origin
from shapely.geometry import LineString

def find_root():
    here=Path(__file__).resolve()
    for p in [here.parent,*here.parents]:
        if (p/'scripts/pass10/compute_reach_terrain.py').exists(): return p
    raise RuntimeError('Cannot locate scripts/pass10/compute_reach_terrain.py')

def main():
    root=find_root(); script=root/'scripts/pass10/compute_reach_terrain.py'
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); arr=np.tile(np.linspace(100,0,300,dtype='float32'),(20,1))
        tif=td/'dem.tif'
        with rasterio.open(tif,'w',driver='GTiff',height=20,width=300,count=1,dtype='float32',crs='EPSG:32620',transform=from_origin(500000,1000,100,100),nodata=-9999) as dst: dst.write(arr,1)
        line=LineString([(500050,50),(529950,50)])
        g=gpd.GeoDataFrame([{'connected_reach_manually_accepted':True,'flow_direction_verified':True,'geometry':line}],crs='EPSG:32620')
        reach=td/'reach.geojson'; g.to_file(reach,driver='GeoJSON')
        out=td/'out.json'; subprocess.run([sys.executable,str(script),'--reach',str(reach),'--dtm',str(tif),'--out',str(out),'--step-m','500'],check=True)
        x=json.load(open(out)); assert x['terrain_metric_only'] is True; assert x['project_gross_head_m'] is None; assert x['capacity_mw'] is None; assert x['terrain_drop_full_reach_m']>90
    print('PASS synthetic terrain test')
if __name__=='__main__': main()
