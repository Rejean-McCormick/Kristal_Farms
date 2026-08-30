# Document Authority Model

This file prevents the repository from turning into a pile of mutually contradictory “final” documents.

## Control classes

| Class | Meaning | Current examples |
|---|---|---|
| **C0 — Control** | Governs project state, strategic principles, decisions, validation, share level and synchronization. | `docs/00-control/*` |
| **C1A — Platform narrative** | Main editable v3 strategic narrative. Defines what Kristal Farms is as a repeatable platform, while clearly marking hypotheses. | Platform Vision EN/FR; Human Infrastructure Vision EN/FR; International Learning Vision EN/FR; Human Dignity Framework EN/FR |
| **C1B — Site/reference architecture narrative** | Detailed working architecture for a site archetype. | Internal Reference; deployment plans |
| **C1C — Partner working narrative** | External-facing Markdown. `v3-working/` is the current platform draft; `v2-working/` is superseded; numbered set remains v1/Nain-Labrador until rebuilt. | `docs/20-partner-package/v3-working/*`; `docs/20-partner-package/v2-working/*`; `en/markdown/*` |
| **C2 — Derived deliverable** | Human-facing export/translation. Must not become an independent source of truth. | EN PDFs; FR PDFs; FR logo DOCX |
| **C3 — Structured evidence** | Supplied datasets/workbooks. Authoritative only for what the file records, as of its source date. | CSVs; XLSX |
| **C4 — Working research/source** | Analysis, screening, cost studies, source reports and extracted text requiring validation before promotion. | site screening; economics; research |
| **C4O — Owner strategic direction** | Project-owner ideas/intent recorded for traceability. Authoritative for intended strategy, **not evidence that factual claims are true**. | `sources/owner-direction/*` |
| **C5 — Legacy/archive** | Older or superseded material retained for traceability. | `sources/legacy/`; `archive/` |

## Current strategic source of truth

For **what the platform is intended to become**, use this order:

1. `docs/00-control/STRATEGIC_PRINCIPLES.md` — control framing and claim discipline;
2. matched strategy files in `docs/10-core/strategy/` — platform, human infrastructure, international learning and human-dignity narratives;
3. `docs/00-control/PROJECT_STATE.md` — current evidence/status;
4. decisions and validation registers.

The detailed Internal Reference remains the primary source for the **community-integrated hydro/heat architecture**, not for every future site archetype.

## Current editing source for the partner set

The numbered English Markdown files remain the edit source for the **v1 partner package** because that is the inherited workflow. They are not automatically authoritative over the newer platform strategy.

Until the v3 partner rebuild is completed, any conflict is handled as follows:

- v3 strategic/control documents govern platform intent;
- v1 partner Markdown governs what the old partner package currently says;
- existing PDFs/DOCX remain historical formatted representations of v1;
- the repository must not label the v1 package “v3 synchronized.”

## Promotion rule

A claim moves from owner/source/research to partner material only when:

1. the source or owner-direction origin is identified;
2. the claim status is recorded;
3. evidence conflicts are resolved or disclosed;
4. required technical/commercial/community/environment/security validation is completed;
5. a project decision approves the external framing where needed;
6. partner Markdown is updated;
7. bilingual deliverables are synchronized;
8. the change is recorded in `CHANGELOG.md` and the manifest.

## Never do this

- Do not treat a PDF as “more final” simply because it looks polished.
- Do not turn project-owner vision into independent evidence.
- Do not call a learning site an accredited university or promise recognized credentials before the relevant authority/partner pathway is established.
- Do not interpret host-language primacy as authority to ignore applicable language law or individual access rights.
- Do not state lower ecological footprint, lower cost, subsea access, mine security or future AI market size as established without the required evidence.
- Do not merge Nain, Nunavik and platform-wide scope without an explicit decision.
- Do not convert a screening estimate into a construction-ready claim.
- Do not expose exact site, fibre or security details merely because they exist in the repository.
- Do not update one language and leave the paired release stale without marking it.
