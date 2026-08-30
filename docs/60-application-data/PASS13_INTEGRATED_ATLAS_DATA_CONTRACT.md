# Pass 13 — Integrated Atlas Data Contract

## Purpose
Connect canonical hydrology to community, logistics, telecom, energy and evidence context without inventing geometry or site merit.

## Domain rules
- Community legacy coordinates are `legacy_approximate_community_centroid`, not port/project coordinates.
- Conceptual research corridors use `geometry = NULL`; they are groups, not routes/boundaries.
- Marine/fibre/service context may be related to communities without a map geometry.
- External projects use `role = external_reference`.
- Old Tier/no-go classifications are provenance only.
- `rights_governance` remains research-required unless specific authoritative evidence is attached.
- River/community links imported from old inventory are `legacy_hydro_context`, not site/proximity/consent relations.
- No public property or visual style may encode site rank or merit.
