# OGC API

## Purpose

Expose publishable geospatial collections in a standards-oriented form so external GIS/software can use Kristal Farms data without depending on the Web application's internal contracts.

## Initial collections

Potential collections include:

```text
communities
energy_assets
reference_projects
corridors
candidate_sites
```

Only collections with appropriate geometry and publication classification should be exposed.

## Evidence

Evidence itself may be available through domain APIs or tabular endpoints; it should not be forced into a spatial collection when it has no geometry.

## Filters

Where supported, expose attribute, bbox, and temporal filtering. Keep authorization rules consistent with publication policy.
