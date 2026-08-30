# Pass 13 — Explorer Contract

## Primary entity flows
- select community → show marine/telecom/energy context and evidence
- select WSC station → show source/observations and related river
- select river → show 10-dimension evidence matrix, monitoring station and contextual relations
- select external reference project → show role/status/source and linked community

## API targets
- `GET /catalog`
- `GET /entities/{id}`
- `GET /entities/{id}/evidence`
- `GET /entities/{id}/screening`
- `GET /search`
- `GET /showcase/stories/kristal-core-thesis`

## No implicit ranking
List order defaults to name/type/relevance, never site merit. Marker size is uniform for communities. Evidence status is visually distinct from opportunity quality.
