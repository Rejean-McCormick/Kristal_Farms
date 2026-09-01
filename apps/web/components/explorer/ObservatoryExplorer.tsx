"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import type {
  EntityKind,
  ExplorerBootstrap,
  GridReachManifest,
  LocalImageryManifest,
  LocalTerrainManifest,
  MapCameraState,
  ObservatoryVisibleLayers,
  PublicMapFeature,
} from "../../lib/explorer-types";
import { formatCoordinate } from "../../lib/format";
import { CompareTray } from "./CompareTray";
import { EntityInspector } from "./EntityInspector";
import { ObservatoryMap } from "./ObservatoryMap";

const DEFAULT_CAMERA: MapCameraState = {
  lng: -69.8,
  lat: 56.2,
  zoom: 3.55,
  bearing: 0,
  pitch: 0,
};

type SearchItem = {
  entityId: string;
  kind: EntityKind;
  title: string;
  subtitle: string;
  keywords: string;
};

export function ObservatoryExplorer({ embedded = false }: { embedded?: boolean } = {}) {
  const [bootstrap, setBootstrap] = useState<ExplorerBootstrap | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedEntityId, setSelectedEntityId] = useState<string | null>(null);
  const [compareIds, setCompareIds] = useState<string[]>([]);
  const [searchOpen, setSearchOpen] = useState(false);
  const [layersOpen, setLayersOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [cursor, setCursor] = useState({ lng: DEFAULT_CAMERA.lng, lat: DEFAULT_CAMERA.lat });
  const [zoom, setZoom] = useState(DEFAULT_CAMERA.zoom);
  const [initialView] = useState(() => readInitialViewFromUrl());
  const [resetViewRequest, setResetViewRequest] = useState(0);
  const [gridFocusRequest, setGridFocusRequest] = useState(0);
  const [localImagery, setLocalImagery] = useState<LocalImageryManifest | null>(null);
  const [localTerrain, setLocalTerrain] = useState<LocalTerrainManifest | null>(null);
  const [gridReach, setGridReach] = useState<GridReachManifest | null>(null);
  const handleCursorChange = useCallback((lng: number, lat: number) => setCursor({ lng, lat }), []);

  const [visibleLayers, setVisibleLayers] = useState<ObservatoryVisibleLayers>({
    communities: true,
    hydrometric_stations: false,
    contextual_hydrography: true,
    contextual_buildings: true,
    contextual_transport: true,
    contextual_facilities: true,
    grid_reach: true,
    satellite: false,
    terrain_relief: false,
    terrain_basins: false,
    labels: true,
  });

  useEffect(() => {
    const controller = new AbortController();
    fetch("/api/explorer/bootstrap", { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error(`Bootstrap failed (${response.status})`);
        return (await response.json()) as ExplorerBootstrap;
      })
      .then((payload) => {
        setBootstrap(payload);
        const params = new URLSearchParams(window.location.search);
        const entity = params.get("entity");
        if (entity) setSelectedEntityId(entity);
        const compare = params.get("compare")?.split(",").filter(Boolean).slice(0, 2) ?? [];
        setCompareIds(compare);
      })
      .catch((caught: unknown) => {
        if ((caught as Error).name !== "AbortError") setError((caught as Error).message);
      });
    return () => controller.abort();
  }, []);

  useEffect(() => {
    const controller = new AbortController();

    fetch("/imagery/local-satellite.json", { signal: controller.signal, cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) return null;
        return (await response.json()) as LocalImageryManifest;
      })
      .then((manifest) => {
        if (!manifest) return;
        // v0.3 Vector Atlas: photographic imagery is available on demand, but
        // never turns itself on. This prevents a local AOI rectangle from
        // replacing the clean vector map unexpectedly.
        setLocalImagery(manifest);
      })
      .catch((caught: unknown) => {
        if ((caught as Error).name !== "AbortError") setLocalImagery(null);
      });

    return () => controller.abort();
  }, []);

  useEffect(() => {
    const controller = new AbortController();

    fetch("/grid/grid-reach.geojson", { signal: controller.signal, cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) return null;
        return (await response.json()) as GridReachManifest;
      })
      .then((manifest) => {
        if (!manifest || manifest.schema !== "kristal-grid-reach/v1") return;
        setGridReach(manifest);
      })
      .catch((caught: unknown) => {
        if ((caught as Error).name !== "AbortError") setGridReach(null);
      });

    return () => controller.abort();
  }, []);

  useEffect(() => {
    const controller = new AbortController();

    fetch("/terrain/terrain-manifest.json", { signal: controller.signal, cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) return null;
        return (await response.json()) as LocalTerrainManifest;
      })
      .then((manifest) => {
        if (!manifest) return;
        setLocalTerrain(manifest);
      })
      .catch((caught: unknown) => {
        if ((caught as Error).name !== "AbortError") setLocalTerrain(null);
      });

    return () => controller.abort();
  }, []);

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key !== "/" || event.metaKey || event.ctrlKey || event.altKey) return;
      const target = event.target as HTMLElement | null;
      if (target?.matches("input, textarea, [contenteditable=true]")) return;
      event.preventDefault();
      setSearchOpen(true);
      setLayersOpen(false);
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, []);

  const updateUrl = useCallback(
    (updates: { entity?: string | null; compare?: string[]; camera?: MapCameraState }) => {
      const url = new URL(window.location.href);
      if ("entity" in updates) {
        if (updates.entity) url.searchParams.set("entity", updates.entity);
        else url.searchParams.delete("entity");
      }
      if (updates.compare) {
        if (updates.compare.length) url.searchParams.set("compare", updates.compare.join(","));
        else url.searchParams.delete("compare");
      }
      if (updates.camera) {
        const c = updates.camera;
        url.searchParams.set(
          "view",
          [c.lng.toFixed(5), c.lat.toFixed(5), c.zoom.toFixed(2), c.bearing.toFixed(1), c.pitch.toFixed(1)].join(","),
        );
      }
      window.history.replaceState({}, "", url);
    },
    [],
  );

  const handleCameraChange = useCallback(
    (camera: MapCameraState) => updateUrl({ camera }),
    [updateUrl],
  );

  const selectEntity = useCallback(
    (entityId: string | null) => {
      setSelectedEntityId(entityId);
      updateUrl({ entity: entityId });
    },
    [updateUrl],
  );

  const addCompare = useCallback(
    (entityId: string) => {
      setCompareIds((current) => {
        const next = current.includes(entityId)
          ? current.filter((id) => id !== entityId)
          : [...current, entityId].slice(-2);
        updateUrl({ compare: next });
        return next;
      });
    },
    [updateUrl],
  );

  const allFeatures = useMemo(
    () => (bootstrap ? [...bootstrap.communities.features, ...bootstrap.stations.features] : []),
    [bootstrap],
  );

  const compareFeatures = useMemo(
    () =>
      compareIds
        .map((id) => allFeatures.find((feature) => feature.properties.entity_id === id))
        .filter((feature): feature is PublicMapFeature => Boolean(feature)),
    [allFeatures, compareIds],
  );

  const searchItems = useMemo<SearchItem[]>(() => {
    if (!bootstrap) return [];
    const points: SearchItem[] = allFeatures.map((feature) => {
      const p = feature.properties;
      return {
        entityId: p.entity_id,
        kind: p.feature_kind,
        title: p.feature_kind === "hydrometric_station" ? p.station_number ?? p.name : p.name,
        subtitle: p.feature_kind === "hydrometric_station" ? p.river_name ?? p.region ?? "" : p.region ?? "",
        keywords: [p.name, p.region ?? "", p.station_number ?? "", p.river_name ?? ""].join(" "),
      };
    });
    const rivers: SearchItem[] = bootstrap.rivers.map((river) => ({
      entityId: river.entity_id,
      kind: "river",
      title: river.name,
      subtitle: [river.region, river.anchor_station_number ? `Station ${river.anchor_station_number}` : null]
        .filter(Boolean)
        .join(" · "),
      keywords: [river.name, river.region ?? "", ...river.aliases, river.anchor_station_number ?? ""].join(" "),
    }));
    return [...rivers, ...points];
  }, [allFeatures, bootstrap]);

  const searchResults = useMemo(() => {
    const q = searchQuery.trim().toLocaleLowerCase();
    if (!q) return searchItems.slice(0, 10);
    return searchItems
      .filter((item) => item.keywords.toLocaleLowerCase().includes(q))
      .slice(0, 14);
  }, [searchItems, searchQuery]);

  if (error) {
    return (
      <main className="fatal-state">
        <span>KRISTAL / NORTHERN ATLAS</span>
        <h1>Explorer unavailable</h1>
        <p>{error}</p>
      </main>
    );
  }

  if (!bootstrap) {
    return (
      <main className="boot-screen">
        <div className="boot-screen__reticle" aria-hidden="true">◎</div>
        <span>KRISTAL / NORTHERN ATLAS</span>
        <strong>Initializing geographic observatory</strong>
      </main>
    );
  }

  const activeLayerCount = Object.values(visibleLayers).filter(Boolean).length;
  const hydroOpportunityCount = bootstrap.hydroSites.length;

  return (
    <main className="observatory-shell">
      <ObservatoryMap
        data={bootstrap}
        selectedEntityId={selectedEntityId}
        visibleLayers={visibleLayers}
        compareIds={compareIds}
        initialCamera={initialView.camera}
        autoFitOnLoad={!initialView.fromUrl}
        resetViewRequest={resetViewRequest}
        localImagery={localImagery}
        localTerrain={localTerrain}
        gridReach={gridReach}
        gridFocusRequest={gridFocusRequest}
        onSelect={selectEntity}
        onCursorChange={handleCursorChange}
        onZoomChange={setZoom}
        onCameraChange={handleCameraChange}
      />

      <header className="top-hud">
        <div className="brand-lockup">
          <span>KRISTAL / NORTHERN ATLAS</span>
          <strong>OBSERVATORY · GEOGRAPHIC EXPLORER</strong>
        </div>
        <div className="top-actions">
          {!embedded && <a className="top-actions__link" href="/international">International 12</a>}
          <button
            type="button"
            className={searchOpen ? "is-active" : ""}
            onClick={() => {
              setSearchOpen((open) => !open);
              setLayersOpen(false);
            }}
          >
            Search
            <kbd>/</kbd>
          </button>
          <button
            type="button"
            onClick={() => {
              setResetViewRequest((value) => value + 1);
              setSearchOpen(false);
              setLayersOpen(false);
            }}
            title="Fit map to the published Kristal extent"
          >
            Reset view
            <span className="reset-glyph" aria-hidden="true">⌖</span>
          </button>
          <button
            type="button"
            className={layersOpen ? "is-active" : ""}
            onClick={() => {
              setLayersOpen((open) => !open);
              setSearchOpen(false);
            }}
          >
            Layers
            <span className="action-count">{activeLayerCount}</span>
          </button>
        </div>
      </header>

      {searchOpen && (
        <section className="floating-panel search-panel" aria-label="Search entities">
          <div className="floating-panel__header">
            <span>ENTITY SEARCH</span>
            <button type="button" onClick={() => setSearchOpen(false)} aria-label="Close search">×</button>
          </div>
          <input
            autoFocus
            type="search"
            value={searchQuery}
            onChange={(event) => setSearchQuery(event.target.value)}
            placeholder="Community, station, river…"
            aria-label="Search communities, rivers and hydrometric stations"
          />
          <div className="search-results">
            {searchResults.map((item) => (
              <button
                type="button"
                key={`${item.kind}:${item.entityId}`}
                onClick={() => {
                  selectEntity(item.entityId);
                  setSearchOpen(false);
                }}
              >
                <span className={`search-dot is-${item.kind}`} aria-hidden="true" />
                <span>
                  <strong>{item.title}</strong>
                  <small>{item.subtitle}</small>
                </span>
              </button>
            ))}
            {!searchResults.length && <p className="search-empty">No matching governed entity.</p>}
          </div>
        </section>
      )}

      {layersOpen && (
        <section className="floating-panel layer-panel" aria-label="Map layers">
          <div className="floating-panel__header">
            <span>LAYER CATALOG</span>
            <button type="button" onClick={() => setLayersOpen(false)} aria-label="Close layers">×</button>
          </div>

          <div className="layer-section-label">Governed overlays</div>
          {bootstrap.layers.map((layer) => {
            const key = layer.id as "communities" | "hydrometric_stations";
            const enabled = Boolean(visibleLayers[key]);
            return (
              <label className="layer-row" key={layer.id}>
                <input
                  type="checkbox"
                  checked={enabled}
                  onChange={(event) =>
                    setVisibleLayers((current) => ({ ...current, [key]: event.target.checked }))
                  }
                />
                <span className={`layer-symbol is-${layer.id}`} aria-hidden="true" />
                <span>
                  <strong>{layer.title}</strong>

                  <small>{layer.layer_group}</small>
                </span>
                <em>{enabled ? "ON" : "OFF"}</em>
              </label>
            );
          })}

          <div className="layer-section-label">Vector atlas</div>
          <ContextLayerRow
            id="contextual_hydrography"
            title="Rivers + lakes"
            subtitle="OpenMapTiles / OpenStreetMap · interactive context"
            checked={visibleLayers.contextual_hydrography}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, contextual_hydrography: checked }))
            }
          />
          <ContextLayerRow
            id="contextual_buildings"
            title="Buildings"
            subtitle="Context geometry · visible at local zoom"
            checked={visibleLayers.contextual_buildings}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, contextual_buildings: checked }))
            }
          />
          <ContextLayerRow
            id="contextual_transport"
            title="Roads + tracks"
            subtitle="Transportation access context"
            checked={visibleLayers.contextual_transport}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, contextual_transport: checked }))
            }
          />
          <ContextLayerRow
            id="contextual_facilities"
            title="Infrastructure + access"
            subtitle="Airports, docks, potential hydro + public facilities · context"
            checked={visibleLayers.contextual_facilities}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, contextual_facilities: checked }))
            }
          />
          <ContextLayerRow
            id="grid_reach"
            title="Electrical grid reach"
            subtitle={
              gridReach
                ? "735 / 315 / 161 kV skeleton + documented 34.5 kV eastern extension"
                : "Loading lightweight Côte-Nord grid context"
            }
            checked={visibleLayers.grid_reach && Boolean(gridReach)}
            disabled={!gridReach}
            status={!gridReach ? "LOAD" : undefined}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, grid_reach: checked }))
            }
          />
          <button
            type="button"
            className="layer-panel__focus-action"
            disabled={!gridReach}
            onClick={() => {
              setVisibleLayers((current) => ({ ...current, grid_reach: true }));
              setGridFocusRequest((value) => value + 1);
            }}
          >
            Focus grid reach · Côte-Nord
          </button>
          <ContextLayerRow
            id="labels"
            title="Map labels"
            subtitle="Places, water names and Observatory labels"
            checked={visibleLayers.labels}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, labels: checked }))
            }
          />

          <div className="layer-section-label">Terrain screening</div>
          <ContextLayerRow
            id="terrain_relief"
            title={localTerrain?.title ?? "Terrain relief"}
            subtitle={
              localTerrain?.available
                ? `HRDEM-derived elevation cells · ${localTerrain.cell_size_m ?? "?"} m screening grid`
                : "Local HRDEM terrain build not published yet"
            }
            checked={visibleLayers.terrain_relief && Boolean(localTerrain?.available)}
            disabled={!localTerrain?.available}
            status={!localTerrain?.available ? "LOCAL" : undefined}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, terrain_relief: checked }))
            }
          />
          <ContextLayerRow
            id="terrain_basins"
            title="Potential basin depth"
            subtitle={
              localTerrain?.available
                ? "Terrain-connected inundation depth · exploratory retention rise"
                : "Build local terrain cells to enable basin screening"
            }
            checked={visibleLayers.terrain_basins && Boolean(localTerrain?.available)}
            disabled={!localTerrain?.available}
            status={!localTerrain?.available ? "LOCAL" : undefined}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, terrain_basins: checked }))
            }
          />

          <div className="layer-section-label">Photographic context</div>
          <ContextLayerRow
            id="satellite"
            title={localImagery?.title ?? "Local satellite imagery"}
            subtitle={
              localImagery?.available
                ? `Local PMTiles snapshot · Z${localImagery.minzoom}–Z${localImagery.maxzoom}`
                : "No local PMTiles snapshot published yet"
            }
            checked={visibleLayers.satellite && Boolean(localImagery?.available)}
            disabled={!localImagery?.available}
            status={!localImagery?.available ? "LOCAL" : undefined}
            onChange={(checked) =>
              setVisibleLayers((current) => ({ ...current, satellite: checked }))
            }
          />
          <div className="layer-panel__note">
            Infrastructure + access prioritizes airport, dock and coastal hydro screening context. Electrical grid reach is a lightweight, source-backed connectivity skeleton; its lines are schematic and must not be measured or interpreted as interconnection capacity. Hydrometric stations remain available but start OFF. Terrain/basin overlays are local HRDEM-derived screening products: connected inundation cells, areas and volumes are exploratory terrain geometry only, never engineered dam or reservoir design. Hydro references remain screening references, not dam locations.
          </div>
        </section>
      )}

      <div className="coordinate-hud" aria-live="off">
        <div>
          <span>{formatCoordinate(cursor.lat, "N", "S")}</span>
          <span>{formatCoordinate(cursor.lng, "E", "W")}</span>
        </div>
        <strong>Z {zoom.toFixed(2)}</strong>
      </div>

      <div className="release-hud">
        <span>{bootstrap.rivers.length} RIVER REFERENCES</span>
        <span>{bootstrap.communities.features.length} COMMUNITIES</span>
        <span>{hydroOpportunityCount} COASTAL HYDRO REFERENCES</span>
        <span>{bootstrap.stations.features.length} HYDROMETRIC STATIONS</span>
        <span>{activeLayerCount} LAYERS ACTIVE</span>
        <strong>RELEASE {bootstrap.release}</strong>
      </div>

      <CompareTray
        features={compareFeatures}
        onRemove={addCompare}
        onSelect={selectEntity}
      />

      <EntityInspector
        entityId={selectedEntityId}
        onClose={() => selectEntity(null)}
        onAddCompare={addCompare}
        compared={Boolean(selectedEntityId && compareIds.includes(selectedEntityId))}
      />
    </main>
  );
}

