# Underground Compute / Mine Infrastructure Reuse

**As of:** 2026-08-31  
**Status:** Research hypothesis. Not an engineering conclusion or security certification.

## Hypothesis

A recently closed, suspended or care-and-maintenance underground mine may preserve expensive enabling infrastructure that could support a future Kristal Farms node or reduce the scope of new civil works.

Potentially reusable systems include:

- surface access roads and airstrips;
- ramps, shafts and service drifts;
- underground electrical rooms, substations and switchgear;
- dewatering and pumping;
- ventilation and mine-air infrastructure;
- communications and safety systems;
- workshops, warehouses, camps and water systems;
- existing disturbed industrial land.

This is an **asset-reuse hypothesis**, not a conclusion that server halls should be placed in mine workings.

## Why recent closures are different

For compute/infrastructure reuse, recent closure can matter materially. A mine that has remained in care and maintenance may still have active pumping, inspections, power systems and documented operational infrastructure. With time, assets may be removed, ground support may deteriorate, workings may flood and restoration activities may intentionally eliminate structures.

Therefore the research workflow should preferentially identify mines that ceased material operations within approximately five years, while still allowing older sites where current condition is documented.

## “Bunker” terminology

“Bunker” is acceptable as informal shorthand for the concept, but repository claims should use terms such as:

- `subsurface_compute_reuse`;
- `hardened_infrastructure_concept`;
- `underground_compute_candidate_geometry`.

A mine does not become blast-resistant, EMP-resistant, high-security or disaster-certified merely because it is underground. Those properties require dedicated engineering and security evidence.

## Engineering questions

Before any occupied or compute use, establish at minimum:

1. rock-mass quality, ground support and seismic/geotechnical condition;
2. water inflow, pumping duty and consequence of pump failure;
3. ventilation and smoke-control concept;
4. independent egress and emergency response;
5. fire compartmentation and suppression;
6. electrical capacity, protection, grounding and power quality;
7. heat rejection from the underground space;
8. equipment transport envelope and maintainability;
9. fibre path diversity and communications;
10. radon, dust, contaminants and mine-atmosphere hazards;
11. legal occupancy, mining/restoration and environmental obligations.

## Heat remains a first-order constraint

Subsurface placement can stabilize ambient temperature and protect equipment from surface weather, but it does not make server heat disappear. Nearly all IT electrical input ultimately becomes heat that must be rejected through air, water or another engineered sink.

Any underground concept must therefore model the complete heat path and failure modes, not merely the rock temperature.

## Reference case — Renard, Québec

Renard is a useful **modern infrastructure analogue**, not a Kristal Farms candidate claim.

Current source-backed facts as of 2026-08-31 include:

- mineral processing began in 2016 and operating activities ended in January 2025;
- the mine entered care and maintenance in March 2025;
- 2025 asset-sale materials listed underground substations, switchgear, pumping stations, mine hoists, wire/cable, surface infrastructure, camp and a powerhouse;
- historical technical reporting describes a common underground ramp serving workings to approximately the 710 m level for Renard 2;
- on 2026-07-14 the Superior Court of Québec approved Li-FT Power's exclusive option to acquire Renard; the option period extends to 2028 unless otherwise changed, and the site is being evaluated for lithium-related reuse.

This means Renard demonstrates the **kind of recent mine infrastructure that can survive a shutdown**, while simultaneously demonstrating why availability and current-use conflict must be checked before treating an asset as a project opportunity.

Sources:

- Li-FT Power, 2026-06-24: https://www.li-ft.com/news/lift-enters-into-binding-call-option-agreement-for-the-acquisition-of-the-renard-mine-site
- Li-FT Power, 2026-07-14: https://www.li-ft.com/news/court-approves-option-to-acquire-the-renard-mine-site
- TCL Asset Group, Renard underground asset sale: https://www.managingyourassets.com/auctions/view_auction?id=446
- Historical Renard technical report (SEC-hosted): https://www.sec.gov/Archives/edgar/data/1627272/000106299319001469/exhibit99-1.htm

## Decision posture

Underground mine reuse should be treated as an **optional CAPEX/risk-reduction pathway**. It must never become a siting requirement that causes Kristal Farms to reject a stronger energy/fibre/community corridor simply because it lacks a mine.
