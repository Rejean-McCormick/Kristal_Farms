# Labrador external electrical projects

**Status:** research context  
**Ranking:** disabled  
**Runtime rule:** applications consume governed published artifacts only; they never read this research registry directly.

## Why this registry exists

`grid_reach` represents documented existing electrical-network context. It must not be polluted with projects that are merely funded, under study, in procurement, rejected by a regulator, or otherwise not operating infrastructure.

`research/grid/electrical_projects.yaml` is the source-backed research registry for those external projects. `pipelines/curate/sync_electrical_projects.py` deterministically syncs the registry into canonical fixture tables (`core_entity`, `core_project`, entity relations, evidence and sources). `pipelines/publish/build_external_reference_energy_public.py` then publishes the governed external-reference layer.

The flow is:

```text
research/grid/electrical_projects.yaml
        ↓ explicit curation sync
canonical fixtures + provenance
        ↓ publisher
external_reference_energy_public.json
        ↓ target-village join / external-reference surfaces
web UI
```

## Status discipline

The registry keeps operating, active, procurement, funded, feasibility and rejected states separate. A source-backed project status never promotes the project into the existing-grid layer. In particular:

- the Nain wind project is an active external project, not operating generation;
- its collector connection is a local 34.5 kV project with no governed route geometry, not a main-grid interconnection;
- the Rigolet tidal record is a feasibility/measurement project only;
- the Labrador isolated-community interconnection record is a system-options study with no selected route;
- the Southern Labrador Regional Interconnection remains `not_approved_2025_appeal_context` and must not be rendered as a committed line.

## Village coverage

The governed references cover Nain, Hopedale, Makkovik, Postville, Rigolet and Natuashish in northern Labrador, plus documented projects/programs in Cartwright, Black Tickle, Norman Bay, Paradise River, Charlottetown, Pinsent's Arm, Lodge Bay, Port Hope Simpson, Mary's Harbour and St. Lewis.

Target-village dossiers do not duplicate project facts. They join projects through canonical community relations (or community metadata where no canonical community entity is yet present).

## Enabling infrastructure is separate

`research/infrastructure/enabling_corridors.yaml` stores the Road to the North as a conceptual enabling corridor. It has `geometry: null`, `electrical_commitment: false` and is not an electrical project. This keeps a studied road corridor from becoming a synthetic power-line route.

## Geometry rule

Null geometry is intentional. Do not draw a straight line merely because endpoints or communities are known. A geometry can be added only when a governed source-backed route/site geometry is ingested with appropriate semantics and confidence.
