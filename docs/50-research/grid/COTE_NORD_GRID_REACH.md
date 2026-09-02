# Northern Atlas electrical network context

**Status:** research context  
**Ranking:** not allowed  
**Geometry:** schematic connectivity only; not engineering geometry

## Purpose

This layer provides a lightweight, source-backed view of material electrical infrastructure across the Northern Atlas study geography. It represents documented transmission links and real electrical nodes rather than artificial map-edge or reach terminals. It is not a complete Hydro-Québec or Newfoundland and Labrador network map.

The machine-readable research model is split into three contracts:

- `research/grid/cote_nord_grid_reach.yaml` — documented connections and map policy;
- `research/grid/electrical_assets.yaml` — generating stations, substations/grid areas, community connections and selected isolated assets;
- `research/grid/electrical_sources.yaml` — source registry shared by the network and assets.

## Network modes

Each node and connection is classified independently:

- `integrated` — part of the interconnected Québec/Labrador transmission context;
- `integrated_extension` — a material extension of the main grid, such as the La Romaine / Unamen Shipu connection;
- `isolated` — a remote electrical system not represented as connected to the main transmission network.

This prevents an isolated generating station from being visually interpreted as the end of a 735 kV or 315 kV corridor.

## Asset scale

There is no single electrical "size" field. The public layer preserves separate concepts:

- `installed_capacity_mw` — generating-station capacity;
- `backup_capacity_mw` — separately identified backup generation;
- `voltage_kv` and `design_voltage_kv` — transmission/substation voltage context;
- `available_capacity` — published connection-capacity context, where available.

Generation-node radius is driven by installed MW. Non-generation nodes are sized by voltage. Published available capacity is metadata only and must not be used as the node's physical or electrical size.

## Material represented assets

The initial asset-backed network includes the Romaine-1 through Romaine-4 generating stations and their documented transmission connections, Arnaud, Montagnais, Sainte-Marguerite-3, Churchill Falls, Muskrat Falls, Labrador West/Fermont context, Natashquan and the La Romaine / Unamen Shipu extension. Selected isolated assets include Menihek, Lac-Robertson and Innavik.

The represented transmission classes include 735 kV, 315 kV, 230 kV, 161 kV, 69 kV asset context and the 34.5 kV eastern extension. Where a line was built for a higher design voltage but documented for lower initial operation, both values remain explicit.

## Geometry discipline

Coordinates in `grid_reach_public.geojson` are schematic connections between documented named anchors. Node coordinates can be named-facility points or explicitly labelled area/municipality proxies. The layer must not be used to:

- measure distance to a conductor or right-of-way;
- infer interconnection or residual hosting capacity except where a separately dated value is explicitly published;
- infer a buildable tie-in point;
- infer land rights, easements or access;
- assert that an unshown local/distribution line does not exist.

Hydro-Québec open right-of-way or vegetation data may later be used as a geometry cross-check, but this research layer deliberately keeps schematic geometry rather than implying surveyed conductor alignment.

## Why the full distribution network is omitted

The layer is intended to show material network context and remote electrical assets, not a pole-by-pole inventory. Publishing the full distribution system would add payload and visual weight while creating false certainty from coverage gaps. Selected lower-voltage links are retained when they materially change interpretation of network reach or isolated-system context.

## Publication

`pipelines/publish/build_grid_reach_public.py` resolves the network, asset and source registries and publishes both `grid_connection` and `grid_node` features. Artificial `reach_marker` features and display gaps are not part of the model.

Generated artifacts:

- `data/publish/current/grid_reach_public.geojson`
- `apps/web/public/grid/grid-reach.geojson`

Both are generated outputs and should not be hand-edited.
