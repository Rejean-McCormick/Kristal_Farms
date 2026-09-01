# Local terrain + potential-basin screening

This pipeline publishes a **local, deterministic HRDEM-derived screening layer** for Observatory.
It does not download terrain at application runtime and does not invent missing topography.

Input:

- a local HRDEM DTM GeoTIFF/mosaic in a projected metre-based CRS;
- `data/publish/current/kristal_hydro_screening_scope_public.json`.

Output:

- `apps/web/public/terrain/terrain-screening.geojson` — coarsened terrain cells around each published hydro screening reference;
- `apps/web/public/terrain/terrain-manifest.json` — local availability, source metadata, bounds and per-site rise summaries.

Each terrain cell contains:

- `elevation_m` — DTM elevation;
- `relative_elevation_m` — elevation relative to the screening reference seed cell;
- `spill_rise_m` — minimum **terrain-connected** rise required for water to reach that cell from the seed, computed with a minimax flood-connectivity pass.

The browser can therefore change the exploratory retention rise without recomputing the DEM. Cells are shown only when `spill_rise_m <= rise` and are colored by approximate depth (`rise - relative_elevation_m`).

This is a **terrain screening visualization only**. The seed coordinates in the current hydro scope are screening references/proxies, not engineered dam locations. The output is not a reservoir design, hydraulic head, flood study, environmental assessment or feasibility determination.

Example:

```bash
python pipelines/terrain/build_terrain_screening.py \
  --dtm D:/terrain/hrdem_north_mosaic.tif \
  --hydro-scope data/publish/current/kristal_hydro_screening_scope_public.json \
  --public-dir apps/web/public/terrain \
  --radius-km 25 \
  --cell-size-m 500 \
  --max-rise-m 150
```

The app detects the generated manifest automatically. Until a local build exists, both terrain controls remain disabled rather than showing fabricated relief.
