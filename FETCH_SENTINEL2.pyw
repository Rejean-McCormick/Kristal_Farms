# -*- coding: utf-8 -*-
"""
FETCH_SENTINEL2.pyw
Kristal Farms - Sentinel-2 L2A local imagery fetcher

- No Copernicus account required.
- No API key required.
- Searches public Element 84 Earth Search Sentinel-2 L2A catalog.
- Reads only the requested AOI window from public Cloud-Optimized GeoTIFFs.
- Creates local True Color GeoTIFF (B04/B03/B02).
- Optionally converts it to local PMTiles with rio-pmtiles.
"""

from __future__ import annotations

import json
import math
import os
import queue
import subprocess
import tempfile
import threading
import traceback
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

EARTH_SEARCH = "https://earth-search.aws.element84.com/v1"
SEARCH_URL = f"{EARTH_SEARCH}/search"
COLLECTION = "sentinel-2-l2a"
USER_AGENT = "Kristal-Farms-Sentinel2-Fetcher/1.0"

DATA_ROOT = Path(r"C:\KristalData")
SOURCE_DIR = DATA_ROOT / "imagery" / "source"
PMTILES_DIR = DATA_ROOT / "imagery" / "pmtiles"
VENV = DATA_ROOT / "tools" / "imagery-venv"
PYTHON = VENV / "Scripts" / "python.exe"
RIO = VENV / "Scripts" / "rio.exe"
PMTILES_EXE = DATA_ROOT / "bin" / "pmtiles.exe"
LOG_PATH = DATA_ROOT / "sentinel2-fetch.log"

PRESETS = {
    "Postville": (-59.7853, 54.9106),
    "Nain": (-61.6925, 56.5428),
    "Hopedale": (-60.2117, 55.4542),
    "Makkovik": (-59.1765, 55.0869),
    "Rigolet": (-58.4289, 54.1797),
    "Kuujjuaq": (-68.4043, 58.1003),
    "Inukjuak": (-78.1014, 58.4547),
    "Puvirnituq": (-77.2756, 60.0338),
    "Custom": (None, None),
}

RASTER_HELPER = '\nimport json\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport rasterio\nfrom rasterio.windows import from_bounds\nfrom rasterio.warp import transform_bounds\n\ncfg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))\nbbox = cfg["bbox"]\nassets = cfg["assets"]\nscales = cfg["scales"]\noutput = Path(cfg["output"])\n\nenv_options = {\n    "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",\n    "CPL_VSIL_CURL_ALLOWED_EXTENSIONS": ".tif,.TIF",\n    "GDAL_HTTP_MULTIRANGE": "YES",\n    "GDAL_HTTP_MERGE_CONSECUTIVE_RANGES": "YES",\n    "VSI_CACHE": "TRUE",\n    "VSI_CACHE_SIZE": "67108864",\n    "GDAL_HTTP_TIMEOUT": "60",\n}\n\narrays = []\nvalid_masks = []\n\nwith rasterio.Env(**env_options):\n    with rasterio.open(assets["red"]) as base:\n        target_bounds = transform_bounds(\n            "EPSG:4326", base.crs, *bbox, densify_pts=21\n        )\n        window = from_bounds(*target_bounds, transform=base.transform)\n        window = window.round_offsets().round_lengths()\n        full = rasterio.windows.Window(0, 0, base.width, base.height)\n        window = window.intersection(full)\n\n        width = int(window.width)\n        height = int(window.height)\n        if width <= 0 or height <= 0:\n            raise RuntimeError("Fenêtre Sentinel vide après reprojection.")\n\n        pixel_count = width * height\n        if pixel_count > 70_000_000:\n            raise RuntimeError(\n                f"AOI trop grande ({width} x {height} pixels). "\n                "Réduis le rayon à 30 km ou moins."\n            )\n\n        print(f"WINDOW {width}x{height} pixels (~{pixel_count/1_000_000:.1f} MP)")\n        out_transform = base.window_transform(window)\n        profile = base.profile.copy()\n        profile.update(\n            driver="GTiff",\n            width=width,\n            height=height,\n            count=3,\n            dtype="uint8",\n            transform=out_transform,\n            crs=base.crs,\n            nodata=0,\n            tiled=True,\n            blockxsize=512,\n            blockysize=512,\n            compress="DEFLATE",\n            predictor=2,\n            interleave="pixel",\n            BIGTIFF="IF_SAFER",\n        )\n\n    for key in ("red", "green", "blue"):\n        print(f"READ {key.upper()}")\n        with rasterio.open(assets[key]) as src:\n            target_bounds = transform_bounds(\n                "EPSG:4326", src.crs, *bbox, densify_pts=21\n            )\n            win = from_bounds(*target_bounds, transform=src.transform)\n            win = win.round_offsets().round_lengths()\n            full = rasterio.windows.Window(0, 0, src.width, src.height)\n            win = win.intersection(full)\n\n            arr = src.read(1, window=win, masked=True)\n\n            scale = float(scales[key][0])\n            offset = float(scales[key][1])\n            reflectance = arr.astype("float32") * scale + offset\n\n            # Copernicus True Color examples use a 2.5x reflectance gain.\n            display = np.clip(reflectance * 2.5, 0.0, 1.0)\n            display = np.power(display, 1.0 / 1.08)\n\n            byte = np.ma.filled(display * 255.0, 0).astype("uint8")\n            arrays.append(byte)\n            valid_masks.append(~np.ma.getmaskarray(arr))\n\n    min_h = min(a.shape[0] for a in arrays)\n    min_w = min(a.shape[1] for a in arrays)\n    arrays = [a[:min_h, :min_w] for a in arrays]\n    valid_masks = [m[:min_h, :min_w] for m in valid_masks]\n\n    valid = valid_masks[0] & valid_masks[1] & valid_masks[2]\n    rgb = np.stack(arrays, axis=0)\n    rgb[:, ~valid] = 0\n\n    profile["height"] = min_h\n    profile["width"] = min_w\n\n    output.parent.mkdir(parents=True, exist_ok=True)\n    with rasterio.open(output, "w", **profile) as dst:\n        dst.write(rgb)\n        dst.update_tags(\n            source="Sentinel-2 L2A COG via Element 84 Earth Search",\n            stac_item=cfg["item_id"],\n            acquired=cfg["acquired"],\n            cloud_cover=str(cfg["cloud"]),\n            earth_search=cfg["earth_search"],\n            processing="True Color RGB B04/B03/B02; gain 2.5; gamma 1.08",\n        )\n\nprint(f"OUTPUT {output}")\nprint(f"BYTES {output.stat().st_size}")\n'


