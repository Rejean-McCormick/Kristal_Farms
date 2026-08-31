# Document Authority Model

This model prevents polished, older or derived documents from overriding current project intent or evidence discipline.

## Authority classes

| Class | Meaning | Location / examples |
|---|---|---|
| **C0 — Project control** | Current scope, principles, state, decisions and release interpretation. | `docs/00-control/` |
| **C1 — Reference architecture** | Current physical/commercial project architecture and deployment strategy. | `docs/10-core/*Reference_Architecture*`, current project vision, deployment and tenancy reference files |
| **C2 — Application contracts** | Product, data, API, scenario, frontend and architecture rules. | `docs/product/`, `docs/architecture/`, `docs/data/`, `contracts/` |
| **C3 — Structured evidence** | Controlled datasets and observations, authoritative only for what their sources support. | `data/`, `sources/` |
| **C4 — Working research** | Research methods, screening, cost studies and source analyses requiring validation before project claims. | `docs/30-site-screening/`, `docs/40-economics/`, `docs/50-research/` including commercial prospect research |
| **C4O — Project direction** | Recorded owner/project intent; authoritative for intent, not independent factual evidence. | `sources/owner-direction/` |
| **C4L — Long-horizon concepts** | Optional future human/community/learning concepts; not prerequisites or commitments. | `docs/70-long-horizon/` |
| **C5 — Archive** | Superseded narratives, old partner packages, build history and research snapshots. | `archive/` |

## Conflict rule

When materials conflict:

1. current project-control documents govern intent and interpretation;
2. current reference architecture governs the physical/commercial model;
3. source evidence governs factual claims within its scope and date;
4. assumptions remain assumptions;
5. archived material never silently overrides active state.

## Promotion rule

A research statement becomes an external project claim only when its source, scope, date, uncertainty and required technical/community/environmental validation are clear.
