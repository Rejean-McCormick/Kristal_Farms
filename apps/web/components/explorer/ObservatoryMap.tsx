"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import maplibregl, {
  type MapGeoJSONFeature,
  type MapMouseEvent,
  type Map as MapLibreMap,
} from "maplibre-gl";
import type {
  ExplorerBootstrap,
  MapCameraState,
  PublicMapFeature,
} from "../../lib/explorer-types";
import { createObservatoryStyle } from "../../lib/map-style";
import { HoverCard } from "./HoverCard";

const COMMUNITY_SOURCE = "communities";
const STATION_SOURCE = "hydrometric-stations";
const COMMUNITY_HIT = "communities-hit";
const STATION_HIT = "stations-hit";
const INTERACTIVE_LAYERS = [COMMUNITY_HIT, STATION_HIT];
const HOVER_DELAY_MS = 95;
const HOVER_EXIT_GRACE_MS = 130;

type Candidate = {
  source: string;
  id: string;
  entityId: string;
  feature: PublicMapFeature;
};

type Props = {
  data: ExplorerBootstrap;
  selectedEntityId: string | null;
  visibleLayers: { communities: boolean; hydrometric_stations: boolean };
  compareIds: string[];
  initialCamera: MapCameraState;
  onSelect: (entityId: string | null) => void;
  onCameraChange: (camera: MapCameraState) => void;
  onCursorChange: (lng: number, lat: number) => void;
  onZoomChange: (zoom: number) => void;
};

