CREATE OR REPLACE VIEW publish.entity_search_v1 AS
SELECT e.id AS entity_id, e.canonical_key, e.name, e.entity_type, e.status,
       e.metadata->>'region' AS region, e.visibility
FROM core.entity e WHERE e.visibility='PUBLIC';
