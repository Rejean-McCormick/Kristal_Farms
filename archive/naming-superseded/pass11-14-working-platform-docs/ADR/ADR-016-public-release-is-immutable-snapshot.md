# ADR-016 — Public atlas releases are immutable snapshots

## Status
Accepted — Pass 13

The Showcase consumes an immutable release snapshot. Live research can continue to change independently. Release metadata records the dataset version, screening mode and `ranking_allowed=false`. This prevents a public story from silently changing as research fixtures evolve.
