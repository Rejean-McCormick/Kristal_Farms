# Kristal Farms API

## Responsibilities

- entity + evidence aggregation;
- search across entity classes;
- scenario create/read/update/archive;
- scenario evaluation;
- scenario comparison;
- authenticated annotations/workflows;
- catalog/policy retrieval when not fully static.

## Candidate endpoints

```text
GET  /v1/catalog
GET  /v1/policy
GET  /v1/search?q=
GET  /v1/entities/{entity_type}/{id}
GET  /v1/entities/{entity_type}/{id}/evidence
POST /v1/scenarios
GET  /v1/scenarios/{id}
PATCH /v1/scenarios/{id}
POST /v1/scenarios/{id}/evaluate
POST /v1/scenarios/compare
```

## Versioning

Use a path or media-type version strategy deliberately. The starter contract uses `/v1`.

## Evidence aggregation

Entity detail responses may aggregate linked evidence for convenience but should retain evidence/source IDs so clients can trace the underlying records.

## Scenario writes

Scenario writes must never mutate canonical research observations.
