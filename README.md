# Kristal Farms — Documentation & Orchestration Repository

> **Visibility: PUBLIC WORKING REPOSITORY.** Kristal Farms is being developed in the open. This repository intentionally exposes working hypotheses, preliminary screening, research, decisions, caveats and evolving documentation so that the project can be examined, challenged and improved. A file being public does **not** mean that every claim in it is validated or adopted.

## Project thesis

Kristal Farms explores a northern infrastructure model built around a simple inversion: **bring compute to renewable energy that is difficult to export, consume the power locally, export digital value by fibre, and reuse the heat.**

The long-term platform combines:

- renewable resources screened for technical, ecological, rights-holder and economic suitability;
- cold-climate, compact and reversible compute infrastructure on low-impact or previously disturbed sites where practical;
- black-box tenancy and higher-assurance security variants that separate physical infrastructure operations from tenant data and models;
- terrestrial and potentially subsea fibre as the long-distance export corridor;
- useful heat recovery for buildings, greenhouses, storage and other validated local sinks;
- harmonious staged deployment, local capability building and community/rights-holder governance;
- climate-adapted housing, civic, health, food, cultural and indoor infrastructure where viable;
- an international learning and research layer that can turn northern operating expertise into portable skills, visiting programs, academic partnerships and eventually university institutions where accreditation and governance permit;
- a Human Dignity Framework that protects host languages, cultures, rites and customs while also protecting individual consent, equality, safety, conscience, privacy, remedy and freedom to leave;
- a long-term opportunity to support increasingly power-intensive AI and scientific compute, subject to demonstrated demand, infrastructure capacity and economics.

Nain remains the first application in the inherited partner package. The broader repository is the controlled playbook for determining which parts of this platform are technically, economically, socially and institutionally defensible at each site.

## Why this repository exists

Kristal Farms is being developed as more than a set of documents. The repository is the control layer that connects:

**source data → research → project decisions → working architecture → partner documents → bilingual deliverables → validation and audit**

The underlying project model combines cold-climate renewable power, village-adjacent modular compute, fibre export of compute results, useful reuse of server heat, black-box tenancy, community governance/FPIC, staged deployment, climate-adapted human infrastructure, and a long-term education/research layer built around transferable northern capabilities.

## Start here

1. [`PROJECT_STATE.md`](docs/00-control/PROJECT_STATE.md) — what the supplied materials currently support.
2. [`DECISIONS_REQUIRED.md`](docs/00-control/DECISIONS_REQUIRED.md) — unresolved choices that must not be silently merged.
3. [`DOCUMENT_AUTHORITY.md`](docs/00-control/DOCUMENT_AUTHORITY.md) — which files are control documents, working narratives, derived deliverables, source evidence, or archive.
4. [`WORKSTREAMS.md`](docs/00-control/WORKSTREAMS.md) — orchestration by workstream.
5. [`CLAIMS_TO_VALIDATE.md`](docs/00-control/CLAIMS_TO_VALIDATE.md) — claims that require engineering, commercial, regulatory, community, or source validation before hard external use.
6. [`BILINGUAL_MATRIX.md`](docs/00-control/BILINGUAL_MATRIX.md) — EN/FR partner-package pairing.
7. [`DATA_CATALOG.md`](data/catalog/DATA_CATALOG.md) — structured data inventory.
8. [`PUBLICATION_POLICY.md`](docs/00-control/PUBLICATION_POLICY.md) — public-by-default repository policy and the narrow categories that stay out of Git.
9. [`SCOPE_BOUNDARIES.md`](docs/00-control/SCOPE_BOUNDARIES.md) — what the project explicitly includes and excludes.
10. [`INTERNATIONAL_LEARNING_VISION_EN.md`](docs/10-core/strategy/INTERNATIONAL_LEARNING_VISION_EN.md) / [`VISION_APPRENTISSAGE_INTERNATIONAL_FR.md`](docs/10-core/strategy/VISION_APPRENTISSAGE_INTERNATIONAL_FR.md) — long-term education, skills-circulation and university pathway.
11. [`HUMAN_DIGNITY_FRAMEWORK_EN.md`](docs/10-core/strategy/HUMAN_DIGNITY_FRAMEWORK_EN.md) / [`CADRE_DIGNITE_HUMAINE_FR.md`](docs/10-core/strategy/CADRE_DIGNITE_HUMAINE_FR.md) — cultural pluralism and individual-rights safeguards.
12. [`EDUCATION_PROGRAM_GATES_EN.md`](docs/10-core/education/EDUCATION_PROGRAM_GATES_EN.md) / [`JALONS_PROGRAMME_EDUCATION_UNIVERSITE_FR.md`](docs/10-core/education/JALONS_PROGRAMME_EDUCATION_UNIVERSITE_FR.md) — gates from training to potential university status.
13. [`LANGUAGE_CHARTER_TEMPLATE_EN.md`](docs/10-core/education/LANGUAGE_CHARTER_TEMPLATE_EN.md) / [`GABARIT_CHARTE_LINGUISTIQUE_FR.md`](docs/10-core/education/GABARIT_CHARTE_LINGUISTIQUE_FR.md) — site-level host-language implementation template.

