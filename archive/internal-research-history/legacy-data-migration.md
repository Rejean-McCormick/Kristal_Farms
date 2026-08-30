# Pass 8 migration

This document maps the supplied **Kristal Farms Research Pass 8 — Energy systems and hosting architecture** bundle into the target platform.

## Source bundle baseline

Pass 8 contains:

- layers 28–33 under `data/layers/pass8/`;
- Hydro-Québec autonomous-grid planning-margin CSV;
- 21-row screening-state override;
- controlled source registry;
- architecture rules/corrections;
- machine QA.

The bundle reports a passing QA state.

## Key migration principle

Most Pass 8 GeoJSON features intentionally contain:

```text
geometry: null
geometry_role: status_record_no_geometry
```

They are primarily **research/evidence records**, not direct map features.

Do not invent coordinates during migration.

## Layer 28 — isolated and remote energy systems

Target:

- create/match `core.place` or `core.asset` subjects when a separately sourced canonical geometry exists;
- store Pass 8 descriptive record as evidence/reference data;
- preserve `large_compute_hosting_from_existing_grid_not_inferred` and `community_load_priority_required` as domain assertions/policy-backed metadata.

## Layer 29 — Hydro-Québec planning margins

Target:

```text
research.observation
metric = planning_power_margin_after_planning_criterion_kw
unit = kW
```

One observation per network and planning period is preferred over embedding the whole time series in a single JSON property.

Mandatory semantic constraint:

```text
planning margin != available compute capacity
```

## Layer 30 — renewable transition reference projects

Target:

- `core.project` for canonical external projects where geometry/identity is established;
- `role = external_reference`;
- evidence records for capacity, operating status, ownership, diesel reduction, and reference value.

## Layer 31 — diesel displacement evidence

Target:

`research.observation` + linked evidence/source.

Preserve whether values are actual, reported, projected, or estimated.

## Layer 32 — corridor energy context

Target:

Primarily evidence/context records linked to regions/corridors. Do not turn contextual regions into precise corridor geometries without a source.

## Layer 33 — Québec data-centre regulatory context

Target:

Research/regulatory evidence linked to the Québec jurisdiction. Regulatory status should be time-aware. Do not encode unresolved applicability as true/false when it is unknown.

## Screening override

`SCREENING_STATE_OVERRIDE.csv` becomes a governed screening-state dataset. Active policy is unranked screening. Legacy tiers remain provenance only.

## Source registry

`sources_pass8.json` seeds `research.source`. Preserve the existing `SRC-*` identifiers as migration aliases even if canonical source IDs later use another internal format.

## QA migration tests

During first import, verify at minimum:

- all 15 Pass 8 source IDs resolve;
- all 72 layer features are accounted for;
- no duplicate feature IDs;
- no fabricated geometries;
- 21 screening override rows imported;
- maximum supplied planning-margin snapshot remains 2007 kW;
- the negative planning-margin value remains represented, not silently clipped;
- ranking remains prohibited.
