# Claims to Validate

This register is a project-control list, not a finding that any claim is wrong. It separates **source-supported concepts**, **screening assumptions**, and **owner strategic hypotheses** from externally defensible claims.

## Site and renewable resources

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| Nain / Fraser River concept around 15–20 MW | Screening basis, not completed feasibility. | Hydrology, head/flow, seasonal low flow, civil concept, environment/permitting, rights/community process, cost. |
| Other Labrador river potential/capacity records | Dataset mixes installed, historical, preliminary, planned and identified potential. | Record-by-record current source check. |
| Nunavik river opportunity ranking | Studies combine evidence of different maturity. | Official hydrology, protected-area/land regime, project status, community/rights process, access/logistics. |
| “Massive valorization” of previously inaccessible rivers/resources | Strategic thesis could overgeneralize; some resources may be protected, uneconomic, technically unsuitable or socially unacceptable. | Portfolio screening with exclusion criteria, developable capacity, economics and community/environment gates. |
| Coastal wind as startup energy | General exposure is not a site-specific wind assessment. | Wind data, icing, geotechnical, avian/environmental, logistics, interconnection, economics. |

## Avoided transmission / environmental footprint

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| Local compute is **less expensive** than long electrical transmission | Depends on distance, voltage, load, reliability, compute/fibre capex and site conditions. | Comparable alternatives, same service level, full capex/opex/lifecycle sensitivity. |
| Local compute has **lower ecological footprint** than a long transmission line | Shorter corridor may reduce clearing/fragmentation, but compute, fibre, generation and cooling also have impacts. | Lifecycle/site comparison: land, habitat, materials, carbon, water, roads, substations, construction, restoration. |
| Long HV corridor can be avoided | Some sites may still require significant network works. | Utility interconnection study and site electrical architecture. |
| Transmission $/km benchmark | Screening cost varies strongly by voltage, terrain, logistics, routing and scope. | Comparable project basis + site-specific route/cost study. |

## Climate, cooling and heat

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| Cold climate materially lowers cooling cost/PUE | Depends on density, cooling architecture and operating conditions. | Site climate + design model + benchmark. |
| Bay/seawater rejection and ΔT limits | Limits are site- and permit-specific. | Regulator criteria, thermal plume, intake/outfall design. |
| Heat demand available for reuse | Heat-first economics depend on actual sink profiles. | Building-by-building load, supply-temperature compatibility, seasonal profiles, greenhouse/storage sizing. |
| Low-impact / near-zero consumptive water design | Architecture supports this in principle but site implementation matters. | Water balance, cooling design, permits and commissioning data. |

## Fibre / subsea connectivity

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| Coastal location gives **direct access to the seabed for fibre** | Coastline alone does not establish a feasible/permitable landing or route. | Landing-zone study, seabed/bathymetry, rights, permits, environment, carrier design, shore-end engineering. |
| Subsea fibre is cheaper/better than terrestrial alternatives | Strongly route- and scale-dependent. | Route alternatives, capex/opex, repair model, latency/capacity, risk comparison. |
| A **northern fibre crown/ring** can connect multiple sites economically | No network architecture or cost case yet. | Node locations, topology, traffic model, carrier participation, marine/terrestrial route costs, redundancy analysis. |
| Fibre availability/latency/path diversity can meet AI tenant SLAs | Existing documents are conceptual. | Carrier data, route ownership, capacity reservation, latency tests, failover tests, repair/MTTR plan. |

## Data security and secure infrastructure

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| Black-box tenancy materially improves tenant data security | Strong architectural separation, but security outcomes depend on implementation/threat model. | Threat model, interface specification, network architecture, audit, access controls, contractual boundary. |
| Decommissioned/deep mines provide **increased security** | Depth/access can help physical protection but introduce ventilation, water, egress, fire and operational risks. | Candidate-specific geotechnical, physical-security, fire/life-safety, ventilation, flooding, access, remediation and operations study. |
| Confidential computing / attestation options meet tenant requirements | Tenant compliance/security needs vary. | Hardware/software architecture, attestation design, independent security assessment, tenant requirements. |

## Economics and commercial model

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| Electricity/tariff advantage | Tariffs and large-load treatment change. | Current utility tariff/service conditions for specific load/site. |
| Cooling share of data-centre cost | Depends on architecture, density, capex treatment, climate and accounting. | Defined cost model + comparable benchmarks. |
| Partner cost-advantage workbook outputs | Illustrative assumptions need dated sources and scenario definitions. | Workbook audit, source cells, version control. |
| Heat reuse creates meaningful economic/community value | Depends on avoided fuel, loop capex, load factor and ownership model. | Heat tariff/avoided-cost model + real demand. |