@dataclass
class Candidate:
    item: dict
    cloud: float
    overlap: float
    acquired: str
    score: float


def ensure_dirs():
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    PMTILES_DIR.mkdir(parents=True, exist_ok=True)
    DATA_ROOT.mkdir(parents=True, exist_ok=True)


def append_log(message):
    ensure_dirs()
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(str(message).rstrip() + "\n")


def slugify(value):
    out = []
    for ch in value.lower().strip():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-") or "satellite"


def bbox_from_center(lon, lat, radius_km):
    lat_delta = radius_km / 111.32
    lon_scale = max(math.cos(math.radians(lat)), 0.15)
    lon_delta = radius_km / (111.32 * lon_scale)
    return [lon - lon_delta, lat - lat_delta, lon + lon_delta, lat + lat_delta]


def bbox_overlap_fraction(a, b):
    west = max(a[0], b[0])
    south = max(a[1], b[1])
    east = min(a[2], b[2])
    north = min(a[3], b[3])
    if east <= west or north <= south:
        return 0.0
    area_a = max((a[2] - a[0]) * (a[3] - a[1]), 1e-12)
    return ((east - west) * (north - south)) / area_a


def post_json(url, payload, timeout=45):
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/geo+json, application/json",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def search_year(bbox, year, max_cloud, emit):
    payload = {
        "collections": [COLLECTION],
        "bbox": bbox,
        "datetime": f"{year}-06-01T00:00:00Z/{year}-09-30T23:59:59Z",
        "limit": 100,
        "query": {"eo:cloud_cover": {"lt": max_cloud}},
        "sortby": [
            {"field": "properties.eo:cloud_cover", "direction": "asc"},
            {"field": "properties.datetime", "direction": "desc"},
        ],
    }
    try:
        data = post_json(SEARCH_URL, payload)
    except urllib.error.HTTPError as exc:
        if exc.code == 400:
            payload.pop("sortby", None)
            data = post_json(SEARCH_URL, payload)
        else:
            raise
    features = data.get("features") or []
    emit(f"{year}: {len(features)} scène(s) sous {max_cloud:.0f}% nuages")
    return features


