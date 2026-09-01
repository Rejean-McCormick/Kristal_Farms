"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { createPortal } from "react-dom";
import * as maplibregl from "maplibre-gl";
import type {
  MapGeoJSONFeature,
  MapMouseEvent,
  Map as MapLibreMap,
} from "maplibre-gl";
import type {
  CommunityInfrastructureSummary,
  ContextInfrastructure,
  ExplorerBootstrap,
  LocalImageryManifest,
  LocalTerrainManifest,
  MapCameraState,
  ObservatoryVisibleLayers,
  PublicHydroScreeningSite,
  PublicCommunityInfrastructure,
  PublicMapFeature,
  PublicRiverReference,
} from "../../lib/explorer-types";
import { createPublishedCommunityFacilityProxy } from "../../lib/context-atlas";
import {
  addLocalSatelliteImagery,
  addLocalTerrainScreening,
  applyObservatoryBasemapTheme,
  createObservatoryStyle,
  setBasemapLabelsVisible,
  setBasemapLayerGroupVisible,
  setContextualHydrographyVisible,
  setLocalSatelliteImageryVisible,
  setLocalTerrainBasinState,
  setLocalTerrainBasinsVisible,
  setLocalTerrainReliefVisible,
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
const POTENTIAL_HYDRO_MAX_MARKERS = 80;

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

type InfrastructureCandidate = {
  kind: "infrastructure";
  infrastructure: ContextInfrastructure;
};

type Candidate = PointCandidate | RiverCandidate | InfrastructureCandidate;

type Props = {
  data: ExplorerBootstrap;
  selectedEntityId: string | null;
  visibleLayers: ObservatoryVisibleLayers;
  compareIds: string[];
  initialCamera: MapCameraState;
  autoFitOnLoad: boolean;
  resetViewRequest: number;
  localImagery: LocalImageryManifest | null;
  localTerrain: LocalTerrainManifest | null;
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
  localTerrain,
  onSelect,
  onCameraChange,
  onCursorChange,
  onZoomChange,
}: Props) {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<MapLibreMap | null>(null);
  const basemapLayersRef = useRef<BasemapLayerIndex>({
    labelLayerIds: [],
    hydrographyLayerIds: [],
    waterwayLayerIds: [],
    buildingLayerIds: [],
    transportLayerIds: [],
    facilityLayerIds: [],
  });
  const visibleLayersRef = useRef(visibleLayers);
  const hoverTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const exitTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const proximityRef = useRef<Candidate | null>(null);
  const hoveredRef = useRef<Candidate | null>(null);
  const selectedContextRiverEntityRef = useRef<string | null>(null);
  const cardEngagedRef = useRef(false);
  const infrastructureMarkersRef = useRef<maplibregl.Marker[]>([]);
  const communityMarkersRef = useRef<maplibregl.Marker[]>([]);
  const infrastructureRef = useRef<ContextInfrastructure[]>([]);
  const communityInfrastructureRef = useRef<Map<string, CommunityInfrastructureSummary>>(new Map());
  const [infrastructureRevision, setInfrastructureRevision] = useState(0);
  const [mapReady, setMapReady] = useState(false);
  const [hovered, setHovered] = useState<Candidate | null>(null);
  const [anchor, setAnchor] = useState({ x: 0, y: 0, width: 0, height: 0 });
  const [activeBasinSiteId, setActiveBasinSiteId] = useState<string | null>(null);
  const [basinRiseM, setBasinRiseM] = useState(50);

  useEffect(() => {
    visibleLayersRef.current = visibleLayers;
  }, [visibleLayers]);

  const terrainProfiles = localTerrain?.site_profiles ?? [];
  const activeTerrainProfile =
    terrainProfiles.find((profile) => profile.site_id === activeBasinSiteId) ?? terrainProfiles[0] ?? null;
  const activeRiseSummary = activeTerrainProfile?.rise_summaries.find(
    (summary) => summary.rise_m === basinRiseM,
  ) ?? null;

  useEffect(() => {
    if (!localTerrain?.available || terrainProfiles.length === 0) {
      setActiveBasinSiteId(null);
      return;
    }
    if (!activeBasinSiteId || !terrainProfiles.some((profile) => profile.site_id === activeBasinSiteId)) {
      setActiveBasinSiteId(terrainProfiles[0].site_id);
    }
  }, [activeBasinSiteId, localTerrain?.available, terrainProfiles]);

  useEffect(() => {
    if (!activeTerrainProfile) return;
    setBasinRiseM(activeTerrainProfile.default_rise_m);
  }, [activeTerrainProfile?.site_id]);

  const allFeatures = useMemo(
    () => [...data.communities.features, ...data.stations.features],
    [data],
  );
  const featureByEntityId = useMemo(
    () => new Map(allFeatures.map((feature) => [feature.properties.entity_id, feature])),
    [allFeatures],
  );
  const publishedInfrastructureByEntityId = useMemo(
    () => new Map(data.communityInfrastructure.map((item) => [item.entity_id, item])),
    [data.communityInfrastructure],
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
      candidate.kind === "point"
        ? candidate.feature.geometry.coordinates
        : candidate.kind === "river"
          ? candidate.anchorCoordinates
          : candidate.infrastructure.coordinates;
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
    return candidate.kind === "point"
      ? `point:${candidate.entityId}`
      : candidate.kind === "river"
        ? `river:${candidate.key}`
        : `infrastructure:${candidate.infrastructure.key}`;
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
        } else if (candidate.kind === "river") {
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
      // Mouse events can fire while the style is still loading or while a
      // style/layer transition is in progress. MapLibre throws if even one
      // requested layer id is currently absent.
      const queryLayers = POINT_INTERACTIVE_LAYERS.filter((layerId) => Boolean(map.getLayer(layerId)));
      if (!queryLayers.length) return null;

      const rendered = map.queryRenderedFeatures(box, { layers: queryLayers });
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
      const waterwayLayers = basemapLayersRef.current.waterwayLayerIds.filter(
        (layerId) => Boolean(map.getLayer(layerId)),
      );
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

  const refreshInfrastructureContext = useCallback(() => {
    const map = mapRef.current;
    if (!map || !map.isStyleLoaded()) return;

    const snapshot = collectInfrastructureSnapshot(
      map,
      data.communities.features,
      publishedInfrastructureByEntityId,
    );
    const hydroSites = buildPotentialHydroInfrastructure(data.hydroSites, data.communities.features, snapshot.communities);

    infrastructureRef.current = hydroSites;
    communityInfrastructureRef.current = snapshot.communities;

    for (const marker of infrastructureMarkersRef.current) marker.remove();
    for (const marker of communityMarkersRef.current) marker.remove();
    infrastructureMarkersRef.current = [];
    communityMarkersRef.current = [];

    for (const feature of data.communities.features) {
      const summary = snapshot.communities.get(feature.properties.entity_id);
      const showAirport = Boolean(summary?.airport);
      const showDock = Boolean(summary?.dock || summary?.hasPublishedMarineContext);
      const placement = getCommunityCalloutPlacement(feature);
      const { element, badges } = createCommunityMapMarkerElement(
        feature.properties.name,
        showAirport,
        showDock,
        placement,
      );

      const candidate: PointCandidate = {
        kind: "point",
        source: COMMUNITY_SOURCE,
        id: feature.id,
        entityId: feature.properties.entity_id,
        feature,
      };
      if (badges) {
        badges.addEventListener("pointerenter", () => engageCandidate(candidate));
        badges.addEventListener("pointerleave", scheduleExit);
        badges.addEventListener("click", (event) => {
          event.stopPropagation();
          onSelect(feature.properties.entity_id);
        });
      }

      const marker = new maplibregl.Marker({ element, anchor: "center" })
        .setLngLat(feature.geometry.coordinates)
        .addTo(map);
      communityMarkersRef.current.push(marker);
    }
    updateCommunityMarkerVisibility(
      communityMarkersRef.current,
      visibleLayersRef.current,
      map.getZoom(),
    );

    const mapBounds = map.getBounds();
    const visibleHydroSites = hydroSites
      .filter((item) => item.kind === "potential_hydro")
      .filter((item) => mapBounds.contains(item.coordinates))
      .slice(0, POTENTIAL_HYDRO_MAX_MARKERS);

    for (const infrastructure of visibleHydroSites) {
      const element = createInfrastructureMarkerElement(infrastructure);
      element.style.display = visibleLayersRef.current.contextual_facilities ? "grid" : "none";
      const candidate: InfrastructureCandidate = { kind: "infrastructure", infrastructure };
      element.addEventListener("pointerenter", () => engageCandidate(candidate));
      element.addEventListener("pointerleave", scheduleExit);
      element.dataset.siteId = infrastructure.key;
      element.addEventListener("click", (event) => {
        event.stopPropagation();
        if (infrastructure.kind === "potential_hydro") setActiveBasinSiteId(infrastructure.key);
      });

      const marker = new maplibregl.Marker({ element, anchor: "center" })
        .setLngLat(infrastructure.coordinates)
        .addTo(map);
      infrastructureMarkersRef.current.push(marker);
    }

    setInfrastructureRevision((value) => value + 1);
  }, [
    data.communities.features,
    data.hydroSites,
    engageCandidate,
    onSelect,
    publishedInfrastructureByEntityId,
    scheduleExit,
  ]);

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

      const localTerrainAvailable = addLocalTerrainScreening(map, localTerrain);
      if (localTerrainAvailable) {
        setLocalTerrainReliefVisible(map, visibleLayersRef.current.terrain_relief);
        setLocalTerrainBasinsVisible(map, visibleLayersRef.current.terrain_basins);
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
      // DOM community labels are intentionally above all infrastructure markers.
      setLayerVisibilitySafe(map, "communities-label", false);
      addStationLayers(map);
      setBasemapLabelsVisible(map, basemapLayersRef.current.labelLayerIds, visibleLayersRef.current.labels);
      setContextualHydrographyVisible(
        map,
        basemapLayersRef.current.hydrographyLayerIds,
        visibleLayersRef.current.contextual_hydrography,
      );
      setBasemapLayerGroupVisible(
        map,
        basemapLayersRef.current.buildingLayerIds,
        visibleLayersRef.current.contextual_buildings,
      );
      setBasemapLayerGroupVisible(
        map,
        basemapLayersRef.current.transportLayerIds,
        visibleLayersRef.current.contextual_transport,
      );
      setBasemapLayerGroupVisible(
        map,
        basemapLayersRef.current.facilityLayerIds,
        visibleLayersRef.current.contextual_facilities,
      );
      setMapReady(true);
      window.requestAnimationFrame(() => refreshInfrastructureContext());
      map.once("idle", refreshInfrastructureContext);

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
      if (candidate?.kind === "infrastructure") return;
      selectedContextRiverEntityRef.current = null;
      setRiverOverlay(RIVER_SELECTED_SOURCE, null);
      onSelect(null);
    });

    map.on("move", () => {
      if (hoveredRef.current) updateAnchor(hoveredRef.current);
      const zoom = map.getZoom();
      updateCommunityMarkerVisibility(communityMarkersRef.current, visibleLayersRef.current, zoom);
      onZoomChange(zoom);
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
      refreshInfrastructureContext();
    });

    return () => {
      clearTimer(hoverTimerRef);
      clearTimer(exitTimerRef);
      for (const marker of infrastructureMarkersRef.current) marker.remove();
      for (const marker of communityMarkersRef.current) marker.remove();
      infrastructureMarkersRef.current = [];
      communityMarkersRef.current = [];
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
    refreshInfrastructureContext,
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
    if (!mapReady || !map || !localTerrain?.available) return;

    const available = addLocalTerrainScreening(map, localTerrain);
    if (available) {
      setLocalTerrainReliefVisible(map, visibleLayers.terrain_relief);
      setLocalTerrainBasinsVisible(map, visibleLayers.terrain_basins);
      setLocalTerrainBasinState(map, activeTerrainProfile?.site_id ?? null, basinRiseM);
    }
  }, [
    activeTerrainProfile?.site_id,
    basinRiseM,
    localTerrain,
    mapReady,
    visibleLayers.terrain_basins,
    visibleLayers.terrain_relief,
  ]);

  useEffect(() => {
    const map = mapRef.current;
    if (!mapReady || !map) return;
     for (const layer of [
      "communities-focus",
      "communities-halo",
      "communities-marker",
      COMMUNITY_HIT,
    ]) {
      setLayerVisibilitySafe(map, layer, visibleLayers.communities);
    }
    for (const layer of ["stations-focus", "stations-halo", "stations-marker", STATION_HIT]) {
      setLayerVisibilitySafe(map, layer, visibleLayers.hydrometric_stations);
    }
    // Community labels are rendered as DOM markers above infrastructure icons so
    // a nearby village name can never be obscured by another village's badges.
    setLayerVisibilitySafe(map, "communities-label", false);
    updateCommunityMarkerVisibility(
      communityMarkersRef.current,
      visibleLayers,
      map.getZoom(),
    );
    setLayerVisibilitySafe(
      map,
      "stations-label",
      visibleLayers.hydrometric_stations && visibleLayers.labels,
    );

    setLocalSatelliteImageryVisible(map, visibleLayers.satellite);
    setLocalTerrainReliefVisible(map, visibleLayers.terrain_relief);
    setLocalTerrainBasinsVisible(map, visibleLayers.terrain_basins);
    setLocalTerrainBasinState(map, activeTerrainProfile?.site_id ?? null, basinRiseM);
    setBasemapLabelsVisible(map, basemapLayersRef.current.labelLayerIds, visibleLayers.labels);
    setContextualHydrographyVisible(
      map,
      basemapLayersRef.current.hydrographyLayerIds,
      visibleLayers.contextual_hydrography,
    );
    setBasemapLayerGroupVisible(
      map,
      basemapLayersRef.current.buildingLayerIds,
      visibleLayers.contextual_buildings,
    );
    setBasemapLayerGroupVisible(
      map,
      basemapLayersRef.current.transportLayerIds,
      visibleLayers.contextual_transport,
    );
    setBasemapLayerGroupVisible(
      map,
      basemapLayersRef.current.facilityLayerIds,
      visibleLayers.contextual_facilities,
    );
    for (const marker of infrastructureMarkersRef.current) {
      marker.getElement().style.display = visibleLayers.contextual_facilities ? "grid" : "none";
    }
    setLayerVisibilitySafe(map, RIVER_HOVER_LAYER, visibleLayers.contextual_hydrography);
    setLayerVisibilitySafe(map, RIVER_SELECTED_LAYER, visibleLayers.contextual_hydrography);

    if (!visibleLayers.contextual_hydrography) {
      clearHovered();
      clearProximity();
    }
  }, [
    activeTerrainProfile?.site_id,
    basinRiseM,
    mapReady,
    visibleLayers,
    clearHovered,
    clearProximity,
  ]);

  useEffect(() => {
    for (const marker of infrastructureMarkersRef.current) {
      const element = marker.getElement();
      element.classList.toggle(
        "is-basin-active",
        Boolean(activeTerrainProfile?.site_id) && element.dataset.siteId === activeTerrainProfile?.site_id,
      );
    }
  }, [activeTerrainProfile?.site_id, infrastructureRevision]);

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
      ? {
          kind: "point",
          feature: hovered.feature,
          infrastructure:
            hovered.feature.properties.feature_kind === "community"
              ? communityInfrastructureRef.current.get(hovered.entityId) ?? null
              : null,
        }
      : hovered.kind === "infrastructure"
        ? { kind: "infrastructure", infrastructure: hovered.infrastructure }
        : {
            kind: "contextual_river",
            name: hovered.name,
            matchedRiver: hovered.matchedRiver,
            contextSource: CONTEXT_SOURCE_LABEL,
          }
    : null;
  void infrastructureRevision;

  return (
    <div className="map-stage" ref={containerRef}>
      {visibleLayers.terrain_basins && localTerrain?.available && activeTerrainProfile && (
        <section className="terrain-basin-control" aria-label="Potential basin screening controls">
          <div className="terrain-basin-control__eyebrow">TERRAIN-CONNECTED BASIN · SCREENING</div>
          <label>
            <span>Hydro reference</span>
            <select
              value={activeTerrainProfile.site_id}
              onChange={(event) => setActiveBasinSiteId(event.target.value)}
            >
              {terrainProfiles.map((profile) => (
                <option key={profile.site_id} value={profile.site_id}>{profile.site_name}</option>
              ))}
            </select>
          </label>
          <label>
            <span>Exploratory retention rise <strong>+{basinRiseM} m</strong></span>
            <input
              type="range"
              min={activeTerrainProfile.min_rise_m}
              max={activeTerrainProfile.max_rise_m}
              step={5}
              value={basinRiseM}
              onChange={(event) => setBasinRiseM(Number(event.target.value))}
            />
          </label>
          <div className="terrain-basin-control__metrics">
            <span><small>Seed terrain</small><strong>{Math.round(activeTerrainProfile.seed_elevation_m)} m</strong></span>
            <span><small>Connected area</small><strong>{activeRiseSummary ? `${activeRiseSummary.area_km2.toFixed(1)} km²` : "—"}</strong></span>
            <span><small>Approx. volume</small><strong>{activeRiseSummary ? formatTerrainVolume(activeRiseSummary.volume_m3) : "—"}</strong></span>
          </div>
          <p>Depth colors show terrain-connected inundation at this exploratory level. This is not a dam layout, hydraulic head, or reservoir design.</p>
        </section>
      )}

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

      {hovered && hoverTarget && typeof document !== "undefined" &&
        createPortal(
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
                : hovered.kind === "river" && hovered.matchedRiver
                  ? () => {
                      selectedContextRiverEntityRef.current = hovered.matchedRiver!.entity_id;
                      setRiverOverlay(RIVER_SELECTED_SOURCE, hovered.geometry);
                      onSelect(hovered.matchedRiver!.entity_id);
                    }
                  : undefined
            }
          />,
          document.body,
        )}
    </div>
  );
}

