# ADR-0005 — Immutable public data releases

**Status:** accepted  
**Date:** 2026-08-30

## Context

The public Showcase must be fast, scalable, stable, auditable, and separable from private/live research data.

## Decision

Publish stable public map datasets as versioned immutable artifacts, primarily PMTiles for vector data and COG for raster, distributed through object storage/CDN.

## Consequences

Live PostGIS remains the research source of truth. Public releases require a formal publish/QA pipeline and can be rolled back by changing the active release reference.