def rank_candidates(items, aoi_bbox):
    candidates = []
    for item in items:
        props = item.get("properties") or {}
        item_bbox = item.get("bbox") or [0, 0, 0, 0]
        try:
            cloud = float(props.get("eo:cloud_cover", 100.0))
        except Exception:
            cloud = 100.0
        overlap = bbox_overlap_fraction(aoi_bbox, item_bbox)
        acquired = str(props.get("datetime") or "")
        try:
            acquired_year = int(acquired[:4])
        except Exception:
            acquired_year = 0
        assets = item.get("assets") or {}
        if not all(key in assets for key in ("red", "green", "blue")):
            continue
        score = cloud + (1.0 - overlap) * 120.0 - acquired_year * 0.001
        candidates.append(Candidate(item, cloud, overlap, acquired, score))
    candidates.sort(key=lambda c: c.score)
    return candidates


def choose_candidate(bbox, summer_count, max_cloud, emit):
    current_year = date.today().year
    years = list(range(current_year, current_year - summer_count, -1))
    items = []
    emit("Recherche Earth Search: " + ", ".join(map(str, years)))
    for year in years:
        items.extend(search_year(bbox, year, max_cloud, emit))

    if not items:
        emit("Aucune scène sous le seuil. Recherche élargie...")
        for year in years:
            items.extend(search_year(bbox, year, 101.0, emit))

    candidates = rank_candidates(items, bbox)
    if not candidates:
        raise RuntimeError("Aucune scène Sentinel-2 L2A compatible trouvée.")

    complete = [c for c in candidates if c.overlap >= 0.985]
    selected = complete[0] if complete else candidates[0]
    emit(
        f"Choix: {selected.item.get('id')} · {selected.acquired[:10]} · "
        f"{selected.cloud:.1f}% nuages · couverture AOI {selected.overlap*100:.1f}%"
    )
    if selected.overlap < 0.90:
        emit("ATTENTION: réduire le rayon si des bords vides apparaissent.")
    return selected


def asset_href(item, key):
    asset = (item.get("assets") or {}).get(key) or {}
    href = asset.get("href")
    if not href:
        raise RuntimeError(f"Asset absent: {key}")
    return str(href)


def asset_scale_offset(item, key):
    asset = (item.get("assets") or {}).get(key) or {}
    bands = asset.get("raster:bands") or []
    band = bands[0] if bands else {}
    try:
        scale = float(band.get("scale", 0.0001))
    except Exception:
        scale = 0.0001
    try:
        offset = float(band.get("offset", 0.0))
    except Exception:
        offset = 0.0
    return [scale, offset]


