"use client";

import type { CSSProperties } from "react";
import type {
  CommunityInfrastructureSummary,
  ContextInfrastructure,
  PublicMapFeature,
  PublicRiverReference,
} from "../../lib/explorer-types";
import { formatNumber, humanizeToken } from "../../lib/format";

export type HoverTarget =
  | {
      kind: "point";
      feature: PublicMapFeature;
      infrastructure?: CommunityInfrastructureSummary | null;
    }
  | {
      kind: "contextual_river";
      name: string;
      matchedRiver: PublicRiverReference | null;
      contextSource: string;
    }
  | {
      kind: "infrastructure";
      infrastructure: ContextInfrastructure;
    };

type Props = {
  target: HoverTarget;
  x: number;
  y: number;
  viewportWidth: number;
  viewportHeight: number;
  onPointerEnter: () => void;
  onPointerLeave: () => void;
  onSelect?: () => void;
};

export function HoverCard({
  target,
  x,
  y,
  viewportWidth,
  viewportHeight,
  onPointerEnter,
  onPointerLeave,
  onSelect,
}: Props) {
  const cardWidth = 356;
  const cardHeightEstimate =
    target.kind === "contextual_river"
      ? 245
      : target.kind === "infrastructure"
        ? target.infrastructure.kind === "potential_hydro"
          ? 420
          : 320
        : 430;
  const placeLeft = x + cardWidth + 32 > viewportWidth;
  const placeAbove = y + cardHeightEstimate + 24 > viewportHeight;

  const style: CSSProperties = {
    left: x,
    top: y,
    transform: `translate(${placeLeft ? "calc(-100% - 22px)" : "22px"}, ${
      placeAbove ? "calc(-100% + 18px)" : "-22px"
    })`,
  };

  if (target.kind === "contextual_river") {
    const river = target.matchedRiver;
    return (
      <div
        className="hover-card hover-card--river"
        style={style}
        onPointerEnter={onPointerEnter}
        onPointerLeave={onPointerLeave}
        role="dialog"
        aria-label={`Map summary for ${river?.name ?? target.name}`}
      >
        <div className="hover-card__eyebrow">
          <span>River context</span>
          <span className="status-glyph" aria-hidden="true">≈</span>
          <span>{river ? "Kristal match" : "Basemap only"}</span>
        </div>
        <div className="hover-card__title">{river?.name ?? target.name}</div>
        <div className="hover-card__subtitle">
          {river?.region ?? `Contextual hydrography · ${target.name}`}
        </div>
        <div className="hover-card__facts">
          <CompactFact label="Reference" value={river ? "Research entity" : "Context only"} />
          <CompactFact label="Station" value={river?.anchor_station_number ?? "—"} />
          <CompactFact
            label="Geometry"
            value={river ? "Kristal flowline pending" : "External basemap"}
          />
        </div>
        <div className="hover-card__footer">
          <span>{target.contextSource} · contextual line, not governed Kristal geometry</span>
          {onSelect && river && (
            <button type="button" onClick={onSelect}>
              Inspect <span aria-hidden="true">↗</span>
            </button>
          )}
        </div>
      </div>
    );
  }

  if (target.kind === "infrastructure") {
    const infra = target.infrastructure;

    if (infra.kind === "potential_hydro") {
      return (
        <div
          className="hover-card hover-card--infrastructure hover-card--hydro"
          style={style}
          onPointerEnter={onPointerEnter}
          onPointerLeave={onPointerLeave}
          role="dialog"
          aria-label={`Potential hydro screening summary for ${infra.name}`}
        >
          <div className="hover-card__eyebrow">
            <span>Coastal hydro screening</span>
            <span className="status-glyph" aria-hidden="true">⚡</span>
            <span>Screening only</span>
          </div>
          <div className="hover-card__title">{infra.name}</div>
          <div className="hover-card__subtitle">
            {infra.riverName ?? "Hydro opportunity"}
            {infra.basinName ? ` · ${infra.basinName}` : ""}
          </div>
          <div className="hover-card__facts hover-card__facts--two">
            <CompactFact label="Potential" value={infra.powerLabel ?? "Not quantified"} />
            <CompactFact label="Status" value={infra.statusLabel ?? "Screening reference"} />
            <CompactFact label="Geometry" value={infra.geometryConfidence ?? "Reference geometry"} />
            <CompactFact
              label="Coast / mouth proxy"
              value={
                infra.coastProxyDistanceKm != null
                  ? `${formatDistance(infra.coastProxyDistanceKm, 1)} km`
                  : "Unavailable"
              }
            />
            <CompactFact
              label="Nearest community"
              value={formatDistanceFact(infra.nearestCommunityName, infra.nearestCommunityDistanceKm)}
            />
            <CompactFact
              label="Nearest airport"
              value={formatDistanceFact(infra.nearestAirportName, infra.nearestAirportDistanceKm)}
            />
            <CompactFact
              label="Nearest dock"
              value={formatDistanceFact(infra.nearestPortName, infra.nearestPortDistanceKm)}
            />
            <CompactFact label="Role" value="Coastal screening reference — not a dam location" />
          </div>
          <div className="hover-card__footer">
            <span>
              {infra.notes ?? "Screening only"} · proxy/gauge coordinates are never presented as engineered dam geometry.
            </span>
          </div>
        </div>
      );
    }

    const kindLabel =
      infra.kind === "airport"
        ? "Airport / airstrip"
        : infra.kind === "dock"
          ? "Port / dock"
          : infra.kind === "power"
            ? "Power facility"
            : "Dam / hydraulic structure";

    const glyph =
      infra.kind === "airport"
        ? "✈"
        : infra.kind === "dock"
          ? "⚓"
          : infra.kind === "power"
            ? "⚡"
            : "▰";

    return (
      <div
        className="hover-card hover-card--infrastructure"
        style={style}
        onPointerEnter={onPointerEnter}
        onPointerLeave={onPointerLeave}
        role="dialog"
        aria-label={`Infrastructure context for ${infra.name}`}
      >
        <div className="hover-card__eyebrow">
          <span>{kindLabel}</span>
          <span className="status-glyph" aria-hidden="true">{glyph}</span>
          <span>Context</span>
        </div>
        <div className="hover-card__title">{infra.name}</div>
        <div className="hover-card__subtitle">{infra.source}</div>
        <div className="hover-card__facts hover-card__facts--two">
          <CompactFact label="Mapped size" value={infra.sizeLabel ?? "Not exposed"} />
          <CompactFact
            label="Power"
            value={
              infra.capacityMw != null
                ? `${formatNumber(infra.capacityMw)} MW ${
                    infra.capacityBasis === "estimated_head_flow" ? "estimated (Q×H)" : "mapped"
                  }`
                : "Estimate unavailable"
            }
          />
          <CompactFact label="Nearest dock" value={infra.nearestPortName ?? "Not detected"} />
          <CompactFact
            label="Port distance"
            value={
              infra.nearestPortDistanceKm != null
                ? `${formatDistance(infra.nearestPortDistanceKm, 1)} km straight-line`
                : "Unavailable"
            }
          />
        </div>
        <div className="hover-card__footer">
          <span>
            Context geometry only. Power is never inferred without a mapped/published capacity or sufficient head/flow evidence.
          </span>
        </div>
      </div>
    );
  }

  const p = target.feature.properties;
  const infra = target.infrastructure ?? null;
  const isCommunity = p.feature_kind === "community";

  return (
    <div
      className="hover-card"
      style={style}
      onPointerEnter={onPointerEnter}
      onPointerLeave={onPointerLeave}
      role="dialog"
      aria-label={`Map summary for ${p.name}`}
    >
      <div className="hover-card__eyebrow">
        <span>{isCommunity ? "Community" : "Hydrometric station"}</span>
        <span className="status-glyph" aria-hidden="true">
          {isCommunity ? "◌" : "●"}
        </span>
        <span>{isCommunity ? "Approx." : humanizeToken(p.evidence_status ?? "verified")}</span>
      </div>

      <div className="hover-card__title">
        {p.feature_kind === "hydrometric_station" ? p.station_number : p.name}
      </div>
      <div className="hover-card__subtitle">
        {p.feature_kind === "hydrometric_station" ? p.river_name : p.region}
      </div>

      {isCommunity ? (
        <div className="hover-card__facts hover-card__facts--two">
          <CompactFact label="Population" value={formatCommunityPopulation(infra)} />
          <CompactFact label="Airport" value={formatCommunityAirport(infra)} />
          <CompactFact label="Runway / airfield" value={formatCommunityAirportSize(infra)} />
          <CompactFact label="Marine access" value={formatCommunityMarineAccess(infra)} />
          <CompactFact label="Port size / draft" value={formatCommunityMarineSize(infra)} />
          <CompactFact label="Hydro context" value={formatHydroAssociations(infra)} />
        </div>
      ) : (
        <div className="hover-card__facts">
          <CompactFact label="Status" value={humanizeToken(p.status)} />
          <CompactFact
            label="Drainage area"
            value={
              p.gross_drainage_area_km2 != null
                ? `${formatNumber(p.gross_drainage_area_km2)} km²`
                : "Unknown"
            }
          />
          <CompactFact label="Region" value={p.region ?? "Unknown"} />
        </div>
      )}

      <div className="hover-card__footer">
        <span>
          {isCommunity
            ? formatCommunitySources(infra)
            : "Official hydrometric station position"}
        </span>
        {onSelect && (
          <button type="button" onClick={onSelect}>
            Inspect <span aria-hidden="true">↗</span>
          </button>
        )}
      </div>
    </div>
  );
}

