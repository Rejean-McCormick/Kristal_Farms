# Data validation pass — 2026-09-01

## Scope

This pass focuses on governed/current data and factual public surfaces in the Kristal Farms snapshot, with special attention to AI-generated claims that could be hallucinated, over-precise, stale, or insufficiently sourced.

Included:

- canonical research provenance fixtures (`research_source`, `research_evidence`, evidence/source links, observations, economic benchmarks);
- current public evidence, community infrastructure, grid-reach and economic benchmark artifacts;
- the International Portfolio research portfolio and its public interface;
- current legal/reference context attached to the jurisdiction policy.

Not certified by this pass:

- legacy/raw/internal research archives that are not promoted as canonical evidence;
- commercial willingness, future delivery, or actual available capacity of third parties;
- legal eligibility of any transaction or counterparty;
- engineering-grade geometry or site-specific cost estimates.

## Executive findings

### 1. Canonical provenance graph: structurally sound

The canonical fixture layer had no broken evidence/source references in the reviewed current snapshot:

- 46 research sources after this pass;
- 127 evidence records;
- 274 evidence↔source links after this pass;
- 100 observations, all with a valid `source_evidence_id`;
- 10 economic benchmarks, all with a valid `source_evidence_id`.

The existing evidence/observation/scenario separation is a strong anti-hallucination control because scenarios are not silently promoted to observations.

### 2. Public economic provenance: broken chain fixed

Before this pass, all 10 public economic benchmarks exposed a `source_evidence_id`, but the corresponding economic evidence records were omitted from `evidence_records_public.json`. The IDs therefore did not resolve in the public evidence ledger.

Fix:

- `build_observatory_public.py` now includes evidence referenced by `economic_benchmarks_public.json`;
- the public evidence ledger increased from 115 to 125 records;
- all 10 public benchmark evidence IDs now resolve to public evidence and source records.

### 3. Northern Labrador road benchmark: numeric correction

The source study states a ROM construction estimate of approximately **CAD 2,089,790,000** for 809 km of gravel road and **CAD 602,393,000** for 809 km of paving, with ROM accuracy of ±50% and costs based on 2023 pricing. The previous fixture metadata rounded these to CAD 2.1B and CAD 600M, and the published per-km benchmarks were calculated from those rounded amounts.

