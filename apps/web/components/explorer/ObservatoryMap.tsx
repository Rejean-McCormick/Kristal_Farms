"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import * as maplibregl from "maplibre-gl";
import type {
  MapGeoJSONFeature,
  MapMouseEvent,
  Map as MapLibreMap,
} from "maplibre-gl";
import type {
  ExplorerBootstrap,
  LocalImageryManifest,
  MapCameraState,
  ObservatoryVisibleLayers,
  PublicMapFeature,
  PublicRiverReference,
} from "../../lib/explorer-types";
import {
  addLocalSatelliteImagery,
  applyObservatoryBasemapTheme,
  createObservatoryStyle,
  setBasemapLabelsVisible,
  setContextualHydrographyVisible,
  setLocalSatelliteImageryVisible,
  type BasemapLayerIndex,
} from "../../lib/map-style";
import { HoverCard, type HoverTarget } from "./HoverCard";

const COMMUNITY_SOURCE = "communities";
const STATION_SOURCE = "hydrometric-stations";
const COMMUNITY_HIT = "communities-hit";
const STATION_HIT = "stations-hit";
const POINT_INTERACTIVE_LAYERS = [COMMUNITY_HIT, STATION_HIT];

const RIVER_HOVER_SOURCE = "contextual-waterway-hover-source";
const RIVER_HOVER_LAYER = "contextual-waterway-hover-layer";
const RIVER_SELECTED_SOURCE = "contextual-waterway-selected-source";
const RIVER_SELECTED_LAYER = "contextual-waterway-selected-layer";

const HOVER_DELAY_MS = 90;
const HOVER_EXIT_GRACE_MS = 135;
const CONTEXT_SOURCE_LABEL = "OpenMapTiles / OpenStreetMap context";

type PointCandidate = {
  kind: "point";
  source: string;
  id: string;
  entityId: string;
  feature: PublicMapFeature;
};

type RiverCandidate = {
  kind: "river";
  key: string;
  name: string;
  geometry: GeoJSON.Geometry;
  anchorCoordinates: [number, number];
  matchedRiver: PublicRiverReference | null;
};

type Candidate = PointCandidate | RiverCandidate;

type Props = {
  data: ExplorerBootstrap;
  selectedEntityId: string | null;
  visibleLayers: ObservatoryVisibleLayers;
  compareIds: string[];
  initialCamera: MapCameraState;
  autoFitOnLoad: boolean;
  resetViewRequest: number;
  localImagery: LocalImageryManifest | null;
  onSelect: (entityId: string | null) => void;
  onCameraChange: (camera: MapCameraState) => void;
  onCursorChange: (lng: number, lat: number) => void;
  onZoomChange: (zoom: number) => void;
};

const emptyFeatureCollection = (): GeoJSON.FeatureCollection => ({
  type: "FeatureCollection",
  features: [],
});

