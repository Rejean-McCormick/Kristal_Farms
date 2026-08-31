# Local satellite imagery

The Observatory satellite layer is a **manual static snapshot**. The browser
does not call MapTiler, Esri, Sentinel Hub, Google, Bing, or another satellite
tile provider at runtime.

## Workflow

1. Download/review imagery outside the product runtime.
2. Record its source, acquisition period and license.
3. Place the original georeferenced raster under `data/source/imagery/`.
4. Build local XYZ tiles:

```powershell
python pipelines/imagery/build_local_satellite.py `
  data/source/imagery/YOUR_IMAGE.tif `
  --id sentinel2-quebec-2020 `
  --title "Sentinel-2 Québec 2020" `
  --source-label "Reviewed static satellite mosaic" `
  --acquired "2020" `
  --license "REVIEWED_LICENSE_ID" `
  --attribution "REQUIRED ATTRIBUTION TEXT" `
  --minzoom 7 `
  --maxzoom 13 `
  --replace
```

GDAL (`gdal2tiles.py` and `gdalinfo`) must be on `PATH`.

The command writes:

- `apps/web/public/imagery/<id>/{z}/{x}/{y}.png`
- `apps/web/public/imagery/local-satellite.json`
- `data/publish/imagery/current/imagery_manifest.json`

The UI detects the published manifest on startup and enables the **Satellite
imagery** layer automatically.

There is deliberately **no automatic downloader** in this pipeline.
