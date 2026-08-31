"use client";

import type { CSSProperties } from "react";
import type { PublicMapFeature } from "../../lib/explorer-types";
import { formatNumber, humanizeToken } from "../../lib/format";

type Props = {
  feature: PublicMapFeature;
  x: number;
  y: number;
  viewportWidth: number;
  viewportHeight: number;
  onPointerEnter: () => void;
  onPointerLeave: () => void;
  onSelect: () => void;
};

export function HoverCard({
  feature,
  x,
  y,
  viewportWidth,
  viewportHeight,
  onPointerEnter,
  onPointerLeave,
  onSelect,
}: Props) {
  const p = feature.properties;
  const cardWidth = 312;
  const cardHeightEstimate = p.feature_kind === "community" ? 270 : 255;
  const placeLeft = x + cardWidth + 32 > viewportWidth;
  const placeAbove = y + cardHeightEstimate + 24 > viewportHeight;

  const style: CSSProperties = {
    left: x,
    top: y,
    transform: `translate(${placeLeft ? "calc(-100% - 22px)" : "22px"}, ${
      placeAbove ? "calc(-100% + 18px)" : "-22px"
    })`,
  };

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
        <span>{p.feature_kind === "community" ? "Community" : "Hydrometric station"}</span>
        <span className="status-glyph" aria-hidden="true">
          {p.feature_kind === "community" ? "◌" : "●"}
        </span>
        <span>
          {p.feature_kind === "community" ? "Approx." : humanizeToken(p.evidence_status ?? "verified")}
        </span>
      </div>

      <div className="hover-card__title">
        {p.feature_kind === "hydrometric_station" ? p.station_number : p.name}
      </div>
      <div className="hover-card__subtitle">
        {p.feature_kind === "hydrometric_station" ? p.river_name : p.region}
      </div>

      {p.feature_kind === "community" ? (
        <div className="hover-card__facts">
          <CompactFact label="Fibre" value={humanizeToken(p.telecom_context)} />
          <CompactFact label="Marine" value={humanizeToken(p.marine_context)} />
          <CompactFact label="Road" value={humanizeToken(p.road_context)} />
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
          {p.feature_kind === "community"
            ? "Reference point · not a facility location"
            : "Official hydrometric station position"}
        </span>
        <button type="button" onClick={onSelect}>
          Inspect
          <span aria-hidden="true">↗</span>
        </button>
      </div>
    </div>
  );
}

function CompactFact({ label, value }: { label: string; value: string }) {
  return (
    <div className="compact-fact">
      <div className="compact-fact__label">{label}</div>
      <div className="compact-fact__value">{value}</div>
    </div>
  );
}
