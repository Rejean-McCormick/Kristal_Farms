# Workstreams

The v3 repository organizes work by dependency and strategic question rather than file format.

| Workstream | Objective | Key current inputs | Next controlled output |
|---|---|---|---|
| **WS-01 Platform thesis & scope** | Lock the v3 project spine, geography and external positioning. | Strategic Principles; Platform Vision; Internal Reference; owner direction; partner package. | Resolve D-001/D-011/D-016; approved platform thesis. |
| **WS-02 Nain pre-feasibility** | Test whether the first target survives technical/community screening. | Nain rows in village/hydro data; hydro screening appendix. | Nain evidence pack + go/no-go checklist. |
| **WS-03 Labrador replication** | Screen Hopedale, Makkovik, Postville, Rigolet and other relevant sites. | Labrador hydro dataset; map points; river report. | Ranked screening matrix with evidence gaps. |
| **WS-04 Nunavik / Québec screening** | Separate reference cases, excluded sites and future candidates. | Village inventory; Nunavik river/transmission studies; precipitation data. | Clean research appendix + candidate classes. |
| **WS-05 Energy & reference architecture** | Define common interfaces across hydro, optional wind, electrical distribution, compute, cooling, heat, storage and reversibility. | Internal Reference; technical partner doc; deployment plans; v3 strategy. | Kristal Farms v3 Reference Architecture + archetype deltas. |
| **WS-06 Avoided transmission & ecological comparison** | Test cost and lifecycle footprint of local-consumption/fibre-export vs electrical-export alternatives. | Transmission study; economics; technical architecture. | Site comparison methodology + first case study. |
| **WS-07 Heat/community value** | Quantify useful heat sinks and community benefit for community-integrated nodes. | Heat partner doc; Internal Reference. | Site heat-demand model + seasonal heat balance. |
| **WS-08 Fibre / subsea / northern network** | Validate terrestrial fibre, marine landing opportunity, route diversity and multi-node crown/ring concepts. | Connectivity doc; coastal geography; strategic research agenda. | Fibre opportunity map + reference topology + route feasibility scopes. |
| **WS-09 Data security / black-box / secure sites** | Formalize tenant trust boundary and screen higher-assurance physical site variants. | Black-box docs; Internal Reference; owner mine/brownfield direction. | Threat model + security interface spec + secure-site screening standard. |
| **WS-10 Mine / brownfield candidate screening** | Determine whether decommissioned mines or industrial sites are viable compute archetypes. | Owner direction; future candidate data to gather. | Candidate inventory + geotechnical/life-safety/fibre/power screen. |
| **WS-11 Economics & commercial** | Build a controlled cost/revenue model across site archetypes. | XLSX workbook; cost studies; transmission comparison; SLA doc. | Versioned assumptions + scenario model. |
| **WS-12 AI tenant demand / market fit** | Test workload, density, latency, security and contract requirements for future AI compute. | Strategic vision; future external research. | Tenant requirements matrix + demand scenarios. |
| **WS-13 Governance / FPIC / benefits** | Define process with communities and rights holders. | Governance partner doc; Internal Reference; deployment plans. | Engagement roadmap + decision-rights matrix. |
| **WS-14 Harmonious deployment / workforce** | Turn staged integration and northern construction expertise into a repeatable implementation method. | EN/FR deployment plans; partner roadmap; owner direction. | Northern Infrastructure Playbook + training/capability plan. |
| **WS-15 Metrics / audit / environment** | Define measurable acceptance gates and environmental controls. | Metrics framework; risk register; Internal Reference. | Evidence-backed KPI dictionary + gate checklist. |
| **WS-16 Partner/data room v3** | Rebuild one coherent external package around the approved v3 thesis while preserving Nain as first application. | v1 00–14 package; V3 rebuild map; approved decisions. | v3 partner package + share-level manifest. |
| **WS-17 Bilingual / brand / publishing** | Keep EN/FR content synchronized and branding controlled. | EN/FR strategy; v1 EN/PDF + FR PDF/DOCX. | Translation sync report + release checklist. |
| **WS-18 Data engineering / maps** | Make datasets reproducible and reviewable while protecting sensitive coordinates. | CSV datasets + workbook. | Data dictionary, validation scripts, controlled map artifacts. |
| **WS-19 Kristals / knowledge commons** | Decide whether and when the optional knowledge layer enters scope. | Internal Reference. | D-009 decision + separate brief if activated. |
| **WS-20 Human infrastructure / welcoming communities** | Test a voluntary, rights-respecting model for climate-adapted living infrastructure and lawful newcomer-community partnerships, separate from territorial politics. | Human Infrastructure Vision; community-governance principles; future qualified partners. | Social-infrastructure requirements + governance/rights safeguards + feasibility scope. |
| **WS-21 International learning / universities** | Build a staged education and research model that converts northern infrastructure expertise into portable skills, international learning and potentially accredited university capacity. | International Learning Vision; Human Dignity Framework; language-charter template; education gates; owner direction; future academic partners. | Partner/accreditation map + pilot skills-circulation program + site-specific education capacity model. |

## Workstream rule

Every workstream should have:

- one owner;
- one current status;
- one next decision/gate;
- evidence links;
- open risks;
- a single next deliverable;
- explicit share level if the work includes site, fibre, security or community-sensitive data.

Use the GitHub `Workstream` issue template rather than creating untracked side documents.


## Platform / data-model foundation — Pass 11

- maintain canonical entity IDs across Web/QGIS/API/publish artifacts;
- migrate pass-numbered research artifacts into `core/research/system` semantics;
- keep public layers derived from `publish` views;
- execute HYDAT and official geometry ingestion when network-enabled;
- preserve KR rules in QA and database validation;
- keep ranking disabled until governance explicitly changes it.
