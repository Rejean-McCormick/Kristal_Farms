# Tenant and Counterparty Due-Diligence Runbook

**Status:** Operational draft implementing the C0 international tenancy policy  
**Scope:** International tenant, anchor-offtaker and tenant-operator onboarding.

## Principle

The workflow determines whether Kristal Farms will enter a commercial relationship. It is **not** a workflow for inspecting tenant compute content.

Use the terms:

- **Counterparty Due Diligence (CDD)** for the overall review;
- **Know Your Business (KYB)** for legal-entity verification;
- **Ultimate Beneficial Owner (UBO)** for beneficial ownership;
- **Enhanced Due Diligence (EDD)** when elevated risk requires deeper review.

## Stage 0 — Intake

Create an internal eligibility record containing only what is needed for review:

- legal counterparty name;
- registration jurisdiction and identifier;
- requested commercial role;
- parent/control structure supplied by the prospect;
- requested capacity range and high-level workload class;
- reseller/subtenant intent;
- named commercial contact;
- initial information classification.

Do not request model weights, datasets, prompts, private application logs or decryption keys as part of CDD.

## Stage 1 — Jurisdictional gate

Check `contracts/policy/jurisdiction-eligibility.yaml`.

- `INELIGIBLE`: stop unless the governing C0 policy is formally changed.
- `SUSPENDED`: do not advance to contracting.
- `ENHANCED_DUE_DILIGENCE`: continue only with EDD.
- `ELIGIBLE`: continue with standard CDD.
- no explicit entry: treat as `ENHANCED_DUE_DILIGENCE` under the current default.

The United States counterparty exclusion is an owner policy; it must not be misrepresented as a Canadian legal prohibition.

## Stage 2 — KYB / ownership and control

Verify, proportionate to transaction size and risk:

- corporate registry information;
- parent entities;
- UBOs;
- voting/control rights;
- directors and persons exercising effective control where material;
- material government ownership or control;
- nominee, trust, holding-company or reseller structures relevant to eligibility.

Do not treat a brand name as the contracting entity.

## Stage 3 — Sanctions, trade and export-control review

Screen the legal counterparty, relevant controlling parties and material affiliates against applicable Canadian requirements.

Where advanced computing hardware, technical data or controlled items may be involved, obtain export-control advice separately from the tenant-policy decision.

Record whether the result is:

- project-policy restriction;
- legal restriction;
- both;
- unresolved pending counsel.

## Stage 4 — Responsible-business review

Use evidence appropriate to the risk. Review material findings concerning:

- bribery/corruption and fraud;
- serious human-rights abuse;
- forced labour;
- state-directed political repression or unlawful mass surveillance;
- offensive cyber conduct;
- material misrepresentation or concealed control;
- relevant military/intelligence/state-security role;
- downstream/reseller exposure.

Separate allegation from substantiated finding. Record source quality and date.

## Stage 4.1 — Downstream/reseller capacity boundary

If the prospect resells GPU/cloud capacity, determine whether Kristal Farms capacity would enter a global pool that can serve an `INELIGIBLE` or `SUSPENDED` downstream counterparty. If yes, require a dedicated eligibility-bounded pool or another auditable allocation mechanism before commercial advancement. Audit commercial eligibility records, not private workload content.

## Stage 5 — Technical/commercial fit

Only after the counterparty may proceed, collect the minimum non-content information needed to design service:

- MW/ramp profile;
- density and cooling envelope;
- fibre capacity and redundancy;
- latency requirements;
- reliability and curtailment tolerance;
- physical-access model;
- hardware ownership;
- maintenance/logistics requirements;
- data-residency constraints;
- contract term and expansion options.

## Stage 6 — Eligibility decision

Issue one categorical state:

`ELIGIBLE` / `ENHANCED_DUE_DILIGENCE` / `SUSPENDED` / `INELIGIBLE`.

Record:

- legal entity and control snapshot;
- decision date;
- evidence considered;
- policy and legal basis;
- reviewer and approver;
- unresolved conditions;
- next review date/trigger.

Do not publish internal CDD records by default.

## Stage 7 — Contract controls

The commercial agreement should address:

- accurate and continuing ownership/control representations;
- sanctions/trade compliance;
- subtenant/reseller controls;
- security and access responsibilities;
- confidentiality and black-box boundary;
- purpose-limited provider telemetry;
- incident cooperation;
- legal-process handling;
- change-of-control notification;
- suspension/termination triggers;
- liability and remedy.

The contract should not promise that Kristal Farms verifies the private contents of encrypted workloads.

## Stage 8 — Ongoing review

Refresh CDD based on time and triggers rather than continuous content surveillance.

Trigger events include:

- ownership/control changes;
- sanctions/regulatory change;
- material public enforcement finding;
- reseller/subtenant change;
- serious shared-infrastructure abuse;
- jurisdictional policy change;
- contract renewal or material capacity expansion.

## Stage 9 — Adverse decision / appeal

For non-automatic policy cases, preserve a documented internal review path so decisions are not made from uncorroborated allegations or inconsistent standards.

A review may correct identity, ownership, source or factual errors. An owner-directed categorical exclusion can be changed only through the appropriate C0 authority.
