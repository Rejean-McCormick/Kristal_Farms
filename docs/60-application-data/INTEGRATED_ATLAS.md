# Integrated Atlas

**Release date:** 2026-08-30

## Purpose

The integrated atlas connects hydrology, communities, marine logistics, telecom, energy references, environment context and screening state through canonical IDs, relations, evidence and observations. It does not force every piece of knowledge into map geometry.

## Current integrated content

- 24 river references and 24 WSC hydrometric stations;
- community reference points explicitly marked as approximate centroids where applicable;
- conceptual research corridors with `geometry = NULL` and `not_route = true`;
- Nunavik marine-management context without facility-specific heavy-lift inference;
- operating/planned telecom relationships without invented cable geometry;
- North Labrador ferry/service context without project-cargo certification;
- selected external renewable-energy reference projects;
- legacy environmental records retained only as unverified historical evidence.

## Public release

Release `2026.08.30` is immutable and publishes only controlled public-safe context. Legacy screening tiers are not included in public community properties.

## Showcase / Explorer

- `packages/catalog/catalog.json` defines the data-driven layer catalog;
- `packages/showcase/story.json` defines the guided narrative without custom site logic;
- `data/publish/current/` contains current public artifacts.

## Remaining gaps

The atlas does not establish authoritative environment or rights/governance coverage for candidate projects. It also does not automatically materialize official river/basin geometry, full HYDAT flow series, project head, design flow, MW or site ranking.
