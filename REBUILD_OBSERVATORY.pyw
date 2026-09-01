# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import queue
import shutil
import socket
import subprocess
import sys
import threading
import time
import traceback
import urllib.request
import webbrowser
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

REPO_ROOT = Path(__file__).resolve().parent
WEB_ROOT = REPO_ROOT / "apps" / "web"

DATA_ROOT = Path(r"C:\KristalData")
SOURCE_DIR = DATA_ROOT / "imagery" / "source"
PMTILES_DIR = DATA_ROOT / "imagery" / "pmtiles"
PMTILES_EXE = DATA_ROOT / "bin" / "pmtiles.exe"

IMAGERY_SERVER_SCRIPT = REPO_ROOT / "START_IMAGERY_SERVER.ps1"
REGISTER_SCRIPT = REPO_ROOT / "REGISTER_LOCAL_IMAGERY.ps1"
HYDRO_SCOPE_SCRIPT = REPO_ROOT / "pipelines" / "publish" / "build_kristal_hydro_scope.py"
COMMUNITY_INFRA_SCRIPT = REPO_ROOT / "pipelines" / "publish" / "build_community_infrastructure.py"

PORT_IMAGERY = 8765
PORT_WEB = 3000
LOG_PATH = DATA_ROOT / "rebuild-observatory.log"


@dataclass
class ImageryRecord:
    manifest_path: Path
    id: str
    place: str
    acquired: str
    source: str
    attribution: str
    pmtiles_path: Path
    created_at: str

    @property
    def label(self) -> str:
        d = self.acquired[:10] if self.acquired else "unknown date"
        return f"{self.place} — {d} — {self.pmtiles_path.name}"


def ensure_dirs():
    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    PMTILES_DIR.mkdir(parents=True, exist_ok=True)


def log_line(msg):
    ensure_dirs()
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(str(msg).rstrip() + "\n")


def find_pwsh():
    for name in ("pwsh.exe", "pwsh", "powershell.exe", "powershell"):
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError("PowerShell / pwsh introuvable.")


