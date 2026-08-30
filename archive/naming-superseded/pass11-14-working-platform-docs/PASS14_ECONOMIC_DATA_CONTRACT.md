# Pass 14 economic data contract

## Evidence
`research.economic_benchmark` stores externally sourced ratios and context. Every row has `usable_as_site_estimate=false`.

## Assumptions
`scenario.assumption` is the only allowed bridge from benchmark/context to a scenario. Unknown site costs are stored as `UNPRICED`, never zero.

## Results
`scenario.result` stores derived outputs with algorithm key/version and completeness state.

## Sensitivity
`scenario.sensitivity_case` stores non-site distance stress cases.

## Forbidden automatic outputs
- project IRR
- bankable NPV
- net project savings
- site score/rank
- project MW/head/design flow

unless a future project-dossier workflow provides the required engineering and commercial evidence.