Source: [Newfoundland and Labrador House of Assembly / Allnorth — Final Draft Project Summary Report, Pre-Feasibility Study for a Road into Northern Labrador](https://www.assembly.nl.ca/business/electronicdocuments/Allnorth-ProjectSummaryReport-RoadToTheNorth.pdf)

Corrected values:

| Benchmark | Previous | Corrected |
| --- | ---: | ---: |
| Gravel-road ROM / km | 2,595,797.280593 CAD/km | **2,583,176.761434 CAD/km** |
| Construction + paving / km | 3,337,453.646477 CAD/km | **3,327,791.100124 CAD/km** |
| Annual maintenance / km-year | 16,069.221261 CAD/km-year | unchanged |

A source-arithmetic validator now recomputes all 10 governed economic benchmarks from their source metadata.

### 4. International Portfolio (12 planning slots): missing attribution fixed

The International Portfolio public artifact previously published factual rationales without any visible source references. This was the largest hallucination risk on an otherwise governed public research surface.

Fixes:

- all 12 candidates now have attributable primary sources;
- 18 candidate source references were added;
- the public JSON carries those sources;
- the web inspector displays clickable references and what each source supports;
- every candidate is marked `PRIMARY_SOURCE_CONFIRMED_NOT_INDEPENDENTLY_AUDITED`;
- the interface explicitly warns that first-party attribution is not independent verification of capacity, commercial appetite, legal eligibility, or future delivery.

Two time-sensitive descriptions were tightened:

- **NAVER Cloud:** a June 2026 announcement says initial 55 MW operations are planned for 2027, with a gigawatt-scale objective; a July 2026 update expanded the planned GAK Sejong deployment from 55 MW to 200 MW. These are plans/future milestones, not 2026 operating capacity. Sources: [NAVER, 2026-06-08](https://navercorp.com/en/media/pressReleasesDetail?seq=10034386) and [NAVER, 2026-07-25](https://www.navercorp.com/en/media/pressReleasesDetail?seq=10034518).
- **SK Telecom / SK Hyper:** SKT announced an up-to-15-GW Korean AIDC program in July 2026, with the first 5 GW staged from 2029, and separately approved SK Hyper as its dedicated AIDC development company. Sources: [SK Telecom, 2026-07-05](https://news.sktelecom.com/en/3155) and [SK Telecom, 2026-07-23](https://news.sktelecom.com/en/3192).

Other primary-source checks added to the portfolio include:

- [OVHcloud AI Training capabilities](https://docs.ovhcloud.com/en/guides/public-cloud/ai-machine-learning/ai-training-capabilities) — BHS/Beauharnois is an active AI Training region; current hardware availability differs from GRA;
- [KDDI, 2026-04-30](https://news.kddi.com/kddi/corporate/csr-topic/2026/04/30/7739.html) — company-reported renewable-electricity procurement, liquid cooling and Telehouse footprint;
- [Verda, 2026-06-02](https://verda.com/blog/nvidia-vr200-r200-early-deployments) — announced Rubin deployments and expected 2027 capacity;
- [Civo sovereign AI](https://www.civo.com/ai/sovereign) — public/private sovereign-AI architecture and residency controls;
- [Sakura Internet, 2026-02-25](https://vip1b.www.sakura.ad.jp/corporate/information/newsreleases/2026/02/25/1968223641/) — company-announced operation of ~1,100 Blackwell GPUs in a containerized Ishikari facility;
- [IONOS service catalog](https://docs.ionos.com/cloud/support/general-information/service-catalog) and [IONOS AI Model Hub governance](https://docs.ionos.com/cloud/ai/ai-model-hub/governance-and-compliance/eu-ai-act) — H200 GPU VMs and German/EU data-residency positioning;
- [Firmus Southgate](https://firmus.co/infrastructure/southgate) and [Firmus 600 MW energy agreement](https://firmus.co/newsroom/firmus-secures-600-mw-energy-supply-agreement-in-south-australia-linked-to-1-2-gw-of-new-renewable-generation-and-battery-storage) — company-described energy-aligned/liquid-cooled infrastructure and energy agreement;
- [Deutsche Telekom / T-Systems Industrial AI Cloud](https://www.telekom.com/en/media/media-information/archive/t-systems-brings-ai-into-the-supply-chain-1105624) — company-reported operation since February 2026 with 10,000 Blackwell GPUs;
- [Nebius infrastructure partners](https://nebius.com/infrastructure-partners), [Meta agreement](https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta), and [Microsoft agreement](https://assets.nebius.com/assets/86625727-9e66-46c1-af79-c27d57434e3c/25-25580-1_Nebius%2520Group%2520N.V._6-K.pdf%3Fcache-buster%3D2025-09-08T21%3A23%3A09.625Z) — partner model and large U.S. counterparties;
- [Scaleway H100](https://www.scaleway.com/en/h100/) — H100 availability in Paris/Warsaw and explicit European-jurisdiction positioning.

### 5. Hydro-Québec data-centre tariff: proposal status qualified with current regulator source

The 0.13 CAD/kWh figure is a **proposed** average price, not a final approved tariff. The canonical evidence already treated it as context-only and non-final. This pass adds the live Régie proceeding as a qualifying source so the current status is traceable.

- [Hydro-Québec proposal](https://nouvelles.hydroquebec.com/nouvelles/communiques/tout-quebec/tarifs-centres-donnees-chaines-blocs-refleteront-valeur-electricite-renouvelable.html)
- [Régie de l’énergie — R-4333-2026](https://www.regie-energie.qc.ca/fr/participants/dossiers/r-4333-2026) — status `En cours` at retrieval on 2026-09-01.

### 6. Jurisdiction policy: legal references added without converting policy into law

The country schedule remains a proposed owner/project policy and explicitly does **not** claim that every listed country is legally prohibited. Four Canadian legal/reference sources were added so reviewers can distinguish internal eligibility policy from Canadian sanctions/export-control law:

- [Global Affairs Canada — Canadian sanctions](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/index.aspx?lang=eng)
- [Global Affairs Canada — Consolidated Canadian Autonomous Sanctions List](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng)
- [Justice Laws — Export and Import Permits Act](https://laws-lois.justice.gc.ca/eng/acts/E-19/index.html)
- [Justice Laws — Export Control List (SOR/89-202)](https://laws-lois.justice.gc.ca/eng/Regulations/SOR-89-202/index.html)

Important: the Government of Canada itself states that the consolidated autonomous sanctions list is an administrative aid, is not a regulation, and has no force of law. Governing regulations and transaction-specific legal review remain controlling.

## Additional current-source spot checks

These high-value active claims were checked against authoritative/current sources and did not require correction in this pass:

- **Nunavik EAUFON-3:** current Kativik Regional Government material targets cable landings/activation in 2027; the canonical evidence correctly treats the phase as planned/under development rather than complete. [KRG EAUFON project update](https://www.krg.ca/en-CA/eaufon-mapping-tools-in-Ungava-Bay)
- **Nunavik fibre funding benchmark:** CRTC Decision 2024-163 authorizes up to CAD 79,419,117 for a 933 km KRG transport-fibre project; the benchmark is correctly labeled a funding-intensity proxy, not a total construction unit cost. [CRTC 2024-163](https://crtc.gc.ca/eng/archive/2024/2024-163.pdf)
- **Nunavut fibre funding benchmark:** CRTC Decision 2024-149 authorizes up to CAD 271,937,242 for approximately 1,300 km; again, the model correctly treats the ratio as a contribution proxy. [CRTC 2024-149](https://web.crtc.gc.ca/eng/archive/2024/2024-149.htm)
- **PUE context:** the Uptime Institute 2025 survey reports average PUE values of 1.48 for facilities commissioned within five years and 1.44 for 20 MW+ facilities; the model correctly labels these as context only, not Kristal Farms site assumptions. [Uptime Institute Global Data Center Survey 2025](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2025.Annual.Survey.Report.pdf?version=0)
- **Lac-Robertson:** Hydro-Québec documentation supports 21 MW hydro plus 4.8 MW diesel and states the system is not connected to the main transmission grid. [Hydro-Québec](https://nouvelles.hydroquebec.com/nouvelles/communiques/montreal/une-entente-visant-a-soutenir-les-initiatives-futures-de-pakua-shipi.html)

## Automated controls added/strengthened

- `pipelines/validate/validate_public_references.py`
  - validates canonical evidence↔source relationships;
  - requires valid evidence references for observations and benchmarks;
  - requires International Portfolio candidate sources and HTTPS URLs;
  - validates community infrastructure source URLs;
  - validates grid `source_ids` against the source registry;
  - validates public evidence source records;
  - requires every public economic benchmark to resolve to public evidence.
- `pipelines/validate/validate_economics.py`
  - now recomputes all 10 benchmark values from source metadata and fails on arithmetic drift.
- publication tests now require candidate references, policy/legal lookup references, UI source exposure, and public benchmark evidence resolution.

## Test result

`pytest -q`: **94 passed**.

The TypeScript typecheck was not run because this snapshot does not contain `apps/web/node_modules`; no dependency installation was performed during the validation pass.

## Remaining risk / next-pass priorities

1. **Primary-source bias:** the International Portfolio sources are mostly company/first-party sources. They prove attribution, not independent truth. A second pass should add independent corroboration for capacity, operating status, ownership/control and customer concentration where it affects decisions.
2. **Legacy internal evidence:** public evidence still contains explicitly typed `internal_legacy_research` records without public URLs. These remain historical context only and should never be treated as current authority.
3. **Source freshness:** fast-changing project schedules, tariffs, sanctions and infrastructure status need a `valid_through`/freshness policy or scheduled revalidation.
4. **Legal status:** sanctions/export-control references are lookup aids; legal screening must resolve the governing regulations and facts for the specific counterparty and transaction.
5. **Publication release discipline:** this work updates the current working publication artifacts but does not create a newly signed/immutable formal release bundle.

## Validation rule of thumb adopted in this pass

A factual statement is not considered decision-ready merely because it has a URL. The minimum acceptable chain is:

**claim → evidence record → attributable source → explicit scope/status/date → publication reference**

For company-announced future capacity, the status must remain **planned/announced** until independently supported as operational.
