# Web application

Implementation home for the Kristal Farms **Showcase**, **Explorer** and **Scenario Studio**.

## Observatory Explorer vertical slice

The repository now includes a working first implementation of the map interaction specification in [`../../docs/frontend/map-observatory-interaction.md`](../../docs/frontend/map-observatory-interaction.md).

Implemented in this slice:

- Next.js + TypeScript application shell;
- MapLibre GL JS map canvas;
- governed public communities and hydrometric stations read server-side from `data/publish/current`;
- stable layer-catalog metadata read from `packages/catalog/catalog.json`;
- layer-catalog-driven visibility controls for the implemented map layers;
- proximity, delayed hover, selected and dimmed map feature states;
- semantic community and station markers with larger invisible pointer hit areas;
- floating hover recognition cards;
- persistent evidence-first Entity Inspector;
- non-geographic relation constellation inside the Inspector;
- URL state for camera, selected entity and comparison pins;
- search, map HUD and release telemetry;
- keyboard-focus targets that trigger the same recognition surface as pointer hover;
- mobile Inspector treatment and reduced-motion support.

External reference projects with `geometry: null` remain panel-only and are not fabricated as map points. Conceptual corridors remain `panel_only` per `packages/shared/visual_semantics.json`.

## Run locally

From this directory:

```bash
npm install
npm run dev
```

Then open `http://localhost:3000`.

The development basemap defaults to CARTO dark raster tiles. Production deployments should set:

```bash
NEXT_PUBLIC_BASE_TILE_URL="https://your-approved-provider/{z}/{x}/{y}.png"
```

or replace the development raster style in `lib/map-style.ts` with the governed production vector style.

## Data boundary

The client does **not** embed canonical community/station fixtures as React constants. Route handlers under `app/api/explorer/` read the current public release server-side, while stable layer metadata comes from `packages/catalog`. The Web application does **not** read `research/`, `pipelines/`, `data/raw/` or `data/fixtures/` at runtime. This is a vertical slice over governed published artifacts; the production data path remains the architecture defined by the repository:

```text
UI -> typed client -> API / tiles -> PostGIS
```

The route handlers are therefore an application boundary, not a replacement source of truth.
