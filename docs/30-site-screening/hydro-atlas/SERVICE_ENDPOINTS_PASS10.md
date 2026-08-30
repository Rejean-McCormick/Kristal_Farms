# Pass 10 official service endpoints

## WSC basin polygons

- Registry/root: `https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/HydrometricNetworkBasinPolygons/`
- Included stations: `.../Included_stations.txt`
- GeoJSON MDA 02: `.../geojson/MDA_ADP_02.zip`
- GeoJSON MDA 03: `.../geojson/MDA_ADP_03.zip`

All 24 pass-9 station IDs are present in the official included-stations registry.

## Québec hydrography — GRHQ

Layer 15 REST endpoint: `https://servicescarto.mern.gouv.qc.ca/pes/rest/services/Territoire/GRHQ_WMS/MapServer/15`

Verified service properties include polyline geometry, GeoJSON query support and fields `UDH`, `TYPECE`, `PERENNITE`, `FONCTION`, `ISOLE`, `O_STRAHLER`, `O_HORTON`, `LONGUEUR_M`, `DIST_DE_M`, `TOPONYME`, source/date fields and `OBJECTID`.

## Labrador / national network

Canada1Water/NHN service endpoint registered: `https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/c1w_stream_index_en/MapServer/0`

Runtime schema discovery remains mandatory.

## Terrain — HRDEM Mosaic

STAC root: `https://datacube.services.geo.ca/stac/api/`
Collections: `hrdem-mosaic-1m`, `hrdem-mosaic-2m`; DTM is preferred. HRDEM Mosaic uses CGVD2013 orthometric heights.

## Runtime limitation

The current container cannot resolve these external hosts. The scripts are included for execution in a network-enabled environment; no natural-feature fallback geometry is authorized.
