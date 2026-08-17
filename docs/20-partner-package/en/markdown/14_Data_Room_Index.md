# 14_Data_Room_Index.md

# Kristal Farms — Data Room Index

**Document status:** Partner-facing control index  
**Package:** Kristal Farms Partner Documentation  
**Version:** v0.1 draft  
**Geographic focus:** Labrador coast, with Nain as the first target community  
**Primary use:** Tell partners what materials exist, which files are authoritative, and which materials are external, NDA-only, or internal archive.

---

## 1. Purpose

This data room index organizes the Kristal Farms partner documentation package into a clean two-level system:

```text
Level 1 — Partner decision documents
Short, polished, strategic, externally readable.

Level 2 — Due diligence appendices
Technical, detailed, evidence-heavy, shared after partner interest and, where appropriate, NDA.
```

The goal is to avoid handing partners a raw compilation. Partners should receive a coherent package built around the Labrador coast thesis:

> Nain first. Labrador coastal replication second. Community-scale hydro, compute, heat reuse, fibre connectivity, black-box tenancy, and community benefit as the core model.

---

## 2. Data room principles

1. **One source of truth per topic.**  
   Each topic should have one authoritative partner-facing document. Supporting files may exist, but should not contradict the current package.

2. **Partner-facing first.**  
   External files should be short, polished, specific, Labrador-focused, and evidence-based.

3. **No raw brainstorming.**  
   Internal Q&A, older strategy drafts, vendor notes, and broad national/global concepts belong in the source archive unless cleaned and approved.

4. **No overclaiming.**  
   Unvalidated financial claims, unconfirmed hydro numbers, unresolved governance details, and speculative timelines must be marked as preliminary or excluded.

5. **Nain is the initial target.**  
   Other Labrador coastal communities are treated as replication candidates, not as equal first-stage sites.

6. **Heat-first architecture governs the package.**  
   The current model places data containers near village heat users, not at a remote dam. The project exports compute by fibre and reuses server heat locally.

7. **Black-box tenancy is a hard boundary.**  
   Host-side monitoring is limited to physical infrastructure metrics. Tenant data, application logs, model content, and packet payloads remain outside the host boundary.

---

## 3. Level 1 — Partner decision documents

These are the first files to share with a serious partner.

| File | Status | Purpose | Share level |
|---|---|---|---|
| `00_Kristal_Farms_Partner_Overview.md` | Current draft | Main 4–6 page partner entry document. Explains the whole opportunity without requiring other files. | External |
| `01_Partner_Ask_and_Roles.md` | Current draft | Defines partner types, what Kristal Farms brings, what the partner brings, and immediate decision points. | External |
| `02_Labrador_Coast_Project_Thesis.md` | Current draft | Explains why the project is focused on Labrador coastal communities, with Nain first. | External |
| `03_Cost_Advantage_and_Strategic_Rationale.md` | Current draft | Explains why the model is structurally advantaged: no long HV buildout, natural cold, heat reuse, modular pads, marine logistics, export compute not electrons. | External |
| `06_Technical_Architecture.md` | Current draft | Partner-facing technical architecture for hydro integration, village substation, pad yard, container interfaces, cooling, heat loop, fibre/NOC, and phasing. | External / NDA depending on detail |
| `07_Heat_Recycling_and_Community_Value.md` | Current draft | Core differentiator document linking technical design to public-building heat, homes, greenhouse, diesel displacement, and community value. | External |
| `08_Connectivity_and_Black_Box_Tenancy.md` | Current draft | Explains fibre dependency, NOC architecture, host/tenant boundaries, and black-box tenancy. | External / NDA depending on tenant detail |
| `11_Governance_FPIC_and_Community_Benefits.md` | Current draft | Frames FPIC, community benefits, governance principles, and open design items. | External |
| `13_Risk_Register.md` | Current draft | Partner diligence summary of major risks, mitigations, owners, and next evidence required. | External / NDA depending on owner detail |

---

## 4. Level 2 — Due diligence appendices