def create_true_color(candidate, bbox, output_tif, emit):
    if not PYTHON.exists():
        raise RuntimeError(f"Python imagery venv introuvable: {PYTHON}")

    config = {
        "bbox": bbox,
        "assets": {
            "red": asset_href(candidate.item, "red"),
            "green": asset_href(candidate.item, "green"),
            "blue": asset_href(candidate.item, "blue"),
        },
        "scales": {
            key: asset_scale_offset(candidate.item, key)
            for key in ("red", "green", "blue")
        },
        "output": str(output_tif),
        "item_id": candidate.item.get("id"),
        "acquired": candidate.acquired,
        "cloud": candidate.cloud,
        "earth_search": EARTH_SEARCH,
    }

    with tempfile.TemporaryDirectory(prefix="kristal-sentinel-") as tmp:
        tmpdir = Path(tmp)
        helper_path = tmpdir / "crop_rgb.py"
        config_path = tmpdir / "config.json"
        helper_path.write_text(RASTER_HELPER, encoding="utf-8")
        config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")

        emit("Lecture ciblée COG B04/B03/B02...")
        emit("Pas de téléchargement de scène Sentinel complète.")

        process = subprocess.Popen(
            [str(PYTHON), str(helper_path), str(config_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        for line in process.stdout:
            emit(line.rstrip())
        code = process.wait()
        if code != 0:
            raise RuntimeError(f"Création GeoTIFF échouée (code {code}).")


def convert_pmtiles(input_tif, output_pmtiles, title, emit):
    if not RIO.exists():
        raise RuntimeError(f"rio.exe introuvable: {RIO}")
    if output_pmtiles.exists():
        output_pmtiles.unlink()

    command = [
        str(RIO), "pmtiles", str(input_tif), str(output_pmtiles),
        "--name", title,
        "--description", "Kristal Farms local Sentinel-2 satellite snapshot",
        "--attribution", "Contains modified Copernicus Sentinel data",
        "--format", "WEBP",
        "--tile-size", "512",
        "--zoom-levels", "7..13",
        "--resampling", "bilinear",
        "--co", "QUALITY=82",
        "--exclude-empty-tiles",
    ]
    emit("Conversion GeoTIFF -> PMTiles (WEBP Z7..Z13)...")
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    for line in process.stdout:
        emit(line.rstrip())
    code = process.wait()
    if code != 0:
        raise RuntimeError(f"rio pmtiles échoué (code {code}).")

    if PMTILES_EXE.exists():
        emit("Vérification PMTiles...")
        completed = subprocess.run(
            [str(PMTILES_EXE), "verify", str(output_pmtiles)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        if completed.stdout:
            emit(completed.stdout.strip())
        if completed.returncode != 0:
            raise RuntimeError("pmtiles verify a échoué.")

    emit(f"PMTiles: {output_pmtiles} ({output_pmtiles.stat().st_size/1024/1024:.1f} MB)")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Kristal Farms — Sentinel-2 Fetcher")
        self.root.geometry("760x650")
        self.root.minsize(700, 590)
        self.events = queue.Queue()
        self.running = False

        outer = ttk.Frame(root, padding=16)
        outer.pack(fill="both", expand=True)

        ttk.Label(
            outer,
            text="Kristal Sentinel-2 Local Snapshot",
            font=("Segoe UI", 16, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            outer,
            text="Public Earth Search COGs · sans clé · lecture AOI ciblée · GeoTIFF / PMTiles",
        ).pack(anchor="w", pady=(2, 14))

        form = ttk.Frame(outer)
        form.pack(fill="x")

        self.place = tk.StringVar(value="Postville")
        self.lon = tk.StringVar(value=str(PRESETS["Postville"][0]))
        self.lat = tk.StringVar(value=str(PRESETS["Postville"][1]))
        self.radius = tk.StringVar(value="25")
        self.summers = tk.StringVar(value="2")
        self.cloud = tk.StringVar(value="20")
        self.file_id = tk.StringVar(value="postville")

        labels = [
            ("Zone", self.place),
            ("Longitude", self.lon),
            ("Latitude", self.lat),
            ("Rayon AOI (km)", self.radius),
            ("Étés à rechercher", self.summers),
            ("Nuages max (%)", self.cloud),
            ("ID fichier", self.file_id),
        ]

        for row, (label, variable) in enumerate(labels):
            ttk.Label(form, text=label).grid(row=row, column=0, sticky="w", pady=4)
            if row == 0:
                widget = ttk.Combobox(
                    form, textvariable=variable,
                    values=list(PRESETS.keys()), state="readonly"
                )
                widget.bind("<<ComboboxSelected>>", self.on_place)
            else:
                widget = ttk.Entry(form, textvariable=variable)
            widget.grid(row=row, column=1, sticky="ew", pady=4)
        form.columnconfigure(1, weight=1)

        self.make_pmtiles = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            outer,
            text="Créer aussi le PMTiles local (WEBP, Z7–Z13)",
            variable=self.make_pmtiles,
        ).pack(anchor="w", pady=(12, 6))

        ttk.Label(
            outer,
            text=(
                "Pilote recommandé: rayon 20–30 km. "
                "Le script lit uniquement la fenêtre utile dans les COGs distants."
            ),
            wraplength=710,
        ).pack(anchor="w", pady=(0, 12))

        buttons = ttk.Frame(outer)
        buttons.pack(fill="x", pady=(0, 10))
        self.start_button = ttk.Button(
            buttons, text="Chercher + télécharger", command=self.start
        )
        self.start_button.pack(side="left")
        ttk.Button(
            buttons,
            text=r"Ouvrir C:\KristalData\imagery",
            command=lambda: os.startfile(str(DATA_ROOT / "imagery")),
        ).pack(side="left", padx=(8, 0))

        self.progress = ttk.Progressbar(outer, mode="indeterminate")
        self.progress.pack(fill="x", pady=(0, 10))

        self.logbox = tk.Text(outer, height=18, wrap="word", font=("Consolas", 9))
        self.logbox.pack(fill="both", expand=True)
        self.root.after(150, self.poll)

    def on_place(self, _event=None):
        name = self.place.get()
        lon, lat = PRESETS[name]
        if lon is not None:
            self.lon.set(str(lon))
            self.lat.set(str(lat))
            self.file_id.set(slugify(name))

    def emit(self, message):
        self.events.put(("log", str(message)))
        append_log(str(message))

    def start(self):
        if self.running:
            return
        try:
            place = self.place.get()
            lon = float(self.lon.get().strip())
            lat = float(self.lat.get().strip())
            radius = float(self.radius.get().strip())
            summers = int(self.summers.get().strip())
            cloud = float(self.cloud.get().strip())
            file_id = slugify(self.file_id.get())
            make_pmtiles = bool(self.make_pmtiles.get())

            if not (-180 <= lon <= 180 and -90 <= lat <= 90):
                raise ValueError("Longitude/latitude invalides.")
            if not (1 <= radius <= 40):
                raise ValueError("Rayon accepté: 1 à 40 km.")
            if not (1 <= summers <= 6):
                raise ValueError("Étés à rechercher: 1 à 6.")
            if not (0 <= cloud <= 100):
                raise ValueError("Nuages max: 0 à 100.")
        except Exception as exc:
            messagebox.showerror("Paramètres invalides", str(exc))
            return

        self.running = True
        self.start_button.configure(state="disabled")
        self.progress.start(10)
        self.logbox.delete("1.0", "end")

        threading.Thread(
            target=self.worker,
            args=(place, lon, lat, radius, summers, cloud, file_id, make_pmtiles),
            daemon=True,
        ).start()

    def worker(self, place, lon, lat, radius, summers, cloud, file_id, make_pmtiles):
        try:
            ensure_dirs()
            bbox = bbox_from_center(lon, lat, radius)
            self.emit("=" * 64)
            self.emit(
                f"AOI {file_id}: lon {lon:.5f}, lat {lat:.5f}, rayon {radius:.1f} km"
            )
            self.emit("BBOX: " + ", ".join(f"{v:.6f}" for v in bbox))

            candidate = choose_candidate(bbox, summers, cloud, self.emit)
            date_slug = candidate.acquired[:10].replace("-", "") or "unknown"
            tif = SOURCE_DIR / f"{file_id}_sentinel2_{date_slug}.tif"

            create_true_color(candidate, bbox, tif, self.emit)
            self.emit(f"GeoTIFF: {tif} ({tif.stat().st_size/1024/1024:.1f} MB)")

            pmtiles = None
            if make_pmtiles:
                pmtiles = PMTILES_DIR / f"{file_id}.pmtiles"
                convert_pmtiles(tif, pmtiles, f"Sentinel-2 — {place}", self.emit)

            manifest = {
                "id": file_id,
                "place": place,
                "center": [lon, lat],
                "radius_km": radius,
                "bbox": bbox,
                "source": "Sentinel-2 L2A COG via Element 84 Earth Search",
                "earth_search_item": candidate.item.get("id"),
                "acquired": candidate.acquired,
                "cloud_cover_percent": candidate.cloud,
                "aoi_scene_overlap": candidate.overlap,
                "geotiff": str(tif),
                "pmtiles": str(pmtiles) if pmtiles else None,
                "created_at": datetime.now().astimezone().isoformat(),
                "attribution": "Contains modified Copernicus Sentinel data",
            }
            manifest_path = SOURCE_DIR / f"{file_id}_sentinel2_manifest.json"
            manifest_path.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            self.emit(f"Manifest: {manifest_path}")
            self.emit("TERMINÉ")
            self.events.put(("done", {
                "tif": str(tif),
                "pmtiles": str(pmtiles) if pmtiles else None,
                "scene": candidate.item.get("id"),
                "date": candidate.acquired[:10],
                "cloud": candidate.cloud,
            }))
        except Exception as exc:
            self.emit("ERREUR: " + str(exc))
            self.emit(traceback.format_exc())
            self.events.put(("error", str(exc)))

    def poll(self):
        try:
            while True:
                kind, payload = self.events.get_nowait()
                if kind == "log":
                    self.logbox.insert("end", payload + "\n")
                    self.logbox.see("end")
                elif kind == "done":
                    self.running = False
                    self.progress.stop()
                    self.start_button.configure(state="normal")
                    msg = (
                        "Téléchargement terminé.\n\n"
                        f"Scène: {payload['scene']}\n"
                        f"Date: {payload['date']}\n"
                        f"Nuages scène: {payload['cloud']:.1f}%\n\n"
                        f"GeoTIFF:\n{payload['tif']}"
                    )
                    if payload["pmtiles"]:
                        msg += f"\n\nPMTiles:\n{payload['pmtiles']}"
                    messagebox.showinfo("Kristal Sentinel-2 — terminé", msg)
                elif kind == "error":
                    self.running = False
                    self.progress.stop()
                    self.start_button.configure(state="normal")
                    messagebox.showerror(
                        "Kristal Sentinel-2 — erreur",
                        payload + f"\n\nJournal:\n{LOG_PATH}",
                    )
        except queue.Empty:
            pass
        self.root.after(150, self.poll)


def main():
    ensure_dirs()
    root = tk.Tk()
    try:
        style = ttk.Style(root)
        if "vista" in style.theme_names():
            style.theme_use("vista")
    except Exception:
        pass
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
