# QGIS workflow

## Purpose

QGIS is the professional desktop GIS interface for authorized analysis and editing against the same canonical PostGIS data used by the Web platform.

## Access model

Use dedicated database roles. Analysts should not connect with migration/admin credentials.

## Recommended workflows

- inspect canonical geometries and attributes;
- edit approved spatial datasets;
- run spatial analysis;
- validate imported data;
- create working layers in explicitly non-canonical schemas;
- export controlled deliverables.

## Editing rules

Research evidence/provenance should not be bypassed by directly editing derived publish views. Canonical writes should target documented editable tables or controlled import workflows.

## Styling

QGIS project styles may support professional workflows, but the Web application's MapLibre style remains a separate product artifact. Do not treat one as an automatically faithful rendering of the other unless a deliberate style-conversion pipeline is adopted.
