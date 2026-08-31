# Offline satellite layer

The Geographic Observatory can display real satellite imagery at high zoom
without a runtime imagery provider.

## Product behavior

- Low zoom: Observatory contextual basemap.
- Regional zoom: Natural Earth relief fades gradually rather than to pitch black.
- High zoom: a local photographic tile pyramid fades in when published.
- Hydrography, boundaries, labels, stations and communities remain above it.
- `Layers → Satellite imagery` controls visibility.
- If no local snapshot has been published, the row is disabled and marked
  `LOCAL`.

The layer reads only `/public/imagery/` assets included with the product
release. It does not update automatically.

## Cartographic semantics

Satellite imagery is **context only**. It must never be presented as evidence
for a claim, a facility position, a corridor, a watershed boundary or a
project geometry unless a separately governed evidence/geometry record exists.

See `pipelines/imagery/README.md` for the manual build workflow.
