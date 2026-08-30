# Data tests

## Required suites

### Identity

- IDs are unique within namespace;
- foreign relations resolve;
- source IDs resolve;
- stable aliases do not collide.

### Spatial

- geometry validity;
- expected geometry types;
- valid CRS/SRID;
- no fabricated geometry on records marked non-spatial;
- publish precision rules respected.

### Semantic

- unit is compatible with metric;
- project roles use allowed enum;
- unresolved regulatory applicability remains nullable/unknown;
- actual/projected/reported observations preserve their qualifier.

### Kristal Farms policy

- planning-margin metrics cannot populate compute capacity fields;
- public ranking outputs absent while ranking is disabled;
- external references do not default to candidates;
- community priority flag/rule preserved in relevant scenario logic.

### Release

- no restricted records/fields in public outputs;
- manifest/checksums exist;
- artifact counts align with publish views;
- release identifiers are immutable.
