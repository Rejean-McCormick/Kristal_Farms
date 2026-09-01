from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


WATERSHED_CONSTANTS = '''const WATERSHED_SOURCE = "watershed-boundaries";
const WATERSHED_FILL_LAYER = "watershed-boundaries-fill";
const WATERSHED_LINE_LAYER = "watershed-boundaries-line";
const WATERSHED_DATA_URL = "/data/watersheds/nhn_workunit_limits.geojson";
'''

WATERSHED_FUNCTIONS = r'''function addWatershedBoundaryLayers(map: MapLibreMap, visible: boolean) {
  if (!map.getSource(WATERSHED_SOURCE)) {
    map.addSource(WATERSHED_SOURCE, {
      type: "geojson",
      data: WATERSHED_DATA_URL,
    });
  }

  const layerVisibility = visible ? "visible" : "none";

  if (!map.getLayer(WATERSHED_FILL_LAYER)) {
    map.addLayer({
      id: WATERSHED_FILL_LAYER,
      type: "fill",
      source: WATERSHED_SOURCE,
      minzoom: 2,
      layout: { visibility: layerVisibility },
      paint: {
        "fill-color": "#83dce8",
        "fill-opacity": ["interpolate", ["linear"], ["zoom"], 2, 0.012, 5, 0.022, 8, 0.035, 12, 0.045],
      },
    });
  }

  if (!map.getLayer(WATERSHED_LINE_LAYER)) {
    map.addLayer({
      id: WATERSHED_LINE_LAYER,
      type: "line",
      source: WATERSHED_SOURCE,
      minzoom: 2,
      layout: { visibility: layerVisibility },
      paint: {
        "line-color": "#9be5ee",
        "line-opacity": ["interpolate", ["linear"], ["zoom"], 2, 0.28, 5, 0.38, 8, 0.5, 12, 0.6],
        "line-width": ["interpolate", ["linear"], ["zoom"], 2, 0.65, 6, 0.85, 10, 1.15, 14, 1.45],
        "line-blur": 0.15,
      },
    });
  }
}

function setWatershedBoundariesVisible(map: MapLibreMap, visible: boolean) {
  const value = visible ? "visible" : "none";
  for (const layerId of [WATERSHED_FILL_LAYER, WATERSHED_LINE_LAYER]) {
    if (map.getLayer(layerId)) map.setLayoutProperty(layerId, "visibility", value);
  }
}

'''

WATERSHED_ROW = '''          <label className="layer-row">
            <input
              type="checkbox"
              checked={visibleLayers.watershed_boundaries}
              onChange={(event) =>
                setVisibleLayers((current) => ({ ...current, watershed_boundaries: event.target.checked }))
              }
            />
            <span className="layer-symbol is-watershed_boundaries" aria-hidden="true" />
            <span>
              <strong>Watershed boundaries</strong>
              <small>NRCan NHN · sub-sub-drainage / work-unit limits · local snapshot</small>
            </span>
            <em>{visibleLayers.watershed_boundaries ? "ON" : "OFF"}</em>
          </label>
'''

WATERSHED_CSS = r'''

/* Kristal watershed boundary overlay */
.layer-symbol.is-watershed_boundaries {
  width: 15px;
  height: 12px;
  border: 1px solid rgba(155, 229, 238, .72);
  border-radius: 2px;
  background:
    linear-gradient(145deg, transparent 43%, rgba(155, 229, 238, .92) 45%, rgba(155, 229, 238, .92) 54%, transparent 56%),
    rgba(131, 220, 232, .045);
  box-shadow: 0 0 10px rgba(114, 220, 255, .05);
}
'''


def root() -> Path:
    return Path(__file__).resolve().parent


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Patch marker not found for {label}. The app version may have changed.")
    return text.replace(old, new, 1)


