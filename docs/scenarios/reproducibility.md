# Scenario reproducibility

Every saved evaluation must record enough context to reproduce it.

## Required metadata

- scenario definition version;
- canonical input values and units;
- data release/snapshot ID;
- model version;
- policy version;
- evaluation timestamp;
- stochastic seed if any stochastic model is introduced;
- warnings/errors.

## Model upgrades

Do not overwrite historical results when the model changes. Re-evaluation creates a new result tied to the new model version.

## Exports

Scenario exports should label outputs as modeled results and include assumptions plus version metadata.
