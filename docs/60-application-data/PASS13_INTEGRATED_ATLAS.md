# Pass 13 — Integrated App-Native Atlas

Date: 2026-08-30

## Purpose
Pass 13 is the first integrated atlas snapshot built for the Kristal Farms application model rather than as a sequence of standalone GeoJSON layers. It connects hydrology to community, marine, telecom, energy and legacy environment context through canonical IDs, relations, evidence and observations.

## What is integrated
- Pass 12 hydrology foundation: 24 rivers + 24 WSC stations and hydrology evidence.
- 20 legacy community reference points migrated as **approximate centroids**, plus Natuashish as geometry-null network context.
- Six conceptual research corridors with `geometry = NULL` and explicit `not_route=true`.
- Nunavik regional marine-port management context; no facility-specific heavy-lift inference.
- EAUFON-1/2 operating community relationships and EAUFON-3 planned 2027 relationships; no cable geometry invented.
- North Labrador ferry service relationships; no project-cargo certification inferred.
- Labrador North broadband withdrawal/unresolved replacement state.
- Current Labrador remote-diesel plant context for six communities.
- External reference energy entities: Innavik, Lac-Robertson and Quaqtaq/Puvirnituq wind contracts.
- Legacy environmental/no-go records migrated only as **unverified historical evidence**, never as active no-go decisions.

## Public release
Release `2026.08.30-pass13` is immutable and publishes only public-safe context. Legacy tiers are not included in community map properties.

## Showcase / Explorer
- `packages/catalog/catalog.pass13.json` is the data-driven layer catalog.
- `packages/showcase/story.pass13.json` defines six story scenes without custom React site logic.
- public fixtures include community points, official hydrometric stations, external references, search index, evidence-panel summaries and the 24-river evidence matrix.

## Remaining gaps
Pass 13 does **not** claim authoritative environment or Indigenous rights/governance coverage. These dimensions remain research-required. It also does not materialize official river/basin geometry, HYDAT flow series, project head, design flow, MW or site ranking.