function formatTerrainVolume(valueM3: number) {
  if (!Number.isFinite(valueM3) || valueM3 <= 0) return "0 hm³";
  if (valueM3 >= 1_000_000_000) return `${(valueM3 / 1_000_000_000).toFixed(2)} km³`;
  return `${(valueM3 / 1_000_000).toFixed(valueM3 >= 100_000_000 ? 0 : 1)} hm³`;
}

function setLayerVisibilitySafe(
  map: MapLibreMap,
  layerId: string,
  visible: boolean,
) {
  if (!map.getLayer(layerId)) return;
  try {
    map.setLayoutProperty(layerId, "visibility", visible ? "visible" : "none");
  } catch {
    // Layer/style transitions must not surface as runtime console errors.
  }
}

function fitToObservatoryExtent(
  map: MapLibreMap,
  data: ExplorerBootstrap,
  inspectorOpen: boolean,
  duration: number,
) {
  const coordinates = [
    ...data.communities.features.map((feature) => feature.geometry.coordinates),
    ...data.hydroSites.map((feature) => feature.coordinates),
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
      "text-font": ["Noto Sans Regular"],
      "text-size": [
        "interpolate",
        ["linear"],
        ["zoom"],
        4.2, 12,
        7, 13.5,
        10, 15,
        13, 16,
        17, 17,
      ],
      "text-offset": [0, 1.15],
      "text-anchor": "top",
      "text-allow-overlap": false,
      "text-padding": 4,
    },
    paint: {
      "text-color": "#f2c38b",
      "text-halo-color": "rgba(3,10,14,.98)",
      "text-halo-width": 2,
      "text-halo-blur": 0.2,
      "text-opacity": ["case", ["boolean", ["feature-state", "dimmed"], false], 0.3, 0.98],
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
      "text-font": ["Noto Sans Regular"],
      "text-size": [
        "interpolate",
        ["linear"],
        ["zoom"],
        6.1, 10.5,
        9, 11.5,
        12, 13,
        15, 14,
        18, 15,
      ],
      "text-offset": [0, 1],
      "text-anchor": "top",
      "text-allow-overlap": false,
      "text-padding": 4,
    },
    paint: {
      "text-color": "#9ae5f5",
      "text-halo-color": "rgba(3,10,14,.98)",
      "text-halo-width": 1.8,
      "text-halo-blur": 0.2,
      "text-opacity": ["case", ["boolean", ["feature-state", "dimmed"], false], 0.24, 0.94],
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


type InfrastructureSnapshot = {
  infrastructure: ContextInfrastructure[];
  communities: Map<string, CommunityInfrastructureSummary>;
};

function collectInfrastructureSnapshot(
  map: MapLibreMap,
  communities: PublicMapFeature[],
  publishedByEntityId: Map<string, PublicCommunityInfrastructure>,
): InfrastructureSnapshot {
  const styleLayers = map.getStyle().layers ?? [];
  const sourceLayers = new Map<string, { source: string; sourceLayer: string }>();

  for (const raw of styleLayers) {
    const layer = raw as { source?: string; "source-layer"?: string };
    if (typeof layer.source !== "string" || typeof layer["source-layer"] !== "string") continue;
    const sourceLayer = layer["source-layer"];
    const lower = sourceLayer.toLowerCase();
    if (
      !lower.includes("poi") &&
      !lower.includes("aero") &&
      !lower.includes("waterway") &&
      !lower.includes("transport")
    ) {
      continue;
    }
    sourceLayers.set(`${layer.source}|${sourceLayer}`, { source: layer.source, sourceLayer });
  }

  const rawInfrastructure: ContextInfrastructure[] = [];
  const seen = new Set<string>();

  for (const { source, sourceLayer } of sourceLayers.values()) {
    let features: MapGeoJSONFeature[] = [];
    try {
      features = map.querySourceFeatures(source, { sourceLayer });
    } catch {
      continue;
    }

    for (const feature of features) {
      const kind = classifyInfrastructureFeature(sourceLayer, feature);
      if (!kind || (kind !== "airport" && kind !== "dock")) continue;
      const coordinates = geometryCenter(feature.geometry as GeoJSON.Geometry);
      if (!coordinates) continue;

      const props = feature.properties ?? {};
      const name = contextFeatureName(props, kind);
      const key = contextFeatureKey(feature, sourceLayer, kind, name, coordinates);
      if (seen.has(key)) continue;
      seen.add(key);

      rawInfrastructure.push({
        key,
        kind,
        name,
        coordinates,
        source: CONTEXT_SOURCE_LABEL,
        sizeLabel: contextSizeLabel(kind, feature),
        capacityMw: null,
        capacityBasis: null,
        nearestPortName: null,
        nearestPortDistanceKm: null,
        geometryConfidence: "mapped basemap geometry",
        notes: kind === "airport" ? "Basemap-detected air access" : "Basemap-detected dock / marine access",
      });
    }
  }

  const airports = rawInfrastructure.filter((item) => item.kind === "airport");
  const docks = rawInfrastructure.filter((item) => item.kind === "dock");
  const byCommunity = new Map<string, CommunityInfrastructureSummary>();

  for (const community of communities) {
    const coordinates = community.geometry.coordinates;
    const published = publishedByEntityId.get(community.properties.entity_id) ?? null;
    const airportMatch = nearestInfrastructure(coordinates, airports, 60);
    const dockMatch = nearestInfrastructure(coordinates, docks, 45);
    const publishedAirport = createPublishedCommunityFacilityProxy(community, published, "airport");
    const publishedDock = createPublishedCommunityFacilityProxy(community, published, "dock");

    const airport = airportMatch?.facility
      ? mergeMappedAndPublishedFacility(airportMatch.facility, publishedAirport)
      : publishedAirport;
    const dock = dockMatch?.facility
      ? mergeMappedAndPublishedFacility(dockMatch.facility, publishedDock)
      : publishedDock;

    byCommunity.set(community.properties.entity_id, {
      population: published?.population.value ?? null,
      populationYear: published?.population.year ?? null,
      populationGeography: published?.population.geography ?? null,
      populationSource: published?.population.source?.name ?? null,
      populationSourceUrl: published?.population.source?.url ?? null,
      populationNote: published?.population.note ?? null,
      airport,
      airportDistanceKm: airportMatch?.distanceKm ?? null,
      airportCode: published?.airport.code ?? null,
      airportPublishedRunwayLengthM: published?.airport.runway_length_m ?? null,
      airportPublishedSurface: published?.airport.runway_surface ?? null,
      airportPublishedSource:
        published?.airport.dimension_source?.name ?? published?.airport.presence_source?.name ?? null,
      airportPublishedSourceUrl:
        published?.airport.dimension_source?.url ?? published?.airport.presence_source?.url ?? null,
      airportPublishedNote: published?.airport.note ?? null,
      dock,
      dockDistanceKm: dockMatch?.distanceKm ?? null,
      marinePublishedDockLengthM: published?.marine.dock_length_m ?? null,
      marinePublishedMaxDraftM: published?.marine.max_draft_m ?? null,
      marineHeavyLiftStatus: published?.marine.heavy_lift_status ?? null,
      marinePublishedSource: published?.marine.source?.name ?? null,
      marinePublishedSourceUrl: published?.marine.source?.url ?? null,
      marinePublishedNote: published?.marine.note ?? null,
      hasPublishedMarineContext: Boolean(published?.marine.access_known),
      associatedHydroSites: [],
    });
  }

  return { infrastructure: rawInfrastructure, communities: byCommunity };
}

function mergeMappedAndPublishedFacility(
  mapped: ContextInfrastructure,
  published: ContextInfrastructure | null,
): ContextInfrastructure {
  if (!published) return mapped;
  return {
    ...mapped,
    name: mapped.name || published.name,
    sizeLabel: mapped.sizeLabel ?? published.sizeLabel,
    sourceNote: mapped.sizeLabel
      ? "Mapped extent from OpenMapTiles / OpenStreetMap context"
      : published.sourceNote,
    notes: mapped.notes ?? published.notes,
  };
}

function buildPotentialHydroInfrastructure(
  sites: PublicHydroScreeningSite[],
  communities: PublicMapFeature[],
  byCommunity: Map<string, CommunityInfrastructureSummary>,
): ContextInfrastructure[] {
  const results: ContextInfrastructure[] = [];
  const airportPool = Array.from(byCommunity.values())
    .map((summary) => summary.airport)
    .filter((value): value is ContextInfrastructure => Boolean(value));
  const dockPool = Array.from(byCommunity.values())
    .map((summary) => summary.dock)
    .filter((value): value is ContextInfrastructure => Boolean(value));

  for (const site of sites) {
    const nearestCommunityMatch = findNearestCommunity(site.coordinates, communities);
    const nearestAirport = nearestInfrastructure(site.coordinates, airportPool, 500);
    const nearestDock = nearestInfrastructure(site.coordinates, dockPool, 500);

    const resolved: ContextInfrastructure = {
      key: site.id,
      kind: "potential_hydro",
      name: site.name,
      coordinates: site.coordinates,
      source: "Kristal published coastal hydro screening scope",
      sizeLabel: null,
      capacityMw: null,
      capacityBasis: "published_potential_label",
      nearestPortName: nearestDock?.facility.name ?? null,
      nearestPortDistanceKm: nearestDock?.distanceKm ?? null,
      nearestAirportName: nearestAirport?.facility.name ?? null,
      nearestAirportDistanceKm: nearestAirport?.distanceKm ?? null,
      nearestCommunityName: site.nearest_active_community ?? nearestCommunityMatch?.community.properties.name ?? null,
      nearestCommunityDistanceKm: site.distance_to_active_community_km ?? nearestCommunityMatch?.distanceKm ?? null,
      populationServed:
        nearestCommunityMatch
          ? (byCommunity.get(nearestCommunityMatch.community.properties.entity_id)?.population ?? null)
          : null,
      screeningConfidence:
        site.geometry_class === "named_or_strong_proxy"
          ? "high"
          : site.geometry_class === "gauge_proxy" || site.geometry_class === "river_proxy"
            ? "medium"
            : "low",
      riverName: site.river_name,
      basinName: null,
      evidenceLabel: site.geometry_role,
      powerLabel: site.capacity_or_potential,
      statusLabel: site.current_status,
      geometryConfidence: site.geometry_confidence,
      coastProxyDistanceKm: site.distance_to_mouth_or_coast_proxy_km,
      sourceNote: site.source_notes,
      notes: site.mapping_note,
    };

    results.push(resolved);

    const communityName = site.nearest_active_community;
    if (!communityName) continue;
    const community = communities.find((candidate) => candidate.properties.name === communityName);
    if (!community) continue;
    const summary = byCommunity.get(community.properties.entity_id);
    if (!summary) continue;
    summary.associatedHydroSites.push({
      facility: resolved,
      distanceKm: site.distance_to_active_community_km ?? haversineKm(site.coordinates, community.geometry.coordinates),
    });
    summary.associatedHydroSites.sort((a, b) => a.distanceKm - b.distanceKm);
    if (summary.associatedHydroSites.length > 3) summary.associatedHydroSites.length = 3;
  }

  return results;
}

function findNearestCommunity(
  origin: [number, number],
  communities: PublicMapFeature[],
): { community: PublicMapFeature; distanceKm: number } | null {
  let best: { community: PublicMapFeature; distanceKm: number } | null = null;
  for (const community of communities) {
    const distanceKm = haversineKm(origin, community.geometry.coordinates);
    if (!best || distanceKm < best.distanceKm) best = { community, distanceKm };
  }
  return best;
}

function classifyInfrastructureFeature(
  sourceLayer: string,
  feature: MapGeoJSONFeature,
): ContextInfrastructure["kind"] | null {
  const p = feature.properties ?? {};
  const text = [
    sourceLayer,
    p.class,
    p.subclass,
    p.type,
    p.kind,
    p.aeroway,
    p.amenity,
    p.man_made,
    p.waterway,
    p.power,
    p.harbour,
    p.harbor,
    p.port,
    p.name,
  ]
    .filter((value) => value !== null && value !== undefined)
    .join(" ")
    .toLowerCase();

  if (/\b(dam|weir|barrage)\b/.test(text)) return "dam";
  if (/\b(power_plant|power plant|hydroelectric|hydro|generator|power station|plant)\b/.test(text)) {
    return "power";
  }
  if (/\b(aerodrome|airport|airfield|runway)\b/.test(text) || sourceLayer.toLowerCase().includes("aeroway")) {
    // Taxiways and aprons alone are not useful badges unless the tile also
    // identifies them as airport/runway context.
    if (/\b(taxiway|apron)\b/.test(text) && !/\b(aerodrome|airport|airfield|runway)\b/.test(text)) return null;
    return "airport";
  }
  if (/\b(dock|wharf|pier|harbour|harbor|port|ferry_terminal|ferry terminal|marina)\b/.test(text)) {
    return "dock";
  }
  return null;
}

function contextFeatureName(
  properties: Record<string, unknown>,
  kind: ContextInfrastructure["kind"],
): string {
  for (const key of ["name:en", "name:fr", "name", "ref", "iata", "icao"]) {
    const value = properties[key];
    if (typeof value === "string" && value.trim()) return value.trim();
  }
  if (kind === "airport") return "Mapped airport / runway";
  if (kind === "dock") return "Mapped dock / port";
  if (kind === "power") return "Mapped power facility";
  return "Mapped dam";
}

function contextFeatureKey(
  feature: MapGeoJSONFeature,
  sourceLayer: string,
  kind: ContextInfrastructure["kind"],
  name: string,
  coordinates: [number, number],
) {
  const osmId = feature.properties?.osm_id ?? feature.properties?.id ?? feature.id;
  if (osmId !== undefined && osmId !== null) return `${sourceLayer}:${kind}:${String(osmId)}`;
  return `${sourceLayer}:${kind}:${normalizePlaceName(name)}:${coordinates[0].toFixed(4)}:${coordinates[1].toFixed(4)}`;
}

function nearestInfrastructure(
  origin: [number, number],
  facilities: ContextInfrastructure[],
  maxDistanceKm: number,
): { facility: ContextInfrastructure; distanceKm: number } | null {
  let best: { facility: ContextInfrastructure; distanceKm: number } | null = null;
  for (const facility of facilities) {
    const distanceKm = haversineKm(origin, facility.coordinates);
    if (distanceKm > maxDistanceKm) continue;
    // Prefer a nearby feature carrying a mapped size over a nameless point
    // when distances are almost equivalent.
    const score = distanceKm - (facility.sizeLabel ? 0.6 : 0);
    const bestScore = best ? best.distanceKm - (best.facility.sizeLabel ? 0.6 : 0) : Infinity;
    if (score < bestScore) best = { facility, distanceKm };
  }
  return best;
}

function resolvePowerCapacity(
  properties: Record<string, unknown>,
): { mw: number; basis: "mapped" | "estimated_head_flow" } | null {
  const mapped = parseCapacityMw(properties);
  if (mapped !== null) return { mw: mapped, basis: "mapped" };

  const head = parseMetricProperty(properties, /(head|hydraulic_head)/i, "m");
  const flow = parseMetricProperty(properties, /(flow|discharge)/i, "m3/s");
  if (head === null || flow === null || head <= 0 || flow <= 0) return null;

  // Screening estimate only: P = rho*g*Q*H*eta, with eta fixed at 0.85.
  // It is shown only when BOTH mapped head and flow values exist.
  const mw = (9.81 * flow * head * 0.85) / 1000;
  return Number.isFinite(mw) && mw > 0 ? { mw, basis: "estimated_head_flow" } : null;
}

function parseMetricProperty(
  properties: Record<string, unknown>,
  keyPattern: RegExp,
  expectedUnit: "m" | "m3/s",
): number | null {
  for (const [key, value] of Object.entries(properties)) {
    if (!keyPattern.test(key)) continue;
    if (typeof value === "number" && Number.isFinite(value)) return value;
    if (typeof value !== "string") continue;
    const normalized = value.replace(",", ".").toLowerCase();
    const match = normalized.match(/([0-9]+(?:\.[0-9]+)?)/);
    if (!match) continue;
    const amount = Number(match[1]);
    if (!Number.isFinite(amount)) continue;
    if (expectedUnit === "m" && /\bft\b/.test(normalized)) return amount * 0.3048;
    return amount;
  }
  return null;

}

function parseCapacityMw(properties: Record<string, unknown>): number | null {
  for (const [key, value] of Object.entries(properties)) {
    const lowerKey = key.toLowerCase();
    if (!/(output|capacity|power)/.test(lowerKey)) continue;
    if (typeof value === "number" && Number.isFinite(value) && /mw/.test(lowerKey)) return value;
    if (typeof value !== "string") continue;
    const normalized = value.replace(",", ".").toLowerCase();
    const match = normalized.match(/([0-9]+(?:\.[0-9]+)?)\s*(gw|mw|kw|w)\b/);
    if (!match) continue;
    const amount = Number(match[1]);
    if (!Number.isFinite(amount)) continue;
    if (match[2] === "gw") return amount * 1000;
    if (match[2] === "mw") return amount;
    if (match[2] === "kw") return amount / 1000;
    return amount / 1_000_000;
  }
  return null;
}

function contextSizeLabel(kind: ContextInfrastructure["kind"], feature: MapGeoJSONFeature): string | null {
  const props = feature.properties ?? {};
  for (const key of ["length", "runway:length", "width", "diameter"]) {
    const raw = props[key];
    if (typeof raw === "number" && Number.isFinite(raw) && raw > 0) {
      return `${kind === "airport" ? "Runway" : "Mapped"} ~${Math.round(raw).toLocaleString("en-CA")} m`;
    }
    if (typeof raw === "string") {
      const match = raw.match(/([0-9]+(?:\.[0-9]+)?)\s*(m|km|ft)?/i);
      if (match) {
        let meters = Number(match[1]);
        const unit = (match[2] ?? "m").toLowerCase();
        if (unit === "km") meters *= 1000;
        if (unit === "ft") meters *= 0.3048;
        if (Number.isFinite(meters) && meters > 0) {
          return `${kind === "airport" ? "Runway" : "Mapped"} ~${Math.round(meters).toLocaleString("en-CA")} m`;
        }
      }
    }
  }

  const span = geometrySpanMeters(feature.geometry as GeoJSON.Geometry);
  if (span === null || span < 25) return null;
  const prefix = kind === "airport" ? "Runway/footprint" : kind === "dam" ? "Mapped span" : "Mapped extent";
  return `${prefix} ~${Math.round(span).toLocaleString("en-CA")} m`;
}

function geometryCenter(geometry: GeoJSON.Geometry): [number, number] | null {
  if (geometry.type === "Point") return geometry.coordinates as [number, number];
  const pairs: [number, number][] = [];
  if (geometry.type === "GeometryCollection") {
    for (const child of geometry.geometries) {
      const center = geometryCenter(child);
      if (center) pairs.push(center);
    }
  } else {
    collectCoordinatePairs(geometry.coordinates, pairs);
  }
  if (!pairs.length) return null;
  const sum = pairs.reduce(
    (acc, point) => [acc[0] + point[0], acc[1] + point[1]] as [number, number],
    [0, 0] as [number, number],
  );
  return [sum[0] / pairs.length, sum[1] / pairs.length];
}

function geometrySpanMeters(geometry: GeoJSON.Geometry): number | null {
  const pairs: [number, number][] = [];
  if (geometry.type === "GeometryCollection") {
    for (const child of geometry.geometries) {
      const center = geometryCenter(child);
      if (center) pairs.push(center);
    }
  } else {
    collectCoordinatePairs(geometry.coordinates, pairs);
  }
  if (pairs.length < 2) return null;
  let max = 0;
  const stride = Math.max(1, Math.floor(pairs.length / 40));
  for (let i = 0; i < pairs.length; i += stride) {
    for (let j = i + stride; j < pairs.length; j += stride) {
      max = Math.max(max, haversineKm(pairs[i], pairs[j]) * 1000);
    }
  }
  return max || null;
}

function collectCoordinatePairs(value: unknown, output: [number, number][]) {
  if (!Array.isArray(value)) return;
  if (
    value.length >= 2 &&
    typeof value[0] === "number" &&
    typeof value[1] === "number" &&
    Number.isFinite(value[0]) &&
    Number.isFinite(value[1])
  ) {
    output.push([value[0], value[1]]);
    return;
  }
  for (const child of value) collectCoordinatePairs(child, output);
}

function haversineKm(a: [number, number], b: [number, number]) {
  const radiusKm = 6371.0088;
  const toRadians = (value: number) => (value * Math.PI) / 180;
  const dLat = toRadians(b[1] - a[1]);
  const dLon = toRadians(b[0] - a[0]);
  const lat1 = toRadians(a[1]);
  const lat2 = toRadians(b[1]);
  const h =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) ** 2;
  return 2 * radiusKm * Math.asin(Math.sqrt(h));
}

function normalizePlaceName(value: string) {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "")
    .trim();
}

