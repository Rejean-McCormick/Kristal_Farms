# Responsible International Tenancy and Counterparty Governance

**Status:** Current project-control policy (C0)  
**Effective:** 2026-08-31  
**Scope:** Tenant, operator, offtaker, reseller and material commercial-counterparty eligibility for Kristal Farms compute infrastructure.  
**Legal note:** This is a project policy, not legal advice, a sanctions determination, or a human-rights rating of any population. Contracting decisions remain subject to applicable Canadian law, trade controls, sanctions, competition rules and legal review.

## 1. Policy objective

Kristal Farms is designed to serve an international compute market without treating maximum tenant volume as the governing objective. The project may decline otherwise lawful business when a counterparty, control structure, jurisdictional exposure or institutional purpose is materially inconsistent with project values, risk tolerance or long-term legitimacy.

The governing sequence is:

> **jurisdictional eligibility → counterparty due diligence → contractual eligibility → black-box tenancy**

Kristal Farms therefore governs **who receives access to project infrastructure**. It does not make routine access to a tenant's private compute content a condition of tenancy.

## 2. International market posture

International tenancy is an intended commercial pathway. Prospecting should prioritize organizations that can use remote or northern compute effectively, including large-scale model training, scientific/HPC workloads, batch processing, sovereign or jurisdiction-controlled cloud capacity, and other high-density workloads whose value is not dependent on metropolitan-edge latency.

Commercial scale does not override the eligibility policy. A large prospective tenant is not automatically preferred over a smaller eligible tenant.

### 2.1 Current owner-directed exclusion

**United States-based or United States-controlled counterparties are not eligible for Kristal Farms tenant, anchor-offtaker or tenant-operator roles under the current owner policy.**

This is a project-level values and commercial-positioning decision. It is not a factual claim that every United States person or organization presents the same conduct or risk. Any future change requires an explicit C0 project-control decision.

This exclusion applies to the **counterparty relationship**. It does not, by itself, prohibit equipment, software, standards, components, financing instruments or supply-chain dependencies originating in the United States. Technology-origin policy is a separate decision and must not be inferred from tenant eligibility.

## 3. Eligibility states

Kristal Farms uses categorical decisions rather than a numerical "ethics score."

| State | Meaning | Contracting posture |
|---|---|---|
| **ELIGIBLE** | No identified policy-level barrier after proportionate review. | Normal commercial diligence may proceed. |
| **ENHANCED_DUE_DILIGENCE** | Material uncertainty, complex ownership, elevated jurisdictional risk or sensitive institutional role requires deeper review. | No binding tenancy until review is closed. |
| **SUSPENDED** | Eligibility cannot presently be determined or external events require a temporary hold. | New contracting and expansion paused. |
| **INELIGIBLE** | Counterparty or controlling relationship conflicts with an explicit project exclusion or unacceptable risk threshold. | No tenancy/offtake/operator agreement. |

The state applies to a **specific legal counterparty and control structure at a point in time**. It must not be generalized to individuals based on nationality, ethnicity, religion or other protected characteristics.

## 4. Jurisdictional screening factors

Country and jurisdiction review is a risk-control input, not a moral ranking of populations. The review should consider, with dated sources and legal review where required:

- rule of law and independence of institutions;
- internationally recognized human-rights conditions;
- sanctions, export-control and trade-restriction exposure;
- armed-conflict, aggression, atrocity, occupation or severe political-instability risk where relevant to the counterparty;
- state-directed censorship, political surveillance or coercive digital-control risk;
- corruption, bribery and beneficial-ownership transparency;
- labour-rights and forced-labour exposure;
- cyber-abuse, state-linked intrusion or technology-transfer risk;
- privacy, data-governance and lawful-access environment;
- the practical ability to identify the counterparty, its controllers and source of funds;
- compatibility with Canadian legal and regulatory obligations.

A jurisdiction may be placed in **ENHANCED_DUE_DILIGENCE**, **SUSPENDED** or **INELIGIBLE** status without asserting that every organization in that jurisdiction has engaged in misconduct.

