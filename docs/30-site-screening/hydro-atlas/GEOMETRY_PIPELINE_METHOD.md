# Hydro geometry pipeline method

## Purpose

Provide a deterministic path from official station references to authoritative basin/flowline/terrain evidence without fabricating natural-feature geometry.

## Pipeline

1. Confirm station inclusion in the official WSC basin-polygon registry.
2. Retrieve the relevant WSC basin package and extract only the target station polygons.
3. Use a fixed request window around the official WSC station to limit hydrography service queries. The window is an operational query geometry, not a basin.
4. Québec: query GRHQ and store **candidate** flow-continuity segments. Labrador: use Canada1Water/NHN candidates.
5. Manual review confirms the connected main reach and flow direction. Automatic toponym matching is only a hint.
6. Only after acceptance, query HRDEM and sample the DTM along the accepted line.
7. Store terrain-drop/slope metrics as terrain evidence. `project_head` remains null until an intake/powerhouse/conveyance concept exists.

## Prohibited shortcuts

- no station-to-mouth straight line used as river geometry;
- no hand-drawn basin;
- no toponym-only automatic reach acceptance;
- no DEM sampling before connected-flowline acceptance;
- no terrain drop promoted to hydraulic head;
- no Q×H MW screening from incomplete evidence;
- no evidence-completeness ranking as site suitability.

Executable workflow: `pipelines/ingest/hydro_geometry/`.
