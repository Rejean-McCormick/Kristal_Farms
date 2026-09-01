# External grid source notes

The governed grid-reach research record is `research/grid/cote_nord_grid_reach.yaml`.

For future higher-resolution contextual geometry, the preferred Hydro-Québec open-data reference is dataset identifier:

`calendrier-travaux-degagement-transport-json`

Portal:
`https://donnees.hydroquebec.com/explore/dataset/calendrier-travaux-degagement-transport-json/`

This is a vegetation/right-of-way planning dataset for the transmission system, not an engineering centerline dataset. Hydro-Québec states that no geometric measurement should be taken from it because precision is estimated as medium.

Do not ingest the full provincial distribution dataset into the browser bundle. If local distribution geometry becomes necessary for a dossier, clip it offline to that corridor and publish it as a separate, explicitly contextual artifact.
