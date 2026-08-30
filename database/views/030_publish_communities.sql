CREATE OR REPLACE VIEW publish.communities_v1 AS
SELECT e.id AS entity_id, e.name, e.status, p.jurisdiction AS region, p.geometry,
       p.metadata->>'geometry_role' AS geometry_role,
       e.metadata->>'screening_mode' AS screening_mode,
       COALESCE((e.metadata->>'ranking_allowed')::boolean,false) AS ranking_allowed
FROM core.entity e JOIN core.place p ON p.entity_id=e.id
WHERE e.entity_type='place' AND p.place_type='community' AND e.visibility='PUBLIC';
