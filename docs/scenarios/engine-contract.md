# Scenario engine contract

## Goal

The scenario engine is independent of React and exposes deterministic, testable functions/services.

## Minimal inputs

```json
{
  "generation_mw": 18,
  "community_priority_mw": 2.5,
  "reserve_mw": 1.0,
  "compute_min_mw": 0,
  "compute_max_mw": 14,
  "siting_variant": "generation_side"
}
```

## Minimal outputs

Potential outputs:

```text
annual_generation_mwh
community_energy_mwh
compute_energy_mwh
compute_utilization
curtailment_mwh
storage_throughput_mwh
heat_available_mwh_th
constraint_events
warnings
```

## Mandatory dispatch rule

Community priority load and required reserve constraints are satisfied before flexible compute whenever available generation/storage can do so.

## Validation rule

Planning-margin observations cannot be used as a default source for `generation_mw` or `compute_max_mw`.

## Determinism

Given the same scenario inputs, source datasets, model version, and deterministic settings, the engine should produce the same outputs.
