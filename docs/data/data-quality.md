# Data quality

## QA levels

### Structural

- schema validity;
- required fields;
- valid IDs;
- valid geometry/SRID;
- unit conformity;
- date parsing;
- relation integrity.

### Provenance

- referenced source IDs exist;
- evidence is linked to a subject where appropriate;
- source dates/retrieval dates are captured where available;
- no orphan evidence unless intentionally standalone.

### Domain

- planning margin cannot populate compute-hosting fields;
- external references cannot silently become Kristal Farms candidates;
- ranking fields are blocked while ranking is disabled;
- scenario outputs cannot populate observed-data tables.

### Publication

- restricted data absent from public artifacts;
- release metadata/version present;
- artifact hashes recorded;
- expected row/feature counts checked.

## CI behavior

Critical QA failures must block publication. Warnings may be allowed only when documented and visible in the release report.

## Pass 8 baseline

The provided Pass 8 bundle reports 6 layers, 72 features, 15 sources, 21 screening override rows, no unexpected non-null geometries, no unknown source IDs, and no ranking-policy violations. Treat these as migration checks, not eternal target counts.
