# Repository Orchestration

Kristal Farms work follows a controlled chain from evidence to project decisions.

## Core chain

**Source → research → reproducible pipeline → evidence/observation → validation → canonical data → decision gate → publishable release → product**

The repository uses a directional dependency rule:

```text
research/ -> pipelines/data/contracts/packages -> apps/services
```

`apps/` and `services/` must not execute exploratory research or ETL code at runtime.

Community, Indigenous rights, environmental review, engineering, logistics, telecom and economics are independent evidence domains. No single technical layer can silently override the others.

## Working loop

1. Review open decisions and evidence gaps.
2. Update the relevant corridor or domain dossier.
3. Preserve source provenance and uncertainty.
4. Run automated validation and tests.
5. Promote only reviewed data into canonical/current state.
6. Regenerate publishable views from canonical data.
7. Review security, rights, privacy and public-release implications.
8. Record material architecture decisions in ADRs.

## Release gates

A public or partner-facing release should not ship unless:

- project scope and terminology are current;
- numeric claims retain source/as-of context;
- approximate, conceptual and verified geometry are visually distinct;
- external references are not presented as Kristal Farms projects;
- screening remains unranked unless governance explicitly changes that policy;
- restricted data is excluded before artifact generation;
- site-specific claims are no stronger than the underlying evidence;
- current documentation, machine-readable contracts and publish outputs agree.

See `docs/00-control/` and `docs/adr/`.
