-- Time-series provenance and derivation model.
CREATE TABLE IF NOT EXISTS research.observation_series (
  id uuid PRIMARY KEY,
  subject_id uuid NOT NULL REFERENCES core.entity(id) ON DELETE CASCADE,
  metric text NOT NULL REFERENCES system.metric_registry(metric),
  unit text,
  source_id uuid NOT NULL REFERENCES research.source(id) ON DELETE RESTRICT,
  source_release text,
  collection_key text NOT NULL,
  record_start date,
  record_end date,
  row_count bigint NOT NULL DEFAULT 0,
  valid_value_count bigint NOT NULL DEFAULT 0,
  provisional_value_count bigint NOT NULL DEFAULT 0,
  raw_artifact_uri text,
  raw_sha256 text,
  retrieved_at timestamptz,
  status text NOT NULL CHECK (status IN ('materialized','partial','superseded','invalid','not_materialized')),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  UNIQUE(subject_id,metric,source_release,collection_key)
);
CREATE INDEX IF NOT EXISTS observation_series_subject_metric_idx ON research.observation_series(subject_id,metric);

ALTER TABLE research.observation ADD COLUMN IF NOT EXISTS series_id uuid REFERENCES research.observation_series(id) ON DELETE RESTRICT;
ALTER TABLE research.observation ADD COLUMN IF NOT EXISTS source_record_id text;
ALTER TABLE research.observation ADD COLUMN IF NOT EXISTS quality_code text;
ALTER TABLE research.observation ADD COLUMN IF NOT EXISTS is_provisional boolean;

CREATE TABLE IF NOT EXISTS research.observation_derivation (
  observation_id uuid PRIMARY KEY REFERENCES research.observation(id) ON DELETE CASCADE,
  algorithm_key text NOT NULL,
  algorithm_version text NOT NULL,
  source_series_ids uuid[] NOT NULL,
  coverage_start date,
  coverage_end date,
  raw_value_count bigint NOT NULL,
  completeness_fraction numeric,
  parameters jsonb NOT NULL DEFAULT '{}'::jsonb,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  CHECK (raw_value_count > 0),
  CHECK (completeness_fraction IS NULL OR (completeness_fraction >= 0 AND completeness_fraction <= 1))
);

CREATE TABLE IF NOT EXISTS system.ingestion_run (
  id uuid PRIMARY KEY,
  job_id uuid NOT NULL REFERENCES system.ingestion_job(id) ON DELETE CASCADE,
  started_at timestamptz NOT NULL,
  finished_at timestamptz,
  status text NOT NULL CHECK (status IN ('running','succeeded','failed','blocked','cancelled')),
  source_release text,
  retrieved_at timestamptz,
  raw_artifact_uri text,
  raw_sha256 text,
  row_count bigint,
  error_class text,
  error_message text,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
