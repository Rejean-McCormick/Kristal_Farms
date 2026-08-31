# Research workspace

`research/` is the active exploratory workspace for Kristal Farms.

It exists to keep exploratory analysis separate from reproducible data production and from the Observatory product.

## Boundary

```text
research/
   exploratory questions, notebooks, candidate analysis, prototypes
        |
        | explicit promotion / review
        v
pipelines/ + data/ + packages/
   reproducible ingest, validation, contracts, publish artifacts
        |
        | immutable/read-only consumption
        v
apps/web/
   Observatory / Showcase / Scenario Studio presentation
```

Research is **not** an application dependency and is **not** a publication surface.

## Allowed here

- exploratory scripts and notebooks;
- source-comparison work;
- candidate-generation experiments;
- one-off diagnostics;
- methods under active investigation;
- intermediate research notes that are not yet governed application data.

## Not allowed here

- frontend/runtime imports from `apps/` or `services/`;
- canonical or publish-ready datasets presented as current truth;
- secrets or restricted source material that violates repository policy;
- silent promotion of research conclusions into `data/publish/current`;
- business rules implemented only in an exploratory notebook or script.

## Promotion rule

A research result becomes product-consumable only after it has a reproducible path through the data platform. Depending on the result, that normally means:

1. preserve source/provenance;
2. implement or update a pipeline under `pipelines/`;
3. validate against contracts/schemas;
4. promote to canonical/current data state;
5. generate a governed publish artifact under `data/publish/current` or a governed API/view;
6. let applications consume that published contract read-only.

The application must never read directly from this directory.

## Workstreams

- [`hydrology/`](hydrology/) — river, basin, station and hydro-resource exploration;
- [`energy/`](energy/) — generation/reference-system exploration;
- [`communities/`](communities/) — community context research before canonicalization;
- [`experiments/`](experiments/) — cross-domain or short-lived methodological experiments.

Historical/superseded research remains under `archive/`; do not move archived material back into active state merely to make it easier to find.
