# Frontend architecture

## Stack

- React
- TypeScript
- Next.js
- MapLibre GL JS
- deck.gl

## Major modules

```text
AppShell
├── Showcase
│   ├── StoryDirector
│   ├── CameraDirector
│   ├── NarrativePanel
│   └── ShowcaseMap
├── Explorer
│   ├── MapWorkspace
│   ├── LayerCatalog
│   ├── Legend
│   ├── FilterPanel
│   ├── Timeline
│   ├── EvidencePanel
│   └── DataDrawer
└── ScenarioStudio
    ├── ScenarioEditor
    ├── SystemDiagram
    ├── Assumptions
    ├── Results
    └── Compare
```

## State categories

### URL state

Must be serializable for shareable views:

- map camera;
- selected entity;
- mode;
- visible layers;
- selected timeline period;
- filters;
- comparison IDs where safe.

### Server state

Fetched from APIs or tile metadata. Use a dedicated query/cache layer rather than duplicating remote records into global UI stores.

### Local UI state

Panel width, temporary hover state, local display preferences.

## Layer rendering

Generic map layers must be instantiated from the layer catalog. Custom React code is justified for special interactions such as scenario editing, animated system flows, or bespoke 3D engineering visualization.

## Type safety

Frontend types should be generated or shared from machine-readable contracts wherever practical. Avoid hand-maintained duplicate enums between frontend and backend.
