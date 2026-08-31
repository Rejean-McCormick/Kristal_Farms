import type { Map as MapLibreMap, StyleSpecification } from "maplibre-gl";
import type { LocalImageryManifest } from "./explorer-types";

const DEFAULT_VECTOR_STYLE = "https://tiles.openfreemap.org/styles/liberty";

const LOCAL_SATELLITE_SOURCE_ID = "kristal-local-satellite-source";
const LOCAL_SATELLITE_LAYER_ID = "kristal-local-satellite";

/**
 * The v0.2 development basemap uses an OpenMapTiles/OpenStreetMap vector style
 * with no application API key. Production may point NEXT_PUBLIC_BASE_STYLE_URL
 * at a self-hosted or otherwise approved MapLibre style.
 *
 * The Observatory theme is applied after style load so the upstream vector
 * schema remains queryable for contextual hydrography.
 */
export function createObservatoryStyle(): string | StyleSpecification {
  return process.env.NEXT_PUBLIC_BASE_STYLE_URL ?? DEFAULT_VECTOR_STYLE;
}

export type BasemapLayerIndex = {
  labelLayerIds: string[];
  waterwayLayerIds: string[];
};

type StyleLayerLike = {
  id: string;
  type: string;
  source?: string;
  "source-layer"?: string;
};

export function applyObservatoryBasemapTheme(map: MapLibreMap): BasemapLayerIndex {
  const style = map.getStyle();
  const labels: string[] = [];
  const waterways: string[] = [];

  for (const rawLayer of style.layers ?? []) {
    const layer = rawLayer as StyleLayerLike;
    const sourceLayer = (layer["source-layer"] ?? "").toLowerCase();
    const id = layer.id.toLowerCase();

    try {
      if (layer.type === "background") {
        map.setPaintProperty(layer.id, "background-color", "#131b20");
        continue;
      }

      if (layer.type === "raster") {
        const sourceId = (layer.source ?? "").toLowerCase();
        const isNaturalEarth =
          layer.id.toLowerCase() === "natural_earth" ||
          sourceId.includes("ne2_shaded") ||
          sourceId.includes("natural_earth");

        if (isNaturalEarth) {
          // OpenFreeMap Liberty normally fades this Natural Earth shaded raster
          // almost completely by z6 and stops rendering it at z7. That exposes
          // the Observatory background and makes land appear progressively black.
          //
          // Keep it alive a little longer using source overzoom, then fade it
          // gently into the neutral Observatory land background.
          map.setLayerZoomRange(layer.id, 0, 9.5);
          map.setPaintProperty(layer.id, "raster-opacity", [
            "interpolate",
            ["linear"],
            ["zoom"],
            0, 0.62,
            4, 0.52,
            6, 0.44,
            7.5, 0.30,
            9, 0.10,
            9.5, 0.0,
          ]);
          map.setPaintProperty(layer.id, "raster-saturation", -0.55);
          map.setPaintProperty(layer.id, "raster-contrast", 0.06);
          map.setPaintProperty(layer.id, "raster-brightness-min", 0.12);
          map.setPaintProperty(layer.id, "raster-brightness-max", 0.74);
        }
        continue;
      }

      if (layer.type === "symbol") {
        const isPoi = sourceLayer.includes("poi") || id.includes("poi");
        if (isPoi) {
          map.setLayoutProperty(layer.id, "visibility", "none");
          continue;
        }
        labels.push(layer.id);
        if (sourceLayer.includes("water") || id.includes("water") || id.includes("river")) {
          map.setPaintProperty(layer.id, "text-color", "#5f9eb0");
          map.setPaintProperty(layer.id, "text-halo-color", "rgba(3, 10, 15, .92)");
          map.setPaintProperty(layer.id, "text-halo-width", 1.25);
        } else {
          map.setPaintProperty(layer.id, "text-color", "#748992");
          map.setPaintProperty(layer.id, "text-halo-color", "rgba(3, 9, 14, .88)");
          map.setPaintProperty(layer.id, "text-halo-width", 1.1);
        }
        continue;
      }

      if (layer.type === "fill") {
        const isPark =
          sourceLayer === "park" ||
          sourceLayer.includes("protected") ||
          id === "park" ||
          id.includes("park_") ||
          id.includes("protected");

        const isLandTheme =
          sourceLayer.includes("landcover") ||
          sourceLayer.includes("landuse") ||
          id.includes("landcover") ||
          id.includes("landuse");

        if (sourceLayer === "water" || id.includes("water")) {
          map.setPaintProperty(layer.id, "fill-color", "#071820");
          map.setPaintProperty(layer.id, "fill-opacity", 0.94);
        } else if (isPark) {
          // Liberty renders parks/protected areas as large pale-green polygons.
          // They are contextual basemap data, not Kristal evidence, and visually
          // overwhelm the Observatory at regional zoom levels.
          map.setLayoutProperty(layer.id, "visibility", "none");
        } else if (isLandTheme) {
          // Keep the Observatory regional view clean. Generic OSM landcover /
          // landuse polygons are not part of the evidence model and otherwise
          // appear suddenly as the vector style crosses minzoom thresholds.
          //
          // Preserve ice as subtle geographic context; hide the rest.
          if (id.includes("ice") || id.includes("glacier")) {
            map.setPaintProperty(layer.id, "fill-color", "#101b22");
            map.setPaintProperty(layer.id, "fill-opacity", 0.34);
          } else {
            map.setLayoutProperty(layer.id, "visibility", "none");
          }
        } else if (sourceLayer.includes("building")) {
          map.setPaintProperty(layer.id, "fill-color", "#0b151b");
          map.setPaintProperty(layer.id, "fill-opacity", 0.48);
        }
        continue;
      }

      if (layer.type === "line") {
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
          map.setLayoutProperty(layer.id, "visibility", "none");
          continue;
        }

        const isWaterway =
          sourceLayer === "waterway" ||
          sourceLayer.includes("waterway") ||
          id.includes("waterway") ||
          id.includes("river");
        if (isWaterway) {
          waterways.push(layer.id);
          map.setPaintProperty(layer.id, "line-color", "#2c7287");
          map.setPaintProperty(layer.id, "line-opacity", 0.72);
        } else if (sourceLayer.includes("transportation") || id.includes("road")) {
          map.setPaintProperty(layer.id, "line-color", "#182a31");
          map.setPaintProperty(layer.id, "line-opacity", 0.38);
        } else if (sourceLayer.includes("boundary") || id.includes("boundary")) {
          map.setPaintProperty(layer.id, "line-color", "#28404a");
          map.setPaintProperty(layer.id, "line-opacity", 0.34);
        }
      }
    } catch {
      // Upstream styles differ. Unsupported paint/layout properties are skipped.
    }
  }

  return { labelLayerIds: labels, waterwayLayerIds: waterways };
}

