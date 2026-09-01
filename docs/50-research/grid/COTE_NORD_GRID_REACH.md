# Northern Atlas electrical grid reach

**Status:** research context  
**Ranking:** not allowed  
**Geometry:** schematic connectivity only; not engineering geometry

## Purpose

This layer answers a narrow project question: **how far does documented existing electrical infrastructure reach west, north and east across the Northern Atlas study geography?** It is deliberately not a complete Hydro-Québec network map.

The public web layer keeps only six connection classes:

- the comparative western 735 kV Abitibi / Amos hub — Chibougamau spine;
- the comparative western 315 kV Abitibi / Amos hub — Lebel-sur-Quévillon branch;
- the 735 kV northbound transmission corridor between the Arnaud area and Poste des Montagnais, continuing toward Churchill Falls;
- the existing 315 kV Sainte-Marguerite-3–Arnaud branch;
- the coastal 161 kV Arnaud–Havre-Saint-Pierre–Johan-Beetz–Natashquan connection (circuits 1619 and 1652 in the cited study);
- the eastern 75 km La Romaine / Unamen Shipu connection, designed for 161 kV and operated at 34.5 kV.

## Reach interpretation

Four markers are emphasized instead of rendering every local conductor:

1. **West reach — Abitibi / Amos area / 735 kV context.** This is the comparative western grid-hub marker that keeps Abitibi visible in the Northern Atlas.
2. **North reach — Poste des Montagnais / 735 kV context.** This is a Côte-Nord reach marker on a corridor that continues into Labrador; it is not represented as a terminal station of the entire circuit.
3. **East 161 kV reach — Natashquan.** Hydro-Québec's corridor study describes circuit 1652 as Havre-Saint-Pierre–Natashquan via Johan-Beetz.
4. **East main-grid extension — La Romaine / Unamen Shipu.** Hydro-Québec commissioned the 75 km line in 2022; its annual reporting states it was designed to handle 161 kV but operates at 34.5 kV.

## Terminal-marker display

The web representation intentionally leaves a small visual gap between a schematic line and any emphasized reach marker. The marker means **documented transmission/grid reach**. It is not a surveyed conductor endpoint, switching point, available interconnection point or substation footprint.

## Geometry discipline

The line coordinates in `grid_reach_public.geojson` are **schematic connections between documented named anchors**. They are intentionally simplified and must not be used to:

- measure distance to a conductor or right-of-way;
- infer interconnection capacity;
- infer a buildable tie-in point;
- infer land rights, easements or access;
- assert that an unshown distribution line does not exist.

Hydro-Québec's open transmission vegetation/right-of-way dataset can be used later as a medium-precision contextual geometry cross-check, but Hydro-Québec explicitly warns that geometric measurements must not be taken from that dataset.

## Why the full distribution network is omitted

The project question is network **reach**, not a pole-by-pole inventory. Hydro-Québec's distribution vegetation dataset is very large and excludes some municipal/cooperative/off-grid territories. Publishing the whole dataset would add visual and payload weight while creating false certainty from gaps. The 34.5 kV La Romaine extension is retained because it materially changes the understood eastern reach of the main grid, and the Abitibi comparative spine is retained because it avoids a false east-only reading of the northern network.

## Source register

The machine-readable source register is maintained in `research/grid/cote_nord_grid_reach.yaml`. Primary references include Hydro-Québec/BAPE corridor documentation, Hydro-Québec current project pages and annual reporting, the Hydro-Québec Abitibi-Témiscamingue regional transport map, Hydro-Québec's 2022 La Romaine connection announcement, and official Québec/Canadian place-name coordinates.
