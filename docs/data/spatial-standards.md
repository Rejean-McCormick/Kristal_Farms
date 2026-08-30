# Spatial standards

## Canonical storage

Use PostGIS geometry/geography with an explicit SRID.

## Web interchange

Web map delivery typically uses WGS84/Web Mercator-compatible representations. Preserve source CRS metadata during ingestion and transform intentionally.

## Precision

Do not publish more spatial precision than the source supports.

Examples:

- community centroid source → centroid-level representation;
- region-only evidence → no fabricated point;
- conceptual corridor → visibly conceptual line with source/assumption metadata.

## Geometry validity

Ingestion QA must check:

- valid geometry;
- expected geometry type;
- non-empty geometry where required;
- coordinate bounds;
- SRID;
- unexpected geometry presence for records defined as non-spatial.

## Generalization

Large layers should have zoom-appropriate simplification or tile generalization. The canonical geometry should remain unsimplified unless source data itself is generalized.
