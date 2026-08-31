# Release Status

**As of:** 2026-08-31

## Active state

| Area | Status | Interpretation |
|---|---|---|
| Project reference architecture | **Current** | Governs current project intent and architecture language. |
| Application architecture | **Current design contract** | Governs data model, UX surfaces, APIs and publishing architecture. |
| Hydrology research registry | **Current research baseline** | Official station anchors and evidence; not dam sites or capacity estimates. |
| Integrated atlas | **Current research/application baseline** | Joins evidence and entities without fabricating geometry. |
| Economic architecture frontier | **Current non-bankable research method** | Structural comparison only; benchmarks are not site costs. |
| Site ranking | **Disabled** | `ranking_allowed = false`. |
| Corridor/site feasibility | **Not established** | Requires project-specific engineering, environment, rights/governance, telecom, logistics and economics. |
| Public application release | **Design/data foundation** | Current data contracts and static outputs exist; production Web/API implementation is not complete. |
| Long-horizon human/learning concepts | **Optional / not prerequisite** | Kept separate from the first-line energy/compute project case and not presented as committed institutions or programs. |
| International tenancy governance | **Current control policy** | Counterparty eligibility is selective; U.S.-based/U.S.-controlled tenant roles are excluded by current owner policy and non-listed jurisdictions default to enhanced due diligence. |
| Tenant confidentiality boundary | **Current reference/security model** | Tenant-controlled encrypted environments are content-blind to routine operator access; counterparty governance does not imply private workload inspection. |
| International prospect inventory | **Research only** | Named organizations are candidates for research and do not imply interest, commitment or eligibility. |
| Mine infrastructure reuse & storage | **Exploratory research** | Recent underground mines may be studied for infrastructure reuse; open pits of any age may be studied for pumped-storage geometry. No mine is selected or represented as available/feasible. |

## External-use rule

Use active documents and current releases only. Superseded partner packages, historical reports and old screening logic are retained under `archive/` for provenance and must not be presented as current project direction.


## Observatory interface sync — 2026-08-31

The repository frontend is synchronized through Observatory v0.2.4:

- MapLibre 6 / Next 16 worker-safe integration
- Geographic Observatory river/context interactions
- human-readable evidence inspector
- corrected feature-state radius expressions
- hydration tolerance for browser-extension body attributes
- clean basemap without park/landuse surface pop-in
- Natural Earth fade fix to avoid pitch-black zoom transitions
- automatic fit to governed published extent + Reset view
- static local satellite imagery contract and manual GDAL publication pipeline
- no runtime satellite API key/provider
