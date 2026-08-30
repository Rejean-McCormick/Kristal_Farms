# Kristal Farms — Pass 9 Hydro Resource Atlas Report

Date: 2026-08-30

## Result

Pass 9 creates the first explicit **river-reach evidence atlas** for Kristal Farms without creating a single new dam-site claim.

The atlas covers **24 river references** across Côte-Nord/Basse-Côte-Nord, Nunavik and Labrador. Each has an official WSC hydrometric anchor with coordinates and station-linked drainage-area metadata.

## What was actually ingested

- 24 official WSC station points;
- 24 WSC station-linked drainage-area metadata values;
- source registries for WSC basin polygons, GRHQ, Canada1Water/NHN and HRDEM;
- research-reach, terrain-status, logistics-status and evidence-completeness objects.

## What was not ingested

- WSC basin polygons: official MDA 02 and MDA 03 packages were identified, but direct binary download failed in this execution environment;
- GRHQ connected flowlines: dataset/index verified, UDH binary geometry not ingested;
- Canada1Water/NHN regional GeoPackages: source verified, binary not ingested;
- HRDEM terrain profiles: deferred because authoritative connected flowlines are not yet available locally;
- HYDAT flow series/statistics: not ingested in this pass.

No fallback polygons or straight-line “rivers” were generated.

## Why this still matters

The project now has a machine-readable distinction between:

**river exists + gauge exists**

and
**basin geometry exists locally + river line exists locally + terrain/hydrology/logistics are complete + engineering site exists**.

Every pass-9 river is still on the first side of that boundary.

## Layers 34–40

- `34_authoritative_watershed_polygons.geojson` — official basin-package registry; geometry null until ingestion.
- `35_authoritative_river_reaches.geojson` — connected-flowline registry; geometry null until ingestion.
- `36_dem_terrain_profiles.geojson` — HRDEM extraction status; all terrain/head values null.
- `37_hydrology_observation_profiles.geojson` — actual WSC station points + drainage metadata.
- `38_hydro_research_reaches.geojson` — unranked research objects, no MW/head/design flow.
- `39_reach_logistics_context.geojson` — join status only; no invented port/road routes.
- `40_hydro_opportunity_evidence_matrix.geojson` — documentation completeness only, no opportunity score despite the historical naming convention.

## Immediate next technical gate

The first successful geometry ingestion should be WSC `MDA_ADP_02.zip` + `MDA_ADP_03.zip`, followed by exact GRHQ UDH selection for the Québec river set and Canada1Water/NHN extraction for Labrador. Only after connected river lines exist should HRDEM profiles be computed.
