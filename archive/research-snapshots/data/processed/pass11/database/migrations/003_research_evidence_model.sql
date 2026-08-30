CREATE TABLE IF NOT EXISTS research.source (
  id uuid PRIMARY KEY, source_key text NOT NULL UNIQUE, title text NOT NULL, publisher text, source_type text, url text,
  publication_date date, retrieved_at date, document_reference text, license text, metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS research.evidence (
  id uuid PRIMARY KEY, evidence_key text NOT NULL UNIQUE, evidence_type text NOT NULL, claim text NOT NULL,
  status text NOT NULL CHECK (status IN ('verified','supported','scoped','unverified','conflicting','unknown')),
  confidence text, valid_from date, valid_to date, observed_at timestamptz, published_at timestamptz, retrieved_at date,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE TABLE IF NOT EXISTS research.evidence_source (
  evidence_id uuid NOT NULL REFERENCES research.evidence(id) ON DELETE CASCADE,
  source_id uuid NOT NULL REFERENCES research.source(id) ON DELETE RESTRICT, source_role text NOT NULL DEFAULT 'supports',
  PRIMARY KEY(evidence_id,source_id,source_role)
);
CREATE TABLE IF NOT EXISTS research.evidence_relation (
  evidence_id uuid NOT NULL REFERENCES research.evidence(id) ON DELETE CASCADE,
  entity_id uuid NOT NULL REFERENCES core.entity(id) ON DELETE CASCADE,
  relation_type text NOT NULL CHECK (relation_type IN ('supports','describes','contradicts','constrains','references')),
  PRIMARY KEY(evidence_id,entity_id,relation_type)
);

CREATE TABLE IF NOT EXISTS research.observation (
  id uuid PRIMARY KEY, subject_id uuid NOT NULL REFERENCES core.entity(id) ON DELETE CASCADE, metric text NOT NULL,
  value_numeric numeric, value_text text, unit text, valid_from date, valid_to date, observed_at timestamptz,
  source_evidence_id uuid REFERENCES research.evidence(id) ON DELETE RESTRICT,
  derivation_type text NOT NULL CHECK (derivation_type IN ('evidence','derived','engineering_assumption','user_input','default')),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  CHECK (value_numeric IS NOT NULL OR value_text IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS research.screening_dimension_state (
  id uuid PRIMARY KEY, entity_id uuid NOT NULL REFERENCES core.entity(id) ON DELETE CASCADE,
  dimension text NOT NULL CHECK (dimension IN ('energy','hydrology','environment','rights_governance','telecom','logistics','community','regulation','economics','engineering')),
  status text NOT NULL, evidence_completeness text, open_questions jsonb NOT NULL DEFAULT '[]'::jsonb,
  last_reviewed date, metadata jsonb NOT NULL DEFAULT '{}'::jsonb, UNIQUE(entity_id,dimension)
);