function updateCommunityMarkerVisibility(
  markers: maplibregl.Marker[],
  visibleLayers: ObservatoryVisibleLayers,
  zoom: number,
) {
  const communitiesVisible = visibleLayers.communities;
  const showLabel = communitiesVisible && visibleLayers.labels && zoom >= 4.2;
  const fontSize = communityLabelFontSize(zoom);

  for (const marker of markers) {
    const element = marker.getElement();
    const name = element.querySelector<HTMLElement>(".community-callout__name");
    const badges = element.querySelector<HTMLElement>(".community-infra-badges");
    const panel = element.querySelector<HTMLElement>(".community-callout__panel");
    const leader = element.querySelector<HTMLElement>(".community-callout__leader");
    const hasInfrastructure = element.dataset.hasInfrastructure === "true";
    const showBadges = communitiesVisible && visibleLayers.contextual_facilities && hasInfrastructure;
    const showCallout = showLabel || showBadges;

    element.style.display = communitiesVisible ? "block" : "none";
    if (name) {
      name.style.display = showLabel ? "block" : "none";
      name.style.fontSize = `${fontSize}px`;
    }
    if (badges) badges.style.display = showBadges ? "flex" : "none";
    if (panel) panel.style.display = showCallout ? "grid" : "none";
    if (leader) leader.style.display = showCallout ? "block" : "none";
    if (showCallout) updateCommunityLeaderGeometry(element);
  }
}