These files support deeper review after initial partner interest.

| File | Status | Purpose | Share level |
|---|---|---|---|
| `04_Project_Map_and_Site_Inventory.md` | Current draft pending KML/CSV validation | Explains project map layers, site inventory logic, included/excluded sites, and current map/data file status. | External / NDA depending on map precision |
| `05_Labrador_Coast_Hydro_Screening_Appendix.md` | Current draft | Technical appendix for candidate hydro sites, exclusions, screening criteria, data gaps, and required next studies. | NDA preferred |
| `09_Commercial_Model_and_SLA.md` | Current draft | Commercial model, SLA framework, metering, tenant eligibility, revenue categories, cost categories, and reversibility. | NDA preferred |
| `10_Project_Roadmap_and_Decision_Gates.md` | Current draft | Phase/gate plan from partner alignment to site validation, FPIC, pre-feasibility, pilot pad, heat loop, and expansion. | External / NDA depending on dates |
| `12_Metrics_Dashboard_and_Audit_Framework.md` | Current draft | Defines project metrics, public scorecard, reporting cadence, quarterly review, and annual audit structure. | External |
| `14_Data_Room_Index.md` | Current draft | Controls package structure, source hierarchy, share levels, and authoritative file list. | External |

---

## 5. Maps and data files

These files should be grouped under a `maps/` folder when available.

| File | Status | Purpose | Share level |
|---|---|---|---|
| `kristal_farms_LABRADOR_COAST_PROJECT_ONLY_colored.kml` | Pending upload / validation | Visual map layer for Labrador coast project sites and exclusions. | NDA or external depending on precision |
| `kristal_farms_LABRADOR_COAST_PROJECT_ONLY_feature_inventory.csv` | Pending upload / validation | Structured site inventory for project features, candidate sites, and map objects. | NDA or external depending on precision |
| `kristal_farms_LABRADOR_COAST_PROJECT_ONLY_validation.csv` | Pending upload / validation | Validation table for source status, inclusion/exclusion logic, and evidence gaps. | Internal / NDA |

**Rule:** Do not finalize site claims in partner documents until map files and source references are validated.

---

## 6. Authoritative source documents

The following current source files are the main basis for the partner package.

| Source file | Use in package | Authority level |
|---|---|---|
| `Documentation Kristal Farms.docx (2)(1).md` | Governance, FPIC, black-box tenancy, SLA logic, metrics, unresolved design items. | Tier 1 |
| `Kristal Farms — Heat Recycling Plan (3)(1).md` | Heat-first design, village siting, two sealed circuits, reuse/store/reject hierarchy, public heat, greenhouse, thermal metrics. | Tier 1 |
| `Kristal Farms (intro) — Cost Advantage & Strategic Rationale (3)(1).md` | Cost stack, avoided HV transmission, natural cold, heat value, modular pads, marine logistics, export compute not electrons. | Tier 1 |
| `Kristal Farms Internal Reference Document.docx (3)(1).md` | System architecture, local hydro integration, MV connection, village substation, compute pads, cooling, operations, phasing. | Tier 1 |
| `Potentiel hydroélectrique isolé au Nunavik et au Labrador (≥ 15 MW).docx (2)(1).md` | Hydro screening, Labrador/Nunavik comparison, excluded sites, Nain/Fraser River preliminary basis. | Tier 1, technical |
| `EC8ADFDE-9E2F-11F0-9303-BF2B70071435.pdf` | Article-style synthesis, black-box pads, reuse/storage/reject hierarchy, FPIC, Kristals layer, community wealth framing. | Tier 1 synthesis |

---

## 7. Supporting diligence sources

These documents may support due diligence, appendices, or internal background, but should not define the first partner package.

