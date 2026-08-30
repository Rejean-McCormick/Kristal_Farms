# Pass 12 — Hydrology derivation policy

## Research statistics are not engineering selections

A climatological monthly mean can be derived automatically when source coverage satisfies a documented QA gate. A **design flow cannot**.

The initial algorithm `hydrology.climatological_monthly_mean@1.0.0` uses configurable defaults:

- minimum 10 sufficiently complete calendar years;
- minimum annual completeness fraction 0.90;
- minimum month completeness fraction 0.80.

These are **Kristal research-QA defaults**, not universal hydrology standards and not evidence of engineering sufficiency. They may be changed only by versioning the algorithm/parameters.

Low-flow frequency metrics, firm-energy selection, environmental flow, design flood and turbine design flow are intentionally deferred to later hydrology/engineering work.
