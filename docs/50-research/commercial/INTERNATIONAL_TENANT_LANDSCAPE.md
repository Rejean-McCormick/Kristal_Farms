# International Tenant Landscape — Optimized 12-Slot Research Portfolio

**As of:** 2026-08-31  
**Status:** Working commercial research (C4), proposed r2 update.  
**Critical caveat:** Inclusion means **research candidate only**. It does not mean the organization has expressed interest in Kristal Farms, passed counterparty due diligence, or agreed to Canadian/northern deployment.

## 1. Governance first

Commercial screening follows:

> **jurisdictional eligibility → legal-counterparty/control review → downstream-customer exposure → workload/site fit → non-binding requirements → service envelope → anchor/offtake discussion**

The proposed r2 jurisdiction schedule expands project-level exclusions/holds beyond the existing United States rule. The schedule remains a counterparty-risk control, not a judgment about individuals or populations. Technology-origin policy remains separate: U.S.-origin GPUs, software or standards are not automatically prohibited merely because a counterparty jurisdiction is ineligible.

A reseller, GPU cloud or operator does not bypass the policy. Where a global capacity pool can serve ineligible downstream counterparties, Kristal Farms should require a **dedicated, auditable, non-ineligible capacity pool** without inspecting private workload content.

## 2. Why the portfolio is being changed

The previous list mixed four different things: probable anchor tenants, AIDC/network operators, sovereignty-oriented clouds whose products may not travel to Canada, and AI-cloud resellers whose downstream customer mix can conflict with the jurisdiction policy.

The optimized portfolio therefore uses role-specific outreach rather than treating twelve logos as equivalent tenants.

## 3. Optimized 12

| Slot | Organization | Home | Engagement | Primary Kristal Farms role | Main gate |
|---:|---|---|---|---|---|
| 1 | **OVHcloud** | France | **Core outreach** | Anchor AI/HPC campus | Validate high-density Canadian expansion appetite |
| 2 | **NAVER Cloud** | South Korea | **Core outreach** | Global AI-factory anchor | Validate Canada-eligible workloads and downstream allocation |
| 3 | **SK Telecom / SK Hyper** | South Korea | **Core outreach** | AIDC co-development | Validate appetite outside Korea-centered 15 GW program |
| 4 | **KDDI / Telehouse** | Japan | **Core outreach** | AIDC/network partner | Validate strategic value of a Canadian energy-side node |
| 5 | **Verda** | Finland | **Core outreach** | Flexible training / AI-cloud anchor | Ownership/control and downstream eligibility review |
| 6 | **Civo** | United Kingdom | **Core outreach** | Private/sovereign AI node | Validate Canadian deployment and residency model |
| 7 | **Sakura Internet** | Japan | Secondary | Training/HPC pilot | Domestic sovereignty may constrain offshore workloads |
| 8 | **IONOS** | Germany | Secondary | Sovereign/private AI capacity | Determine whether Canada can fit its sovereignty proposition |
| 9 | **Firmus Technologies** | Australia | Strategic exploration | Energy-aware AIDC co-development | Ownership/control + downstream ring-fencing review |
| 10 | **Deutsche Telekom / T-Systems** | Germany | Selective | Industrial AI/HPC node | Germany/Europe sovereignty orientation |
| 11 | **Nebius** | Netherlands | **Conditional only** | Partner-hosted AI cloud | Dedicated non-US/non-ineligible capacity pool required |
| 12 | **Scaleway / iliad** | France | Selective | Sovereign AI research | European residency posture may make Canada unsuitable |

### Removed from the core twelve

- **Nscale** — excellent technical fit, but current growth is materially concentrated in Microsoft-linked deployments. Keep on watchlist; re-enter only if a contractually isolated non-ineligible customer pool is credible.
- **Infomaniak** — retain as a privacy/sustainability benchmark, not as a likely Canadian tenant while Swiss processing/residency is central to the product.
- **Exoscale** — retain as a European sovereign-cloud benchmark; current residency logic makes Canadian deployment a weak prospect.

## 4. Role-specific commercial offers

### A. KF Anchor AI Campus

For OVHcloud and NAVER first; potentially IONOS later.

- firm high-density power envelope;
- liquid-cooling interface;
- redundant fibre handoff;
- tenant-controlled hardware/software/data/keys;
- staged expansion rather than a single all-or-nothing campus;
- site-specific reliability/curtailment terms.

Do not promise a fixed MW before corridor/site engineering and tenant requirements converge.

### B. KF Flexible Training Node

For Verda, Sakura and conditionally Nebius.

- firm base capacity plus an optional flexible tranche;
- workloads biased toward training, HPC, batch and checkpointable processing;
- explicit curtailment profile rather than assuming GPUs can simply stop whenever generation falls;
- commercial separation from any ineligible global customer pool.