| Source file | Use | Treatment |
|---|---|---|
| `Containerized Data Centers — Vendor Landscape, Use Cases & Lessons.docx.md` | Vendor landscape, modular data center examples, procurement context. | Due diligence / appendix |
| `Comparable Projects — AI Knowledge Systems & HydroContainer Data Centers.docx.md` | Comparable projects and Kristals-related precedents. | Due diligence / appendix |
| `Modular AI Farms at Hydropower Sites — Feasibility & Cooling System Design.docx.md` | Cooling design, modular deployment risks, technical feasibility context. | Technical support |
| `Northern Hydropower for Compute — Opportunities, Cooling Advantage & Strategy.docx.md` | Broad northern hydro/cooling opportunity framing. | Background only |
| `Comprehensive Program Outline — Hydropowered Containerized AI & Kristals (Canada).md` | National Canada framing and broader program structure. | Use selectively; not Labrador spine |

---

## 8. Internal source archive

The following categories should remain internal unless cleaned, validated, and shared under NDA.

```text
99_INTERNAL_SOURCE_ARCHIVE/
  raw_compilation/
  old_nunavik_material/
  internal_q_and_a/
  vendor_landscape/
  comparable_projects/
  old_maps/
  generated_working_csvs/
  old_canada_global_strategy/
  old_manicouagan_material/
  kristals_background/
```

### Internal-only or archive-first documents

| Source file | Reason for archive treatment |
|---|---|
| `Program Blueprint & Section Outline for a Green AI Compute Initiative.docx.md` | Useful for structure, but too broad and not Labrador/Nain-specific. |
| `Rapport détaillé — Infrastructure d’IA modulaire et bibliothèque de Kristals.docx.md` | Useful for Kristals background, but too broad and narrative-heavy for first package. |
| `Hydro-Backed Modular AI & Open Knowledge — Global Program Brief.docx.md` | Global framing can distract from Labrador partner decision-making. |
| `Hydro-Powered Container Compute — Global Collaboration & Competition Framework.docx.md` | Broad geopolitical/collaboration framing; not appropriate for first partner package. |
| `Government Proposal Outline — Hydropowered Containerized Data Centers & Turbine-Water Cooling (Manicouagan).docx.md` | Manicouagan-focused; should not drive Labrador coast package. |
| `Executive Brief — Kristals & Hydropowered Modular AI Data Centers (Canada).docx.md` | Older Canada-wide framing; useful only after cleaning. |
| `Green AI Compute & Knowledge Platform — Canada Strategy and Model.docx.md` | Broad strategy source; avoid in first Labrador-focused package unless rewritten. |

---

## 9. Partner package v1

Recommended first-meeting package:

```text
Kristal_Farms_Partner_Package_v1/
  00_Kristal_Farms_Partner_Overview.md
  01_Partner_Ask_and_Roles.md
  02_Labrador_Coast_Project_Thesis.md
  03_Cost_Advantage_and_Strategic_Rationale.md
  06_Technical_Architecture.md
  07_Heat_Recycling_and_Community_Value.md
  08_Connectivity_and_Black_Box_Tenancy.md
  11_Governance_FPIC_and_Community_Benefits.md
  13_Risk_Register.md
```

Add only after validation:

```text
  04_Project_Map_and_Site_Inventory.md
  maps/
    kristal_farms_LABRADOR_COAST_PROJECT_ONLY_colored.kml
    kristal_farms_LABRADOR_COAST_PROJECT_ONLY_feature_inventory.csv
```

Hold for deeper diligence:

```text
  05_Labrador_Coast_Hydro_Screening_Appendix.md
  09_Commercial_Model_and_SLA.md
  10_Project_Roadmap_and_Decision_Gates.md
  12_Metrics_Dashboard_and_Audit_Framework.md
  14_Data_Room_Index.md
```

---

## 10. File naming and versioning

Use this convention:

```text
NN_Title_With_Underscores.md
```

For controlled revisions:

```text
NN_Title_With_Underscores_v0.1.md
NN_Title_With_Underscores_v0.2.md
NN_Title_With_Underscores_v1.0.md
```

Recommended status labels:

```text
Draft
Internal review
Partner-facing draft
NDA draft
Approved external
Archived
Superseded
```

Every file should include:

