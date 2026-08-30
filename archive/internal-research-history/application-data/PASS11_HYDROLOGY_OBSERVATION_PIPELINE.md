# Hydrology observation pipeline

## Source

ECCC exposes monitoring-station, HYDAT daily-mean and HYDAT monthly-mean collections through MSC GeoMet OGC API. Wateroffice also documents a CSV historical daily-mean endpoint.

## Import rule

`raw response -> staging normalized rows -> research.evidence/source -> research.observation`

Do not write raw API rows directly to `core`.

## Metrics

- `daily_mean_discharge_m3s`: source observation
- `monthly_mean_discharge_m3s`: source observation
- future seasonal/low-flow statistics: `derived`, with algorithm/model version in metadata
- `design_flow_m3s`: engineering value; must never be auto-created from daily/monthly observations

## Current Pass 11 state

Network calls are represented as jobs but not executed in this runtime because container DNS access to ECCC hosts is unavailable. No flow value is therefore added to the fixture.