def backup(paths: list[Path], repo: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    directory = repo / ".overlay-backups" / f"watersheds-{stamp}"
    for path in paths:
        rel = path.relative_to(repo)
        target = directory / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    return directory


def patch_types(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "watershed_boundaries: boolean;" in text:
        return False
    text = replace_once(
        text,
        "  contextual_hydrography: boolean;\n",
        "  contextual_hydrography: boolean;\n  watershed_boundaries: boolean;\n",
        "ObservatoryVisibleLayers",
    )
    path.write_text(text, encoding="utf-8")
    return True


def patch_explorer(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False

    if "watershed_boundaries:" not in text:
        text = replace_once(
            text,
            "    contextual_hydrography: true,\n",
            "    contextual_hydrography: true,\n    watershed_boundaries: true,\n",
            "visible layer defaults",
        )
        changed = True

    if "is-watershed_boundaries" not in text:
        marker = '          <ContextLayerRow\n            id="contextual_hydrography"'
        if marker not in text:
            # Some later builds may insert another context row first. Anchor on
            # the first hydrography row without depending on the surrounding group.
            marker = '<ContextLayerRow\n            id="contextual_hydrography"'
            index = text.find(marker)
            if index < 0:
                raise RuntimeError("Could not find the contextual hydrography row in ObservatoryExplorer.tsx")
            line_start = text.rfind("\n", 0, index) + 1
            text = text[:line_start] + WATERSHED_ROW + text[line_start:]
        else:
            text = text.replace(marker, WATERSHED_ROW + marker, 1)
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def patch_map(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False

    if "const WATERSHED_SOURCE" not in text:
        marker = 'const RIVER_SELECTED_LAYER = "contextual-waterway-selected-layer";\n'
        text = replace_once(text, marker, marker + WATERSHED_CONSTANTS + "\n", "watershed map constants")
        changed = True

    if "addWatershedBoundaryLayers(map" not in text:
        text = replace_once(
            text,
            "      addContextualRiverOverlayLayers(map);\n",
            "      addContextualRiverOverlayLayers(map);\n      addWatershedBoundaryLayers(map, visibleLayersRef.current.watershed_boundaries);\n",
            "watershed layer initialization",
        )
        changed = True

    if "setWatershedBoundariesVisible(map, visibleLayers.watershed_boundaries);" not in text:
        text = replace_once(
            text,
            "    setBasemapLabelsVisible(map, basemapLayersRef.current.labelLayerIds, visibleLayers.labels);\n",
            "    setBasemapLabelsVisible(map, basemapLayersRef.current.labelLayerIds, visibleLayers.labels);\n"
            "    setWatershedBoundariesVisible(map, visibleLayers.watershed_boundaries);\n",
            "watershed visibility effect",
        )
        changed = True

    if "function addWatershedBoundaryLayers" not in text:
        marker = "function addContextualRiverOverlayLayers(map: MapLibreMap) {\n"
        text = replace_once(text, marker, WATERSHED_FUNCTIONS + marker, "watershed map helper functions")
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def patch_css(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if ".layer-symbol.is-watershed_boundaries" in text:
        return False
    path.write_text(text.rstrip() + WATERSHED_CSS + "\n", encoding="utf-8")
    return True


def show(title: str, message: str, error: bool = False) -> None:
    try:
        import tkinter as tk
        from tkinter import messagebox
        window = tk.Tk()
        window.withdraw()
        if error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)
        window.destroy()
    except Exception:
        pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-fetch", action="store_true", help="Patch the app but do not download watershed data.")
    parser.add_argument("--silent", action="store_true", help="Do not display a GUI completion dialog.")
    args = parser.parse_args()

    repo = root()
    files = {
        "types": repo / "apps" / "web" / "lib" / "explorer-types.ts",
        "explorer": repo / "apps" / "web" / "components" / "explorer" / "ObservatoryExplorer.tsx",
        "map": repo / "apps" / "web" / "components" / "explorer" / "ObservatoryMap.tsx",
        "css": repo / "apps" / "web" / "app" / "globals.css",
    }

    missing = [str(path) for path in files.values() if not path.exists()]
    if missing:
        message = "Missing expected Observatory file(s):\n\n" + "\n".join(missing)
        if not args.silent:
            show("Kristal Watershed Overlay — error", message, True)
        return 2

    try:
        backup_dir = backup(list(files.values()), repo)
        changes = {
            "explorer-types.ts": patch_types(files["types"]),
            "ObservatoryExplorer.tsx": patch_explorer(files["explorer"]),
            "ObservatoryMap.tsx": patch_map(files["map"]),
            "globals.css": patch_css(files["css"]),
        }

        fetch_status = "skipped"
        if not args.no_fetch:
            fetcher = repo / "FETCH_WATERSHEDS.pyw"
            completed = subprocess.run(
                [sys.executable, str(fetcher), "--northern-atlas", "--silent"],
                cwd=str(repo),
                timeout=180,
            )
            fetch_status = "ready" if completed.returncode == 0 else "download failed — run FETCH_WATERSHEDS.pyw manually"

        changed_names = [name for name, changed in changes.items() if changed]
        message = (
            "Watershed overlay installed.\n\n"
            f"Patched: {', '.join(changed_names) if changed_names else 'already installed'}\n"
            f"Watershed data: {fetch_status}\n"
            f"Backup: {backup_dir}\n\n"
            "Next: run REBUILD_OBSERVATORY.pyw"
        )
        if not args.silent:
            show("Kristal Watershed Overlay", message)
        return 0
    except Exception as exc:
        if not args.silent:
            show("Kristal Watershed Overlay — error", str(exc), True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
