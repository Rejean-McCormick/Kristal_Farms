import type { Map as MapLibreMap, StyleSpecification } from "maplibre-gl";
import type { GridReachManifest, LocalImageryManifest, LocalTerrainManifest } from "./explorer-types";

const DEFAULT_VECTOR_STYLE = "https://tiles.openfreemap.org/styles/liberty";

const LOCAL_SATELLITE_SOURCE_ID = "kristal-local-satellite-source";
const LOCAL_SATELLITE_LAYER_ID = "kristal-local-satellite";

/**
 * Observatory v0.3.3 defaults to a Kristal-branded VECTOR ATLAS.
 *
 * OpenFreeMap/OpenMapTiles remains the contextual basemap, but the visual
 * language is intentionally reduced to the objects useful to Kristal:
 * water, waterways, buildings, transport access, infrastructure/facility
 * context, boundaries and labels.
 *
 * Photographic imagery is optional and never enabled automatically.
 */
export function createObservatoryStyle(): string | StyleSpecification {
  return process.env.NEXT_PUBLIC_BASE_STYLE_URL ?? DEFAULT_VECTOR_STYLE;
}

export type BasemapLayerIndex = {
  labelLayerIds: string[];
  hydrographyLayerIds: string[];
  waterwayLayerIds: string[];
  buildingLayerIds: string[];
  transportLayerIds: string[];
  facilityLayerIds: string[];
};

type StyleLayerLike = {
  id: string;
  type: string;
  source?: string;
  "source-layer"?: string;
};

const FACILITY_LAYER_HINTS = [
  "aerodrome",
  "airport",
  "airfield",
  "ferry",
  "harbour",
  "harbor",
  "port",
  "public",
  "hospital",
  "health",
  "clinic",
  "pharmacy",
  "fire",
  "police",
  "post",
  "school",
  "education",
  "college",
  "university",
  "transport",
  "fuel",
  "power",
  "utility",
  "communications",
  "telecom",
];

type LayoutPropertyName = Parameters<MapLibreMap["setLayoutProperty"]>[1];
type PaintPropertyName = Parameters<MapLibreMap["setPaintProperty"]>[1];

function safeLayout(map: MapLibreMap, layerId: string, property: LayoutPropertyName, value: unknown) {
  try {
    map.setLayoutProperty(layerId, property, value as never);
  } catch {
    // Upstream styles differ; unsupported properties are ignored.
  }
}

function safePaint(map: MapLibreMap, layerId: string, property: PaintPropertyName, value: unknown) {
  try {
    map.setPaintProperty(layerId, property, value as never);
  } catch {
    // Upstream styles differ; unsupported properties are ignored.
  }
}

function isFacilityPoiLayer(id: string) {
  return FACILITY_LAYER_HINTS.some((hint) => id.includes(hint));
}

