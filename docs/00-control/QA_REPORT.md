# Repository QA Report

**Refactor date:** 2026-08-17

## Structural checks

- Partner package completeness: **15/15** numbered documents have EN Markdown, EN PDF, FR PDF, and FR logo DOCX.
- New structured data integrated:
  - **21** village/community inventory records;
  - **58** Labrador hydro records;
  - **88** map-point records.
- Cost workbook inspected:
  - 5 sheets (`Dashboard`, `Cost_Model`, `Chart_Data`, `Partner_Message`, `Sources`);
  - illustrative index model only, not a validated project finance model.
- New analysis DOCX sources are preserved unchanged under `sources/originals/`.
- Raw CSV/XLSX data is preserved under `data/raw/`.
- No individual repository file approaches GitHub's 100 MB per-file limit.
- Territorial-politics scope guardrail is explicit in `SCOPE_BOUNDARIES.md`, README and v3 strategy.
- Matched EN/FR human-infrastructure strategy documents are present.
- Matched EN/FR international-learning strategy documents are present.
- Matched EN/FR Human Dignity Framework documents are present.
- Bilingual host-language charter templates and education/university gate documents are present.
- Current partner working overview is v3; v2 working drafts are retained only for traceability.

## Link check

A repository-wide relative Markdown-link check of active root/docs/catalog material checked **103** normal relative links and found **0 missing**.

The preserved pre-refactor archive contains **10 stale relative links** that point to its historical folder layout. They are intentionally not rewritten because the archive is retained as a snapshot, not active navigation. One legacy source also contains an opaque `file://file_...` style reference inherited from its source environment; it is retained rather than repaired by guessing.

## Publication blockers

Two working research files contain non-portable assistant/UI citation artifacts:

- `docs/30-site-screening/nunavik/Rivieres_littoral_ouest_Nord_quebecois_nord_La_Grande.md`
- `docs/50-research/Partners_inventory_deep-research-report.md`

Both are explicitly marked with a publication-blocker warning.

## Source hygiene

- `utm_source=chatgpt.com` tracking parameters were removed from searchable Markdown extractions.
- Original supplied DOCX sources remain unchanged.
- No missing sources were invented to repair citation artifacts.
- Literary/fictional/ethics-demo material is not treated as factual project evidence unless separately promoted through project control.

## Final repository size

- Files: **178**
- Size: **47.5 MiB**
- Hash manifest: `data/catalog/FILE_MANIFEST.csv`


## Pass 9 QA — Hydro Resource Atlas

- Target river references: **24**.
- Official WSC station point geometries: **24**.
- New structured layers: **7** (34–40).
- Basin polygons fabricated: **0**.
- River flowlines fabricated: **0**.
- Project head/design flow/MW values introduced: **0**.
- Ranking/suitability values introduced: **0**.
- Official binary geometry retrieval failures are recorded, not hidden.

Machine QA: `data/processed/pass9/QA_PASS9.json`.


## Pass 10 QA — official geometry pipeline

- WSC basin inclusion registry: **24/24 target stations confirmed**.
- New layers: **7** (41–47), **128 records**.
- Operational request-window polygons: **24**, explicitly not basin/reach/project geometry.
- Natural-feature basin/reach geometry newly ingested: **0**.
- Project head/design flow/MW/ranking fields populated: **0**.
- Pass-10 scripts compile: **yes**.
- Synthetic terrain test: **PASS**; outputs are test-only.

Machine QA: `data/processed/pass10/QA_PASS10.json`.


## Pass 11 QA — 2026-08-30

- canonical entities: 48 (24 rivers + 24 WSC station assets);
- evidence: 48; observations: 24; screening states: 240; ingestion jobs: 125; dataset schemas: 3;
- canonical physical geometries: 24 WSC station Points only;
- river/watershed geometry invented: 0;
- project head/design flow/MW observations: 0;
- ranking allowed: false;
- Pydantic schemas generated; platform validation script and pytest suite included.

Machine QA: `data/processed/pass11/QA_PASS11.json`.


## Pass 12 QA — 2026-08-30

- 24 canonical hydrometric stations retained.
- 72 station/collection HYDAT jobs registered: daily, monthly, annual statistics.
- Full real HYDAT observation series materialized in this runtime: **0** (DNS blocker recorded).
- Derived real climatology rows: **0** until source series are materialized and coverage gates pass.
- Synthetic derivation tests validate 12 monthly climatology outputs and lineage metadata.
- `design_flow_m3s`, project head, MW, hosting capacity and ranking remain forbidden outputs of the hydrology observation pipeline.
- Natashquan WSC/CEHQ area values are both preserved; no silent overwrite.


## Pass 13 QA — integrated app-native atlas

- canonical entities: **92**; places: **22**; assets: **32**; external/reference projects: **4**; corridors: **10**;
- canonical entity relations: **126**;
- sources: **37**; evidence records: **116**; observations: **100**; screening states: **240**;
- public communities: **20** approximate legacy community centroids, never port/project coordinates;
- published official WSC station points: **24**;
- public catalog layers: **12**; Showcase scenes: **6**;
- legacy tiers/ranking fields leaked into public community release: **0**;
- conceptual corridors with invented geometry: **0**;
- active no-go decisions inferred from legacy environment records: **0**;
- forbidden hosting capacity/design flow/project head/MW observations: **0**;
- relative Markdown links checked in active docs/catalog: **136**, missing: **0**.

Machine results are stored in `data/processed/pass13/QA_PASS13.json` and `data/processed/pass13/REPO_QA_PASS13.json`.


## Pass 14 QA — economic frontier

- economic benchmark records: **10**; all `usable_as_site_estimate=false`;
- scenario templates: **3**; all non-site and ranking disabled;
- generic sensitivity cases: **64**;
- cases labelled project savings/NPV/IRR: **0**;
- fibre references promoted from funding proxy to total construction cost: **0**;
- Kristal site-specific CAPEX silently set to zero: **0**; unknown components remain `UNPRICED`;
- automatic bankable NPV/IRR function: **blocked by design**;
- public catalog layers after Pass 14: **15**;
- Showcase scenes after Pass 14: **7**.

Machine QA is stored in `data/processed/pass14/QA_PASS14.json`.

Pass-14 execution result: **36/36 pytest tests PASS**; economic recomputation matches the published 64-case table; active docs/catalog relative Markdown links checked: **140**, missing: **0**. The conservative reference frontier is positive in **60/64** generic stress cases and non-positive in **4/64**; these counts are sensitivity behavior, not site probabilities.