function formatCommunityPopulation(summary: CommunityInfrastructureSummary | null) {
  if (!summary || summary.population == null) return "Unknown · no published value";
  const year = summary.populationYear != null ? ` · Census ${summary.populationYear}` : "";
  return `${formatNumber(summary.population)}${year}`;
}

function formatCommunityAirport(summary: CommunityInfrastructureSummary | null) {
  if (!summary?.airport) return "Not verified";
  const identity = [summary.airportCode, summary.airport.name].filter(Boolean).join(" · ");
  const distance =
    summary.airportDistanceKm != null && summary.airportDistanceKm > 0.2
      ? ` · ${formatDistance(summary.airportDistanceKm, 1)} km from community ref.`
      : "";
  return `${identity || "Air access confirmed"}${distance}`;
}

function formatCommunityAirportSize(summary: CommunityInfrastructureSummary | null) {
  if (!summary?.airport) return "Not verified";
  if (summary.airport.sizeLabel) return summary.airport.sizeLabel;
  if (summary.airportPublishedRunwayLengthM != null) {
    const surface = summary.airportPublishedSurface ? ` · ${summary.airportPublishedSurface}` : "";
    return `Runway ${formatNumber(summary.airportPublishedRunwayLengthM)} m${surface}`;
  }
  return "Runway dimensions not verified";
}

