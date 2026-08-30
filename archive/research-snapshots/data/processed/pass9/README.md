# Pass 9 — Hydro Resource Atlas data

This directory contains the pass-9 research state for 24 river references across Côte-Nord/Basse-Côte-Nord, Nunavik and Labrador.

## What is real geometry in this pass

- `layers/37_hydrology_observation_profiles.geojson`: official WSC hydrometric station points.
- `layers/40_hydro_opportunity_evidence_matrix.geojson`: the same station anchors used only to visualize documentation completeness.

## What remains null

- WSC basin polygons;
- authoritative connected river flowlines;
- HRDEM terrain profiles;
- project intake/powerhouse/head;
- verified port/road/fibre routes.

The missing geometry is intentional. See `GEOMETRY_INGESTION_LOG_PASS9.json`.

No file in this directory ranks sites.
