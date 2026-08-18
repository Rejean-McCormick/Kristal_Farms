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

A repository-wide relative Markdown-link check of active root/docs/catalog/wiki material checked **137** relative links and found **0 missing**. GitHub Wiki extensionless sidebar links were resolved against their `.md` pages.

The preserved pre-refactor archive contains **10 stale relative links** that point to its historical folder layout. They are intentionally not rewritten because the archive is retained as a snapshot, not active navigation. One legacy source also contains an opaque `file://file_...` style reference inherited from its source environment; it is retained rather than repaired by guessing.

## Publication / promotion status

The repository is **public by default** under `PUBLICATION_POLICY.md`. Working drafts and imperfect research may remain visible when clearly labeled. “Not publication-ready” blocks promotion as authoritative evidence; it does not automatically block repository visibility.

Two working research files contain non-portable assistant/UI citation artifacts:

- `docs/30-site-screening/nunavik/Rivieres_littoral_ouest_Nord_quebecois_nord_La_Grande.md`
- `docs/50-research/Partners_inventory_deep-research-report.md`

Both require citation cleanup before their claims are promoted into formal partner, engineering, regulatory or investor materials.

## Source hygiene

- `utm_source=chatgpt.com` tracking parameters were removed from searchable Markdown extractions.
- Original supplied DOCX sources remain unchanged.
- No missing sources were invented to repair citation artifacts.
- Literary/fictional/ethics-demo material is not treated as factual project evidence unless separately promoted through project control.
- A basic credential/secret-pattern scan of the public working tree found no obvious private keys, GitHub/API tokens, AWS access-key IDs or password assignments.

## Final repository size

- Files: **199** (including the manifest)
- Size: **47.6 MiB**
- Public wiki: **19 Markdown files** under `public-wiki/`
- Hash manifest: `data/catalog/FILE_MANIFEST.csv`