export function ObservatoryMap({
  data,
  selectedEntityId,
  visibleLayers,
  compareIds,
  initialCamera,
  autoFitOnLoad,
  resetViewRequest,
  localImagery,
  onSelect,
  onCameraChange,
  onCursorChange,
  onZoomChange,
}: Props) {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<MapLibreMap | null>(null);
  const basemapLayersRef = useRef<BasemapLayerIndex>({ labelLayerIds: [], waterwayLayerIds: [] });
  const visibleLayersRef = useRef(visibleLayers);
  const hoverTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const exitTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const proximityRef = useRef<Candidate | null>(null);
  const hoveredRef = useRef<Candidate | null>(null);
  const selectedContextRiverEntityRef = useRef<string | null>(null);
  const cardEngagedRef = useRef(false);
  const [mapReady, setMapReady] = useState(false);
  const [hovered, setHovered] = useState<Candidate | null>(null);
  const [anchor, setAnchor] = useState({ x: 0, y: 0, width: 0, height: 0 });

  useEffect(() => {
    visibleLayersRef.current = visibleLayers;
  }, [visibleLayers]);

  const allFeatures = useMemo(
    () => [...data.communities.features, ...data.stations.features],
    [data],
  );
  const featureByEntityId = useMemo(
    () => new Map(allFeatures.map((feature) => [feature.properties.entity_id, feature])),
    [allFeatures],
  );

  const clearTimer = (timer: typeof hoverTimerRef) => {
    if (timer.current) clearTimeout(timer.current);
    timer.current = null;
  };

  const setFeatureState = useCallback(
    (candidate: PointCandidate | null, state: "proximity" | "hovered", value: boolean) => {
      const map = mapRef.current;
      if (!map || !candidate) return;
      try {
        map.setFeatureState({ source: candidate.source, id: candidate.id }, { [state]: value });
      } catch {
        // Source may be rebuilding during teardown or a style transition.
      }
    },
    [],
  );

  const setRiverOverlay = useCallback((sourceId: string, geometry: GeoJSON.Geometry | null) => {
    const map = mapRef.current;
    if (!map) return;
    const source = map.getSource(sourceId) as maplibregl.GeoJSONSource | undefined;
    if (!source) return;
    source.setData(
      geometry
        ? ({
            type: "Feature",
            properties: {},
            geometry,
          } satisfies GeoJSON.Feature)
        : emptyFeatureCollection(),
    );
  }, []);

  const clearHovered = useCallback(() => {
    clearTimer(hoverTimerRef);
    if (hoveredRef.current?.kind === "point") {
      setFeatureState(hoveredRef.current, "hovered", false);
    }
    hoveredRef.current = null;
    setHovered(null);
  }, [setFeatureState]);

  const clearProximity = useCallback(() => {
    if (proximityRef.current?.kind === "point") {
      setFeatureState(proximityRef.current, "proximity", false);
    }
    if (proximityRef.current?.kind === "river") setRiverOverlay(RIVER_HOVER_SOURCE, null);
    proximityRef.current = null;
  }, [setFeatureState, setRiverOverlay]);

  const scheduleExit = useCallback(() => {
    clearTimer(exitTimerRef);
    exitTimerRef.current = setTimeout(() => {
      if (cardEngagedRef.current) return;
      clearHovered();
      clearProximity();
    }, HOVER_EXIT_GRACE_MS);
  }, [clearHovered, clearProximity]);

  const updateAnchor = useCallback((candidate: Candidate) => {
    const map = mapRef.current;
    const container = containerRef.current;
    if (!map || !container) return;
    const coordinates =
      candidate.kind === "point" ? candidate.feature.geometry.coordinates : candidate.anchorCoordinates;
    const projected = map.project(coordinates);
    setAnchor({
      x: projected.x,
      y: projected.y,
      width: container.clientWidth,
      height: container.clientHeight,
    });
  }, []);

  const candidateIdentity = (candidate: Candidate | null) => {
    if (!candidate) return null;
    return candidate.kind === "point" ? `point:${candidate.entityId}` : `river:${candidate.key}`;
  };

  const engageCandidate = useCallback(
    (candidate: Candidate | null) => {
      clearTimer(exitTimerRef);

      if (!candidate) {
        scheduleExit();
        return;
      }

      const sameProximity = candidateIdentity(proximityRef.current) === candidateIdentity(candidate);
      if (!sameProximity) {
        clearHovered();
        clearProximity();
        proximityRef.current = candidate;
        if (candidate.kind === "point") {
          setFeatureState(candidate, "proximity", true);
        } else {
          setRiverOverlay(RIVER_HOVER_SOURCE, candidate.geometry);
        }
      } else if (candidate.kind === "river") {
        // Rendered vector geometry can change as the cursor crosses tile boundaries.
        proximityRef.current = candidate;
        setRiverOverlay(RIVER_HOVER_SOURCE, candidate.geometry);
      }

      updateAnchor(candidate);

      if (candidateIdentity(hoveredRef.current) === candidateIdentity(candidate)) return;
      clearTimer(hoverTimerRef);
      hoverTimerRef.current = setTimeout(() => {
        if (candidateIdentity(proximityRef.current) !== candidateIdentity(candidate)) return;
        hoveredRef.current = candidate;
        if (candidate.kind === "point") setFeatureState(candidate, "hovered", true);
        setHovered(candidate);
        updateAnchor(candidate);
      }, HOVER_DELAY_MS);
    },
    [clearHovered, clearProximity, scheduleExit, setFeatureState, setRiverOverlay, updateAnchor],
  );

  const resolvePointCandidate = useCallback(
    (event: MapMouseEvent): PointCandidate | null => {
      const map = mapRef.current;
      if (!map) return null;
      const radius = 15;
      const box: [[number, number], [number, number]] = [
        [event.point.x - radius, event.point.y - radius],
        [event.point.x + radius, event.point.y + radius],
      ];
      const rendered = map.queryRenderedFeatures(box, { layers: POINT_INTERACTIVE_LAYERS });
      let best: { rendered: MapGeoJSONFeature; distance: number } | null = null;

      for (const renderedFeature of rendered) {
        if (renderedFeature.geometry.type !== "Point") continue;
        const projected = map.project(renderedFeature.geometry.coordinates as [number, number]);
        const distance = Math.hypot(projected.x - event.point.x, projected.y - event.point.y);
        if (!best || distance < best.distance) best = { rendered: renderedFeature, distance };
      }

      if (!best) return null;
      const entityId = String(best.rendered.properties?.entity_id ?? best.rendered.id ?? "");
      const feature = featureByEntityId.get(entityId);
      if (!feature || best.rendered.id === undefined) return null;

      return {
        kind: "point",
        source: best.rendered.source,
        id: String(best.rendered.id),
        entityId,
        feature,
      };
    },
    [featureByEntityId],
  );

  const resolveRiverCandidate = useCallback(
    (event: MapMouseEvent): RiverCandidate | null => {
      const map = mapRef.current;
      if (!map || !visibleLayersRef.current.contextual_hydrography) return null;
      const waterwayLayers = basemapLayersRef.current.waterwayLayerIds;
      if (!waterwayLayers.length) return null;

      const radius = 5;
      const box: [[number, number], [number, number]] = [
        [event.point.x - radius, event.point.y - radius],
        [event.point.x + radius, event.point.y + radius],
      ];
      const rendered = map.queryRenderedFeatures(box, { layers: waterwayLayers });

      for (const feature of rendered) {
        if (feature.geometry.type !== "LineString" && feature.geometry.type !== "MultiLineString") continue;
        const name = getWaterwayName(feature);
        if (!name) continue;
        const matchedRiver = matchRiverReference(name, data.rivers);
        return {
          kind: "river",
          key: matchedRiver?.entity_id ?? normalizeWaterName(name),
          name,
          geometry: feature.geometry as GeoJSON.Geometry,
          anchorCoordinates: [event.lngLat.lng, event.lngLat.lat],
          matchedRiver,
        };
      }
      return null;
    },
    [data.rivers],
  );

  const resolveCandidate = useCallback(
    (event: MapMouseEvent): Candidate | null => {
      return resolvePointCandidate(event) ?? resolveRiverCandidate(event);
    },
    [resolvePointCandidate, resolveRiverCandidate],
  );

  useEffect(() => {
    if (!containerRef.current || mapRef.current) return;

    maplibregl.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");

    const map = new maplibregl.Map({
      container: containerRef.current,
      style: createObservatoryStyle(),
      center: [initialCamera.lng, initialCamera.lat],
      zoom: initialCamera.zoom,
      bearing: initialCamera.bearing,
      pitch: initialCamera.pitch,
      minZoom: 2.25,
      maxZoom: 20,
      attributionControl: false,
      cooperativeGestures: false,
    });

    mapRef.current = map;
    map.addControl(new maplibregl.AttributionControl({ compact: true }), "bottom-right");
    map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }), "bottom-left");

    map.on("load", () => {
      basemapLayersRef.current = applyObservatoryBasemapTheme(map);

      const localSatelliteAvailable = addLocalSatelliteImagery(map, localImagery);
      if (localSatelliteAvailable) {
        setLocalSatelliteImageryVisible(map, visibleLayersRef.current.satellite);
      }

      map.addSource(RIVER_HOVER_SOURCE, { type: "geojson", data: emptyFeatureCollection() });
      map.addSource(RIVER_SELECTED_SOURCE, { type: "geojson", data: emptyFeatureCollection() });
      addContextualRiverOverlayLayers(map);

      map.addSource(COMMUNITY_SOURCE, {
        type: "geojson",
        data: data.communities as GeoJSON.FeatureCollection,
      });
      map.addSource(STATION_SOURCE, {
        type: "geojson",
        data: data.stations as GeoJSON.FeatureCollection,
      });

      addCommunityLayers(map);
      addStationLayers(map);
      setBasemapLabelsVisible(map, basemapLayersRef.current.labelLayerIds, visibleLayersRef.current.labels);
      setContextualHydrographyVisible(
        map,
        basemapLayersRef.current.waterwayLayerIds,
        visibleLayersRef.current.contextual_hydrography,
      );
      setMapReady(true);

      if (autoFitOnLoad) {
        window.requestAnimationFrame(() => fitToObservatoryExtent(map, data, false, 0));
      }
    });

    map.on("mousemove", (event) => {
      onCursorChange(event.lngLat.lng, event.lngLat.lat);
      const candidate = resolveCandidate(event);
      map.getCanvas().style.cursor = candidate ? "crosshair" : "default";
      engageCandidate(candidate);
    });

    map.on("mouseout", () => {
      map.getCanvas().style.cursor = "default";
      scheduleExit();
    });

    map.on("click", (event) => {
      const candidate = resolveCandidate(event);
      if (candidate?.kind === "point") {
        selectedContextRiverEntityRef.current = null;
        setRiverOverlay(RIVER_SELECTED_SOURCE, null);
        onSelect(candidate.entityId);
        return;
      }
      if (candidate?.kind === "river" && candidate.matchedRiver) {
        selectedContextRiverEntityRef.current = candidate.matchedRiver.entity_id;
        setRiverOverlay(RIVER_SELECTED_SOURCE, candidate.geometry);
        onSelect(candidate.matchedRiver.entity_id);
        return;
      }
      selectedContextRiverEntityRef.current = null;
      setRiverOverlay(RIVER_SELECTED_SOURCE, null);
      onSelect(null);
    });

    map.on("move", () => {
      if (hoveredRef.current) updateAnchor(hoveredRef.current);
      onZoomChange(map.getZoom());
    });

    map.on("moveend", () => {
      const center = map.getCenter();
      onCameraChange({
        lng: center.lng,
        lat: center.lat,
        zoom: map.getZoom(),
        bearing: map.getBearing(),
        pitch: map.getPitch(),
      });
    });

    return () => {
      clearTimer(hoverTimerRef);
      clearTimer(exitTimerRef);
      map.remove();
      mapRef.current = null;
    };
  }, [
    autoFitOnLoad,
    data,
    engageCandidate,
    initialCamera,
    onCameraChange,
    onCursorChange,
    onSelect,
    onZoomChange,
    resolveCandidate,
    scheduleExit,
    setRiverOverlay,
    updateAnchor,
  ]);

  useEffect(() => {
    const map = mapRef.current;
    if (!mapReady || !map || !localImagery?.available) return;

    const available = addLocalSatelliteImagery(map, localImagery);
    if (available) {
      setLocalSatelliteImageryVisible(map, visibleLayers.satellite);
    }
  }, [localImagery, mapReady, visibleLayers.satellite]);

  useEffect(() => {
    const map = mapRef.current;
    if (!mapReady || !map) return;
    const visibility = (visible: boolean) => (visible ? "visible" : "none") as "visible" | "none";

    for (const layer of [
      "communities-focus",
      "communities-halo",
      "communities-marker",
      COMMUNITY_HIT,
    ]) {
      map.setLayoutProperty(layer, "visibility", visibility(visibleLayers.communities));
    }
    for (const layer of ["stations-focus", "stations-halo", "stations-marker", STATION_HIT]) {
      map.setLayoutProperty(layer, "visibility", visibility(visibleLayers.hydrometric_stations));
    }
    map.setLayoutProperty(
      "communities-label",
      "visibility",
      visibility(visibleLayers.communities && visibleLayers.labels),
    );
    map.setLayoutProperty(
      "stations-label",
      "visibility",
      visibility(visibleLayers.hydrometric_stations && visibleLayers.labels),
    );

    setLocalSatelliteImageryVisible(map, visibleLayers.satellite);
    setBasemapLabelsVisible(map, basemapLayersRef.current.labelLayerIds, visibleLayers.labels);
    setContextualHydrographyVisible(
      map,
      basemapLayersRef.current.waterwayLayerIds,
      visibleLayers.contextual_hydrography,
    );
    map.setLayoutProperty(
      RIVER_HOVER_LAYER,
      "visibility",
      visibility(visibleLayers.contextual_hydrography),
    );
    map.setLayoutProperty(
      RIVER_SELECTED_LAYER,
      "visibility",
      visibility(visibleLayers.contextual_hydrography),
    );

    if (!visibleLayers.contextual_hydrography) {
      clearHovered();
      clearProximity();
    }
  }, [mapReady, visibleLayers, clearHovered, clearProximity]);

  useEffect(() => {
    const map = mapRef.current;
    if (!mapReady || !map || resetViewRequest <= 0) return;
    fitToObservatoryExtent(map, data, Boolean(selectedEntityId), 520);
  }, [data, mapReady, resetViewRequest]);

  useEffect(() => {
    const map = mapRef.current;
    if (!mapReady || !map) return;

    const selectedRiver = data.rivers.find((river) => river.entity_id === selectedEntityId) ?? null;

    for (const feature of allFeatures) {
      const source =
        feature.properties.feature_kind === "community" ? COMMUNITY_SOURCE : STATION_SOURCE;
      const selected = feature.properties.entity_id === selectedEntityId;
      const compared = compareIds.includes(feature.properties.entity_id);
      const related = Boolean(
        selectedRiver && feature.properties.river_entity_id === selectedRiver.entity_id,
      );
      map.setFeatureState(
        { source, id: feature.id },
        {
          selected,
          compared,
          related,
          dimmed: Boolean(selectedEntityId) && !selected && !compared && !related,
        },
      );
    }

    if (selectedContextRiverEntityRef.current !== selectedEntityId) {
      selectedContextRiverEntityRef.current = null;
      setRiverOverlay(RIVER_SELECTED_SOURCE, null);
    }

    if (!selectedEntityId) return;
    const selectedFeature = featureByEntityId.get(selectedEntityId);
    const targetCoordinates = selectedFeature?.geometry.coordinates ?? selectedRiver?.anchor?.coordinates;
    if (!targetCoordinates) return;

    const rightPadding = typeof window !== "undefined" && window.innerWidth >= 860 ? 450 : 24;
    const targetZoom = selectedRiver
      ? 5.3
      : selectedFeature?.properties.feature_kind === "hydrometric_station"
        ? 6.35
        : 5.7;
    map.easeTo({
      center: targetCoordinates,
      zoom: Math.max(map.getZoom(), targetZoom),
      duration: 560,
      padding: { top: 70, right: rightPadding, bottom: 70, left: 70 },
      essential: false,
    });
  }, [
    allFeatures,
    compareIds,
    data.rivers,
    featureByEntityId,
    mapReady,
    selectedEntityId,
    setRiverOverlay,
  ]);

  const keyboardTargets = useMemo(
    () =>
      allFeatures.filter((feature) => {
        if (feature.properties.feature_kind === "community") return visibleLayers.communities;
        return visibleLayers.hydrometric_stations;
      }),
    [allFeatures, visibleLayers],
  );

  const hoverTarget: HoverTarget | null = hovered
    ? hovered.kind === "point"
      ? { kind: "point", feature: hovered.feature }
      : {
          kind: "contextual_river",
          name: hovered.name,
          matchedRiver: hovered.matchedRiver,
          contextSource: CONTEXT_SOURCE_LABEL,
        }
    : null;

  return (
    <div className="map-stage" ref={containerRef}>
      {mapReady && (
        <AccessibleFeatureTargets
          map={mapRef.current}
          features={keyboardTargets}
          onFocus={(feature) => {
            const source =
              feature.properties.feature_kind === "community" ? COMMUNITY_SOURCE : STATION_SOURCE;
            const candidate: PointCandidate = {
              kind: "point",
              source,
              id: feature.id,
              entityId: feature.properties.entity_id,
              feature,
            };
            cardEngagedRef.current = true;
            engageCandidate(candidate);
            if (candidateIdentity(hoveredRef.current) !== candidateIdentity(candidate)) {
              clearTimer(hoverTimerRef);
              hoveredRef.current = candidate;
              setFeatureState(candidate, "hovered", true);
              setHovered(candidate);
              updateAnchor(candidate);
            }
          }}
          onBlur={() => {
            cardEngagedRef.current = false;
            scheduleExit();
          }}
          onSelect={(feature) => onSelect(feature.properties.entity_id)}
        />
      )}

      {hovered && hoverTarget && (
        <HoverCard
          target={hoverTarget}
          x={anchor.x}
          y={anchor.y}
          viewportWidth={anchor.width}
          viewportHeight={anchor.height}
          onPointerEnter={() => {
            cardEngagedRef.current = true;
            clearTimer(exitTimerRef);
          }}
          onPointerLeave={() => {
            cardEngagedRef.current = false;
            scheduleExit();
          }}
          onSelect={
            hovered.kind === "point"
              ? () => onSelect(hovered.entityId)
              : hovered.matchedRiver
                ? () => {
                    selectedContextRiverEntityRef.current = hovered.matchedRiver!.entity_id;
                    setRiverOverlay(RIVER_SELECTED_SOURCE, hovered.geometry);
                    onSelect(hovered.matchedRiver!.entity_id);
                  }
                : undefined
          }
        />
      )}
    </div>
  );
}

