# Backend architecture

## Service responsibilities

### Kristal Farms API — FastAPI

Owns domain-specific operations that do not map naturally to generic geospatial standards:

- scenario CRUD/evaluation;
- entity evidence aggregation;
- cross-domain search;
- comparison operations;
- authenticated annotations/workflows;
- model execution.

### OGC API — pygeoapi

Provides standards-based access to publishable geospatial collections.

### Tile service — Martin

Provides MVT tiles from PostGIS and/or prepared tile sources.

## Deployment principle

These are logical services. During early development they may share infrastructure or deployment units. Separate them operationally only when scaling, security, or ownership requires it.

## API boundary

No browser should receive direct database credentials. QGIS access is a separate professional workflow with controlled database roles.

## Business rules

Domain rules belong in a testable model/service layer. Route handlers should validate input, authorize operations, call domain functions, and serialize results.
