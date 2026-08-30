# Hydro Resource Atlas Method — Pass 9

Date: 2026-08-30

## Objective

Build a defensible northern hydro atlas without turning map references into dam sites. The object of study is a **river research reach**, not a project.

## Evidence sequence

1. official named watercourse / WSC station anchor;
2. official station drainage-area metadata;
3. authoritative WSC station-basin polygon;
4. authoritative connected river flowline (GRHQ in Québec; national NHN/Canada1Water where needed);
5. official hydrometric time series / HYDAT extraction;
6. HRDEM terrain profile along the connected reach;
7. environmental + rights/governance joins;
8. port/road/fibre/logistics joins;
9. only then a site-specific intake/powerhouse concept;
10. only then project head, design flow, MW and economics.

## Critical distinctions

- **Gauge point ≠ dam site.**
- **Station drainage area ≠ a hand-drawn watershed.**
- **Terrain drop ≠ hydraulic project head.**
- **Mean river flow ≠ design flow.**
- **Q × H screening ≠ feasible MW.**
- **Straight-line distance ≠ access route.**
- **Evidence completeness ≠ opportunity/suitability.**

## Pass-9 limitation

Official WSC basin packages, GRHQ hydrography and Canada1Water/NHN source families were verified. Binary geometry could not be ingested in this execution environment. Therefore layers 34–36 and 38–39 intentionally use null geometry where the desired polygon/flowline/route is unavailable. Layer 37 contains actual official WSC station point geometry.

No synthetic watershed, river line, terrain profile or project site is permitted as a fallback.