function ContextLayerRow({
  id,
  title,
  subtitle,
  checked,
  disabled = false,
  status,
  onChange,
}: {
  id:
    | "contextual_hydrography"
    | "contextual_buildings"
    | "contextual_transport"
    | "contextual_facilities"
    | "grid_reach"
    | "terrain_relief"
    | "terrain_basins"
    | "satellite"
    | "labels";
  title: string;
  subtitle: string;
  checked: boolean;
  disabled?: boolean;
  status?: string;
  onChange: (checked: boolean) => void;
}) {
  return (
    <label className={`layer-row${disabled ? " is-disabled" : ""}`}>
      <input
        type="checkbox"
        checked={checked}
        disabled={disabled}
        onChange={(event) => onChange(event.target.checked)}
      />
      <span className={`layer-symbol is-${id}`} aria-hidden="true" />
      <span>
        <strong>{title}</strong>
        <small>{subtitle}</small>
      </span>
      <em>{status ?? (checked ? "ON" : "OFF")}</em>
    </label>
  );
}

function readInitialViewFromUrl(): { camera: MapCameraState; fromUrl: boolean } {
  if (typeof window === "undefined") return { camera: DEFAULT_CAMERA, fromUrl: false };

  const raw = new URLSearchParams(window.location.search).get("view");
  if (!raw) return { camera: DEFAULT_CAMERA, fromUrl: false };

  const values = raw.split(",").map(Number);
  if (values.length < 3 || values.some((value) => !Number.isFinite(value))) {
    return { camera: DEFAULT_CAMERA, fromUrl: false };
  }

  return {
    fromUrl: true,
    camera: {
      lng: values[0],
      lat: values[1],
      zoom: values[2],
      bearing: values[3] ?? 0,
      pitch: values[4] ?? 0,
    },
  };
}
