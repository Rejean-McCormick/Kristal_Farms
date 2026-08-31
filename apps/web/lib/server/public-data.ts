import "server-only";

import { readFile } from "node:fs/promises";
import path from "node:path";
import type {
  EntityDetail,
  EntityScreeningDimension,
  EvidenceRecord,
  EvidenceSummary,
  ExplorerBootstrap,
  LayerCatalogEntry,
  PublicFeatureCollection,
  PublicMapFeature,
  PublicRiverReference,
  RelationItem,
  RiverScreeningDimension,
} from "../explorer-types";
import { humanizeToken } from "../format";

const workingDirectory = process.cwd();
const repoRoot = process.env.KRISTAL_REPO_ROOT
  ? path.resolve(process.env.KRISTAL_REPO_ROOT)
  : workingDirectory.endsWith(path.join("apps", "web"))
    ? path.resolve(workingDirectory, "../..")
    : workingDirectory;
const publishRoot = path.join(repoRoot, "data", "publish", "current");
const catalogPath = path.join(repoRoot, "packages", "catalog", "catalog.json");

async function readJson<T>(filePath: string): Promise<T> {
  return JSON.parse(await readFile(filePath, "utf8")) as T;
}

type StableLayerCatalog = {
  layers: Array<{
    id: string;
    title: string;
    group: string;
    display: {
      renderer: string;
      layer_type?: string;
      min_zoom?: number;
      max_zoom?: number;
    };
    evidence?: { enabled?: boolean };
    permissions?: { public?: boolean };
    semantics?: Record<string, unknown>;
  }>;
};

function normalizeLayerCatalog(input: StableLayerCatalog): LayerCatalogEntry[] {
  return input.layers.map((layer) => ({
    id: layer.id,
    title: layer.title,
    layer_group: layer.group,
    display_config: layer.display,
    evidence_config: layer.evidence,
    permissions: layer.permissions,
    semantics: layer.semantics,
  }));
}