export function setBasemapLabelsVisible(
  map: MapLibreMap,
  layerIds: string[],
  visible: boolean,
) {
  for (const id of layerIds) {
    try {
      map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
    } catch {
      // Style may have changed while the control was toggled.
    }
  }
}

export function setContextualHydrographyVisible(
  map: MapLibreMap,
  layerIds: string[],
  visible: boolean,
) {
  for (const id of layerIds) {
    try {
      map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
    } catch {
      // Style may have changed while the control was toggled.
    }
  }
}


/**
 * Add a manually published local satellite tile pyramid.
 *
 * No external satellite provider is contacted at runtime. The manifest must
 * reference a local path such as /imagery/sentinel2-quebec-2020/{z}/{x}/{y}.png.
 */
export function addLocalSatelliteImagery(
  map: MapLibreMap,
  manifest: LocalImageryManifest | null,
): boolean {
  if (!manifest?.available || !manifest.tile_template.startsWith("/")) return false;

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
          layout: {
            visibility: "none",
          },
          paint: {
            "raster-opacity": [
              "interpolate",
              ["linear"],
              ["zoom"],
              Math.max(0, manifest.minzoom - 0.25),
              0.0,
              manifest.minzoom + 0.5,
              0.18,
              manifest.minzoom + 1.5,
              0.52,
              manifest.minzoom + 2.5,
              0.82,
              manifest.minzoom + 3.5,
              0.96,
            ],
            "raster-saturation": -0.08,
            "raster-contrast": 0.06,
            "raster-brightness-min": 0.03,
            "raster-brightness-max": 0.96,
            "raster-fade-duration": 260,
          },
        },
        firstLineOrSymbol?.id,
      );
    }

    return true;
  } catch {
    // A malformed local tile pyramid must never prevent the Observatory from loading.
    return false;
  }
}

export function setLocalSatelliteImageryVisible(map: MapLibreMap, visible: boolean) {
  if (!map.getLayer(LOCAL_SATELLITE_LAYER_ID)) return;

  try {
    map.setLayoutProperty(
      LOCAL_SATELLITE_LAYER_ID,
      "visibility",
      visible ? "visible" : "none",
    );
  } catch {
    // Style may be rebuilding during a toggle.
  }
}