function fitToObservatoryExtent(
  map: MapLibreMap,
  data: ExplorerBootstrap,
  inspectorOpen: boolean,
  duration: number,
) {
  const coordinates = [
    ...data.communities.features.map((feature) => feature.geometry.coordinates),
    ...data.stations.features.map((feature) => feature.geometry.coordinates),
  ];

  if (!coordinates.length) return;

  const bounds = coordinates.reduce(
    (current, coordinate) => current.extend(coordinate),
    new maplibregl.LngLatBounds(coordinates[0], coordinates[0]),
  );

  const wide = typeof window !== "undefined" && window.innerWidth >= 860;

  map.fitBounds(bounds, {
    padding: {
      top: wide ? 96 : 72,
      right: wide && inspectorOpen ? 500 : wide ? 110 : 48,
      bottom: wide ? 88 : 72,
      left: wide ? 110 : 48,
    },
    maxZoom: 5.6,
    duration,
    essential: false,
  });
}

function addContextualRiverOverlayLayers(map: MapLibreMap) {
  map.addLayer({
    id: RIVER_SELECTED_LAYER,
    type: "line",
    source: RIVER_SELECTED_SOURCE,
    paint: {
      "line-color": "#59dcff",
      "line-opacity": 0.92,
      "line-width": ["interpolate", ["linear"], ["zoom"], 3, 2.2, 7, 4.4, 12, 7.2],
      "line-blur": 0.6,
    },
  });

  map.addLayer({
    id: RIVER_HOVER_LAYER,
    type: "line",
    source: RIVER_HOVER_SOURCE,
    paint: {
      "line-color": "#74e4ff",
      "line-opacity": 0.9,
      "line-width": ["interpolate", ["linear"], ["zoom"], 3, 1.8, 7, 3.6, 12, 6],
      "line-blur": 0.35,
    },
  });
}

