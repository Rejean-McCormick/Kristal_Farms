# Observatory v0.2.4 repository synchronization

This repository snapshot consolidates the interface updates developed during
the v0.2 Geographic Observatory work.

Included:

- MapLibre GL JS 6 ESM/worker integration retained
- river/context hover and inspection retained
- human-readable evidence and hydrology inspector retained
- feature-state radius expression hotfix retained
- browser-extension hydration warning suppression on `<body>`
- clean basemap: park/protected/landuse/landcover surface pop-in removed
- Natural Earth fade extended to avoid pitch-black zoom transitions
- automatic initial fit to published Kristal communities/stations
- `Reset view` control
- map maximum zoom increased to Z20
- local static satellite imagery layer contract
- no MapTiler/Esri/Sentinel-Hub satellite API key or runtime imagery refresh
- manual GDAL GeoTIFF → XYZ tile publication pipeline
- local imagery manifest in both product static assets and published data
- diagnostic `.pyw` helper retained at repository root
- favicon added to eliminate `/favicon.ico` 404 during development

Satellite image pixels are **not** bundled in this update because no reviewed
source raster was supplied. Put a reviewed GeoTIFF under
`data/source/imagery/` and run `pipelines/imagery/build_local_satellite.py`.

The contextual OpenFreeMap vector basemap is still externally hosted. This ADR
only freezes the high-zoom photographic layer. A fully offline vector basemap
would be a separate publication step.
