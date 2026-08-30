# ADR-0002 — PostGIS as operational source of truth

**Status:** accepted  
**Date:** 2026-08-30

## Context

The application and data system must scale beyond static GeoJSON, support GIS professionals, preserve relationships/provenance, and serve multiple interfaces.

## Decision

Use PostgreSQL/PostGIS as the canonical operational database.

## Consequences

GeoJSON, GeoParquet, MVT, PMTiles, COG, and GeoPackage are derived/interchange representations. The frontend must not become the canonical store.
