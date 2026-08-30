CREATE OR REPLACE VIEW system.kr_rule_violations AS
SELECT 'KR-02'::text AS rule_id, o.id::text AS object_id, 'validated_hosting_capacity_kw requires explicit evidence and validation basis'::text AS violation
FROM research.observation o
WHERE o.metric='validated_hosting_capacity_kw'
  AND (o.source_evidence_id IS NULL OR COALESCE(o.metadata->>'validation_basis','')='')
UNION ALL
SELECT 'KR-08', e.id::text, 'ranking metadata present while ranking_allowed=false'
FROM core.entity e CROSS JOIN system.governance_state g
WHERE g.ranking_allowed=false AND (e.metadata ? 'rank' OR e.metadata ? 'score' OR e.metadata ? 'priority_score')
UNION ALL
SELECT 'KR-07', p.entity_id::text, 'external reference metadata also marks project as Kristal Farms candidate'
FROM core.project p
WHERE p.role='external_reference' AND COALESCE((p.metadata->>'kristal_farms_candidate')::boolean,false)=true;
