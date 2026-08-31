"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import type {
  ExplorerBootstrap,
  MapCameraState,
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

export function ObservatoryExplorer() {
  const [bootstrap, setBootstrap] = useState<ExplorerBootstrap | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedEntityId, setSelectedEntityId] = useState<string | null>(null);
  const [compareIds, setCompareIds] = useState<string[]>([]);
  const [searchOpen, setSearchOpen] = useState(false);
  const [layersOpen, setLayersOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [cursor, setCursor] = useState({ lng: DEFAULT_CAMERA.lng, lat: DEFAULT_CAMERA.lat });
  const [zoom, setZoom] = useState(DEFAULT_CAMERA.zoom);
  const [initialCamera] = useState<MapCameraState>(() => readCameraFromUrl());
  const handleCursorChange = useCallback((lng: number, lat: number) => setCursor({ lng, lat }), []);

  const [visibleLayers, setVisibleLayers] = useState({
    communities: true,
    hydrometric_stations: true,
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
    () => compareIds.map((id) => allFeatures.find((feature) => feature.properties.entity_id === id)).filter((feature): feature is PublicMapFeature => Boolean(feature)),
    [allFeatures, compareIds],
  );

  const searchResults = useMemo(() => {
    const q = searchQuery.trim().toLocaleLowerCase();
    if (!q) return allFeatures.slice(0, 8);
    return allFeatures
      .filter((feature) => {
        const p = feature.properties;
        return [p.name, p.region ?? "", p.station_number ?? "", p.river_name ?? ""]
          .join(" ")
          .toLocaleLowerCase()
          .includes(q);
      })
      .slice(0, 12);
  }, [allFeatures, searchQuery]);

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
        <strong>Initializing observatory</strong>
      </main>
    );
  }

  const activeLayerCount = Number(visibleLayers.communities) + Number(visibleLayers.hydrometric_stations);

  return (
    <main className="observatory-shell">
      <ObservatoryMap
        data={bootstrap}
        selectedEntityId={selectedEntityId}
        visibleLayers={visibleLayers}
        compareIds={compareIds}
        initialCamera={initialCamera}
        onSelect={selectEntity}
        onCursorChange={handleCursorChange}
        onZoomChange={setZoom}
        onCameraChange={handleCameraChange}
      />

      <header className="top-hud">
        <div className="brand-lockup">
          <span>KRISTAL / NORTHERN ATLAS</span>
          <strong>OBSERVATORY · EXPLORER</strong>
        </div>
        <div className="top-actions">
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
            aria-label="Search communities and hydrometric stations"
          />
          <div className="search-results">
            {searchResults.map((feature) => (
              <button
                type="button"
                key={feature.id}
                onClick={() => {
                  selectEntity(feature.properties.entity_id);
                  setSearchOpen(false);
                }}
              >
                <span className={`search-dot is-${feature.properties.feature_kind}`} aria-hidden="true" />
                <span>
                  <strong>
                    {feature.properties.feature_kind === "hydrometric_station"
                      ? feature.properties.station_number
                      : feature.properties.name}
                  </strong>
                  <small>
                    {feature.properties.feature_kind === "hydrometric_station"
                      ? feature.properties.river_name
                      : feature.properties.region}
                  </small>
                </span>
              </button>
            ))}
          </div>
        </section>
      )}

      {layersOpen && (
        <section className="floating-panel layer-panel" aria-label="Map layers">
          <div className="floating-panel__header">
            <span>LAYER CATALOG</span>
            <button type="button" onClick={() => setLayersOpen(false)} aria-label="Close layers">×</button>
          </div>
          {bootstrap.layers.map((layer) => {
            const key = layer.id as keyof typeof visibleLayers;
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
          <div className="layer-panel__note">Catalog-driven · ranking semantics disabled</div>
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
        <span>{bootstrap.communities.features.length} COMMUNITIES</span>
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

function readCameraFromUrl(): MapCameraState {
  if (typeof window === "undefined") return DEFAULT_CAMERA;
  const raw = new URLSearchParams(window.location.search).get("view");
  if (!raw) return DEFAULT_CAMERA;
  const values = raw.split(",").map(Number);
  if (values.length < 3 || values.some((value) => !Number.isFinite(value))) return DEFAULT_CAMERA;
  return {
    lng: values[0],
    lat: values[1],
    zoom: values[2],
    bearing: values[3] ?? 0,
    pitch: values[4] ?? 0,
  };
}
