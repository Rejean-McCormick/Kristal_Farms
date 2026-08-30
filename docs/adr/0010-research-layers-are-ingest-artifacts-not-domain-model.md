# ADR-010 — Research exchange layers are ingest artifacts, not the domain model

**Status:** Accepted

Research GeoJSON snapshots remain useful for reproducibility and exchange. They are no longer treated as the application source of truth.

Examples:

- Hydro-geometry analysis windows -> `system.ingestion_job.request_geometry`;
- extraction jobs -> `system.ingestion_job`;
- terrain/evidence gates -> `research.screening_dimension_state`;
- WSC station points -> `core.asset`;
- drainage area -> `research.observation`;
- basin availability -> `research.evidence`;
- river/watershed/reach -> `core.natural_feature` once canonicalized.

Public GeoJSON/PMTiles are generated from `publish` views.