function communityLabelFontSize(zoom: number) {
  if (zoom <= 4.2) return 12;
  if (zoom <= 7) return 12 + ((zoom - 4.2) / 2.8) * 1.5;
  if (zoom <= 10) return 13.5 + ((zoom - 7) / 3) * 1.5;
  if (zoom <= 13) return 15 + ((zoom - 10) / 3);
  if (zoom <= 17) return 16 + ((zoom - 13) / 4);
  return 17;
}

type CommunityCalloutPlacement = {
  x: number;
  y: number;
};

function getCommunityCalloutPlacement(feature: PublicMapFeature): CommunityCalloutPlacement {
  // Aupaluk sits in a dense cluster at the current overview scale; keep its
  // callout explicitly above the house marker to avoid the neighbouring labels.
  if (normalizePlaceName(feature.properties.name) === "aupaluk") {
    return { x: 0, y: -74 };
  }

  const key = `${feature.properties.entity_id}:${feature.properties.name}`;
  let hash = 2166136261;
  for (let index = 0; index < key.length; index += 1) {
    hash ^= key.charCodeAt(index);
    hash = Math.imul(hash, 16777619);
  }

  // Eight stable directions distribute nearby village callouts instead of stacking
  // every label and access icon directly below the mapped settlement coordinate.
  const placements: CommunityCalloutPlacement[] = [
    { x: 0, y: -54 },
    { x: 62, y: -38 },
    { x: 76, y: 0 },
    { x: 62, y: 38 },
    { x: 0, y: 54 },
    { x: -62, y: 38 },
    { x: -76, y: 0 },
    { x: -62, y: -38 },
  ];
  return placements[(hash >>> 0) % placements.length];
}