```text
Document status:
Version:
Date:
Audience:
Geographic focus:
Confidentiality:
Source basis:
```

---

## 11. Document dependency map

| If writing this file | Complete or consult first |
|---|---|
| `00_Kristal_Farms_Partner_Overview.md` | Heat Plan, Cost Advantage, Internal Reference, Hydro Thesis |
| `01_Partner_Ask_and_Roles.md` | Overview, black-box tenancy, commercial model assumptions |
| `02_Labrador_Coast_Project_Thesis.md` | Hydro Potential, Cost Advantage, map/site inventory |
| `03_Cost_Advantage_and_Strategic_Rationale.md` | Heat Plan, Internal Reference |
| `04_Project_Map_and_Site_Inventory.md` | Hydro Screening Appendix, KML/CSV files |
| `05_Labrador_Coast_Hydro_Screening_Appendix.md` | Hydro Potential source validation |
| `06_Technical_Architecture.md` | Heat Plan, Internal Reference, Connectivity/Black-Box |
| `07_Heat_Recycling_and_Community_Value.md` | Heat Plan, metrics framework |
| `08_Connectivity_and_Black_Box_Tenancy.md` | Documentation Kristal Farms, Internal Reference |
| `09_Commercial_Model_and_SLA.md` | Partner Ask, Technical Architecture, Black-Box Tenancy |
| `10_Project_Roadmap_and_Decision_Gates.md` | Overview, Governance/FPIC, Risk Register |
| `11_Governance_FPIC_and_Community_Benefits.md` | Documentation Kristal Farms, community benefit principles |
| `12_Metrics_Dashboard_and_Audit_Framework.md` | Heat Plan, black-box metrics, SLA metrics |
| `13_Risk_Register.md` | All major docs |
| `14_Data_Room_Index.md` | All current and planned files |

---

## 12. Files not for external distribution before cleanup

Do not share these in raw form:

```text
- Internal Q&A files
- Older Nunavik-first drafts
- Manicouagan government proposal drafts
- Global collaboration / competition drafts
- Raw vendor landscape files
- Raw comparable-project research
- Generated working CSVs
- Old maps
- Unvalidated hydro tables
- Any file containing speculative financial projections
- Any file implying finalized governance powers where design remains open
```

---

## 13. Open items before partner release

| Open item | Required action |
|---|---|
| Final Labrador-only KML | Upload, validate, and lock version. |
| Feature inventory CSV | Upload and check every site against source evidence. |
| Validation CSV | Mark included, excluded, preliminary, and data-gap items. |
| Nain hydro evidence | Validate any numerical power claims before external release. |
| Community governance | Separate confirmed principles from open design decisions. |
| Financial model | Keep out of non-NDA package unless validated. |
| Fibre status | Confirm available paths, redundancy, latency, and ownership before hard SLA claims. |
| Heat offtake | Confirm first public buildings, greenhouse sink, and thermal storage assumptions. |
| Environmental safeguards | Confirm permitting path for non-contact bay/seawater heat exchange. |

---

## 14. Release rule

A document is ready for external partner use only when it passes this test:

```text
1. It supports the Labrador coast / Nain-first thesis.
2. It does not rely on outdated Canada-wide or global framing.
3. It separates confirmed facts from preliminary assumptions.
4. It avoids unvalidated financial or technical claims.
5. It does not expose internal Q&A, unresolved governance, or raw source language.
6. It gives the partner a clear decision path.
```

---

## 15. Summary

The data room should present Kristal Farms as a disciplined Labrador coast infrastructure opportunity, not as a loose collection of AI, hydro, and Kristals ideas.

The authoritative partner narrative is:

```text
Kristal Farms develops village-sited modular compute pads on the Labrador coast.
Nain is the first target.
Power comes from local hydro through short MV connection.
Compute is exported by fibre.
Waste heat is reused locally for public buildings, homes, and greenhouse loads.
Tenants operate black-box containers.
Community value, FPIC, reversibility, and transparent metrics are built into the model.
```
