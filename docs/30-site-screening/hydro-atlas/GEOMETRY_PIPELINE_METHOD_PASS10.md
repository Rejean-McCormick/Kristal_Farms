# Pass 10 Geometry Pipeline Method

## Purpose

Pass 10 converts the official-source blockage from a vague TODO into a deterministic executable pipeline. It does **not** claim successful basin, river-line or DEM ingestion in this runtime.

## Pipeline

1. Confirm station inclusion in the official WSC basin-polygon registry.
2. Download MDA 02 / 03 and extract only the 24 target station polygons.
3. Use a fixed 50 km half-width request window around each official WSC station to limit hydrography service queries. The window is an operational polygon, not a basin.
4. Québec: query GRHQ layer 15 spatially and store **candidate** flow-continuity segments. Labrador: use Canada1Water/NHN candidates.
5. Manual review must confirm the connected main reach and flow direction. Automatic toponym matching is only a hint.
6. Only after acceptance, query HRDEM STAC and sample the DTM along the connected line.
7. Store terrain-drop/slope metrics as terrain evidence. `project_head` stays null until an intake/powerhouse/conveyance concept exists.

## Prohibited shortcuts

- no station-to-mouth straight line used as river geometry;
- no hand-drawn basin;
- no toponym-only automatic reach acceptance;
- no DEM sampling before connected-flowline acceptance;
- no terrain drop promoted to hydraulic head;
- no Q×H MW screening from incomplete evidence;
- no evidence-completeness ranking as site suitability.
