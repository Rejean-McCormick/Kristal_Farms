# Kristal Farms — Pass 10 Geometry + Terrain Pipeline

Date: 2026-08-30

## Result

Pass 10 does **not** falsely report that official WSC basin polygons, GRHQ/Canada1Water flowlines or HRDEM terrain were downloaded. External DNS resolution remains unavailable in the execution container. Instead, the pass turns the blockage into an executable, fail-closed geometry pipeline.

## New verified fact

All **24/24** Hydro Resource Atlas WSC stations are explicitly present in the official `Included_stations.txt` registry for the national hydrometric basin-polygon dataset. The pass stores the WSC active/discontinued status separately from project relevance.

## New layers 41–47

- 41 — basin-polygon availability anchored to official station points;
- 42 — GRHQ / Canada1Water extraction jobs;
- 43 — fixed operational request windows (explicitly not basins);
- 44 — source schema/runtime discovery registry;
- 45 — HRDEM STAC jobs, gated behind accepted flowlines;
- 46 — actual execution/failure status;
- 47 — hard reach/terrain evidence gate.

Total Pass-10 records: **128**. Natural-feature basin/reach geometry ingested in this pass: **0**. Operational request-window polygons: **24**.

## Executable pipeline

The repo now contains scripts to:

1. fetch MDA 02/03 and extract only the 24 WSC polygons;
2. query GRHQ layer 15 around Québec stations;
3. query Canada1Water around Labrador stations;
4. stop for manual connected-reach review;
5. discover HRDEM DTM assets by STAC;
6. sample a manually accepted reach and compute terrain-only 10 km / 25 km / full-reach drops.

The terrain script hardcodes `project_gross_head_m = null`, `project_net_head_m = null`, `design_flow_m3s = null`, `capacity_mw = null`.

## Test

A synthetic raster/LineString unit test verifies the terrain code runs and still refuses to generate project head or MW. Synthetic outputs are test-only and are not copied into project layers.

## What remains

The next meaningful data jump requires running the included scripts where official binary/service endpoints can actually be reached, followed by manual connectivity review. Only then can real HRDEM terrain evidence appear.

## Registry export

`data/processed/wsc_target_basin_registry_pass10.csv` contains the 24 station IDs, WSC active/discontinued status, MDA package assignment and explicit non-ingestion flag.
