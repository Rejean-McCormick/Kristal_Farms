CREATE OR REPLACE VIEW publish.entity_evidence_v1 AS
SELECT er.entity_id, ev.id AS evidence_id, ev.evidence_type, ev.claim, ev.status, ev.confidence,
       ev.valid_from, ev.valid_to, ev.published_at, ev.retrieved_at, er.relation_type,
       array_agg(DISTINCT src.source_key) FILTER (WHERE src.id IS NOT NULL) AS source_keys
FROM research.evidence_relation er
JOIN research.evidence ev ON ev.id=er.evidence_id
LEFT JOIN research.evidence_source es ON es.evidence_id=ev.id
LEFT JOIN research.source src ON src.id=es.source_id
GROUP BY er.entity_id, ev.id, ev.evidence_type, ev.claim, ev.status, ev.confidence,
         ev.valid_from, ev.valid_to, ev.published_at, ev.retrieved_at, er.relation_type;
