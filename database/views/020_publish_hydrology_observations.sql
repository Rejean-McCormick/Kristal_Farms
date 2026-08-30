CREATE OR REPLACE VIEW publish.hydrology_observations_v1 AS
SELECT o.id, o.subject_id, e.name AS subject_name, e.canonical_key,
       o.metric, o.value_numeric, o.value_text, o.unit, o.valid_from, o.valid_to, o.observed_at,
       o.derivation_type, o.quality_code, o.is_provisional, o.series_id,
       ev.status AS evidence_status, ev.confidence AS evidence_confidence, ev.retrieved_at AS evidence_retrieved_at,
       o.metadata
FROM research.observation o
JOIN core.entity e ON e.id=o.subject_id
LEFT JOIN research.evidence ev ON ev.id=o.source_evidence_id
WHERE e.visibility='PUBLIC';

CREATE OR REPLACE VIEW publish.hydrology_screening_v1 AS
SELECT s.entity_id, e.name, e.canonical_key, s.status, s.evidence_completeness,
       s.open_questions, s.last_reviewed, s.metadata
FROM research.screening_dimension_state s
JOIN core.entity e ON e.id=s.entity_id
WHERE s.dimension='hydrology' AND e.visibility='PUBLIC';
