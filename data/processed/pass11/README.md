# Pass 11 — platform-native migration package

This directory is the first application-oriented representation of the hydro research stack.

It does **not** replace Pass 9/10 source artifacts. Those remain provenance/reproducibility inputs. Pass 11 adds canonical fixtures and contracts that can be loaded into the proposed Kristal Farms application data model.

Key contents:

- `fixtures/` — canonical entity/source/evidence/observation/screening/job records;
- `database/` — PostGIS migrations, seeds and publish/validation views;
- `schemas/` — Pydantic and JSON Schema contracts;
- `catalog/` — data-driven map-layer catalog;
- `pipelines/` — migration, WSC flow-ingestion and validation scripts;
- `publish/` — derived public GeoJSON fixture;
- `PASS_11_REPORT.md` and `QA_PASS11.json`.

Only WSC monitoring-station points are physical geometry in the current canonical fixture. River and watershed geometry remains absent until official ingestion succeeds.
