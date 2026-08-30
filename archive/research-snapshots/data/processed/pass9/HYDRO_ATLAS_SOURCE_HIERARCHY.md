# Hydro Atlas Source Hierarchy — Pass 9

## Québec

1. WSC station metadata and WSC station-basin polygons for gauge-linked hydrology.
2. GRHQ for connected hydrography across Québec.
3. GRHQ-HR only where actual coverage is verified; it is not assumed in Nunavik.
4. HRDEM Mosaic for elevation only after the river line is known.
5. Canada1Water/NHN as national/cross-border supporting network.

## Labrador

1. WSC station metadata and WSC station-basin polygons.
2. Canada1Water/NHN Strahler network for national connected hydrography.
3. HRDEM Mosaic for terrain after the line geometry is ingested.
4. Supplied historical Labrador hydro files only as contextual evidence, never as substitute authoritative geometry.

## Data governance

The most recent source does not automatically overwrite a different datum silently. Source date and provenance remain attached. If WSC polygon-derived drainage area and WSC station metadata differ, pass 9 keeps the official station metadata value and records the polygon prerelease warning.