The machine-readable jurisdiction schedule uses **ENHANCED_DUE_DILIGENCE as the default for non-listed jurisdictions** until a review establishes an explicit posture. Absence from the schedule is therefore not automatic approval. See `contracts/policy/jurisdiction-eligibility.yaml`.

## 5. Counterparty due diligence

Before signing a tenancy, anchor-offtake or tenant-operator agreement, Kristal Farms should establish, proportionate to risk:

1. legal name, registration and principal place of business;
2. ultimate beneficial ownership and persons/entities exercising effective control;
3. relevant parent, subsidiary and affiliated entities;
4. sanctions and restricted-party screening under applicable Canadian law;
5. material export-control or controlled-technology implications known at contracting time;
6. source of funds and financing structure where commercially material;
7. significant public enforcement, corruption, fraud, human-rights or cyber-abuse findings relevant to the relationship;
8. whether the counterparty acts for an undisclosed government, military, intelligence service or sanctioned party;
9. whether the tenant will resell/sublease capacity and, if so, how downstream counterparties remain within the same policy boundary;
10. a high-level declared workload class sufficient for safety, power, cooling, networking and legal classification **without requiring disclosure of private models, datasets, prompts or application content**.

Due diligence should be evidence-backed and periodically refreshed. Rumour, social-media controversy or nationality alone is insufficient for an adverse decision.

## 5.1 Institutional-purpose risk treatment

Some organization types require a higher bar even when the private workload is not visible. The decision concerns the **counterparty and its externally verifiable institutional role**, not a hidden inspection of tenant content.

Presumptive **INELIGIBLE** treatment may apply, when substantiated, to a counterparty whose relevant institutional purpose or conduct includes sanctions evasion/prohibited-party concealment, material eligibility fraud, state-directed repression or unlawful mass surveillance, or offensive cyber activity directed at civilian/shared infrastructure.

At minimum **ENHANCED_DUE_DILIGENCE** should apply to military/defence entities, intelligence or state-security bodies, population-scale biometric-surveillance providers, high-risk dual-use technology providers, and reseller/subtenant aggregators. A later C0 decision may tighten or relax these classes.

This treatment does not require Kristal Farms to determine the content of an encrypted workload. It is based on the identity, control, declared relationship and externally verifiable conduct of the counterparty.

## 6. Black-box tenancy principle

After an eligible counterparty is admitted, the default service is a **tenant-controlled encrypted environment**. "Black-box tenancy" is an acceptable commercial shorthand; the normative meaning is:

- tenant-controlled hardware and/or logically dedicated systems as contracted;
- tenant-controlled operating systems, models, datasets and applications;
- tenant-controlled cryptographic keys;
- no operator key escrow as a default service requirement;
- no routine Kristal Farms access to decrypted application payloads;
- no routine inspection of tenant models, training data, prompts, outputs or internal telemetry;
- no covert monitoring mechanism or standing backdoor created for commercial-policy enforcement.

Kristal Farms cannot truthfully promise to verify the private content of an encrypted tenant environment that it is contractually and technically designed not to inspect.

The project rule is therefore:

> **Select counterparties; do not inspect private compute.**

See `docs/security/TENANT_CONFIDENTIALITY_BOUNDARY.md` and ADR-0021.

## 7. What Kristal Farms may observe

Content blindness does not mean operational blindness. Kristal Farms may collect the minimum information reasonably necessary to provide and protect shared infrastructure, including as contractually defined:

- power consumption, power quality and curtailment state;
- cooling demand, thermal and environmental telemetry;
- physical-access and facility-security events;
- network availability, aggregate utilization, routing and fault telemetry;
- security signals needed to protect shared facility/network infrastructure without decrypting tenant application content;
- billing, metering, SLA and maintenance records;
- information voluntarily shared by the tenant for support or incident response.

Telemetry must be purpose-limited, access-controlled and retained according to an explicit policy.

## 8. Contractual compliance without content inspection

The tenant agreement should rely on **representations, warranties, covenants and termination rights**, not hidden workload surveillance.

