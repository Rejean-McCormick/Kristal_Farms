# Content Sanitation / Citation Hygiene

## Publication blockers

The following working files contain non-portable assistant/UI-style citation artifacts and must remain internal until they are re-sourced:

- `docs/30-site-screening/nunavik/Rivieres_littoral_ouest_Nord_quebecois_nord_La_Grande.md`
- `docs/50-research/Partners_inventory_deep-research-report.md`

Examples include:
- `turn...search...` reference IDs;
- assistant entity/citation markers;
- private-use Unicode citation symbols;
- `filecite`-style tokens embedded in source text.

These markers are not stable bibliographic references.

A legacy source under `sources/legacy/` also contains an opaque assistant-era reference. Legacy material is never publication-ready by default.

## Remediation

For each affected claim:
1. identify the underlying human-readable source;
2. record title/organization/date/URL or project document;
3. distinguish primary source from inference;
4. replace UI tokens with normal citations;
5. re-check time-sensitive claims for the intended publication date;
6. only then promote the claim into partner material.

## URL sanitation

Searchable Markdown extractions created during this refactor remove `utm_source=chatgpt.com` tracking parameters from normal source URLs. The original supplied DOCX remains preserved unchanged.

## Release scan

Before release, scan non-legacy material for:
- `turn[0-9]`;
- `filecite`;
- private-use Unicode characters;
- raw AI/tool markup;
- placeholder citations;
- AI-session tracking parameters;
- unverified “current” claims;
- internal-only file paths or notes.
