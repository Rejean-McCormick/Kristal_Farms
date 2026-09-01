import type {
  ContextInfrastructure,
  PublicCommunityInfrastructure,
  PublicMapFeature,
} from "./explorer-types";

export const CONTEXT_DATA_SOURCE = "Kristal published community infrastructure";

export function normalizeCommunityKey(value: string) {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "")
    .trim();
}

export function createPublishedCommunityFacilityProxy(
  community: PublicMapFeature,
  published: PublicCommunityInfrastructure | null,
  kind: "airport" | "dock",
): ContextInfrastructure | null {
  if (!published) return null;

  if (kind === "airport") {
    if (!published.airport.access_known) return null;
    const runway = published.airport.runway_length_m;
    const surface = published.airport.runway_surface;
    const sizeLabel =
      runway != null
        ? `Runway ${Math.round(runway).toLocaleString("en-CA")} m${surface ? ` · ${surface}` : ""}`
        : null;
    return {
      key: `published-${published.entity_id}-airport`,
      kind: "airport",
      name: published.airport.name ?? `${community.properties.name} airport / air access`,
      coordinates: community.geometry.coordinates,
      source: published.airport.presence_source?.name ?? CONTEXT_DATA_SOURCE,
      sizeLabel,
      capacityMw: null,
      capacityBasis: null,
      nearestPortName: null,
      nearestPortDistanceKm: null,
      geometryConfidence: "community reference proxy",
      sourceNote: published.airport.dimension_source?.reference_date
        ? `Runway reference: ${published.airport.dimension_source.reference_date}`
        : null,
      notes:
        published.airport.note ??
        "Community-level access marker. The icon is not an airport coordinate; mapped basemap geometry is preferred when available.",
    };
  }

  if (!published.marine.access_known) return null;
  const sizeBits: string[] = [];
  if (published.marine.dock_length_m != null) {
    sizeBits.push(`Dock ${Math.round(published.marine.dock_length_m).toLocaleString("en-CA")} m`);
  }
  if (published.marine.max_draft_m != null) {
    sizeBits.push(`Draft ${published.marine.max_draft_m.toLocaleString("en-CA")} m`);
  }

  return {
    key: `published-${published.entity_id}-dock`,
    kind: "dock",
    name: published.marine.facility_name ?? `${community.properties.name} marine access`,
    coordinates: community.geometry.coordinates,
    source: published.marine.source?.name ?? CONTEXT_DATA_SOURCE,
    sizeLabel: sizeBits.length ? sizeBits.join(" · ") : null,
    capacityMw: null,
    capacityBasis: null,
    nearestPortName: null,
    nearestPortDistanceKm: null,
    geometryConfidence: "community reference proxy",
    sourceNote:
      published.marine.heavy_lift_status === "confirmed"
        ? "Heavy-lift capability confirmed"
        : published.marine.heavy_lift_status === "not_verified"
          ? "Heavy-lift capability not verified"
          : null,
    notes:
      published.marine.note ??
      "Community-level marine-access marker. The icon is not a dock coordinate; mapped basemap geometry is preferred when available.",
  };
}
