# Design system

## Product character

The interface should communicate northern geography, infrastructure, precision, and technical seriousness without resembling a generic enterprise GIS theme.

## Two densities

### Showcase density

- large editorial typography;
- fewer controls;
- cinematic spacing;
- guided narrative;
- strong visual hierarchy.

### Explorer density

- compact technical controls;
- persistent metadata/evidence access;
- tables and filters;
- predictable workstation layout.

Shared tokens should keep both modes recognizably one product.

## Semantic tokens

Define design tokens for object/status semantics rather than hardcoding colors in components. Example namespaces:

```text
community.*
asset.energy.*
project.external_reference.*
scenario.*
evidence.verified
evidence.unknown
corridor.conceptual
```

Do not create `site.good`, `site.bad`, or equivalent ranking semantics while ranking is disabled.

## Map interaction character

The map-specific expression of these tokens is defined in [Map observatory interaction](map-observatory-interaction.md). The “Observatory” language is intentionally restrained: precision, hierarchy, evidence state, and responsive focus create the technical character; permanent glow and decorative telemetry do not.