function addCommunityLayers(map: MapLibreMap) {
  map.addLayer({
    id: "communities-focus",
    type: "circle",
    source: COMMUNITY_SOURCE,
    paint: {
      "circle-radius": ["case", ["boolean", ["feature-state", "selected"], false], 22, 0],
      "circle-color": "rgba(0,0,0,0)",
      "circle-stroke-color": "#ffc27b",
      "circle-stroke-width": ["case", ["boolean", ["feature-state", "selected"], false], 1.2, 0],
      "circle-stroke-opacity": ["case", ["boolean", ["feature-state", "selected"], false], 0.72, 0],
    },
  });

  map.addLayer({
    id: "communities-halo",
    type: "circle",
    source: COMMUNITY_SOURCE,
    paint: {
      "circle-radius": [
        "interpolate",
        ["linear"],
        ["zoom"],
        3,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          18,
          ["boolean", ["feature-state", "hovered"], false],
          14,
          ["boolean", ["feature-state", "compared"], false],
          11,
          ["boolean", ["feature-state", "proximity"], false],
          10,
          5.5,
        ],
        7,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          18,
          ["boolean", ["feature-state", "hovered"], false],
          14,
          ["boolean", ["feature-state", "compared"], false],
          11,
          ["boolean", ["feature-state", "proximity"], false],
          10,
          8.5,
        ],
        11,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          18,
          ["boolean", ["feature-state", "hovered"], false],
          14,
          ["boolean", ["feature-state", "compared"], false],
          11,
          ["boolean", ["feature-state", "proximity"], false],
          10,
          11,
        ],
      ],
      "circle-color": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        "#ffaf55",
        ["boolean", ["feature-state", "compared"], false],
        "#54e1c1",
        "#ffaf55",
      ],
      "circle-opacity": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        0.18,
        ["boolean", ["feature-state", "hovered"], false],
        0.14,
        ["boolean", ["feature-state", "compared"], false],
        0.11,
        ["boolean", ["feature-state", "proximity"], false],
        0.08,
        0.025,
      ],
      "circle-stroke-color": "#ffbd70",
      "circle-stroke-width": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        1.4,
        ["boolean", ["feature-state", "hovered"], false],
        1.1,
        0.65,
      ],
      "circle-stroke-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.18,
        0.6,
      ],
      "circle-blur": 0.45,
    },
  });

  map.addLayer({
    id: "communities-marker",
    type: "circle",
    source: COMMUNITY_SOURCE,
    paint: {
      "circle-radius": [
        "interpolate",
        ["linear"],
        ["zoom"],
        3,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          6.1,
          ["boolean", ["feature-state", "hovered"], false],
          5.4,
          3.7,
        ],
        7,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          6.1,
          ["boolean", ["feature-state", "hovered"], false],
          5.4,
          4.8,
        ],
        11,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          6.1,
          ["boolean", ["feature-state", "hovered"], false],
          5.4,
          6.2,
        ],
      ],
      "circle-color": "#ff9f43",
      "circle-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.26,
        0.96,
      ],
      "circle-stroke-color": "#ffe0b3",
      "circle-stroke-width": 1.15,
      "circle-stroke-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.22,
        0.78,
      ],
    },
  });

  map.addLayer({
    id: "communities-label",
    type: "symbol",
    source: COMMUNITY_SOURCE,
    minzoom: 4.2,
    layout: {
      "text-field": ["get", "name"],
      "text-size": ["interpolate", ["linear"], ["zoom"], 4.2, 9, 8, 11, 12, 13],
      "text-offset": [0, 1.15],
      "text-anchor": "top",
      "text-allow-overlap": false,
      "text-padding": 4,
    },
    paint: {
      "text-color": "#e4b67f",
      "text-halo-color": "rgba(4,10,15,.92)",
      "text-halo-width": 1.2,
      "text-opacity": ["case", ["boolean", ["feature-state", "dimmed"], false], 0.25, 0.82],
    },
  });

  map.addLayer({
    id: COMMUNITY_HIT,
    type: "circle",
    source: COMMUNITY_SOURCE,
    paint: {
      "circle-radius": 18,
      "circle-color": "#ffffff",
      "circle-opacity": 0.001,
    },
  });
}

