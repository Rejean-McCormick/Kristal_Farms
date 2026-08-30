# Economic data contract

## Evidence

`research.economic_benchmark` stores externally sourced ratios and context. Every benchmark is marked `usable_as_site_estimate=false`.

## Assumptions

`scenario.assumption` is the explicit bridge from benchmark/context to a scenario. Unknown site costs are stored as `UNPRICED`, never silently treated as zero.

## Results

`scenario.result` stores derived outputs with algorithm key/version and completeness state.

## Sensitivity

`scenario.sensitivity_case` stores non-site distance stress cases.

## Forbidden automatic outputs

The generic economic workflow does not produce project IRR, bankable NPV, net project savings, site rank, project MW/head/design flow or a winning-site conclusion. Those require a project-specific dossier with engineering and commercial evidence.
