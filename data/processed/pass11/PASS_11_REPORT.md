# Pass 11 — Platform-native hydrology foundation

Date: 2026-08-30

## Why this pass changed direction

The Kristal Farms application architecture makes PostGIS the operational source of truth and explicitly separates geography, evidence, observations and scenarios. Pass 11 therefore stops treating every research artifact as a permanent map layer.

## Canonical migration completed

- **48 canonical entities**: 24 rivers + 24 WSC hydrometric stations;
- **24 station→river relations**;
- **19 source records**;
- **48 evidence records**;
- **24 drainage-area observations**;
- **240 screening-dimension states**;
- **125 ingestion jobs**;
- **24 real geometries**, all WSC station Points;
- **0 river line**, **0 watershed polygon**, **0 project head**, **0 design flow**, **0 MW**, **0 ranking**.

## Key model refinement

A `core.entity` supertype and `core.natural_feature` subtype are added. Rivers/watersheds/reaches no longer need to be forced into `place`, `asset`, `project` or conceptual corridor. This gives Evidence/Observation one stable FK target and preserves IDs when better geometry arrives later.

## Pass 9–10 migration semantics

- WSC station -> `core.asset`;
- river -> `core.natural_feature`;
- drainage area -> `research.observation`;
- basin registry availability -> `research.evidence`;
- analysis/extraction windows -> `system.ingestion_job`;
- evidence matrix/terrain gates -> `research.screening_dimension_state`;
- public map features -> `publish` views/GeoJSON, not source-of-truth tables.

## Hydrology pipeline

ECCC GeoMet exposes station, daily mean and monthly mean HYDAT collections; Wateroffice documents a daily-mean CSV service. Pass 11 creates 48 flow-ingestion jobs (daily + monthly) for the 24 stations, but does not execute them because this runtime cannot resolve ECCC DNS endpoints. No discharge value is fabricated.

## Next technical gate

Run the PostGIS migrations and load the pass-11 fixtures; then execute network jobs in a connected environment. Once actual river/basin geometry and flow observations are ingested, the next research work can compute transparent derived seasonality/low-flow statistics while keeping `design_flow_m3s` an engineering value.