function addStationLayers(map: MapLibreMap) {
  map.addLayer({
    id: "stations-focus",
    type: "circle",
    source: STATION_SOURCE,
    paint: {
      "circle-radius": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        20,
        ["boolean", ["feature-state", "related"], false],
        15,
        0,
      ],
      "circle-color": "rgba(0,0,0,0)",
      "circle-stroke-color": [
        "case",
        ["boolean", ["feature-state", "related"], false],
        "#54e1c1",
        "#75ddff",
      ],
      "circle-stroke-width": [
        "case",
        ["any", ["boolean", ["feature-state", "selected"], false], ["boolean", ["feature-state", "related"], false]],
        1.15,
        0,
      ],
      "circle-stroke-opacity": [
        "case",
        ["any", ["boolean", ["feature-state", "selected"], false], ["boolean", ["feature-state", "related"], false]],
        0.78,
        0,
      ],
    },
  });

  map.addLayer({
    id: "stations-halo",
    type: "circle",
    source: STATION_SOURCE,
    paint: {
      "circle-radius": [
        "interpolate",
        ["linear"],
        ["zoom"],
        3,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          14,
          ["boolean", ["feature-state", "related"], false],
          12,
          ["boolean", ["feature-state", "hovered"], false],
          11,
          ["boolean", ["feature-state", "compared"], false],
          9,
          ["boolean", ["feature-state", "proximity"], false],
          8,
          3.5,
        ],
        7,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          14,
          ["boolean", ["feature-state", "related"], false],
          12,
          ["boolean", ["feature-state", "hovered"], false],
          11,
          ["boolean", ["feature-state", "compared"], false],
          9,
          ["boolean", ["feature-state", "proximity"], false],
          8,
          5.5,
        ],
        11,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          14,
          ["boolean", ["feature-state", "related"], false],
          12,
          ["boolean", ["feature-state", "hovered"], false],
          11,
          ["boolean", ["feature-state", "compared"], false],
          9,
          ["boolean", ["feature-state", "proximity"], false],
          8,
          8,
        ],
      ],
      "circle-color": [
        "case",
        ["boolean", ["feature-state", "related"], false],
        "#54e1c1",
        ["boolean", ["feature-state", "compared"], false],
        "#54e1c1",
        "#58d8ff",
      ],
      "circle-opacity": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        0.19,
        ["boolean", ["feature-state", "related"], false],
        0.16,
        ["boolean", ["feature-state", "hovered"], false],
        0.13,
        ["boolean", ["feature-state", "compared"], false],
        0.11,
        ["boolean", ["feature-state", "proximity"], false],
        0.08,
        0.02,
      ],
      "circle-stroke-color": [
        "case",
        ["boolean", ["feature-state", "related"], false],
        "#79f0d6",
        "#75ddff",
      ],
      "circle-stroke-width": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        1.2,
        ["boolean", ["feature-state", "hovered"], false],
        0.9,
        0.45,
      ],
      "circle-stroke-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.16,
        0.52,
      ],
      "circle-blur": 0.5,
    },
  });

  map.addLayer({
    id: "stations-marker",
    type: "circle",
    source: STATION_SOURCE,
    paint: {
      "circle-radius": [
        "interpolate",
        ["linear"],
        ["zoom"],
        3,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          4.9,
          ["boolean", ["feature-state", "related"], false],
          4.2,
          ["boolean", ["feature-state", "hovered"], false],
          3.8,
          2.2,
        ],
        7,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          4.9,
          ["boolean", ["feature-state", "related"], false],
          4.2,
          ["boolean", ["feature-state", "hovered"], false],
          3.8,
          3,
        ],
        11,
        [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          4.9,
          ["boolean", ["feature-state", "related"], false],
          4.2,
          ["boolean", ["feature-state", "hovered"], false],
          3.8,
          4.2,
        ],
      ],
      "circle-color": [
        "case",
        ["boolean", ["feature-state", "related"], false],
        "#54e1c1",
        "#5bd4ff",
      ],
      "circle-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.22,
        0.98,
      ],
      "circle-stroke-color": "#d9f8ff",
      "circle-stroke-width": 0.9,
      "circle-stroke-opacity": 0.84,
    },
  });

  map.addLayer({
    id: "stations-label",
    type: "symbol",
    source: STATION_SOURCE,
    minzoom: 6.1,
    layout: {
      "text-field": ["get", "station_number"],
      "text-size": ["interpolate", ["linear"], ["zoom"], 6.1, 8, 10, 10.5, 13, 12],
      "text-offset": [0, 1],
      "text-anchor": "top",
      "text-allow-overlap": false,
      "text-padding": 4,
    },
    paint: {
      "text-color": "#7bcce2",
      "text-halo-color": "rgba(4,10,15,.92)",
      "text-halo-width": 1.1,
      "text-opacity": ["case", ["boolean", ["feature-state", "dimmed"], false], 0.2, 0.78],
    },
  });

  map.addLayer({
    id: STATION_HIT,
    type: "circle",
    source: STATION_SOURCE,
    paint: {
      "circle-radius": 16,
      "circle-color": "#ffffff",
      "circle-opacity": 0.001,
    },
  });
}

