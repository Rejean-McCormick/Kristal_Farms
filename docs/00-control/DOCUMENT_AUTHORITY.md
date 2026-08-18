# Document Authority

No single file is the source of truth for every type of statement. Authority depends on the question being asked.

| Class | Role | Current location |
|---|---|---|
| **A0 — Current public narrative** | Current English explanation, terminology, confidence framing and project thesis. | `public-wiki/*` |
| **A1 — Control** | Project state, decisions, validation, authority, publication and orchestration rules. | `docs/00-control/*` |
| **A2 — Technical baseline** | Detailed architecture and operating model. | `docs/10-core/Kristal_Farms_Internal_Reference.md` and relevant numbered partner technical documents |
| **A3 — Deployment / governance frameworks** | Harmonious deployment, human infrastructure, dignity, language and education pathways. | `docs/10-core/deployment/*`, `docs/10-core/strategy/*`, `docs/10-core/education/*` |
| **A4 — Working evidence** | Site screening, economic studies, transmission/cooling comparisons and supporting research. | `docs/30-site-screening/*`, `docs/40-economics/*`, `docs/50-research/*` |
| **A5 — Structured supplied data** | Raw CSV/XLSX datasets and their catalogue. | `data/raw/*`, `data/catalog/*` |
| **A6 — Source originals** | Preserved supplied original files and earlier source material. | `sources/originals/*`, `sources/legacy/*`, `sources/owner-direction/*` |
| **A7 — Inherited deliverables** | Existing Nain/Labrador partner package and formatted outputs. Useful evidence of prior project framing, but not the current public narrative. | `docs/20-partner-package/*` |
| **A8 — Archive** | Superseded repository/narrative layers retained for history. | `archive/*` |

## Conflict rules

1. **For current project framing and terminology**, use the current public wiki plus control documents.
2. **For a technical claim**, use the detailed technical source, not a wiki summary.
3. **For a numeric/economic claim**, use the underlying study/workbook and its as-of/source context.
4. **For a site fact**, use current site-specific evidence and the relevant confidence label.
5. **For a discrepancy between a supplied original and a searchable extraction**, preserve the original as authoritative for what was supplied.
6. **For historical v1/v2/v3 narrative differences**, do not silently merge them. The current wiki supersedes the old working narrative, while the old files remain traceable.

## Current narrative transition

The older v2/v3 working partner narratives and pre-wiki platform vision have been moved to `archive/` because the uploaded 2026-08-18 English wiki now provides the clearest current public structure:

**core idea → structural advantage → transmission vs digital export → cooling → heat → fibre → security → environmental selection → harmonious deployment → first application → network/AI → human/education layers → evidence/confidence.**
