# Project Direction — Application and Data Architecture

**Captured:** 2026-08-30
**Authority:** project/application architecture direction, not external technical evidence.

The Kristal Farms application is data-driven and uses PostgreSQL/PostGIS as its intended operational source of truth. It separates geography from evidence, observations and scenarios, and keeps screening unranked.

The application should connect hydrology, communities, logistics, telecom, energy, environment, governance and economics through canonical IDs and provenance rather than forcing all knowledge into map geometry.

Public Showcase data is a versioned release; live research may evolve independently. Community priority, planning-margin != compute-capacity, external-reference != project-candidate and no-ranking rules are mandatory.
