# ADR-020 — One monorepo with three logical systems

## Status

Accepted

## Context

Kristal Farms contains exploratory research, reproducible geospatial/data pipelines and a Web product. As the Observatory implementation began, hydrology research concerns and frontend display concerns became easy to treat as one implementation surface even though they have different lifecycle, quality and dependency rules.

The project needs a boundary that keeps research fast, data publication governed and product code stable without introducing the operational overhead of multiple repositories prematurely.

## Decision

Keep one canonical Git repository and divide it into three logical systems:

1. **Knowledge / research** — `research/` plus controlled source/research documentation. Exploratory and non-runtime.
2. **Data platform / contract** — `pipelines/`, `database/`, `contracts/`, `packages/` and `data/`. Reproducible ingest, validation, canonicalization and publication.
3. **Product** — `apps/` and `services/`. Showcase, Explorer/Observatory and Scenario Studio runtime surfaces.

Dependencies flow toward governed publication:

```text
research -> data platform -> product
```

Product runtime code must not import or execute `research/` or `pipelines/`. File-based development consumers may read immutable `data/publish/...` artifacts and stable package/contracts. Production continues to target governed APIs/tiles backed by PostGIS.

## Consequences

### Positive

- research can remain exploratory without weakening application semantics;
- Observatory can evolve independently from hydrology methodology;
- data publication becomes the explicit contract boundary;
- cross-cutting changes can still be reviewed atomically in one pull request;
- repository splitting remains possible later because dependencies are already directional.

### Costs

- some concepts appear in both research documentation and product documentation and must be linked rather than conflated;
- promotion from research to product requires deliberate pipeline/contract work;
- automated boundary tests are needed to prevent convenient direct imports.

## Alternatives considered

### Three repositories

Rejected for now. It would require independent versioning, coordinated releases and cross-repository CI before those costs are justified.

### Two repositories (research/data and product)

Deferred. This can become appropriate when the Web application has an independent deployment/release team or when public data contracts are versioned as an external dependency.

### One repository without enforced boundaries

Rejected. Folder proximity must not allow exploratory research to become an implicit application dependency.
