# Visual regression

## Scope

Visual regression is valuable for:

- Showcase hero scenes;
- key camera transitions at resting states;
- legend/symbol semantics;
- hypothesis vs verified styling;
- terrain-enabled scenes;
- Evidence Panel layout;
- reduced-motion variants.

## Avoid brittle tests

Do not snapshot every map pixel across arbitrary basemap/network conditions. Prefer controlled fixtures, deterministic map states, and stable screenshots for a curated set of important scenes.

## Semantic review

A visual diff that is aesthetically acceptable can still be wrong if it weakens uncertainty or hypothesis cues. Review cartographic semantics, not only pixel similarity.