At minimum, an eligible tenant should contractually undertake to:

- comply with applicable Canadian law and valid regulatory requirements;
- comply with applicable sanctions, export controls and trade restrictions;
- not use the tenancy as a vehicle for sanctions evasion or concealed prohibited-party access;
- provide accurate ownership/control information and report material changes;
- apply the same eligibility boundary to authorized subtenants/resellers where subletting is permitted;
- maintain appropriate security for its own systems, credentials and keys;
- cooperate with proportionate legal/compliance inquiries that do not require routine disclosure of private compute content;
- notify Kristal Farms when a material change makes a prior eligibility representation inaccurate.

A contractual statement is not the same as technical verification of content. Documentation must preserve that distinction.

## 9. Review, suspension and termination triggers

A counterparty may be re-reviewed, suspended or terminated when supported by evidence and contract, including:

- sanctions designation or a legally binding prohibition;
- material undisclosed beneficial-ownership/control change;
- substantiated sanctions-evasion or concealed prohibited-party access;
- material fraud in eligibility representations;
- serious, externally verifiable conduct inconsistent with the adopted counterparty policy;
- repeated facility/network abuse that threatens shared infrastructure or other tenants;
- legal inability to continue providing the service.

The response should be proportionate and documented. The policy does not authorize Kristal Farms to defeat tenant encryption to search for possible violations.

## 10. Legal process and government requests

Kristal Farms should maintain a legal-request procedure based on:

- validation of jurisdiction and legal authority;
- scope minimization;
- disclosure only of information Kristal Farms actually possesses or controls;
- tenant notice where legally permitted;
- no voluntary creation of a standing decryption capability;
- no weakening of tenant encryption merely to make future access easier;
- documented handling and independent legal review for exceptional requests.

If Kristal Farms does not possess tenant keys or decrypted content, documentation must not imply otherwise.

## 11. Resellers, operators and layered tenancy

A tenant must not be permitted to defeat the eligibility policy through undisclosed subleasing, nominee structures or reseller chains.

Where downstream tenancy is allowed, contracts should define:

- whether Kristal Farms approves each downstream legal counterparty or approves a documented eligibility process operated by the primary tenant;
- audit rights over the **eligibility process and records**, not private workload content;
- notification of material control changes;
- suspension rights where the downstream structure cannot be verified.

## 12. Governance and evidence discipline

International eligibility decisions should record:

- decision state and date;
- legal counterparty and ownership/control snapshot;
- sources reviewed;
- reviewer/approver;
- unresolved issues;
- next review date or trigger;
- whether the decision is project-policy, legal requirement, or both.

Do not convert third-party democracy, corruption, sanctions or human-rights indices into an automatic Kristal Farms score. External indices are research inputs; project eligibility remains an explicit decision with documented reasoning.

## 13. Reference baseline

The policy may draw from, without treating any single source as dispositive:

- internationally recognized human-rights instruments already listed in `docs/50-research/governance/HUMAN_RIGHTS_REFERENCE_BASE.md`;
- UN Guiding Principles on Business and Human Rights;
- OECD Guidelines for Multinational Enterprises on Responsible Business Conduct;
- OECD AI Principles where AI actors/workloads are relevant;
- current Canadian sanctions regulations and official consolidated reference lists;
- current Canadian export-control rules;
- jurisdiction-specific legal advice where a real transaction is contemplated.

See `docs/50-research/governance/INTERNATIONAL_TENANT_SCREENING_REFERENCE_BASE.md`.

## 14. Policy boundary

This document governs **commercial eligibility and confidentiality boundaries**. It does not:

- claim that Kristal Farms can determine the contents of an encrypted tenant environment;
- authorize discrimination against individuals on protected grounds;
- replace sanctions/export-control legal advice;
- establish that a specific prospective organization has expressed interest in Kristal Farms;
- establish a technology-origin embargo;
- create a blanket military/intelligence prohibition beyond the current enhanced-due-diligence treatment unless a later explicit C0 decision does so.
