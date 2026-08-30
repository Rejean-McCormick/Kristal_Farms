CREATE OR REPLACE VIEW publish.screening_matrix_v1 AS
SELECT e.id AS entity_id, e.name, s.dimension, s.status, s.evidence_completeness,
       s.open_questions, s.last_reviewed,
       false AS ranking_allowed
FROM research.screening_dimension_state s
JOIN core.entity e ON e.id=s.entity_id
WHERE e.visibility='PUBLIC';
