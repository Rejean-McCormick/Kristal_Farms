-- Pass 13: data-driven catalog, releases and showcase stories.
CREATE TABLE IF NOT EXISTS system.release (
  id uuid PRIMARY KEY,
  release_key text NOT NULL UNIQUE,
  release_date date NOT NULL,
  immutable boolean NOT NULL DEFAULT true,
  screening_mode text NOT NULL,
  ranking_allowed boolean NOT NULL DEFAULT false,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS system.layer_catalog (
  id text PRIMARY KEY,
  title text NOT NULL,
  layer_group text NOT NULL,
  source_config jsonb NOT NULL,
  geometry_config jsonb NOT NULL,
  display_config jsonb NOT NULL,
  evidence_config jsonb NOT NULL DEFAULT '{}'::jsonb,
  filter_config jsonb NOT NULL DEFAULT '[]'::jsonb,
  timeline_config jsonb NOT NULL DEFAULT '{}'::jsonb,
  permissions jsonb NOT NULL DEFAULT '{}'::jsonb,
  semantics jsonb NOT NULL DEFAULT '{}'::jsonb,
  catalog_version text NOT NULL
);

CREATE TABLE IF NOT EXISTS system.showcase_story (
  id text PRIMARY KEY,
  title text NOT NULL,
  story_version text NOT NULL,
  definition jsonb NOT NULL,
  screening_mode text NOT NULL DEFAULT 'unranked',
  ranking_allowed boolean NOT NULL DEFAULT false
);
