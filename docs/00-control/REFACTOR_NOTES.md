# Refactor Notes — 2026-08-17

## Refactor stage 1 — repository orchestration

The first refactor reorganized the supplied material around control and orchestration rather than file type. It integrated structured site/hydro/map data, Labrador and Nunavik screening studies, economic/transmission/cooling studies, bilingual deployment plans, and the complete 15-document French logo-DOCX package.

## Refactor stage 2 — strategic v2 integration

The second refactor changes the **center of gravity of the project narrative**.

Kristal Farms is no longer framed only as a cold-climate hydro-powered data-centre project. The v2 platform thesis is:

> **Bring compute to renewable energy that is difficult or expensive to export; consume energy locally, export digital value by fibre, reuse the heat, preserve the tenant data boundary, and deploy through compact, reversible, evidence-gated infrastructure.**

### New strategic dimensions integrated

1. **Resource valorization** — test whether remote/difficult-to-export rivers and renewable assets can become useful through local compute demand.
2. **Avoided transmission** — compare local compute/fibre architecture against long electrical corridors on both cost and lifecycle/ecological footprint.
3. **Fibre as export infrastructure** — elevate connectivity from utility to primary value-export corridor.
4. **Coastal/subsea fibre** — create a dedicated research track for landings, marine routes and multi-node resilience.
5. **Data security** — elevate black-box tenancy and higher-assurance options as core differentiators.
6. **Secure mines/brownfields** — add an exploratory site archetype for hardened/decommissioned infrastructure, without assuming technical feasibility.
7. **Harmonious integration** — treat community process, training, enabling infrastructure, fibre, energy, compute and heat as a staged integration sequence.
8. **Northern fibre crown/network** — add a future multi-node platform architecture workstream.
9. **Northern expertise** — treat repeated cold/coastal/remote construction and operations know-how as a platform asset.
10. **Future AI infrastructure** — add Québec–Labrador high-density AI compute positioning as a market hypothesis requiring validation.

## Major repository changes

1. Added `STRATEGIC_PRINCIPLES.md` as the v2 control framing.
2. Added matched EN/FR platform-vision documents under `docs/10-core/strategy/`.
3. Updated the Internal Reference so its village hydro design is explicitly the first detailed **site archetype**, not the whole future platform.
4. Added owner-direction provenance under `sources/owner-direction/` so intent is not confused with evidence.
5. Expanded `DECISIONS_REQUIRED.md`, `CLAIMS_TO_VALIDATE.md` and `WORKSTREAMS.md` for transmission footprint, subsea fibre, secure sites, network architecture and AI demand.
6. Added a strategic infrastructure research agenda.
7. Preserved the 15-document partner package as **v1** and added a document-by-document v2 rebuild map.
8. Added a matched EN/FR working v2 partner overview.
9. Updated document authority and bilingual controls so polished v1 PDFs/DOCX cannot be mistaken for v2 synchronized releases.
10. Added a GitHub strategic-hypothesis issue template and expanded PR controls for sensitive fibre/security/environment/market claims.

## Important non-merge decisions

The v2 refactor intentionally does **not**:

- claim that local compute is always cheaper than transmission;
- claim a categorically lower ecological footprint without a defined comparison;
- claim a specific subsea-fibre route, landing point or commercial arrangement;
- claim that a decommissioned mine is automatically safe or suitable for compute;
- claim future AI demand or Québec/Labrador market share as a fact;
- replace Nain as the current first application;
- silently rewrite old PDFs/DOCX and label them v2;
- make Nunavik an active project geography by default;
- make coastal wind mandatory at every site;
- clean citation-contaminated research by inventing replacement sources.

Those items are surfaced as controlled decisions and evidence-producing workstreams.