export function applyObservatoryBasemapTheme(map: MapLibreMap): BasemapLayerIndex {
  const labels: string[] = [];
  const hydrography: string[] = [];
  const waterways: string[] = [];
  const buildings: string[] = [];
  const transport: string[] = [];
  const facilities: string[] = [];

  const style = map.getStyle();

  for (const rawLayer of style.layers ?? []) {
    const layer = rawLayer as StyleLayerLike;
    const sourceLayer = (layer["source-layer"] ?? "").toLowerCase();
    const id = layer.id.toLowerCase();

    if (layer.type === "background") {
      // Kristal brand land: intentionally bold and uniform at every zoom.
      // Water/hydrography remains blue and carries the geographic structure.
      safePaint(map, layer.id, "background-color", "#1E6864");
      continue;
    }

    // v0.3.3 VECTOR ATLAS: remove shaded-relief / Natural Earth raster context.
    // Local satellite is added later as a separate explicitly toggled layer.
    if (layer.type === "raster" || layer.type === "hillshade") {
      safeLayout(map, layer.id, "visibility", "none");
      continue;
    }

    const isParkOrLandTheme =
      sourceLayer === "park" ||
      sourceLayer.includes("protected") ||
      sourceLayer.includes("landcover") ||
      sourceLayer.includes("landuse") ||
      id.includes("park") ||
      id.includes("protected") ||
      id.includes("landcover") ||
      id.includes("landuse");

    if (isParkOrLandTheme) {
      safeLayout(map, layer.id, "visibility", "none");
      continue;
    }

    if (sourceLayer === "housenumber" || id.includes("housenumber")) {
      safeLayout(map, layer.id, "visibility", "none");
      continue;
    }

    const isWater = sourceLayer === "water" || id.includes("water_fill") || id === "water";
    const isWaterway =
      sourceLayer === "waterway" ||
      sourceLayer.includes("waterway") ||
      id.includes("waterway") ||
      id.includes("river");
    const isBuilding = sourceLayer.includes("building") || id.includes("building");
    const isTransportGeometry = sourceLayer === "transportation";
    const isAeroway =
      sourceLayer === "aeroway" ||
      sourceLayer === "aerodrome_label" ||
      id.includes("aeroway") ||
      id.includes("aerodrome") ||
      id.includes("airport");
    const isPoi = sourceLayer === "poi" || sourceLayer.includes("poi");
    const isFacilityPoi = isPoi && isFacilityPoiLayer(id);
    const isBoundary = sourceLayer.includes("boundary") || id.includes("boundary") || id.includes("admin_");

    if (isWater) {
      hydrography.push(layer.id);
      if (layer.type === "fill") {
        safePaint(map, layer.id, "fill-color", [
          "interpolate",
          ["linear"],
          ["zoom"],
          0, "#082633",
          8, "#0a3142",
          14, "#0d3d52",
          20, "#104a61",
        ]);
        safePaint(map, layer.id, "fill-opacity", 0.98);
      } else if (layer.type === "line") {
        safePaint(map, layer.id, "line-color", "#43a3c2");
        safePaint(map, layer.id, "line-opacity", 0.92);
      }
      continue;
    }

    if (isWaterway) {
      hydrography.push(layer.id);
      if (layer.type === "line") {
        waterways.push(layer.id);
        const isMajorRiver = id.includes("river") || id.includes("canal");
        safePaint(map, layer.id, "line-color", isMajorRiver ? "#4bb2d3" : "#3f94b0");
        safePaint(map, layer.id, "line-opacity", isMajorRiver ? 0.96 : 0.82);
        safePaint(map, layer.id, "line-width", [
          "interpolate",
          ["linear"],
          ["zoom"],
          7, isMajorRiver ? 0.7 : 0.35,
          11, isMajorRiver ? 1.25 : 0.65,
          14, isMajorRiver ? 2.2 : 1.05,
          17, isMajorRiver ? 3.1 : 1.45,
          20, isMajorRiver ? 4.0 : 1.9,
        ]);
      }
      if (layer.type === "symbol") {
        safeLayout(map, layer.id, "text-font", ["Noto Sans Regular"]);
        safeLayout(map, layer.id, "text-size", [
          "interpolate", ["linear"], ["zoom"],
          5, 11.5,
          8, 12.5,
          11, 13.5,
          14, 15,
          18, 16,
        ]);
        safePaint(map, layer.id, "text-color", "#9bdcf0");
        safePaint(map, layer.id, "text-halo-color", "rgba(3, 12, 17, .98)");
        safePaint(map, layer.id, "text-halo-width", 1.8);
        safePaint(map, layer.id, "text-halo-blur", 0.25);
        labels.push(layer.id);
      }
      continue;
    }

    if (isBuilding) {
      buildings.push(layer.id);
      if (layer.type === "fill") {
        safePaint(map, layer.id, "fill-color", "#71868b");
        safePaint(map, layer.id, "fill-opacity", 0.62);
        safePaint(map, layer.id, "fill-outline-color", "#9aadb1");
      } else if (layer.type === "fill-extrusion") {
        safePaint(map, layer.id, "fill-extrusion-color", "#71868b");
        safePaint(map, layer.id, "fill-extrusion-opacity", 0.56);
      } else if (layer.type === "line") {
        safePaint(map, layer.id, "line-color", "#9aadb1");
        safePaint(map, layer.id, "line-opacity", 0.66);
      }
      continue;
    }

    if (isTransportGeometry) {
      transport.push(layer.id);
      if (layer.type === "line") {
        const isTrack = id.includes("path") || id.includes("track");
        safePaint(map, layer.id, "line-color", isTrack ? "#64747a" : "#7c8d92");
        safePaint(map, layer.id, "line-opacity", isTrack ? 0.36 : 0.58);
      } else if (layer.type === "fill") {
        safePaint(map, layer.id, "fill-color", "#5d6d72");
        safePaint(map, layer.id, "fill-opacity", 0.48);
      }
      continue;
    }

    if (isAeroway) {
      facilities.push(layer.id);
      if (layer.type === "line") {
        safePaint(map, layer.id, "line-color", "#9a927d");
        safePaint(map, layer.id, "line-opacity", 0.52);
      } else if (layer.type === "fill") {
        safePaint(map, layer.id, "fill-color", "#756f60");
        safePaint(map, layer.id, "fill-opacity", 0.34);
      } else if (layer.type === "symbol") {
        safeLayout(map, layer.id, "text-font", ["Noto Sans Regular"]);
        safeLayout(map, layer.id, "text-size", [
          "interpolate", ["linear"], ["zoom"],
          7, 11.5,
          11, 13,
          15, 14.5,
          19, 16,
        ]);
        safePaint(map, layer.id, "text-color", "#ddd5bc");
        safePaint(map, layer.id, "text-halo-color", "rgba(3, 12, 17, .98)");
        safePaint(map, layer.id, "text-halo-width", 1.8);
        safePaint(map, layer.id, "text-halo-blur", 0.25);
      }
      continue;
    }

    if (isPoi) {
      // Generic commercial / leisure POIs are noise for the Observatory.
      // Keep only infrastructure/public-service style POI layers as context.
      if (!isFacilityPoi) {
        safeLayout(map, layer.id, "visibility", "none");
        continue;
      }

      facilities.push(layer.id);
      if (layer.type === "symbol") {
        safeLayout(map, layer.id, "text-font", ["Noto Sans Regular"]);
        safeLayout(map, layer.id, "text-size", [
          "interpolate", ["linear"], ["zoom"],
          8, 11.5,
          12, 13,
          16, 14.5,
          20, 15.5,
        ]);
        safePaint(map, layer.id, "text-color", "#c7dce1");
        safePaint(map, layer.id, "text-halo-color", "rgba(3, 12, 17, .98)");
        safePaint(map, layer.id, "text-halo-width", 1.75);
        safePaint(map, layer.id, "text-halo-blur", 0.25);
        safePaint(map, layer.id, "icon-opacity", 0.9);
      }
      continue;
    }

    if (isBoundary) {
      if (layer.type === "line") {
        safePaint(map, layer.id, "line-color", "#53676e");
        safePaint(map, layer.id, "line-opacity", 0.42);
      }
      continue;
    }

    if (layer.type === "symbol") {
      // Observatory owns community naming. Upstream place labels (city/town/
      // village) duplicate the governed Kristal community label at the same
      // coordinates, so suppress them while retaining water/road/context names.
      const isPlaceLabel =
        sourceLayer === "place" ||
        sourceLayer.includes("place") ||
        id.includes("place") ||
        id.includes("city") ||
        id.includes("town") ||
        id.includes("village");
      if (isPlaceLabel) {
        safeLayout(map, layer.id, "visibility", "none");
        continue;
      }

      // Force a single supported font to avoid mixed Open Sans + Arial Unicode
      // glyph requests in MapLibre v6.
      safeLayout(map, layer.id, "text-font", ["Noto Sans Regular"]);

      const isTransportLabel =
        sourceLayer.includes("transportation_name") ||
        id.includes("road") ||
        id.includes("street") ||
        id.includes("highway");

      safeLayout(map, layer.id, "text-size", isTransportLabel
        ? ["interpolate", ["linear"], ["zoom"], 8, 11, 12, 12.5, 16, 14, 20, 15]
        : ["interpolate", ["linear"], ["zoom"], 3, 11.5, 7, 12.5, 11, 13.5, 15, 14.5, 20, 15.5]);
      safePaint(map, layer.id, "text-color", "#c5d9de");
      safePaint(map, layer.id, "text-halo-color", "rgba(3, 12, 17, .94)");
      safePaint(map, layer.id, "text-halo-width", 1.7);
      safePaint(map, layer.id, "text-halo-blur", 0.25);
      labels.push(layer.id);
      continue;
    }

    // Everything else is intentionally suppressed in Atlas mode. This keeps
    // regional and high-zoom views stable instead of revealing arbitrary OSM
    // thematic fills as zoom thresholds are crossed.
    if (layer.type === "fill" || layer.type === "line" || layer.type === "circle") {
      safeLayout(map, layer.id, "visibility", "none");
    }
  }

  return {
    labelLayerIds: labels,
    hydrographyLayerIds: hydrography,
    waterwayLayerIds: waterways,
    buildingLayerIds: buildings,
    transportLayerIds: transport,

    facilityLayerIds: facilities,
  };
}

