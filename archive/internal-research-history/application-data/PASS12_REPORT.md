# Pass 12 — Hydrology Observations

**Date:** 2026-08-30  
**Status:** PASS

## Objective

Move hydrology from “source jobs exist” to a production-ready, app-native observation contract: versioned source series, source/knowledge time, quality flags, derived-statistic lineage and Evidence Matrix states.

## What is materially available

- 24 canonical WSC station assets and 24 associated river natural features remain the Hydro Resource Atlas backbone.
- Official HYDAT daily mean, monthly mean and annual daily-extrema collections are registered for all 24 stations.
- Target database release is **HYDAT 2026-07-17**.
- 72 station/collection jobs exist (24 × 3).
- The runtime DNS check failed for ECCC/Wateroffice hosts. Therefore **0 real daily/monthly HYDAT series were materialized**, and the platform contains no fabricated replacement series.

## New data contract

Pass 12 adds `research.observation_series`, `research.observation_derivation`, `system.ingestion_run` and `system.algorithm_registry`. Source observations can retain source-record IDs, quality codes, provisional status, series UUID, source release, retrieval time and raw checksum. Derived observations require source-series lineage, algorithm semantic version, coverage, raw count, completeness and parameters.

## Current verified hydrology evidence added

### Natashquan / 02WB003

The current CEHQ record identifies station 074903 / 02WB003 as open from June 1980, with a **15,693 km² basin at station**, `Non influencé` flow regime, and historical files validated through **2025-09-30** with later data preliminary.

The existing WSC source record in Kristal carries **15,400 km² gross drainage area**. Pass 12 preserves both under distinct metrics and creates an explicit source-discrepancy evidence record. It does not silently overwrite either value.

A 2013 Newfoundland and Labrador government hydrology study is retained separately as a historical study summary for 1980–2001: mean annual flows reported from 271 to 427 m³/s, with study-reported minimum 44.8 m³/s and maximum 2,795 m³/s. These are not raw HYDAT rows and are not design-flow values.

### Alexis / 03QC002

The 2018 NLH/Hatch Annex documents Alexis as the long-record reference gauge used to correlate short Gilbert and St. Lewis records. It reports WSC data collection at Alexis since 1978. The report's regression equations and R² values are stored as **derived-method evidence**, not as observed Alexis flow values.

## Derivation gate

`hydrology.climatological_monthly_mean@1.0.0` is implemented and tested. Default research-QA gates are configurable and versioned; they are not hydrology engineering standards. The algorithm refuses to derive when coverage is insufficient.

The pipeline is prohibited from emitting:

- `design_flow_m3s`;
- project head;
- MW;
- validated compute hosting capacity;
- ranking.

## QA

- Pytest: **12 passed**.
- App validator: **PASS**.
- App Markdown links checked: **0**, missing **0**.
- Docs Markdown links checked: **126**, missing **0**.
- Canonical entities: **48**.
- Sources: **25**.
- Evidence records: **79**.
- Observations: **34**.
- Real materialized hydrology series: **0**.
- HYDAT station/collection jobs: **72**.

## Exit condition for Pass 12

The hydrology data model, provenance rules, ingestion code, derivation gate and selected verified evidence are complete enough for the application foundation. Bulk series ingestion remains an execution dependency for the next network-enabled run; it is not disguised as completed research.