## Repository architecture

```text
.
├── docs/
│   ├── 00-control/              # Project state, decisions, authority, orchestration
│   ├── 10-core/                 # Internal reference + program/deployment concepts
│   ├── 20-partner-package/      # Numbered partner set, EN + FR deliverables
│   ├── 30-site-screening/       # Labrador, Nunavik, climate/source screening
│   ├── 40-economics/            # Cost, transmission, cooling, savings studies
│   └── 50-research/             # Supporting research
├── data/
│   ├── raw/                     # Supplied CSV/XLSX datasets, unchanged
│   └── catalog/                 # Dataset descriptions and controls
├── public-wiki/                  # Public-facing plain-language GitHub Wiki source
├── sources/
│   ├── originals/               # New supplied originals, preserved
│   ├── extracted/               # Searchable Markdown extracts of DOCX sources
│   └── legacy/                  # Previous source archive and supporting material
└── .github/                     # Issue templates for decisions, validation, workstreams
```

## Current working spine

The existing partner package and the newly supplied village inventory both identify **Nain as the first/primary target**, while the new inventory treats **Inukjuak as a reference case** and keeps a broader set of Labrador/Nunavik communities in later screening or appendix categories.

A newly supplied deployment plan also introduces a possible **coastal-wind bootstrap sequence** before heavier hydro/compute build-out. That concept is retained as a working program option, not silently merged into the current hydro-first partner narrative. See `DECISIONS_REQUIRED.md`.

## Scope guardrail

Kristal Farms is an infrastructure, education-capability and community-development project operating within applicable existing legal frameworks. **Separatism, border revision, sovereignty disputes, territorial occupation strategies and internationalization of Labrador as a political objective are explicitly outside the repository scope.** Long-term welcoming-community concepts are treated as social/infrastructure work, not territorial politics.

See [`SCOPE_BOUNDARIES.md`](docs/00-control/SCOPE_BOUNDARIES.md).

## Editing rule

Do not promote a source claim directly into a partner document. Route changes through the control layer:

1. identify source/evidence;
2. record or update the relevant decision/validation item;
3. update the working narrative;
4. synchronize EN/FR deliverables;
5. update the data-room index and changelog.

## Publication rule

This repository is **public by default**. Drafts, hypotheses, unvalidated calculations and imperfect research may remain visible when their status and limitations are clear. “Not publication-ready” means “do not promote this as an authoritative project claim yet”; it does **not** automatically mean “hide this file.”

Material should stay **out of the public repository** only when there is a concrete reason, such as credentials/secrets, personal information, legally or contractually restricted third-party material, or operational security details whose disclosure would create a real risk. See [`PUBLICATION_POLICY.md`](docs/00-control/PUBLICATION_POLICY.md).

Public visibility does not by itself grant reuse rights. No open-source or open-document license is assigned yet.