export function setBasemapLayerGroupVisible(
  map: MapLibreMap,
  layerIds: string[],
  visible: boolean,
) {
  for (const id of layerIds) {
    safeLayout(map, id, "visibility", visible ? "visible" : "none");
  }
}

export function setBasemapLabelsVisible(
  map: MapLibreMap,
  layerIds: string[],
  visible: boolean,
) {
  setBasemapLayerGroupVisible(map, layerIds, visible);
}

export function setContextualHydrographyVisible(
  map: MapLibreMap,
  layerIds: string[],
  visible: boolean,
) {
  setBasemapLayerGroupVisible(map, layerIds, visible);
}

/**
 * Add a manually published local satellite tile pyramid.
 *
 * No external satellite provider is contacted at runtime. The manifest must
 * reference a repo-local or loopback/local-network ZXY endpoint, e.g.
 * http://127.0.0.1:8765/postville/{z}/{x}/{y}.webp.
 *
 * v0.3.2 deliberately keeps this layer hidden until the user turns it on.
 */
export function addLocalSatelliteImagery(
  map: MapLibreMap,
  manifest: LocalImageryManifest | null,
): boolean {
  if (!manifest?.available || !/^(\/|https?:\/\/)/i.test(manifest.tile_template)) return false;

  try {
    if (!map.getSource(LOCAL_SATELLITE_SOURCE_ID)) {
      map.addSource(LOCAL_SATELLITE_SOURCE_ID, {
        type: "raster",
        tiles: [manifest.tile_template],
        tileSize: manifest.tile_size,
        minzoom: manifest.minzoom,
        maxzoom: manifest.maxzoom,
        ...(manifest.bounds ? { bounds: manifest.bounds } : {}),
        attribution: manifest.attribution ?? "Local imagery snapshot",
      });
    }

    if (!map.getLayer(LOCAL_SATELLITE_LAYER_ID)) {
      const firstLineOrSymbol = (map.getStyle().layers ?? []).find(
        (layer) => layer.type === "line" || layer.type === "symbol",
      );

      map.addLayer(
        {
          id: LOCAL_SATELLITE_LAYER_ID,
          type: "raster",
          source: LOCAL_SATELLITE_SOURCE_ID,
          minzoom: Math.max(0, manifest.minzoom - 0.25),
          maxzoom: 20.01,
          layout: { visibility: "none" },
          paint: {
            "raster-opacity": [
              "interpolate",
              ["linear"],
              ["zoom"],
              Math.max(0, manifest.minzoom - 0.25), 0.0,
              manifest.minzoom + 0.5, 0.12,
              manifest.minzoom + 1.5, 0.34,
              manifest.minzoom + 2.5, 0.52,
              manifest.minzoom + 3.5, 0.62,
            ],
            "raster-saturation": -0.14,
            "raster-contrast": 0.02,
            "raster-brightness-min": 0.08,
            "raster-brightness-max": 0.92,
            "raster-fade-duration": 220,
          },
        },
        firstLineOrSymbol?.id,
      );
    }

    return true;
  } catch {
    return false;
  }
}