function createCommunityMapMarkerElement(
  name: string,
  showAirport: boolean,
  showDock: boolean,
  placement: CommunityCalloutPlacement,
) {
  const element = document.createElement("div");
  element.className = "community-map-marker";
  element.dataset.hasInfrastructure = String(showAirport || showDock);

  const house = document.createElement("span");
  house.className = "community-house-marker";
  house.setAttribute("aria-hidden", "true");
  house.innerHTML =
    '<svg viewBox="0 0 24 24" focusable="false" aria-hidden="true"><path d="M3.5 11.2 12 4l8.5 7.2v8.3a1 1 0 0 1-1 1h-5v-5.8h-5v5.8h-5a1 1 0 0 1-1-1z"/></svg>';
  element.appendChild(house);

  const leader = document.createElement("span");
  leader.className = "community-callout__leader";
  leader.setAttribute("aria-hidden", "true");
  element.appendChild(leader);

  const panel = document.createElement("div");
  panel.className = "community-callout__panel";
  panel.style.left = `${placement.x}px`;
  panel.style.top = `${placement.y}px`;
  panel.dataset.calloutX = String(placement.x);
  panel.dataset.calloutY = String(placement.y);

  const label = document.createElement("span");
  label.className = "community-callout__name community-name-overlay";
  label.textContent = name;
  label.setAttribute("aria-hidden", "true");
  panel.appendChild(label);

  const badges = showAirport || showDock
    ? createCommunityInfrastructureBadge(showAirport, showDock)
    : null;
  if (badges) panel.appendChild(badges);

  element.appendChild(panel);
  return { element, badges };
}

