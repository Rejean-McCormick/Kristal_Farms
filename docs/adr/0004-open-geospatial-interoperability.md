# ADR-0004 — Open geospatial interoperability

**Status:** accepted  
**Date:** 2026-08-30

## Context

Kristal Farms data should be usable by professional GIS users and external systems rather than only by the Kristal Farms frontend.

## Decision

Support PostGIS/QGIS workflows and standards-oriented geospatial APIs, initially OGC API features via pygeoapi where appropriate.

## Consequences

The platform retains an open data architecture. Domain-specific workflows may still use a separate FastAPI service rather than forcing them into OGC feature semantics.