export function setLocalSatelliteImageryVisible(map: MapLibreMap, visible: boolean) {
  if (!map.getLayer(LOCAL_SATELLITE_LAYER_ID)) return;
  safeLayout(map, LOCAL_SATELLITE_LAYER_ID, "visibility", visible ? "visible" : "none");
}

const LOCAL_TERRAIN_SOURCE_ID = "kristal-local-terrain-source";
const LOCAL_TERRAIN_RELIEF_LAYER_ID = "kristal-local-terrain-relief";
const LOCAL_TERRAIN_BASIN_LAYER_ID = "kristal-local-terrain-basin";

/**
 * Add locally generated HRDEM screening cells. The source is deliberately a
 * repo-local GeoJSON product so the public map never invents relief geometry
 * or depends on a runtime DEM provider.
 */
export function addLocalTerrainScreening(
  map: MapLibreMap,
  manifest: LocalTerrainManifest | null,
): boolean {
  if (!manifest?.available || !manifest.geojson_url.startsWith("/")) return false;

  try {
    if (!map.getSource(LOCAL_TERRAIN_SOURCE_ID)) {
      map.addSource(LOCAL_TERRAIN_SOURCE_ID, {
        type: "geojson",
        data: manifest.geojson_url,
        attribution: `${manifest.source ?? "Local terrain"}${manifest.vertical_datum ? ` · ${manifest.vertical_datum}` : ""}`,
      });
    }

    const firstLineOrSymbol = (map.getStyle().layers ?? []).find(
      (layer) => layer.type === "line" || layer.type === "symbol",
    );

    if (!map.getLayer(LOCAL_TERRAIN_RELIEF_LAYER_ID)) {
      map.addLayer(
        {
          id: LOCAL_TERRAIN_RELIEF_LAYER_ID,
          type: "fill",
          source: LOCAL_TERRAIN_SOURCE_ID,
          minzoom: Math.max(0, manifest.minzoom - 0.5),
          maxzoom: Math.min(20.01, manifest.maxzoom + 1),
          layout: { visibility: "none" },
          paint: {
            "fill-antialias": false,
            "fill-color": [
              "interpolate",
              ["linear"],
              ["get", "elevation_m"],
              0, "#0e4d58",
              40, "#26736f",
              100, "#5a8a6b",
              200, "#9b9867",
              400, "#a77b5b",
              700, "#8f6e68",
              1000, "#c3bbb0",
            ],
            "fill-opacity": [
              "interpolate",
              ["linear"],
              ["zoom"],
              manifest.minzoom, 0.25,
              Math.min(manifest.maxzoom, manifest.minzoom + 3), 0.46,
              manifest.maxzoom, 0.58,
            ],
          },
        },
        firstLineOrSymbol?.id,
      );
    }

    if (!map.getLayer(LOCAL_TERRAIN_BASIN_LAYER_ID)) {
      map.addLayer(
        {
          id: LOCAL_TERRAIN_BASIN_LAYER_ID,
          type: "fill",
          source: LOCAL_TERRAIN_SOURCE_ID,
          minzoom: Math.max(0, manifest.minzoom - 0.5),
          maxzoom: Math.min(20.01, manifest.maxzoom + 1),
          filter: ["==", ["get", "site_id"], "__none__"],
          layout: { visibility: "none" },
          paint: {
            "fill-antialias": false,
            "fill-color": basinDepthColorExpression(50),
            "fill-opacity": [
              "interpolate",
              ["linear"],
              ["zoom"],
              manifest.minzoom, 0.52,
              Math.min(manifest.maxzoom, manifest.minzoom + 3), 0.72,
              manifest.maxzoom, 0.82,
            ],
          },
        },
        firstLineOrSymbol?.id,
      );
    }

    return true;
  } catch {
    return false;
  }
}