function clamp(value: number, minimum: number, maximum: number) {
  return Math.min(maximum, Math.max(minimum, value));
}

function updateCommunityLeaderGeometry(element: HTMLElement) {
  const panel = element.querySelector<HTMLElement>(".community-callout__panel");
  const leader = element.querySelector<HTMLElement>(".community-callout__leader");
  if (!panel || !leader || panel.style.display === "none") return;

  const centerX = Number(panel.dataset.calloutX ?? 0);
  const centerY = Number(panel.dataset.calloutY ?? 0);
  const panelWidth = panel.offsetWidth;
  const panelHeight = panel.offsetHeight;
  if (!panelWidth || !panelHeight) return;

  const halfWidth = panelWidth / 2;
  const halfHeight = panelHeight / 2;
  const panelGap = 3;
  const houseRadius = 13;

  // Connect to the closest point on the label card instead of aiming at its
  // centre. This naturally produces clean horizontal/vertical leaders when the
  // card overlaps the village axis, and only uses a diagonal when it is useful.
  const left = centerX - halfWidth - panelGap;
  const right = centerX + halfWidth + panelGap;
  const top = centerY - halfHeight - panelGap;
  const bottom = centerY + halfHeight + panelGap;
  let targetX = clamp(0, left, right);
  let targetY = clamp(0, top, bottom);

  let targetDistance = Math.hypot(targetX, targetY);
  if (targetDistance <= houseRadius + 2) {
    // Defensive fallback for an unusually large card: use the callout centre
    // direction and stop just outside the house marker.
    const centerDistance = Math.hypot(centerX, centerY);
    if (centerDistance < 0.001) {
      leader.style.display = "none";
      return;
    }
    const unitX = centerX / centerDistance;
    const unitY = centerY / centerDistance;
    targetX = unitX * (houseRadius + 5);
    targetY = unitY * (houseRadius + 5);
    targetDistance = Math.hypot(targetX, targetY);
  }

  const unitX = targetX / targetDistance;
  const unitY = targetY / targetDistance;
  const startX = unitX * houseRadius;
  const startY = unitY * houseRadius;
  const length = Math.max(3, targetDistance - houseRadius);
  const angle = Math.atan2(targetY, targetX) * (180 / Math.PI);

  leader.style.left = `${startX}px`;
  leader.style.top = `${startY}px`;
  leader.style.width = `${length}px`;
  leader.style.transform = `rotate(${angle}deg)`;
}

