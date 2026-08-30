# Hydrology observation pipeline

## Source model

Official hydrometric data is ingested into a source-preserving workflow:

`raw response → staging normalized rows → research source/evidence → research observation`

Raw API rows are never written directly into `core` entities.

## Metrics

- `daily_mean_discharge_m3s` — source observation;
- `monthly_mean_discharge_m3s` — source observation;
- seasonal/climatological statistics — derived observations with algorithm version;
- `design_flow_m3s` — engineering value and therefore never auto-created from daily/monthly observations.

## Current runtime state

Hydrology ingestion jobs are registered for the canonical WSC stations, but the full source series were not materialized in the research runtime because the external hosts were not reachable from that execution environment. No flow values were fabricated to fill the gap.