function basinDepthColorExpression(riseM: number): any {
  const depth = ["max", 0, ["-", riseM, ["get", "relative_elevation_m"]]];
  return [
    "interpolate",
    ["linear"],
    depth,
    0, "rgba(142, 231, 244, 0.34)",
    5, "rgba(91, 201, 232, 0.50)",
    15, "rgba(43, 153, 210, 0.66)",
    30, "rgba(26, 105, 177, 0.76)",
    60, "rgba(27, 67, 137, 0.84)",
    120, "rgba(48, 43, 105, 0.90)",
  ];
}

export function setLocalTerrainReliefVisible(map: MapLibreMap, visible: boolean) {
  if (!map.getLayer(LOCAL_TERRAIN_RELIEF_LAYER_ID)) return;
  safeLayout(map, LOCAL_TERRAIN_RELIEF_LAYER_ID, "visibility", visible ? "visible" : "none");
}

export function setLocalTerrainBasinsVisible(map: MapLibreMap, visible: boolean) {
  if (!map.getLayer(LOCAL_TERRAIN_BASIN_LAYER_ID)) return;
  safeLayout(map, LOCAL_TERRAIN_BASIN_LAYER_ID, "visibility", visible ? "visible" : "none");
}

export function setLocalTerrainBasinState(
  map: MapLibreMap,
  siteId: string | null,
  riseM: number,
) {
  if (!map.getLayer(LOCAL_TERRAIN_BASIN_LAYER_ID)) return;
  const safeRise = Math.max(0, Math.min(500, Number.isFinite(riseM) ? riseM : 0));
  try {
    map.setFilter(LOCAL_TERRAIN_BASIN_LAYER_ID,
      siteId
        ? [
            "all",
            ["==", ["get", "site_id"], siteId],
            ["<=", ["get", "spill_rise_m"], safeRise],
            ["<=", ["get", "relative_elevation_m"], safeRise],
          ]
        : ["==", ["get", "site_id"], "__none__"],
    );
    map.setPaintProperty(LOCAL_TERRAIN_BASIN_LAYER_ID, "fill-color", basinDepthColorExpression(safeRise));
  } catch {
    // Ignore style transitions during teardown/reload.
  }
}

