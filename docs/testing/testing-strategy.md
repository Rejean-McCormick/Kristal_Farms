# Testing strategy

## Layers

### Unit tests

- domain rules;
- unit conversions;
- catalog parsing;
- scenario functions;
- permission/policy evaluation.

### Integration tests

- PostGIS repositories;
- API endpoints;
- OGC configuration;
- Martin/publish views;
- migration compatibility.

### Data tests

- schema and relation integrity;
- provenance;
- units;
- geometry validity;
- Pass 8 migration expectations;
- publication classification checks.

### UI tests

- layer toggles;
- selection/inspector;
- timeline;
- URL state;
- authentication/authorization states;
- reduced-motion behavior.

### Visual regression

Use for cartographic and Showcase scenes where styling/camera changes can materially alter communication.

## Policy tests

Automated tests must explicitly fail if implementation creates forbidden ranking outputs while `ranking_allowed` is false or reuses planning-margin metrics as compute capacity.