function normalizeCollection(
  input: Omit<PublicFeatureCollection, "features"> & {
    features: Array<
      Omit<PublicMapFeature, "properties"> & { properties: Record<string, unknown> }
    >;
  },
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

type HydroDimensionRaw = {
  status: string;
  evidence_completeness: string;
  open_questions?: string[];
  last_reviewed?: string | null;
};

type HydroMatrixItem = {
  entity_id: string;
  name: string;
  canonical_key: string;
  ranking_allowed: false;
  dimensions: Record<string, HydroDimensionRaw>;
};

type HydroMatrixPayload = { items: HydroMatrixItem[] };

type ReleaseManifest = {
  release_id: string;
  generated_at: string;
  screening_mode: "unranked";
  ranking_allowed: false;
};

function riverAliases(name: string): string[] {
  const aliases = new Set<string>([name]);
  for (const part of name.split("/")) {
    const trimmed = part.trim();
    if (trimmed) aliases.add(trimmed);
  }
  return [...aliases];
}

function toRiverDimension(value: HydroDimensionRaw | undefined): RiverScreeningDimension | null {
  if (!value) return null;
  return {
    status: value.status,
    evidence_completeness: value.evidence_completeness,
    open_questions: value.open_questions ?? [],
    last_reviewed: value.last_reviewed ?? null,
  };
}

function buildRiverReferences(
  matrix: HydroMatrixPayload,
  stations: PublicFeatureCollection,
): PublicRiverReference[] {
  const stationByRiver = new Map<string, PublicMapFeature>();
  for (const station of stations.features) {
    const riverId = station.properties.river_entity_id;
    if (riverId && !stationByRiver.has(riverId)) stationByRiver.set(riverId, station);
  }

  return matrix.items.map((item) => {
    const station = stationByRiver.get(item.entity_id) ?? null;
    return {
      entity_id: item.entity_id,
      canonical_key: item.canonical_key,
      name: item.name,
      region: station?.properties.region ?? null,
      status: "research_reference",
      ranking_allowed: false,
      aliases: riverAliases(item.name),
      anchor: station?.geometry ?? null,
      anchor_station_entity_id: station?.properties.entity_id ?? null,
      anchor_station_number: station?.properties.station_number ?? null,
      gross_drainage_area_km2: station?.properties.gross_drainage_area_km2 ?? null,
      geometry_status: "authoritative_flowline_not_ingested",
      hydrology: toRiverDimension(item.dimensions.hydrology),
      engineering: toRiverDimension(item.dimensions.engineering),
    };
  });
}

export async function getExplorerBootstrap(): Promise<ExplorerBootstrap> {
  const [release, communitiesRaw, stationsRaw, hydroMatrix, stableLayerCatalog] = await Promise.all([
    readJson<ReleaseManifest>(path.join(publishRoot, "release_manifest.json")),
    readJson<PublicFeatureCollection>(path.join(publishRoot, "communities_public.geojson")),
    readJson<PublicFeatureCollection>(path.join(publishRoot, "hydrometric_stations_public.geojson")),
    readJson<HydroMatrixPayload>(path.join(publishRoot, "hydro_evidence_matrix_public.json")),
    readJson<StableLayerCatalog>(catalogPath),
  ]);

  const communities = normalizeCollection(communitiesRaw, "community");
  const stations = normalizeCollection(stationsRaw, "hydrometric_station");
  const layerCatalog = normalizeLayerCatalog(stableLayerCatalog);
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
    communities,
    stations,
    rivers: buildRiverReferences(hydroMatrix, stations),
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
type EvidenceRecordsPayload = { items: EvidenceRecord[] };

function fact(label: string, value: string | number | null | undefined) {
  if (value === null || value === undefined || value === "") return null;
  return { label, value: String(value) };
}

function contextRelation(
  id: string,
  label: string,
  value: string | null | undefined,
): RelationItem | null {
  if (!value) return null;
  return { id, label, value: humanizeToken(value), kind: "context" };
}

function relatedEvidenceRecords(
  summary: EvidenceSummary | null,
  records: EvidenceRecord[],
): EvidenceRecord[] {
  if (!summary) return [];
  const wanted = new Set(summary.evidence_ids);
  return records.filter((record) => wanted.has(record.id));
}

function screeningDimension(
  id: string,
  value: RiverScreeningDimension | null,
  appliesTo: string | null,
): EntityScreeningDimension | null {
  if (!value) return null;
  return {
    id,
    label: humanizeToken(id),
    status: value.status,
    evidenceCompleteness: value.evidence_completeness,
    openQuestions: value.open_questions,
    lastReviewed: value.last_reviewed,
    appliesTo,
  };
}

export async function getEntityDetail(entityId: string): Promise<EntityDetail | null> {
  const [bootstrap, communityContextPayload, evidencePayload, evidenceRecordsPayload] =
    await Promise.all([
      getExplorerBootstrap(),
      readJson<{ items: CommunityContext[] }>(
        path.join(publishRoot, "community_context_public.json"),
      ),
      readJson<EvidencePayload>(path.join(publishRoot, "evidence_panel_summary_public.json")),
      readJson<EvidenceRecordsPayload>(path.join(publishRoot, "evidence_records_public.json")),
    ]);

  const evidence = evidencePayload.items.find((item) => item.entity_id === entityId) ?? null;
  const evidenceRecords = relatedEvidenceRecords(evidence, evidenceRecordsPayload.items);
  const feature = [...bootstrap.communities.features, ...bootstrap.stations.features].find(
    (candidate) => candidate.properties.entity_id === entityId,
  );

  if (!feature) {
    const river = bootstrap.rivers.find((candidate) => candidate.entity_id === entityId);
    if (!river) return null;

    const station = river.anchor_station_entity_id
      ? bootstrap.stations.features.find(
          (candidate) => candidate.properties.entity_id === river.anchor_station_entity_id,
        ) ?? null
      : null;

    const relations: RelationItem[] = station
      ? [
          {
            id: "hydrometric-station",
            label: "Hydrometric station",
            value: `${station.properties.station_number ?? station.properties.name} · ${humanizeToken(station.properties.status)}`,
            kind: "entity",
            entityId: station.properties.entity_id,
          },
        ]
      : [];

    const dimensions = [
      screeningDimension("hydrology", river.hydrology, river.name),
      screeningDimension("engineering", river.engineering, river.name),
    ].filter((item): item is EntityScreeningDimension => item !== null);

    const facts = [
      fact("Region", river.region),
      fact("Station anchor", river.anchor_station_number),
      river.gross_drainage_area_km2 != null
        ? fact(
            "Drainage area at station",
            `${Number(river.gross_drainage_area_km2).toLocaleString("en-CA")} km²`,
          )
        : null,
      fact("Hydrology", river.hydrology ? humanizeToken(river.hydrology.status) : null),
      fact("Screening", "Unranked"),
      fact("River geometry", "Authoritative flowline not yet ingested"),
    ].filter((item): item is { label: string; value: string } => item !== null);

    return {
      entityId,
      featureKind: "river",
      title: river.name,
      subtitle: river.region,
      status: "research reference",
      geometry: river.anchor,
      geometryRole: "station_linked_reference_anchor_only",
      geometryPrecision: null,
      mapGeometryStatus: "unavailable",
      mapNote:
        "Kristal has not ingested an authoritative connected river flowline for this research entity. Any visible basemap river line is contextual OpenStreetMap/OpenMapTiles data, not the governed Kristal geometry.",
      notFacilityCoordinate: false,
      facts,
      relations,
      evidence,
      evidenceRecords,
      screeningDimensions: dimensions,
      release: bootstrap.release,
      rankingAllowed: false,
    };
  }

  const p = feature.properties;

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
      mapGeometryStatus: "approximate",
      mapNote:
        "This coordinate is an approximate community reference and must not be interpreted as a facility location.",
      notFacilityCoordinate: Boolean(p.not_facility_coordinate),
      facts,
      relations,
      evidence,
      evidenceRecords,
      screeningDimensions: [],
      release: bootstrap.release,
      rankingAllowed: false,
    };
  }

  const linkedRiver = p.river_entity_id
    ? bootstrap.rivers.find((candidate) => candidate.entity_id === p.river_entity_id) ?? null
    : null;

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
      ? fact(
          "Drainage area",
          `${Number(p.gross_drainage_area_km2).toLocaleString("en-CA")} km²`,
        )
      : null,
    fact("Position", "Official WSC station coordinate"),
  ].filter((item): item is { label: string; value: string } => item !== null);

  const dimensions = linkedRiver
    ? [
        screeningDimension("hydrology", linkedRiver.hydrology, linkedRiver.name),
        screeningDimension("engineering", linkedRiver.engineering, linkedRiver.name),
      ].filter((item): item is EntityScreeningDimension => item !== null)
    : [];

  return {
    entityId,
    featureKind: "hydrometric_station",
    title: p.station_number ?? p.name,
    subtitle: p.river_name ?? p.region,
    status: p.evidence_status ? humanizeToken(p.evidence_status) : p.status ?? null,
    geometry: feature.geometry,
    geometryRole: p.geometry_role ?? null,
    geometryPrecision: "official",
    mapGeometryStatus: "official",
    mapNote:
      "Published geometry is the official hydrometric station position. It is not a project intake, powerhouse, dam site, river reach or basin polygon.",
    notFacilityCoordinate: false,
    facts,
    relations,
    evidence,
    evidenceRecords,
    screeningDimensions: dimensions,
    release: bootstrap.release,
    rankingAllowed: false,
  };
}