export function ObservatoryMap({
  data,
  selectedEntityId,
  visibleLayers,
  compareIds,
  initialCamera,
  onSelect,
  onCameraChange,
  onCursorChange,
  onZoomChange,
}: Props) {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<MapLibreMap | null>(null);
  const hoverTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const exitTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const proximityRef = useRef<Candidate | null>(null);
  const hoveredRef = useRef<Candidate | null>(null);
  const cardEngagedRef = useRef(false);
  const [mapReady, setMapReady] = useState(false);
  const [hovered, setHovered] = useState<Candidate | null>(null);
  const [anchor, setAnchor] = useState({ x: 0, y: 0, width: 0, height: 0 });

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
    (candidate: Candidate | null, state: "proximity" | "hovered", value: boolean) => {
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

  const clearHovered = useCallback(() => {
    clearTimer(hoverTimerRef);
    if (hoveredRef.current) setFeatureState(hoveredRef.current, "hovered", false);
    hoveredRef.current = null;
    setHovered(null);
  }, [setFeatureState]);

  const clearProximity = useCallback(() => {
    if (proximityRef.current) setFeatureState(proximityRef.current, "proximity", false);
    proximityRef.current = null;
  }, [setFeatureState]);

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
    const projected = map.project(candidate.feature.geometry.coordinates);
    setAnchor({
      x: projected.x,
      y: projected.y,
      width: container.clientWidth,
      height: container.clientHeight,
    });
  }, []);

  const engageCandidate = useCallback(
    (candidate: Candidate | null) => {
      clearTimer(exitTimerRef);

      if (!candidate) {
        scheduleExit();
        return;
      }

      const sameProximity = proximityRef.current?.entityId === candidate.entityId;
      if (!sameProximity) {
        clearHovered();
        clearProximity();
        proximityRef.current = candidate;
        setFeatureState(candidate, "proximity", true);
      }

      updateAnchor(candidate);

      if (hoveredRef.current?.entityId === candidate.entityId) return;
      clearTimer(hoverTimerRef);
      hoverTimerRef.current = setTimeout(() => {
        if (proximityRef.current?.entityId !== candidate.entityId) return;
        hoveredRef.current = candidate;
        setFeatureState(candidate, "hovered", true);
        setHovered(candidate);
        updateAnchor(candidate);
      }, HOVER_DELAY_MS);
    },
    [clearHovered, clearProximity, scheduleExit, setFeatureState, updateAnchor],
  );

  const resolveCandidate = useCallback(
    (event: MapMouseEvent): Candidate | null => {
      const map = mapRef.current;
      if (!map) return null;
      const radius = 15;
      const box: [[number, number], [number, number]] = [
        [event.point.x - radius, event.point.y - radius],
        [event.point.x + radius, event.point.y + radius],
      ];
      const rendered = map.queryRenderedFeatures(box, { layers: INTERACTIVE_LAYERS });
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
        source: best.rendered.source,
        id: String(best.rendered.id),
        entityId,
        feature,
      };
    },
    [featureByEntityId],
  );

  useEffect(() => {
    if (!containerRef.current || mapRef.current) return;

    const map = new maplibregl.Map({
      container: containerRef.current,
      style: createObservatoryStyle(),
      center: [initialCamera.lng, initialCamera.lat],
      zoom: initialCamera.zoom,
      bearing: initialCamera.bearing,
      pitch: initialCamera.pitch,
      minZoom: 2.25,
      maxZoom: 14,
      attributionControl: false,
      cooperativeGestures: false,
    });

    mapRef.current = map;
    map.addControl(new maplibregl.AttributionControl({ compact: true }), "bottom-right");

    map.on("load", () => {
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
      setMapReady(true);
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
      onSelect(candidate?.entityId ?? null);
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
  }, [data, engageCandidate, initialCamera, onCameraChange, onCursorChange, onSelect, onZoomChange, resolveCandidate, scheduleExit, updateAnchor]);

  useEffect(() => {
    const map = mapRef.current;
    if (!mapReady || !map) return;
    const visibility = (visible: boolean) => (visible ? "visible" : "none") as "visible" | "none";
    for (const layer of ["communities-halo", "communities-marker", COMMUNITY_HIT]) {
      map.setLayoutProperty(layer, "visibility", visibility(visibleLayers.communities));
    }
    for (const layer of ["stations-halo", "stations-marker", STATION_HIT]) {
      map.setLayoutProperty(layer, "visibility", visibility(visibleLayers.hydrometric_stations));
    }
  }, [mapReady, visibleLayers]);

  useEffect(() => {
    const map = mapRef.current;
    if (!mapReady || !map) return;

    for (const feature of allFeatures) {
      const source = feature.properties.feature_kind === "community" ? COMMUNITY_SOURCE : STATION_SOURCE;
      const selected = feature.properties.entity_id === selectedEntityId;
      const compared = compareIds.includes(feature.properties.entity_id);
      map.setFeatureState(
        { source, id: feature.id },
        { selected, compared, dimmed: Boolean(selectedEntityId) && !selected && !compared },
      );
    }

    if (!selectedEntityId) return;
    const selected = featureByEntityId.get(selectedEntityId);
    if (!selected) return;

    const rightPadding = typeof window !== "undefined" && window.innerWidth >= 860 ? 430 : 24;
    map.easeTo({
      center: selected.geometry.coordinates,
      duration: 520,
      padding: { top: 70, right: rightPadding, bottom: 70, left: 70 },
      essential: false,
    });
  }, [allFeatures, compareIds, featureByEntityId, mapReady, selectedEntityId]);

  const keyboardTargets = useMemo(
    () => allFeatures.filter((feature) => {
      if (feature.properties.feature_kind === "community") return visibleLayers.communities;
      return visibleLayers.hydrometric_stations;
    }),
    [allFeatures, visibleLayers],
  );

  return (
    <div className="map-stage" ref={containerRef}>
      {mapReady && (
        <AccessibleFeatureTargets
          map={mapRef.current}
          features={keyboardTargets}
          onFocus={(feature) => {
            const source = feature.properties.feature_kind === "community" ? COMMUNITY_SOURCE : STATION_SOURCE;
            const candidate: Candidate = {
              source,
              id: feature.id,
              entityId: feature.properties.entity_id,
              feature,
            };
            cardEngagedRef.current = true;
            engageCandidate(candidate);
            if (hoveredRef.current?.entityId !== candidate.entityId) {
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

      {hovered && (
        <HoverCard
          feature={hovered.feature}
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
          onSelect={() => onSelect(hovered.entityId)}
        />
      )}
    </div>
  );
}

function addCommunityLayers(map: MapLibreMap) {
  map.addLayer({
    id: "communities-halo",
    type: "circle",
    source: COMMUNITY_SOURCE,
    paint: {
      "circle-radius": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        18,
        ["boolean", ["feature-state", "hovered"], false],
        14,
        ["boolean", ["feature-state", "compared"], false],
        11,
        ["boolean", ["feature-state", "proximity"], false],
        10,
        7,
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
        0.16,
        ["boolean", ["feature-state", "hovered"], false],
        0.13,
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
        "case",
        ["boolean", ["feature-state", "selected"], false],
        5.8,
        ["boolean", ["feature-state", "hovered"], false],
        5.2,
        4.4,
      ],
      "circle-color": "#ff9f43",
      "circle-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.28,
        0.96,
      ],
      "circle-stroke-color": "#ffe0b3",
      "circle-stroke-width": 1.25,
      "circle-stroke-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.24,
        0.78,
      ],
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
    id: "stations-halo",
    type: "circle",
    source: STATION_SOURCE,
    paint: {
      "circle-radius": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        14,
        ["boolean", ["feature-state", "hovered"], false],
        11,
        ["boolean", ["feature-state", "compared"], false],
        9,
        ["boolean", ["feature-state", "proximity"], false],
        8,
        4.5,
      ],
      "circle-color": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        "#58d8ff",
        ["boolean", ["feature-state", "compared"], false],
        "#54e1c1",
        "#58d8ff",
      ],
      "circle-opacity": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        0.18,
        ["boolean", ["feature-state", "hovered"], false],
        0.13,
        ["boolean", ["feature-state", "compared"], false],
        0.11,
        ["boolean", ["feature-state", "proximity"], false],
        0.08,
        0.02,
      ],
      "circle-stroke-color": "#75ddff",
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
        "case",
        ["boolean", ["feature-state", "selected"], false],
        4.6,
        ["boolean", ["feature-state", "hovered"], false],
        3.8,
        2.7,
      ],
      "circle-color": "#5bd4ff",
      "circle-opacity": [
        "case",
        ["boolean", ["feature-state", "dimmed"], false],
        0.24,
        0.98,
      ],
      "circle-stroke-color": "#d9f8ff",
      "circle-stroke-width": 0.9,
      "circle-stroke-opacity": 0.84,
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