const GRID_REACH_SOURCE_ID = "kristal-grid-reach-source";
const GRID_REACH_MAJOR_LAYER_ID = "kristal-grid-reach-major";
const GRID_REACH_LOCAL_LAYER_ID = "kristal-grid-reach-local";
const GRID_REACH_TERMINAL_HALO_LAYER_ID = "kristal-grid-reach-terminal-halo";
const GRID_REACH_MARKER_LAYER_ID = "kristal-grid-reach-markers";
const GRID_REACH_TERMINAL_CORE_LAYER_ID = "kristal-grid-reach-terminal-core";
const GRID_REACH_LABEL_LAYER_ID = "kristal-grid-reach-labels";

/** Lightweight source-backed electrical reach context. Geometry is schematic. */
export function addGridReach(map: MapLibreMap, manifest: GridReachManifest | null): boolean {
  if (!manifest?.features?.length) return false;
  try {
    const existing = map.getSource(GRID_REACH_SOURCE_ID) as { setData?: (data: any) => void } | undefined;
    if (existing?.setData) existing.setData(manifest as any);
    else map.addSource(GRID_REACH_SOURCE_ID, { type: "geojson", data: manifest as any });

    const before = (map.getStyle().layers ?? []).find((layer) => layer.type === "symbol")?.id;
    if (!map.getLayer(GRID_REACH_MAJOR_LAYER_ID)) {
      map.addLayer({
        id: GRID_REACH_MAJOR_LAYER_ID,
        type: "line",
        source: GRID_REACH_SOURCE_ID,
        minzoom: 3,
        filter: ["all", ["==", ["get", "feature_role"], "grid_connection"], ["!=", ["get", "voltage_class"], "local_extension"]],
        layout: { visibility: "visible", "line-cap": "round", "line-join": "round" },
        paint: {
          "line-color": [
            "case",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 700], "#f2b35d",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 300], "#d9c36d",
            "#6bc7dc",
          ],
          "line-width": [
            "interpolate", ["linear"], ["zoom"],
            3, ["case", [">=", ["coalesce", ["get", "voltage_kv"], 0], 700], 2.2, 1.25],
            8, ["case", [">=", ["coalesce", ["get", "voltage_kv"], 0], 700], 4.4, 2.5],
          ],
          "line-opacity": 0.82,
        },
      }, before);
    }
    if (!map.getLayer(GRID_REACH_LOCAL_LAYER_ID)) {
      map.addLayer({
        id: GRID_REACH_LOCAL_LAYER_ID,
        type: "line",
        source: GRID_REACH_SOURCE_ID,
        minzoom: 4,
        filter: ["all", ["==", ["get", "feature_role"], "grid_connection"], ["==", ["get", "voltage_class"], "local_extension"]],
        layout: { visibility: "visible", "line-cap": "round", "line-join": "round" },
        paint: {
          "line-color": "#9fb7be",
          "line-width": ["interpolate", ["linear"], ["zoom"], 4, 1, 9, 2.2],
          "line-opacity": 0.76,
          "line-dasharray": [2, 2],
        },
      }, before);
    }
    if (!map.getLayer(GRID_REACH_TERMINAL_HALO_LAYER_ID)) {
      map.addLayer({
        id: GRID_REACH_TERMINAL_HALO_LAYER_ID,
        type: "circle",
        source: GRID_REACH_SOURCE_ID,
        minzoom: 3.25,
        filter: ["==", ["get", "feature_role"], "reach_marker"],
        layout: { visibility: "visible" },
        paint: {
          "circle-radius": ["interpolate", ["linear"], ["zoom"], 3.25, 8, 8, 13],
          "circle-color": [
            "case",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 700], "#f2b35d",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 100], "#6bc7dc",
            "#9fb7be",
          ],
          "circle-opacity": 0.12,
        },
      });
    }
    if (!map.getLayer(GRID_REACH_MARKER_LAYER_ID)) {
      map.addLayer({
        id: GRID_REACH_MARKER_LAYER_ID,
        type: "circle",
        source: GRID_REACH_SOURCE_ID,
        minzoom: 3.25,
        filter: ["==", ["get", "feature_role"], "reach_marker"],
        layout: { visibility: "visible" },
        paint: {
          "circle-radius": ["interpolate", ["linear"], ["zoom"], 3.25, 5.5, 8, 8],
          "circle-color": "#061217",
          "circle-stroke-color": [
            "case",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 700], "#f2b35d",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 100], "#6bc7dc",
            "#9fb7be",
          ],
          "circle-stroke-width": 2,
          "circle-opacity": 0.98,
        },
      });
    }
    if (!map.getLayer(GRID_REACH_TERMINAL_CORE_LAYER_ID)) {
      map.addLayer({
        id: GRID_REACH_TERMINAL_CORE_LAYER_ID,
        type: "circle",
        source: GRID_REACH_SOURCE_ID,
        minzoom: 3.25,
        filter: ["==", ["get", "feature_role"], "reach_marker"],
        layout: { visibility: "visible" },
        paint: {
          "circle-radius": ["interpolate", ["linear"], ["zoom"], 3.25, 1.8, 8, 2.8],
          "circle-color": [
            "case",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 700], "#f2b35d",
            [">=", ["coalesce", ["get", "voltage_kv"], 0], 100], "#6bc7dc",
            "#9fb7be",
          ],
          "circle-opacity": 1,
        },
      });
    }
    if (!map.getLayer(GRID_REACH_LABEL_LAYER_ID)) {
      map.addLayer({
        id: GRID_REACH_LABEL_LAYER_ID,
        type: "symbol",
        source: GRID_REACH_SOURCE_ID,
        minzoom: 4.25,
        filter: ["==", ["get", "feature_role"], "reach_marker"],
        layout: {
          visibility: "visible",
          "text-field": ["get", "name"],
          "text-font": ["Noto Sans Regular"],
          "text-size": ["interpolate", ["linear"], ["zoom"], 4.25, 9.5, 8, 11.5],
          "text-offset": [1.15, 0],
          "text-anchor": "left",
          "text-allow-overlap": false,
        },
        paint: {
          "text-color": "#e7f6f9",
          "text-halo-color": "rgba(3, 12, 17, .94)",
          "text-halo-width": 1.5,
        },
      });
    }
    return true;
  } catch {
    return false;
  }
}

export function setGridReachVisible(map: MapLibreMap, visible: boolean) {
  for (const layerId of [
    GRID_REACH_MAJOR_LAYER_ID,
    GRID_REACH_LOCAL_LAYER_ID,
    GRID_REACH_TERMINAL_HALO_LAYER_ID,
    GRID_REACH_MARKER_LAYER_ID,
    GRID_REACH_TERMINAL_CORE_LAYER_ID,
    GRID_REACH_LABEL_LAYER_ID,
  ]) {
    if (!map.getLayer(layerId)) continue;
    safeLayout(map, layerId, "visibility", visible ? "visible" : "none");
  }
}

