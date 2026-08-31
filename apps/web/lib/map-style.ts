import type { StyleSpecification } from "maplibre-gl";

/**
 * Development basemap. Production deployments should set NEXT_PUBLIC_BASE_TILE_URL
 * to an approved raster source or replace this with the governed vector style.
 */
export function createObservatoryStyle(): StyleSpecification {
  const tileUrl =
    process.env.NEXT_PUBLIC_BASE_TILE_URL ??
    "https://a.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png";

  return {
    version: 8,
    name: "Kristal Observatory",
    sources: {
      basemap: {
        type: "raster",
        tiles: [tileUrl],
        tileSize: 256,
        attribution:
          "© OpenStreetMap contributors © CARTO — development basemap; configure an approved production provider",
      },
    },
    layers: [
      {
        id: "background",
        type: "background",
        paint: { "background-color": "#050a10" },
      },
      {
        id: "basemap",
        type: "raster",
        source: "basemap",
        paint: {
          "raster-opacity": 0.66,
          "raster-saturation": -0.45,
          "raster-contrast": 0.14,
          "raster-brightness-min": 0.02,
          "raster-brightness-max": 0.72,
          "raster-fade-duration": 120,
        },
      },
    ],
  };
}
