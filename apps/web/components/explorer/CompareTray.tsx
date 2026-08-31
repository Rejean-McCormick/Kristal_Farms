"use client";

import type { PublicMapFeature } from "../../lib/explorer-types";

export function CompareTray({
  features,
  onRemove,
  onSelect,
}: {
  features: PublicMapFeature[];
  onRemove: (id: string) => void;
  onSelect: (id: string) => void;
}) {
  if (features.length === 0) return null;

  return (
    <div className="compare-tray" aria-label="Comparison tray">
      <div className="compare-tray__label">COMPARE · {features.length}/2</div>
      {features.map((feature, index) => (
        <div className="compare-chip" key={feature.properties.entity_id}>
          <button type="button" onClick={() => onSelect(feature.properties.entity_id)}>
            <span>{index === 0 ? "A" : "B"}</span>
            {feature.properties.feature_kind === "hydrometric_station"
              ? feature.properties.station_number
              : feature.properties.name}
          </button>
          <button
            type="button"
            aria-label={`Remove ${feature.properties.name} from comparison`}
            onClick={() => onRemove(feature.properties.entity_id)}
          >
            ×
          </button>
        </div>
      ))}
    </div>
  );
}
