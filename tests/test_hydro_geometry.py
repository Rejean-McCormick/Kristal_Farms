import json, subprocess, sys, tempfile
from pathlib import Path
import numpy as np, rasterio, geopandas as gpd
from rasterio.transform import from_origin
from shapely.geometry import LineString

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'pipelines/ingest/hydro_geometry/compute_reach_terrain.py'


def test_synthetic_terrain_profile_does_not_create_project_head_or_capacity():
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        arr = np.tile(np.linspace(100, 0, 300, dtype='float32'), (20, 1))
        tif = td / 'dem.tif'
        with rasterio.open(tif, 'w', driver='GTiff', height=20, width=300, count=1, dtype='float32', crs='EPSG:32620', transform=from_origin(500000, 1000, 100, 100), nodata=-9999) as dst:
            dst.write(arr, 1)
        line = LineString([(500050, 50), (529950, 50)])
        frame = gpd.GeoDataFrame([{'connected_reach_manually_accepted': True, 'flow_direction_verified': True, 'geometry': line}], crs='EPSG:32620')
        reach = td / 'reach.geojson'
        frame.to_file(reach, driver='GeoJSON')
        out = td / 'out.json'
        subprocess.run([sys.executable, str(SCRIPT), '--reach', str(reach), '--dtm', str(tif), '--out', str(out), '--step-m', '500'], check=True)
        result = json.load(open(out))
        assert result['terrain_metric_only'] is True
        assert result['project_gross_head_m'] is None
        assert result['capacity_mw'] is None
        assert result['terrain_drop_full_reach_m'] > 90
