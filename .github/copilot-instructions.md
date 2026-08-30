Follow the repository's root `AGENTS.md` and accepted ADRs before generating or modifying code.

In particular:
- keep canonical data in PostGIS, not frontend constants;
- keep evidence separate from geometry;
- do not infer compute capacity from planning margin;
- enforce `ranking_allowed: false` from policy;
- use layer catalog configuration for generic map layers;
- keep scenario assumptions/results separate from observed research data;
- update machine contracts and documentation when semantics change.
