# Information architecture

Kristal Farms uses two complementary information axes. They are intentionally separated so a reader can distinguish **project/domain authority** from **software/data-platform implementation** without guessing from filenames.

## Project and domain axis

| Area | Purpose | Authority tendency |
|---|---|---|
| `docs/00-control/` | Current project state, principles, decisions and release interpretation | C0 |
| `docs/10-core/` | Physical/commercial **project reference architecture**, deployment and tenancy | C1 |
| `docs/30-site-screening/` | Site/corridor screening methods and technical research | C4 |
| `docs/40-economics/` | Economic research and benchmark methods | C4 |
| `docs/50-research/` | Active domain/commercial/governance research | C4 |
| `docs/70-long-horizon/` | Optional long-horizon concepts | C4L |

## Software and data-platform axis

| Area | Purpose |
|---|---|
| `docs/architecture/` | Software/data-platform architecture and system boundaries |
| `docs/data/` | Application data model, evidence, provenance, hydrology/economic data contracts and publishing semantics |
| `docs/product/` | Product surfaces and product-facing data contracts |
| `docs/frontend/` | Interaction, cartography, accessibility and UI implementation rules |
| `docs/api/` | Service/API contracts and behavior |
| `docs/scenarios/` | Scenario-engine contracts and economic scenario method |
| `docs/operations/`, `docs/security/`, `docs/testing/` | Operational controls |
| `docs/adr/` | Durable technical decision history |

The former `docs/60-application-data/` bucket was removed because it mixed this second axis back into the numbered project/domain axis. Its documents now live under `data/`, `product/` or `scenarios/` according to responsibility.

## Repository information flow

```text
sources / research
        ↓ promotion + validation
pipelines / database / contracts / packages
        ↓ governed publish/API/tiles
apps / services
```

`archive/` is historical provenance, not active authority. It remains versioned but is excluded from default local search/index behavior through the root `.ignore`; historical work should opt into `archive/` explicitly.

## Observatory workspace model

The top-level Observatory remains a flat six-workspace cockpit for speed, but the workspaces have a stable conceptual grouping:

- **Explore** — Northern Atlas, Villages, Corridors.
- **Evaluate** — Economics.
- **Govern** — Evidence, International Portfolio.

The grouping describes user intent; URLs remain stable (`section=atlas|villages|corridors|economics|evidence|international`). The International Portfolio may currently contain twelve planning slots, but the count is state, not navigation taxonomy.