function createCommunityInfrastructureBadge(showAirport: boolean, showDock: boolean) {
  const element = document.createElement("div");
  element.className = "community-infra-badges";
  element.setAttribute("role", "button");
  element.setAttribute("tabindex", "0");
  const labels: string[] = [];
  if (showAirport) labels.push("airport");
  if (showDock) labels.push("dock or marine access");
  element.setAttribute("aria-label", labels.join(" and "));

  if (showAirport) {
    const badge = document.createElement("span");
    badge.className = "community-infra-badge community-infra-badge--airport";
    badge.textContent = "✈";
    badge.title = "Airport / airstrip context";
    element.appendChild(badge);
  }
  if (showDock) {
    const badge = document.createElement("span");
    badge.className = "community-infra-badge community-infra-badge--dock";
    badge.textContent = "⚓";
    badge.title = "Dock / marine-access context";
    element.appendChild(badge);
  }
  return element;
}

function createInfrastructureMarkerElement(infrastructure: ContextInfrastructure) {
  const element = document.createElement("button");
  element.type = "button";
  element.className = `context-infrastructure-marker context-infrastructure-marker--${infrastructure.kind}`;
  element.setAttribute(
    "aria-label",
    infrastructure.kind === "potential_hydro"
      ? `${infrastructure.name}, potential hydro screening site`
      : `${infrastructure.name}, ${infrastructure.kind} context`,
  );
  element.title = infrastructure.name;
  element.textContent =
    infrastructure.kind === "potential_hydro"
      ? "⚡"
      : infrastructure.kind === "power"
        ? "⚡"
        : infrastructure.kind === "dock"
          ? "⚓"
          : infrastructure.kind === "airport"
            ? "✈"
            : "▰";
  return element;
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