## Future AI market / regional platform

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| AI compute demand will rise enough to absorb a large Québec–Labrador platform | Directionally plausible but repository has no controlled forecast. | Current market research, power-demand forecasts, tenant pipeline, workload segmentation. |
| Québec/Labrador can host a significant share of future AI compute | Requires comparative competitiveness and infrastructure capacity. | Resource/capacity inventory, fibre, capex, latency, regulation, security, workforce and competitor benchmark. |
| Northern construction expertise becomes a durable competitive moat | Needs repeat deployments and measurable performance. | Skills map, training outcomes, project delivery metrics, vendor ecosystem, lessons-learned program. |


## International education / university network

| Claim / assumption | Why validation is needed | Required evidence |
|---|---|---|
| Kristal Farms can become an international university network | No accreditation, degree-granting authority, faculty model, institutional partner or sustainable academic budget is established. | Jurisdiction-specific accreditation/degree-authority review, governance design, qualified academic partners, faculty/research plan, financing and credential-recognition pathway. |
| International students can travel north, develop skills and return with portable qualifications | Depends on program quality, legal mobility pathways, recognition of credentials and home-country/institution partnerships. | Partner MOUs, visa/status review, credential portability, curriculum mapping, student-support and return-network design. |
| Host-people languages can be the institutionally primary languages | Appropriate as a design objective but must be reconciled with applicable public-language, education, employment and accessibility requirements. | Host-community decision, language-law review, operational language charter, translation capacity and teaching-resource plan. |
| Cultural rites/customs can be institutionally protected within a common dignity framework | Requires clear governance so cultural autonomy and individual rights are both protected. | Human-rights/legal review, community consultation, safeguarding rules, consent/opt-out procedures, independent complaint and remedy mechanisms. |

## Community / governance / territory

Validate with relevant rights holders and communities:

- FPIC/CLPE process and terminology;
- decision rights and project-governance model;
- benefit-agreement structure;
- heat allocation priorities;
- local hiring/training commitments;
- public dashboard data;
- grievance and incident procedures;
- land, water, marine and cultural-rights implications of energy, fibre and site infrastructure.

## Publication hygiene

Any document containing `turn...search`, `filecite`, private-use citation symbols, or other assistant/UI reference markers must be re-sourced before external use.

Owner strategic direction is traceable in `sources/owner-direction/` but is **not independent evidence**.


## Pass 9 — hydro atlas claims

| Claim / assumption | Status | Required next evidence |
|---|---|---|
| A WSC gauge point identifies a buildable hydro site | **False / prohibited inference** | Separate engineering intake/powerhouse concept. |
| Station drainage area is enough to estimate project MW | **Not supported** | Official flow series, terrain, design flow, head, losses, environmental/engineering constraints. |
| Terrain elevation drop can be labelled project head | **False / prohibited inference** | Defined intake/conveyance/powerhouse and hydraulic-loss basis. |
| Official basin/river geometry has been ingested in pass 9 | **No** | Retrieve WSC MDA 02/03 packages and GRHQ/Canada1Water flowline packages. |
| Pass-9 evidence completeness identifies the best rivers | **No** | Evidence completeness is not suitability; future transparent multi-domain screening only after data maturation. |


## Pass 14 — economic frontier

| Claim / assumption | Current status | Required next evidence |
|---|---|---|
| Kristal is cheaper than long road + HV at every northern site | **Not supported / prohibited generalization** | Site-specific route, voltage, port, fibre, pad, local electrical, O&M, financing and regulatory model. |
| Completed transmission project $/km ratios are valid Kristal site estimates | **No** | Conceptual/FEED route and project estimate; benchmarks remain reference-only. |
| CRTC fibre contribution per km equals fibre construction cost | **No** | Carrier/engineering route quotation and funding/cost breakdown. |
| Positive Pass-14 headroom is project savings | **No** | Price all Kristal-specific infrastructure and conventional alternative on equal scope before NPV. |
| Dedicated local generation avoids Québec data-centre tariff/selection rules | **Unknown** | Legal/utility determination; R-4333-2026 remains active in current review. |
| Broad research can now identify a winning river | **No** | Project dossier with hydrology, head, environmental/rights, logistics, telecom, engineering and economics. |