def http_text(url, timeout=3):
    req = urllib.request.Request(url, headers={"User-Agent": "Kristal-Rebuild/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def url_ok(url, timeout=2):
    try:
        http_text(url, timeout)
        return True
    except Exception:
        return False


def port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0


def load_records():
    records = []
    for path in SOURCE_DIR.glob("*_sentinel2_manifest.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            image_id = str(data.get("id") or "").strip()
            pmtiles_value = data.get("pmtiles")
            if not image_id or not pmtiles_value:
                continue

            pmtiles_path = Path(str(pmtiles_value))
            if not pmtiles_path.exists():
                fallback = PMTILES_DIR / f"{image_id}.pmtiles"
                if fallback.exists():
                    pmtiles_path = fallback
                else:
                    continue

            records.append(
                ImageryRecord(
                    manifest_path=path,
                    id=image_id,
                    place=str(data.get("place") or image_id),
                    acquired=str(data.get("acquired") or ""),
                    source=str(data.get("source") or "Sentinel-2 L2A / Earth Search"),
                    attribution=str(
                        data.get("attribution")
                        or "Contains modified Copernicus Sentinel data"
                    ),
                    pmtiles_path=pmtiles_path,
                    created_at=str(data.get("created_at") or ""),
                )
            )
        except Exception:
            pass

    def key(rec):
        try:
            return datetime.fromisoformat(
                rec.created_at.replace("Z", "+00:00")
            ).timestamp()
        except Exception:
            try:
                return rec.manifest_path.stat().st_mtime
            except Exception:
                return 0

    return sorted(records, key=key, reverse=True)


def ps_capture(command):
    completed = subprocess.run(
        [
            find_pwsh(),
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            command,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=30,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    output = completed.stdout or ""
    if completed.returncode != 0:
        raise RuntimeError(output.strip() or "PowerShell command failed.")
    return output.strip()


def get_listening_pid(port):
    cmd = (
        f"$c = Get-NetTCPConnection -LocalPort {port} -State Listen "
        "-ErrorAction SilentlyContinue | Select-Object -First 1; "
        "if ($c) { Write-Output $c.OwningProcess }"
    )
    try:
        out = ps_capture(cmd).strip()
        return int(out) if out else None
    except Exception:
        return None


def get_cmdline(pid):
    cmd = (
        f'$p = Get-CimInstance Win32_Process -Filter "ProcessId={pid}" '
        "-ErrorAction SilentlyContinue; "
        "if ($p) { Write-Output $p.CommandLine }"
    )
    try:
        return ps_capture(cmd)
    except Exception:
        return ""


def stop_tree(pid):
    completed = subprocess.run(
        ["taskkill", "/PID", str(pid), "/T", "/F"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=20,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    if completed.returncode not in (0, 128):
        raise RuntimeError((completed.stdout or "").strip() or f"Stop PID {pid} failed.")


def looks_like_kristal():
    try:
        page = http_text("http://127.0.0.1:3000/", 2.5).lower()
        return (
            "kristal farms" in page
            or "northern atlas" in page
            or "observatory" in page
        )
    except Exception:
        return False


def start_imagery_server(record, emit):
    tilejson = f"http://127.0.0.1:{PORT_IMAGERY}/{record.id}.json"

    if url_ok(tilejson):
        emit("Serveur PMTiles local déjà actif.")
        return

    if port_open(PORT_IMAGERY):
        raise RuntimeError(
            f"Port {PORT_IMAGERY} occupé mais {record.id}.json inaccessible."
        )

    if not IMAGERY_SERVER_SCRIPT.exists():
        raise RuntimeError(f"Script absent: {IMAGERY_SERVER_SCRIPT}")

    if not PMTILES_EXE.exists():
        raise RuntimeError(f"PMTiles absent: {PMTILES_EXE}")

    emit("Démarrage serveur PMTiles local...")

    startup = subprocess.STARTUPINFO()
    startup.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startup.wShowWindow = 6

    subprocess.Popen(
        [
            find_pwsh(),
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(IMAGERY_SERVER_SCRIPT),
        ],
        cwd=str(REPO_ROOT),
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        startupinfo=startup,
    )

    deadline = time.time() + 20
    while time.time() < deadline:
        if url_ok(tilejson, 1.5):
            emit(f"PMTiles OK: {tilejson}")
            return
        time.sleep(0.5)

    raise RuntimeError(f"TileJSON ne répond pas: {tilejson}")


def register_imagery(record, emit):
    if not REGISTER_SCRIPT.exists():
        raise RuntimeError(f"Script absent: {REGISTER_SCRIPT}")

    emit(f"Enregistrement: {record.label}")

    cmd = [
        find_pwsh(),
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(REGISTER_SCRIPT),
        "-Id",
        record.id,
        "-Title",
        f"Sentinel-2 — {record.place}",
        "-Source",
        record.source,
        "-Acquired",
        record.acquired[:10] if record.acquired else "",
        "-Attribution",
        record.attribution,
    ]

    completed = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=30,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    output = (completed.stdout or "").strip()
    if output:
        for line in output.splitlines():
            emit(line)

    if completed.returncode != 0:
        raise RuntimeError(output or "REGISTER_LOCAL_IMAGERY.ps1 failed.")


def publish_hydro_scope(emit):
    if not HYDRO_SCOPE_SCRIPT.exists():
        emit("Hydro scope publisher absent; using existing published artifact.")
        return

    emit("Publication du scope hydro côtier Kristal...")
    completed = subprocess.run(
        [sys.executable, str(HYDRO_SCOPE_SCRIPT)],
        cwd=str(REPO_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=120,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    output = (completed.stdout or "").strip()
    if output:
        for line in output.splitlines():
            emit(line)
    if completed.returncode != 0:
        raise RuntimeError(output or "Hydro scope publication failed.")


def publish_community_infrastructure(emit):
    if not COMMUNITY_INFRA_SCRIPT.exists():
        emit("Community infrastructure publisher absent; using existing published artifact.")
        return

    emit("Publication population + aéroports + accès maritimes...")
    completed = subprocess.run(
        [sys.executable, str(COMMUNITY_INFRA_SCRIPT)],
        cwd=str(REPO_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=120,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    output = (completed.stdout or "").strip()
    if output:
        for line in output.splitlines():
            emit(line)
    if completed.returncode != 0:
        raise RuntimeError(output or "Community infrastructure publication failed.")


def stop_existing_web(emit):
    if not port_open(PORT_WEB):
        emit("Aucun serveur sur le port 3000.")
        return

    if not looks_like_kristal():
        raise RuntimeError(
            "Port 3000 utilisé par un serveur qui ne semble pas être Kristal; "
            "arrêt automatique refusé."
        )

    pid = get_listening_pid(PORT_WEB)
    if not pid:
        raise RuntimeError("Impossible de trouver le PID du serveur Kristal.")

    emit(f"Arrêt ancien serveur Kristal PID {pid}...")
    cmdline = get_cmdline(pid)
    if cmdline:
        emit("Processus: " + cmdline[:180])

    stop_tree(pid)

    deadline = time.time() + 10
    while time.time() < deadline:
        if not port_open(PORT_WEB):
            emit("Ancien serveur arrêté.")
            return
        time.sleep(0.35)

    raise RuntimeError("Le port 3000 est toujours occupé.")


def clear_next(emit):
    target = WEB_ROOT / ".next"
    if target.exists():
        emit("Suppression apps/web/.next...")
        shutil.rmtree(target, ignore_errors=False)


def ensure_node_modules(emit):
    pkg = WEB_ROOT / "node_modules" / "maplibre-gl" / "package.json"
    if pkg.exists():
        emit("node_modules / MapLibre: OK")
        return

    emit("Dépendances absentes -> npm ci...")

    completed = subprocess.run(
        ["npm.cmd", "ci"],
        cwd=str(WEB_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=600,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    output = (completed.stdout or "").strip()
    if output:
        for line in output.splitlines():
            emit(line)

    if completed.returncode != 0:
        raise RuntimeError(output or "npm ci failed.")

    if not pkg.exists():
        raise RuntimeError("maplibre-gl/package.json toujours absent après npm ci.")


def start_web(emit):
    emit("Démarrage npm run dev...")

    startup = subprocess.STARTUPINFO()
    startup.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startup.wShowWindow = 6

    subprocess.Popen(
        ["cmd.exe", "/k", "npm run dev"],
        cwd=str(WEB_ROOT),
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        startupinfo=startup,
    )

    deadline = time.time() + 45
    while time.time() < deadline:
        try:
            page = http_text("http://127.0.0.1:3000/", 2).lower()
            if (
                "kristal farms" in page
                or "northern atlas" in page
                or "observatory" in page
            ):
                emit("Observatory prêt: http://localhost:3000")
                return
        except Exception:
            pass
        time.sleep(0.75)

    raise RuntimeError("Observatory n'a pas répondu dans les 45 secondes.")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Kristal Farms — Rebuild Observatory")
        self.root.geometry("780x560")
        self.root.minsize(720, 500)

        self.events = queue.Queue()
        self.running = False
        self.records = load_records()

        outer = ttk.Frame(root, padding=16)
        outer.pack(fill="both", expand=True)

        ttk.Label(
            outer,
            text="Rebuild Observatory",
            font=("Segoe UI", 17, "bold"),
        ).pack(anchor="w")

        ttk.Label(
            outer,
            text=(
                "Satellite local → PMTiles → registration → clean .next → restart Next.js"
            ),
        ).pack(anchor="w", pady=(2, 14))

        if not (WEB_ROOT / "package.json").exists():
            ttk.Label(
                outer,
                text="ERREUR: place ce .pyw à la racine du repo Kristal.",
            ).pack(anchor="w")
            return

        row = ttk.Frame(outer)
        row.pack(fill="x", pady=(0, 12))
        ttk.Label(row, text="Imagery active").pack(side="left")

        labels = [r.label for r in self.records]
        self.selected = tk.StringVar(
            value=labels[0] if labels else "(aucun manifest Sentinel trouvé)"
        )

        self.combo = ttk.Combobox(
            row,
            textvariable=self.selected,
            values=labels,
            state="readonly" if labels else "disabled",
            width=66,
        )
        self.combo.pack(side="left", fill="x", expand=True, padx=(12, 0))

        self.open_browser_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            outer,
            text="Ouvrir Observatory après le rebuild",
            variable=self.open_browser_var,
        ).pack(anchor="w", pady=(0, 10))

        ttk.Label(
            outer,
            text=(
                "Le port 3000 n'est arrêté automatiquement que si la page "
                "détectée ressemble à Kristal Farms."
            ),
            wraplength=730,
        ).pack(anchor="w", pady=(0, 12))

        controls = ttk.Frame(outer)
        controls.pack(fill="x", pady=(0, 10))

        self.rebuild_btn = ttk.Button(
            controls,
            text="REBUILD",
            command=self.start,
            state="normal" if labels else "disabled",
        )
        self.rebuild_btn.pack(side="left")

        ttk.Button(
            controls,
            text="Rafraîchir satellites",
            command=self.refresh,
        ).pack(side="left", padx=(8, 0))

        ttk.Button(
            controls,
            text=r"Ouvrir C:\KristalData\imagery",
            command=lambda: os.startfile(str(DATA_ROOT / "imagery")),
        ).pack(side="left", padx=(8, 0))

        self.progress = ttk.Progressbar(outer, mode="indeterminate")
        self.progress.pack(fill="x", pady=(0, 10))

        self.logbox = tk.Text(outer, height=19, wrap="word", font=("Consolas", 9))
        self.logbox.pack(fill="both", expand=True)

        self.root.after(150, self.poll)

    def refresh(self):
        self.records = load_records()
        labels = [r.label for r in self.records]
        self.combo.configure(
            values=labels,
            state="readonly" if labels else "disabled",
        )
        self.selected.set(labels[0] if labels else "(aucun manifest Sentinel trouvé)")
        self.rebuild_btn.configure(state="normal" if labels else "disabled")

    def selected_record(self):
        label = self.selected.get()
        for record in self.records:
            if record.label == label:
                return record
        raise RuntimeError("Satellite sélectionné introuvable.")

    def emit(self, msg):
        self.events.put(("log", str(msg)))
        log_line(str(msg))

    def start(self):
        if self.running:
            return

        try:
            record = self.selected_record()
        except Exception as exc:
            messagebox.showerror("Kristal Rebuild", str(exc))
            return

        if not messagebox.askyesno(
            "Kristal Farms — Rebuild",
            "Rebuild complet ?\n\n"
            f"{record.label}\n\n"
            "Le script va:\n"
            "• démarrer/vérifier PMTiles\n"
            "• réenregistrer l'imagerie\n"
            "• arrêter l'ancien Next.js Kristal\n"
            "• supprimer .next\n"
            "• relancer npm run dev",
        ):
            return

        self.running = True
        self.rebuild_btn.configure(state="disabled")
        self.progress.start(10)
        self.logbox.delete("1.0", "end")

        threading.Thread(target=self.worker, args=(record,), daemon=True).start()

    def worker(self, record):
        try:
            ensure_dirs()
            self.emit("=" * 70)
            self.emit("KRISTAL FARMS — REBUILD OBSERVATORY")
            self.emit(f"Repo: {REPO_ROOT}")
            self.emit(f"Imagery: {record.label}")
            self.emit(f"PMTiles: {record.pmtiles_path}")
            self.emit("")

            publish_hydro_scope(self.emit)
            publish_community_infrastructure(self.emit)
            start_imagery_server(record, self.emit)
            register_imagery(record, self.emit)
            stop_existing_web(self.emit)
            clear_next(self.emit)
            ensure_node_modules(self.emit)
            start_web(self.emit)

            self.emit("")
            self.emit("REBUILD TERMINÉ")
            self.events.put(("done", record))
        except Exception as exc:
            self.emit("")
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
                    self.rebuild_btn.configure(state="normal")

                    if self.open_browser_var.get():
                        webbrowser.open("http://localhost:3000")

                    messagebox.showinfo(
                        "Kristal Farms — Rebuild terminé",
                        "Observatory est prêt.\n\n"
                        f"Satellite actif:\n{payload.label}\n\n"
                        "http://localhost:3000",
                    )

                elif kind == "error":
                    self.running = False
                    self.progress.stop()
                    self.rebuild_btn.configure(state="normal")
                    messagebox.showerror(
                        "Kristal Farms — Rebuild échoué",
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
