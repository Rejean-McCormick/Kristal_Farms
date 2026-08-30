# Kristal Farms Documentation

Documentation repository for **Kristal Farms**, a proposed cold-climate, hydro-powered compute project that places modular compute near community heat users, exports compute results over fibre, and reuses server waste heat for buildings, greenhouses, and other local uses.

> **Repository visibility:** Private recommended. This repository contains an internal reference document, diligence material, preliminary project claims, and source research that should not all be treated as public-facing.

## Project thesis

Kristal Farms combines:

- local or nearby renewable hydro power;
- village-adjacent modular compute pads;
- fibre connectivity for exporting compute rather than bulk electricity;
- a heat-first architecture using non-contact heat exchange;
- black-box tenancy that separates host infrastructure from tenant data and workloads;
- community governance, FPIC, benefits, and transparent operating metrics;
- phased deployment with formal go/no-go decision gates.

The current partner package is focused on the **Labrador coast, with Nain as the first target community** and other coastal communities treated as later replication candidates.

## Repository map

```text
.
├── README.md
├── CONTRIBUTING.md
├── docs/
│   ├── partners/
│   │   ├── README.md
│   │   ├── markdown/        # Authoritative partner-facing working documents
│   │   └── pdf/
│   │       ├── en/          # English partner PDFs
│   │       └── fr/          # French partner PDFs
│   ├── internal/            # Internal reference material — do not publish by default
│   ├── plans/               # Deployment and cost-advantage supporting PDFs
│   └── research/            # Supporting research reports
├── data/                    # Cost workbook and future structured data
└── source-material/         # Background/source documents; not authoritative partner copy
```

## Start here

For partner review, begin with:

1. [`00_Kristal_Farms_Partner_Overview.md`](docs/partners/markdown/00_Kristal_Farms_Partner_Overview.md)
2. [`01_Partner_Ask_and_Roles.md`](docs/partners/markdown/01_Partner_Ask_and_Roles.md)
3. [`02_Labrador_Coast_Project_Thesis.md`](docs/partners/markdown/02_Labrador_Coast_Project_Thesis.md)
4. [`03_Cost_Advantage_and_Strategic_Rationale.md`](docs/partners/markdown/03_Cost_Advantage_and_Strategic_Rationale.md)
5. [`06_Technical_Architecture.md`](docs/partners/markdown/06_Technical_Architecture.md)
6. [`07_Heat_Recycling_and_Community_Value.md`](docs/partners/markdown/07_Heat_Recycling_and_Community_Value.md)
7. [`08_Connectivity_and_Black_Box_Tenancy.md`](docs/partners/markdown/08_Connectivity_and_Black_Box_Tenancy.md)
8. [`11_Governance_FPIC_and_Community_Benefits.md`](docs/partners/markdown/11_Governance_FPIC_and_Community_Benefits.md)
9. [`13_Risk_Register.md`](docs/partners/markdown/13_Risk_Register.md)

The complete control index is [`14_Data_Room_Index.md`](docs/partners/markdown/14_Data_Room_Index.md).

## Source-of-truth rules

- The numbered files under `docs/partners/markdown/` are the current partner-document set.
- Use `14_Data_Room_Index.md` to determine whether a document is external, NDA-preferred, or internal.
- Material in `source-material/` is background/source material and may include older assumptions or broader concepts; do not treat it as current partner copy without validation.
- The current internal synthesis is `docs/internal/Kristal_Farms_Internal_Reference.md`.
- Preliminary site, hydro, financial, schedule, governance, environmental, or technical claims should remain clearly marked until validated.
- Tenant data, application logs, model content, and packet payloads remain outside the host-side black-box boundary described by the project documents.

## Editing workflow

1. Make substantive edits in Markdown first.
2. Keep one authoritative partner-facing file per topic.
3. Update the data-room index when document status or share level changes.
4. Validate cross-document claims before promoting source material into the partner set.
5. Regenerate human-facing PDFs after Markdown content is approved.
6. Use pull requests for review when multiple contributors are working in the repository.

## Licensing and distribution

No open-source or open-document license is assigned in the supplied materials. Treat the contents as private/proprietary until the project owner explicitly chooses a license and public distribution policy.
