# Explorer data contract

## Primary entity flows

- select community → show marine/telecom/energy context and evidence;
- select hydrometric station → show source/observations and related river;
- select river → show evidence dimensions, monitoring station and contextual relations;
- select external reference project → show role/status/source and linked context.

## API targets

- `GET /catalog`
- `GET /entities/{id}`
- `GET /entities/{id}/evidence`
- `GET /entities/{id}/screening`
- `GET /search`
- `GET /showcase/stories/kristal-farms-core-thesis`

## No implicit ranking

List order defaults to name/type/relevance, never site merit. Marker size is not a merit signal. Evidence status is visually distinct from opportunity quality.
