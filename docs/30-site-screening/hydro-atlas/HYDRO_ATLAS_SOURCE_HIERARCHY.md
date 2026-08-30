# Hydro Atlas source hierarchy

## Québec

1. WSC station metadata and station-basin polygons for gauge-linked hydrology.
2. GRHQ for connected hydrography across Québec.
3. GRHQ-HR only where actual coverage is verified.
4. HRDEM Mosaic for elevation only after the connected river line is known.
5. Canada1Water/NHN as national/cross-border supporting network where needed.

## Labrador

1. WSC station metadata and station-basin polygons.
2. Canada1Water/NHN for connected national hydrography.
3. HRDEM Mosaic for terrain after line geometry is accepted.
4. Historical Labrador hydro files as contextual evidence only, never substitute authoritative geometry.

## Data governance

A newer source does not silently overwrite a differently defined datum. Source date, definition and provenance remain attached. If polygon-derived drainage area and station metadata differ, both records remain distinguishable until the definition difference is resolved.
