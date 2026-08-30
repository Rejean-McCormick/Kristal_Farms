# Pass 12 — Hydrology data contract

## Operational model

Hydrology is stored as provenance-rich observations, not as attributes pasted onto river geometries.

```text
research.source
  ↓
research.evidence
  ↓
research.observation_series
  ↓
research.observation
  ↓
research.observation_derivation (derived values only)
```

A series is materialized only when raw source rows have actually been retrieved. In the current runtime, the 24-station HYDAT series are **not materialized** because external DNS resolution failed. Empty placeholders are not published as data.

## Source observations

- `daily_mean_discharge_m3s` — HYDAT daily mean source value.
- `monthly_mean_discharge_m3s` — HYDAT monthly mean source value.
- annual max/min daily mean discharge — HYDAT annual statistics source values.

Daily and monthly values preserve source record ID, time, quality flag when published, provisional state when known, source release, retrieval time and raw artifact checksum.

## Derived observations

Derived hydrology must have:

- `derivation_type = derived`;
- algorithm key + semantic version;
- source series UUIDs;
- coverage start/end;
- raw value count;
- completeness fraction;
- parameters.

Pass 12 implements `hydrology.climatological_monthly_mean@1.0.0` as a research statistic with a configurable completeness gate.

## Forbidden automatic outputs

The hydrology pipeline must not produce:

- `design_flow_m3s`;
- `project_gross_head_m`;
- `project_net_head_m`;
- `capacity_mw`;
- `validated_hosting_capacity_kw`;
- any site score/rank.

These require later engineering, service-validation or governance decisions.
