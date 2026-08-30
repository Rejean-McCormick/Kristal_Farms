# Hydrology data contract

## Operational model

Hydrology is stored as provenance-rich observations rather than pasted onto river geometry.

```text
research.source
  ↓
research.evidence
  ↓
research.observation_series
  ↓
research.observation
  ↓
research.observation_derivation   # derived values only
```

A series is materialized only after raw source rows are actually retrieved. In the current research runtime, full HYDAT series have not been materialized; empty placeholders are not published as data.

## Source observations

Examples include:

- `daily_mean_discharge_m3s`;
- `monthly_mean_discharge_m3s`;
- annual maximum/minimum daily-mean discharge.

Source values preserve record identity, measurement time, source release, retrieval time, quality/provisional flags when available and raw-artifact lineage.

## Derived observations

Derived hydrology must preserve:

- derivation type;
- algorithm key and semantic version;
- source series IDs;
- coverage start/end;
- raw value count;
- completeness fraction;
- parameters.

The current research statistic `hydrology.climatological_monthly_mean@1.0.0` is completeness-gated and is not an engineering design-flow selector.

## Forbidden automatic outputs

The hydrology pipeline must not automatically produce:

- `design_flow_m3s`;
- `project_gross_head_m`;
- `project_net_head_m`;
- `capacity_mw`;
- `validated_hosting_capacity_kw`;
- site score/rank.

Those values require later engineering, utility/service validation or governance decisions.
