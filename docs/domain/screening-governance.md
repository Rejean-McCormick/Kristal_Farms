# Screening governance

## Current state

The active decision model is **unranked evidence screening**.

Legacy tiers and historical priorities may be retained for provenance, but they are not active decision outputs.

## Policy fields

The machine-readable policy file is `contracts/policy/kristal-farms-policy.yaml`.

Required behavior while ranking is disabled:

- no numeric composite site score;
- no rank order presented as a recommendation;
- no green/yellow/red opportunity classification;
- no badge such as “best”, “top”, or “priority”; 
- no marker size encoding that implies preference;
- no default sorting by legacy tier as if it were current priority.

## Evidence matrix

Screening should instead track completeness/status by domain, for example:

- energy;
- hydrology;
- environment;
- rights/governance;
- telecom;
- logistics;
- community;
- regulation;
- economics;
- engineering.

## Enabling ranking later

Ranking requires:

1. explicit governance decision;
2. documented methodology;
3. transparent criteria and weights;
4. evidence-quality handling;
5. traceable input values;
6. sensitivity analysis where appropriate;
7. an ADR and policy-version change.
