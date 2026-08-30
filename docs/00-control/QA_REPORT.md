# Repository QA

**Current validation date:** 2026-08-30

## Automated status

- Python tests: **32 passed**.
- Domain model validator: **PASS** — 92 entities, 24 hydrometric stations, 24 river references, 100 observations, 240 screening-dimension states.
- Hydrology validator: **PASS** — 72 HYDAT ingestion jobs; no fabricated observation series.
- Integrated atlas validator: **PASS** — 92 entities, 126 relations, 15 catalog layers, 7 Showcase scenes.
- Economics validator: **PASS** — 10 benchmarks, 3 scenarios, 64 sensitivity cases.
- Active repository Markdown links: **101 checked, 0 broken**.
- Wiki links and local assets: **74 checked, 0 broken**.
- Repository-hygiene tests: **PASS** — no internal research numbering, retired product naming, unrelated project terminology or superseded siting rules in active surfaces.
- Screening: **unranked**.

## Required invariants

- Planning margin is not converted into hosting capacity.
- Project head, design flow and buildable MW are not inferred by generic hydrology pipelines.
- Conceptual corridors do not gain synthetic route geometry.
- External reference projects are not silently promoted to Kristal Farms candidates.
- Economic benchmarks remain reference-only and cannot produce bankable NPV/IRR automatically.
- Unknown and unpriced inputs remain explicit.
- Public releases contain no legacy ranking fields or private data hidden only by UI state.
- Active project documentation uses current Kristal Farms terminology.
- Superseded working-source extractions and old deployment narratives remain outside active documentation.

Historical QA and older research snapshots are preserved under `archive/` for provenance only.