function formatCommunityMarineAccess(summary: CommunityInfrastructureSummary | null) {
  if (!summary) return "Unknown";
  if (summary.dock) {
    const distance =
      summary.dockDistanceKm != null && summary.dockDistanceKm > 0.2
        ? ` · ${formatDistance(summary.dockDistanceKm, 1)} km from community ref.`
        : "";
    return `${summary.dock.name}${distance}`;
  }
  if (summary.hasPublishedMarineContext) return "Marine / port access confirmed";
  return "Not verified";
}

function formatCommunityMarineSize(summary: CommunityInfrastructureSummary | null) {
  if (!summary) return "Unknown";
  const parts: string[] = [];
  if (summary.dock?.sizeLabel) parts.push(summary.dock.sizeLabel);
  else if (summary.marinePublishedDockLengthM != null) {
    parts.push(`Dock ${formatNumber(summary.marinePublishedDockLengthM)} m`);
  } else {
    parts.push("Dock size not verified");
  }
  if (summary.marinePublishedMaxDraftM != null) {
    parts.push(`Draft ${formatNumber(summary.marinePublishedMaxDraftM)} m`);
  } else {
    parts.push("draft not verified");
  }
  if (summary.marineHeavyLiftStatus === "confirmed") parts.push("heavy lift confirmed");
  else if (summary.marineHeavyLiftStatus === "not_verified") parts.push("heavy lift not verified");
  return parts.join(" · ");
}

function formatCommunitySources(summary: CommunityInfrastructureSummary | null) {
  if (!summary) return "Published infrastructure record unavailable.";
  const sources = [
    summary.populationSource ? `population: ${summary.populationSource}` : null,
    summary.airportPublishedSource ? `airport: ${summary.airportPublishedSource}` : null,
    summary.marinePublishedSource ? `marine: ${summary.marinePublishedSource}` : null,
  ].filter((value): value is string => Boolean(value));
  const prefix = sources.length ? sources.join(" · ") : "Published provenance incomplete";
  return `${prefix}. Basemap geometry may enrich facility size; unknown values stay unknown.`;
}

function formatDistanceFact(name: string | null | undefined, distanceKm: number | null | undefined) {
  if (!name) return "Not detected";
  if (distanceKm == null) return name;
  return `${name} · ${formatDistance(distanceKm, 1)} km`;
}

function formatHydroAssociations(summary: CommunityInfrastructureSummary | null) {
  if (!summary?.associatedHydroSites.length) return "No nearby screening site";
  return summary.associatedHydroSites
    .slice(0, 2)
    .map(({ facility, distanceKm }) => `${facility.name} · ${formatDistance(distanceKm, 0)} km`)
    .join("; ");
}

function formatDistance(value: number, maximumFractionDigits: number) {
  return new Intl.NumberFormat("en-CA", { maximumFractionDigits }).format(value);
}

function CompactFact({ label, value }: { label: string; value: string }) {
  return (
    <div className="compact-fact">
      <div className="compact-fact__label">{label}</div>
      <div className="compact-fact__value">{value}</div>
    </div>
  );
}
