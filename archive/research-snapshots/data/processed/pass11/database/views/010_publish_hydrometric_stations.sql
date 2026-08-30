CREATE OR REPLACE VIEW publish.hydrometric_stations_v1 AS
SELECT e.id AS entity_id, e.canonical_key, e.name, e.status, a.geometry, a.operational_status,
       a.metadata->>'station_number' AS station_number, a.metadata->>'geometry_role' AS geometry_role
FROM core.entity e JOIN core.asset a ON a.entity_id=e.id
WHERE e.entity_type='asset' AND a.asset_type='hydrometric_station' AND e.visibility='PUBLIC';
