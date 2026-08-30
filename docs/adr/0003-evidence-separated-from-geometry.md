# ADR-0003 — Evidence separated from geometry

**Status:** accepted  
**Date:** 2026-08-30

## Context

Historical research contains valid records whose geometry is intentionally null. Forcing every claim into a map geometry would invent spatial precision and blur the difference between evidence and physical objects.

## Decision

Model sources, evidence, observations, and evidence relations separately from places/assets/projects/corridors.

## Consequences

The UI fetches evidence related to selected spatial subjects. Non-spatial evidence remains first-class data. Import pipelines must not fabricate coordinates merely for visualization.
