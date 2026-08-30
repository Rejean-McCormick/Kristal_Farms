# Official hydro and terrain service endpoints

## WSC basin polygons

- Registry/root: `https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/HydrometricNetworkBasinPolygons/`
- Included stations: `.../Included_stations.txt`
- GeoJSON MDA 02: `.../geojson/MDA_ADP_02.zip`
- GeoJSON MDA 03: `.../geojson/MDA_ADP_03.zip`

All 24 current Hydro Resource Atlas station IDs are present in the controlled included-stations registry used by the research fixture.

## Québec hydrography — GRHQ

Layer 15 REST endpoint: `https://servicescarto.mern.gouv.qc.ca/pes/rest/services/Territoire/GRHQ_WMS/MapServer/15`

Relevant fields include `UDH`, `TYPECE`, `PERENNITE`, `FONCTION`, `ISOLE`, `O_STRAHLER`, `O_HORTON`, `LONGUEUR_M`, `DIST_DE_M`, `TOPONYME`, source/date fields and `OBJECTID`.

## Labrador / national network

Canada1Water/NHN service endpoint: `https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/c1w_stream_index_en/MapServer/0`

Runtime schema discovery remains mandatory.

## Terrain — HRDEM Mosaic

STAC root: `https://datacube.services.geo.ca/stac/api/`
Collections: `hrdem-mosaic-1m`, `hrdem-mosaic-2m`. DTM is preferred. HRDEM Mosaic uses CGVD2013 orthometric heights.

## Execution rule

If the execution environment cannot reach an official host, the job remains blocked/retryable. No natural-feature fallback geometry is authorized.