### C. KF AIDC Development Partnership

For SK Telecom/SK Hyper, KDDI/Telehouse and Firmus.

Kristal Farms develops the energy/site/community/logistics layer; the partner may contribute facility design, liquid cooling, network, DC operations and AI-factory integration. This is a different pitch from a normal rack lease.

### D. KF Selective Sovereign Node

For Civo, IONOS, Deutsche Telekom/T-Systems and Scaleway.

The question is not whether these firms like sovereignty in the abstract. It is whether they have a workload/product class whose sovereignty requirements can be satisfied **in Canada** under tenant control. If not, they remain useful benchmarks but should not absorb major business-development effort.

## 5. Concentration rules

The twelve-slot portfolio is a resilience experiment, not a coalition. Commercial development should avoid hidden concentration by:

- country/control structure;
- one global customer appearing behind multiple resellers;
- GPU supply chain;
- carrier and landing route;
- port/logistics route;
- one site/corridor;
- one financing source.

No slot should be treated as committed capacity without attributable evidence such as an RFI/RFP response, requirements exchange, LOI or contract.

## 6. Sources — current market-role signals only

These sources support the **research posture**, not interest in Kristal Farms:

- OVHcloud AI Training regions / Beauharnois: https://docs.ovhcloud.com/en/guides/public-cloud/ai-machine-learning/ai-training-capabilities
- NAVER global AI-factory roadmap (2026-06-08): https://navercorp.com/en/media/pressReleasesDetail?seq=10034386
- NAVER / Brookfield / NVIDIA 200 MW expansion (2026-07-25): https://www.navercorp.com/en/media/pressReleasesDetail?seq=10034518
- SK Telecom 15 GW AIDC roadmap (2026-07-05): https://news.sktelecom.com/en/3155
- SK Hyper launch (2026-07-23): https://news.sktelecom.com/en/3192
- KDDI data-center renewables and liquid cooling (2026-04-30): https://news.kddi.com/kddi/corporate/csr-topic/2026/04/30/7739.html
- Verda global Rubin deployments (2026-06-02): https://verda.com/blog/nvidia-vr200-r200-early-deployments
- Civo sovereign/private AI: https://www.civo.com/ai/sovereign
- Civo Vera Rubin allocation (2026-07-23): https://www.civo.com/newsroom/civo-to-host-nvidia-vera-rubin-sovereign-uk-infrastructure
- Sakura Blackwell container infrastructure (2026-02-25): https://www.sakura.ad.jp/corporate/information/newsreleases/2026/02/25/1968223641/
- IONOS H200 Cloud GPU VMs: https://docs.ionos.com/cloud/compute-services/compute-engine/cloud-gpu-vm
- Firmus energy-aware AI factory software: https://firmus.co/newsroom/firmus-to-build-grid-integrated-ai-factory-software-with-nvidia
- Firmus Australia renewable AI-factory network: https://firmus.co/newsroom/southgate-expansion
- Deutsche Telekom / T-Systems Industrial AI Cloud: https://www.telekom.com/en/media/media-information/archive/t-systems-brings-ai-into-the-supply-chain-1105624
- Nebius infrastructure-partner model (2026-07-15): https://nebius.com/newsroom/nebius-introduces-business-model-to-scale-ai-cloud-globally-through-infrastructure-partnerships
- Nebius / Meta agreement (2026-03-16): https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta
- Nebius / Microsoft agreement (2025-09-08): https://nebius.com/newsroom/nebius-announces-multi-billion-dollar-agreement-with-microsoft-for-ai-infrastructure
- Nscale / Microsoft deployments: https://www.nscale.com/press-releases/nscale-microsoft-2025
- Scaleway GPU clusters: https://www.scaleway.com/en/gpu-clusters/

## 7. Prospect-fit questions

Before moving any candidate past research, establish:

1. legal contracting entity, UBO and effective control;
2. material downstream customer exposure and reseller structure;
3. minimum initial MW and expansion increments;
4. required fibre capacity, peering points, path diversity and repair SLA;
5. rack/pod density, power quality and cooling envelope;
6. firm-power requirement and acceptable flexible/curtailable tranche;
7. data-residency and sovereignty constraints;
8. tenant-owned versus operator-owned hardware;
9. minimum contract term, credit/offtake structure and termination conditions;
10. physical-security, access, spare-parts and maintenance model;
11. whether black-box/content-blind operation is commercially valued or required;
12. export-control implications for the intended hardware stack;
13. whether capacity can be contractually isolated from ineligible downstream counterparties;
14. whether the organization can contract directly or requires a Canadian affiliate/partner.
