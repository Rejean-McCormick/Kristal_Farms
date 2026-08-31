import "server-only";

import { readFile } from "node:fs/promises";
import path from "node:path";
import type {
  EntityDetail,
  EvidenceSummary,
  ExplorerBootstrap,
  LayerCatalogEntry,
  PublicFeatureCollection,
  PublicMapFeature,
  RelationItem,
} from "../explorer-types";
import { humanizeToken } from "../format";

const workingDirectory = process.cwd();
const repoRoot = process.env.KRISTAL_REPO_ROOT
  ? path.resolve(process.env.KRISTAL_REPO_ROOT)
  : workingDirectory.endsWith(path.join("apps", "web"))
    ? path.resolve(workingDirectory, "../..")
    : workingDirectory;
const publishRoot = path.join(repoRoot, "data", "publish", "current");
const fixturesRoot = path.join(repoRoot, "data", "fixtures", "current");

async function readJson<T>(filePath: string): Promise<T> {
  return JSON.parse(await readFile(filePath, "utf8")) as T;
}

async function readJsonLines<T>(filePath: string): Promise<T[]> {
  const content = await readFile(filePath, "utf8");
  return content
    .split(/\r?\n/)
    .filter(Boolean)
    .map((line) => JSON.parse(line) as T);
}

function normalizeCollection(
  input: Omit<PublicFeatureCollection, "features"> & { features: Array<Omit<PublicMapFeature, "properties"> & { properties: Record<string, unknown> }> },
  kind: "community" | "hydrometric_station",
): PublicFeatureCollection {
  return {
    type: "FeatureCollection",
    release: input.release,
    features: input.features.map((feature) => ({
      ...feature,
      id: String(feature.id),
      properties: {
        ...feature.properties,
        entity_id: String(feature.properties.entity_id ?? feature.id),
        name: String(feature.properties.name ?? "Unnamed entity"),
        region: feature.properties.region ? String(feature.properties.region) : null,
        feature_kind: kind,
        ranking_allowed: false,
      } as PublicMapFeature["properties"],
    })),
  };
}

export async function getExplorerBootstrap(): Promise<ExplorerBootstrap> {
  const [release, communitiesRaw, stationsRaw, layerCatalog] = await Promise.all([
    readJson<{
      release_id: string;
      generated_at: string;
      screening_mode: "unranked";
      ranking_allowed: false;
    }>(path.join(publishRoot, "release_manifest.json")),
    readJson<PublicFeatureCollection>(path.join(publishRoot, "communities_public.geojson")),
    readJson<PublicFeatureCollection>(path.join(publishRoot, "hydrometric_stations_public.geojson")),
    readJsonLines<LayerCatalogEntry>(path.join(fixturesRoot, "system_layer_catalog.jsonl")),
  ]);

  const mapLayers = layerCatalog.filter(
    (layer) =>
      layer.permissions?.public !== false &&
      ["communities", "hydrometric_stations"].includes(layer.id),
  );

  return {
    release: release.release_id,
    generatedAt: release.generated_at,
    screeningMode: "unranked",
    rankingAllowed: false,
    communities: normalizeCollection(communitiesRaw, "community"),
    stations: normalizeCollection(stationsRaw, "hydrometric_station"),
    layers: mapLayers,
  };
}

type CommunityContext = {
  entity_id: string;
  marine_context: string | null;
  telecom_context: string | null;
  road_context: string | null;
  energy_context: string | null;
};

type EvidencePayload = { items: EvidenceSummary[] };

function fact(label: string, value: string | number | null | undefined) {
  if (value === null || value === undefined || value === "") return null;
  return { label, value: String(value) };
}

function contextRelation(id: string, label: string, value: string | null | undefined): RelationItem | null {
  if (!value) return null;
  return { id, label, value: humanizeToken(value), kind: "context" };
}

export async function getEntityDetail(entityId: string): Promise<EntityDetail | null> {
  const [bootstrap, communityContextPayload, evidencePayload] = await Promise.all([
    getExplorerBootstrap(),
    readJson<{ items: CommunityContext[] }>(path.join(publishRoot, "community_context_public.json")),
    readJson<EvidencePayload>(path.join(publishRoot, "evidence_panel_summary_public.json")),
  ]);

  const feature = [...bootstrap.communities.features, ...bootstrap.stations.features].find(
    (candidate) => candidate.properties.entity_id === entityId,
  );
  if (!feature) return null;

  const p = feature.properties;
  const evidence = evidencePayload.items.find((item) => item.entity_id === entityId) ?? null;

  if (p.feature_kind === "community") {
    const context = communityContextPayload.items.find((item) => item.entity_id === entityId);
    const relations = [
      contextRelation("telecom", "Telecom", context?.telecom_context ?? p.telecom_context),
      contextRelation("marine", "Marine", context?.marine_context ?? p.marine_context),
      contextRelation("road", "Road", context?.road_context ?? p.road_context),
      contextRelation("energy", "Energy", context?.energy_context ?? p.energy_context),
    ].filter((item): item is RelationItem => item !== null);

    const facts = [
      fact("Region", p.region),
      fact("Screening", "Unranked"),
      fact("Geometry", "Approximate community reference"),
    ].filter((item): item is { label: string; value: string } => item !== null);

    return {
      entityId,
      featureKind: "community",
      title: p.name,
      subtitle: p.region,
      status: "contextual record",
      geometry: feature.geometry,
      geometryRole: p.geometry_role ?? null,
      geometryPrecision: p.geometry_precision ?? null,
      notFacilityCoordinate: Boolean(p.not_facility_coordinate),
      facts,
      relations,
      evidence,
      release: bootstrap.release,
      rankingAllowed: false,
    };
  }

  const relations: RelationItem[] = p.river_entity_id
    ? [
        {
          id: "river",
          label: "River",
          value: p.river_name ?? "Hydrologic feature",
          kind: "entity",
          entityId: p.river_entity_id,
        },
      ]
    : [];

  const facts = [
    fact("Station", p.station_number),
    fact("Region", p.region),
    fact("Status", humanizeToken(p.status)),
    p.gross_drainage_area_km2 != null
      ? fact("Drainage area", `${Number(p.gross_drainage_area_km2).toLocaleString("en-CA")} km²`)
      : null,
  ].filter((item): item is { label: string; value: string } => item !== null);

  return {
    entityId,
    featureKind: "hydrometric_station",
    title: p.station_number ?? p.name,
    subtitle: p.river_name ?? p.region,
    status: p.evidence_status ? humanizeToken(p.evidence_status) : p.status ?? null,
    geometry: feature.geometry,
    geometryRole: p.geometry_role ?? null,
    geometryPrecision: "official",
    notFacilityCoordinate: false,
    facts,
    relations,
    evidence,
    release: bootstrap.release,
    rankingAllowed: false,
  };
}
