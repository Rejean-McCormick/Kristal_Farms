# ADR-017 — Economic benchmarks are not site costs

Pass 14 registers completed-project ratios and public funding-intensity ratios as **research benchmarks**. `usable_as_site_estimate=false` is mandatory. A benchmark becomes a scenario input only through an explicit `scenario.assumption` with evidence lineage.

No benchmark may silently populate a candidate-site CAPEX.