function getWaterwayName(feature: MapGeoJSONFeature): string | null {
  const p = feature.properties ?? {};
  const candidates = [p["name:en"], p["name:fr"], p.name, p["name_int"]];
  for (const value of candidates) {
    if (typeof value === "string" && value.trim()) return value.trim();
  }
  return null;
}

function normalizeWaterName(value: string): string {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/\b(river|riviere|rivière|riv|stream|brook|ruisseau|fleuve)\b/g, " ")
    .replace(/\b(the|de|du|des|la|le|les|d)\b/g, " ")
    .replace(/[^a-z0-9]+/g, "")
    .trim();
}

function matchRiverReference(
  mapName: string,
  rivers: PublicRiverReference[],
): PublicRiverReference | null {
  const normalized = normalizeWaterName(mapName);
  if (normalized.length < 4) return null;

  for (const river of rivers) {
    for (const alias of river.aliases) {
      const candidate = normalizeWaterName(alias);
      if (!candidate) continue;
      if (candidate === normalized) return river;
      if (candidate.length >= 6 && normalized.length >= 6) {
        if (candidate.includes(normalized) || normalized.includes(candidate)) return river;
      }
    }
  }
  return null;
}

function AccessibleFeatureTargets({
  map,
  features,
  onFocus,
  onBlur,
  onSelect,
}: {
  map: MapLibreMap | null;
  features: PublicMapFeature[];
  onFocus: (feature: PublicMapFeature) => void;
  onBlur: () => void;
  onSelect: (feature: PublicMapFeature) => void;
}) {
  const [, forceRender] = useState(0);

  useEffect(() => {
    if (!map) return;
    const render = () => forceRender((value) => value + 1);
    map.on("move", render);
    map.on("resize", render);
    return () => {
      map.off("move", render);
      map.off("resize", render);
    };
  }, [map]);

  if (!map) return null;

  return (
    <div className="accessible-map-targets" aria-label="Interactive map features">
      {features.map((feature) => {
        const point = map.project(feature.geometry.coordinates);
        const label =
          feature.properties.feature_kind === "community"
            ? `${feature.properties.name}, community`
            : `${feature.properties.station_number ?? feature.properties.name}, hydrometric station`;
        return (
          <button
            key={feature.id}
            type="button"
            className="accessible-map-target"
            style={{ left: point.x, top: point.y }}
            aria-label={`${label}. Focus for summary, press Enter to inspect.`}
            onFocus={() => onFocus(feature)}
            onBlur={onBlur}
            onClick={() => onSelect(feature)}
          />
        );
      })}
    </div>
  );
}
