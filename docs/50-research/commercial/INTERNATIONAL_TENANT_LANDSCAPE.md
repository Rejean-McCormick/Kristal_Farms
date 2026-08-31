# International Tenant Landscape — Research Inventory

**As of:** 2026-08-31  
**Status:** Working commercial research (C4).  
**Critical caveat:** Inclusion means **research candidate only**. It does not mean the organization has expressed interest in Kristal Farms, passed counterparty due diligence, or agreed to Canadian/northern deployment.

## Screening assumptions

This inventory applies the current project posture:

- United States-based or United States-controlled counterparties are excluded from tenant/anchor-offtaker/tenant-operator roles by owner policy;
- international prospects remain subject to jurisdictional and counterparty due diligence;
- the technical/commercial model is tenant-controlled encrypted compute on serviced infrastructure;
- prospect fit is strongest for training, HPC, batch and other workloads that can tolerate non-metropolitan placement;
- data-residency or domestic-sovereignty commitments may make an otherwise attractive organization a poor Canadian tenant;
- United States technology dependencies are a separate supply-chain issue and are **not** automatically excluded by the current tenant policy.

## Priority research jurisdictions

The initial outbound research set should emphasize stable, rules-based markets with significant AI/HPC/cloud operators and plausible international deployment behavior:

- France;
- Netherlands;
- United Kingdom;
- Switzerland;
- Norway, Sweden, Finland, Denmark and Iceland;
- Germany;
- Japan;
- South Korea;
- Australia and New Zealand.

This list is a prospecting focus, not an automatic country whitelist.

## Candidate organizations

| Organization | Home market | Potential Kristal Farms role | Research posture |
|---|---|---|---|
| **OVHcloud** | France | cloud / bare-metal / potential Canadian capacity operator | **Priority** — already operates Canadian infrastructure; investigate AI/HPC expansion fit. |
| **Nebius** | Netherlands | AI-cloud platform / infrastructure-partnership offtaker | **Priority** — its 2026 partner model explicitly allows third parties to own/operate infrastructure hosting Nebius capacity. |
| **Nscale** | United Kingdom | AI-cloud tenant/operator on partner-run sites | **Priority with enhanced review** — partner-run renewable sites fit the model; material U.S. activity means ownership/control and customer concentration should be reviewed against project policy. |
| **SK Telecom** | South Korea | GPUaaS / AI-infrastructure operator | **Priority research** — operates large-scale Blackwell GPU infrastructure; investigate international node strategy. |
| **NAVER / NAVER Cloud** | South Korea | cloud / AI infrastructure | **Research** — investigate international capacity and Canadian deployment appetite before any claim. |
| **Sakura Internet** | Japan | GPU cloud / managed supercomputing | **Priority research** — substantial current AI-infrastructure investment; domestic sovereignty orientation may limit offshore workloads. |
| **KDDI** | Japan | telecom + GPU cloud + data-center operator | **Priority research** — strong integration of network and AI compute; determine whether international capacity is strategically relevant. |
| **Deutsche Telekom / T-Systems** | Germany | industrial AI cloud / HPC operator | **Selective research** — strong compute demand but current sovereign offerings emphasize European/German control. |
| **Scaleway / iliad** | France | GPU cloud / dedicated AI clusters | **Selective research** — strong values/sovereignty fit, but explicit European data-residency posture may make Canadian placement unsuitable for core sovereign products. |
| **Infomaniak** | Switzerland | sovereign cloud / AI services | **Comparative / selective** — strong privacy and sustainability alignment; Swiss-only processing commitments make Canadian tenancy less natural. |
| **Exoscale** | Switzerland/Europe | sovereign European cloud | **Comparative / selective** — European-only residency positioning is a likely geographic constraint. |

## Source starting points

The following official/current sources support the **market-role observations only**. They do not establish interest in Kristal Farms.

- OVHcloud global locations / Beauharnois and Toronto: https://www.ovhcloud.com/fr-ca/datacenter/
- Nebius infrastructure-partnership model (2026-07-15): https://nebius.com/newsroom/nebius-introduces-business-model-to-scale-ai-cloud-globally-through-infrastructure-partnerships
- Nscale AI infrastructure / partner-run sites: https://www.nscale.com/ai-infrastructure
- SK Telecom Blackwell GPU infrastructure / GPUaaS: https://news.sktelecom.com/en/2812
- Sakura Internet Blackwell infrastructure (2026-02-25): https://www.sakura.ad.jp/corporate/information/newsreleases/2026/02/25/1968223641/
- KDDI GPU Cloud / GB200 NVL72: https://newsroom.kddi.com/news/detail/kddi_nr-796_4171.html
- Deutsche Telekom / T-Systems Industrial AI Cloud: https://www.telekom.com/de/medien/medieninformationen/detail/t-systems-und-supplyon-bringen-ki-in-europas-lieferketten-1105618
- Scaleway GPU clusters: https://www.scaleway.com/en/gpu-clusters/
- Infomaniak sovereign AI services: https://www.infomaniak.com/en/hosting/ai-services
- Exoscale AI cloud infrastructure: https://www.exoscale.com/ai-cloud-infrastructure/

## Prospect-fit questions

Before a candidate becomes a commercial target, establish:

1. minimum initial contracted MW and expansion increments;
2. acceptable distance/latency from major peering markets;
3. required fibre capacity, path diversity and repair SLA;
4. rack/pod density and power-quality requirements;
5. liquid-cooling and heat-rejection requirements;
6. acceptable curtailment/interruption profile, if any;
7. data-residency and sovereignty constraints;
8. tenant-owned versus operator-owned hardware preference;
9. minimum contract term and credit/offtake structure;
10. physical-security, access and maintenance model;
11. whether black-box/content-blind operations are commercially valued or required;
12. beneficial ownership, controlling jurisdiction and material downstream customer exposure;
13. export-control implications for the intended hardware stack;
14. whether the organization can contract directly or only through a Canadian affiliate/partner.

## Commercial sequencing

The preferred sequence is:

> **screen eligibility → validate workload/site fit → obtain non-binding requirements → define service envelope → pursue anchor/offtake structure**

Do not lead with a specific hydro site before the tenant requirement envelope is understood, and do not present a research candidate as a committed partner.
