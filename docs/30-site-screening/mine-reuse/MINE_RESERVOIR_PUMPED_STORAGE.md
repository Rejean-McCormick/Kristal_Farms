# Mine-Pit Reservoir and Pumped-Storage Research

**As of:** 2026-08-31  
**Status:** Research hypothesis / screening method. Not a project design, storage commitment or environmental conclusion.

## 1. Concept

Open-pit mines can be investigated as existing excavations for pumped-storage hydropower (PSH; `STEP` in French). Depending on site geometry, a pit may serve as the upper or lower reservoir.

Potential configurations include:

1. **paired mine pits** — one upper and one lower;
2. **mine pit + purpose-built reservoir**;
3. **mine pit + freshwater lower/upper basin**, subject to water and ecological constraints;
4. **elevated coastal mine pit + ocean lower reservoir** using seawater.

The user-supplied concept note for the coastal variant is preserved at `sources/user-provided/step_mine_ocean.md`.

## 2. Old mines are eligible for reservoir screening

Unlike underground compute reuse, reservoir suitability is not primarily a function of recent closure.

**Historical/old open-pit mines are explicitly eligible for research.** A decades-old pit can remain attractive if its geometry, usable water volume, reservoir separation, rock stability, hydrogeology, environmental state, rights/governance and grid context are favorable.

The age of the mine is therefore metadata, not a rejection threshold.

## 3. Existing precedents

### Kidston, Australia — abandoned mine pits

Genex's Kidston Pumped Storage Hydro Project reuses the Wises and Eldridge pits of a former gold mine as upper and lower reservoirs. Current project specifications report:

- 250 MW nameplate;
- 8 hours generation duration;
- approximately 2,000 MWh storage;
- maximum gross head about 218 m;
- reuse of mining accommodation, road access and airstrip in addition to the pits.

This is direct evidence that **old mine pits can be central pumped-storage infrastructure**. It does not imply that any northern Québec/Labrador pit is suitable.

Source: https://genexpower.com.au/250mw-kidston-pumped-storage-hydro-project/

### Okinawa Yanbaru, Japan — seawater demonstration

The Okinawa Yanbaru demonstration showed that a pumped-storage plant can use the ocean as the lower reservoir. The IEA Hydropower case study reports approximately:

- 30 MW output;
- 136 m effective head;
- a lined excavated upper pond;
- underground waterways/powerhouse elements;
- seawater-specific engineering.

The facility was a demonstration and was later dismantled; it is evidence of technical feasibility, not a current commercial template.

Source: https://www.ieahydro.org/media/c522ecf0/Annex_VIII_CaseStudy0101_Okinawa_SeawaterPS_Japan.pdf

## 4. Energy-screening physics

For screening only:

```text
E = ρ g h V
```

where `h` is the actual hydraulic level difference and `V` is the usable cycled volume, not total excavation volume.

A useful approximation for freshwater is:

```text
E_kWh ≈ 0.002725 × h_m × V_m3
```

Illustrative gross energy per 1 million m³:

| Gross head | Approx. gross energy |
|---:|---:|
| 150 m | 0.41 GWh |
| 300 m | 0.82 GWh |
| 500 m | 1.36 GWh |
| 670 m | 1.83 GWh |
| 1,000 m | 2.73 GWh |

These are physics checks, not project capacities. Real usable energy depends on operating water levels, losses, dead storage, hydraulic design and round-trip efficiency.

## 5. Initial GIS screening

A research pass may calculate — without ranking — fields such as:

- mine/open-pit geometry;
- lifecycle and restoration state;
- pit rim/floor and candidate operating elevations;
- estimated usable volume with provenance/confidence;
- distance to candidate lower reservoir;
- terrain profile and hydraulic distance;
- proximity to transmission/generation;
- road/air/port/fibre context;
- geology, faults and hydrogeology;
- protected areas, rights/governance and community context.

For a **coastal seawater** concept, a search filter may examine geometries such as high-elevation pits near the coast. Thresholds (for example >500 m elevation or <25 km from the ocean) are research filters only and must not be presented as feasibility standards.

## 6. Seawater-specific constraints

Using the ocean can eliminate the need to build a conventional lower reservoir, but creates first-order constraints:

- corrosion of turbines, pumps, valves and metallic components;
- liner/seepage requirements for the upper reservoir;
- saltwater interaction with groundwater;
- mine-wall geochemistry and contaminant mobilization;
- marine intake/outfall impacts;
- biofouling;
- permitting and rights/governance for both land and marine systems.

No coastal mine should be promoted on geometry alone.

## 7. Mine-specific geotechnical/environmental constraints

Repeated filling and drawdown can affect:

- pit-wall stability;
- pore pressure and fractures;
- waste-rock and tailings stability;
- seepage pathways;
- acid-rock drainage and metal mobilization.

Québec's abandoned-mine program explicitly identifies drainage, contaminants, unstable openings and pit-wall/waste-rock/tailings instability as issues that require site-specific characterization and engineering.

Sources:

- https://www.quebec.ca/en/agriculture-environment-and-natural-resources/mining/mining-reclamation/restoration-abandoned-mining-site/reclaim-abandoned-mine-site
- https://www.quebec.ca/agriculture-environnement-et-ressources-naturelles/mines/restauration-miniere/a-propos

## 8. Power and economic semantics

Pumped storage **does not create net energy**. It shifts energy in time and consumes more electricity while pumping than it later returns.

Therefore Kristal Farms should model mine storage only when there is a specific system reason, such as:

- firming variable renewable generation;
- providing reserves or fast response;
- supporting islanded/weak-grid operations;
- improving utilization of a generation asset or interconnection;
- moving energy between periods with different system value.

Do not claim that a mine reservoir solves a generation shortage.

## 9. Northern research implications

The first northern pass should distinguish:

- **historical open pits** around Schefferville and elsewhere, which can remain valid reservoir research objects even though they are old;
- **recent underground mines** such as Renard, which are more relevant to infrastructure reuse than to a coastal reservoir concept;
- **high-environmental-liability sites** such as asbestos-related mines, which can be kept as geometry/reference cases while carrying explicit contamination constraints.

No current northern mine is selected by this document.
