# -*- coding: utf-8 -*-
"""Kristal Farms Observatory — controlled rebuild / due-process launcher.

Double-click this file after repository files have changed.

The launcher intentionally does more than a quick dev start:
1. stop an existing Kristal dev server safely;
2. clean generated caches only;
3. create/repair the local Python .venv when needed;
4. regenerate governed public artifacts whose publishers are present;
5. run the complete Python test suite;
6. ensure frontend dependencies, run TypeScript typecheck and Next production build;
7. optionally re-register local PMTiles imagery;
8. start the Observatory dev server and health-check it before opening the browser.

It never deletes source data, research data, node_modules, or the virtual environment.
"""
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

# Force child Python processes to use UTF-8 on Windows. This keeps fixture reads
# and publisher/test output independent of the active Windows ANSI code page.
os.environ["PYTHONUTF8"] = "1"
os.environ["PYTHONIOENCODING"] = "utf-8"

REPO_ROOT = Path(__file__).resolve().parent
WEB_ROOT = REPO_ROOT / "apps" / "web"
VENV_ROOT = REPO_ROOT / ".venv"
REQUIREMENTS = REPO_ROOT / "requirements-dev.txt"

DATA_ROOT = Path(r"C:\KristalData")
SOURCE_DIR = DATA_ROOT / "imagery" / "source"
PMTILES_DIR = DATA_ROOT / "imagery" / "pmtiles"
PMTILES_EXE = DATA_ROOT / "bin" / "pmtiles.exe"
LOG_PATH = DATA_ROOT / "rebuild-observatory.log"

IMAGERY_SERVER_SCRIPT = REPO_ROOT / "START_IMAGERY_SERVER.ps1"
REGISTER_SCRIPT = REPO_ROOT / "REGISTER_LOCAL_IMAGERY.ps1"

PORT_IMAGERY = 8765
PORT_WEB = 3000
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
NEW_CONSOLE = getattr(subprocess, "CREATE_NEW_CONSOLE", 0)

PUBLISHERS = [
    ("Hydro scope", "pipelines/publish/build_kristal_hydro_scope.py"),
    ("Community infrastructure", "pipelines/publish/build_community_infrastructure.py"),
    ("International 12", "pipelines/publish/build_international_portfolio_public.py"),
    ("Grid Reach", "pipelines/publish/build_grid_reach_public.py"),
    ("Observatory evidence", "pipelines/publish/build_observatory_public.py"),
]

PYTHON_IMPORT_CHECK = (
    "import pydantic, yaml, numpy, rasterio, geopandas, shapely, pyproj, requests, pytest; "
    "print('python test stack ok')"
)


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
        date = self.acquired[:10] if self.acquired else "unknown date"
        return f"{self.place} — {date} — {self.pmtiles_path.name}"


def ensure_data_dirs() -> None:
    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    PMTILES_DIR.mkdir(parents=True, exist_ok=True)


def log_line(message: str) -> None:
    ensure_data_dirs()
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(str(message).rstrip() + "\n")


def find_pwsh() -> str:
    for name in ("pwsh.exe", "pwsh", "powershell.exe", "powershell"):
        found = shutil.which(name)
        if found:
            return found
    raise RuntimeError("PowerShell / pwsh introuvable.")


def http_text(url: str, timeout: float = 3) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Kristal-Rebuild/2.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def url_ok(url: str, timeout: float = 2) -> bool:
    try:
        http_text(url, timeout)
        return True
    except Exception:
        return False


def port_open(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex(("127.0.0.1", port)) == 0


def load_records() -> list[ImageryRecord]:
    records: list[ImageryRecord] = []
    if not SOURCE_DIR.exists():
        return records
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
                    attribution=str(data.get("attribution") or "Contains modified Copernicus Sentinel data"),
                    pmtiles_path=pmtiles_path,
                    created_at=str(data.get("created_at") or ""),
                )
            )
        except Exception:
            continue

    def key(record: ImageryRecord) -> float:
        try:
            return datetime.fromisoformat(record.created_at.replace("Z", "+00:00")).timestamp()
        except Exception:
            try:
                return record.manifest_path.stat().st_mtime
            except Exception:
                return 0

    return sorted(records, key=key, reverse=True)


def run_command(command: list[str], cwd: Path, emit, timeout: int = 900) -> str:
    emit("$ " + subprocess.list2cmdline(command))
    process = subprocess.Popen(
        command,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=NO_WINDOW,
    )
    lines: list[str] = []
    assert process.stdout is not None
    try:
        started = time.time()
        while True:
            line = process.stdout.readline()
            if line:
                text = line.rstrip()
                lines.append(text)
                emit(text)
            elif process.poll() is not None:
                break
            elif time.time() - started > timeout:
                process.kill()
                raise RuntimeError(f"Commande expirée après {timeout}s: {command[0]}")
            else:
                time.sleep(0.05)
    finally:
        if process.poll() is None:
            process.kill()
    if process.returncode != 0:
        tail = "\n".join(lines[-30:])
        raise RuntimeError(f"Commande échouée ({process.returncode}): {subprocess.list2cmdline(command)}\n{tail}")
    return "\n".join(lines)


def run_probe(command: list[str], cwd: Path | None = None, timeout: int = 30) -> bool:
    try:
        completed = subprocess.run(
            command,
            cwd=str(cwd) if cwd else None,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout,
            creationflags=NO_WINDOW,
        )
        return completed.returncode == 0
    except Exception:
        return False


def ps_capture(command: str) -> str:
    completed = subprocess.run(
        [find_pwsh(), "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=30,
        creationflags=NO_WINDOW,
    )
    output = completed.stdout or ""
    if completed.returncode != 0:
        raise RuntimeError(output.strip() or "PowerShell command failed.")
    return output.strip()


def get_listening_pid(port: int) -> int | None:
    command = (
        f"$c = Get-NetTCPConnection -LocalPort {port} -State Listen "
        "-ErrorAction SilentlyContinue | Select-Object -First 1; "
        "if ($c) { Write-Output $c.OwningProcess }"
    )
    try:
        output = ps_capture(command).strip()
        return int(output) if output else None
    except Exception:
        return None


def get_cmdline(pid: int) -> str:
    command = (
        f'$p = Get-CimInstance Win32_Process -Filter "ProcessId={pid}" '
        "-ErrorAction SilentlyContinue; if ($p) { Write-Output $p.CommandLine }"
    )
    try:
        return ps_capture(command)
    except Exception:
        return ""


def stop_tree(pid: int) -> None:
    completed = subprocess.run(
        ["taskkill", "/PID", str(pid), "/T", "/F"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=20,
        creationflags=NO_WINDOW,
    )
    if completed.returncode not in (0, 128):
        raise RuntimeError((completed.stdout or "").strip() or f"Stop PID {pid} failed.")


def looks_like_kristal() -> bool:
    try:
        page = http_text("http://127.0.0.1:3000/", 2.5).lower()
        return "kristal farms" in page or "northern atlas" in page or "observatory" in page
    except Exception:
        return False


def stop_existing_web(emit) -> None:
    if not port_open(PORT_WEB):
        emit("Port 3000 libre.")
        return
    if not looks_like_kristal():
        raise RuntimeError("Port 3000 occupé par un serveur qui ne ressemble pas à Kristal; arrêt automatique refusé.")
    pid = get_listening_pid(PORT_WEB)
    if not pid:
        raise RuntimeError("Impossible d'identifier le processus Kristal sur le port 3000.")
    emit(f"Arrêt du serveur Kristal existant (PID {pid})...")
    cmdline = get_cmdline(pid)
    if cmdline:
        emit("Processus: " + cmdline[:180])
    stop_tree(pid)
    deadline = time.time() + 10
    while time.time() < deadline:
        if not port_open(PORT_WEB):
            emit("Serveur précédent arrêté.")
            return
        time.sleep(0.35)
    raise RuntimeError("Le port 3000 est toujours occupé.")


def clean_generated(emit) -> None:
    emit("Nettoyage des caches générés...")
    direct = [WEB_ROOT / ".next", REPO_ROOT / ".pytest_cache", WEB_ROOT / "public" / "maplibre"]
    for path in direct:
        if path.exists():
            emit(f"  remove {path.relative_to(REPO_ROOT)}")
            shutil.rmtree(path, ignore_errors=False)

    prune = {".git", ".venv", "node_modules", "archive", ".next"}
    removed_dirs = 0
    removed_files = 0
    for root, dirs, files in os.walk(REPO_ROOT, topdown=True):
        dirs[:] = [d for d in dirs if d not in prune]
        root_path = Path(root)
        for dirname in list(dirs):
            if dirname == "__pycache__":
                target = root_path / dirname
                shutil.rmtree(target, ignore_errors=True)
                dirs.remove(dirname)
                removed_dirs += 1
        for filename in files:
            if filename.endswith((".pyc", ".pyo")):
                try:
                    (root_path / filename).unlink()
                    removed_files += 1
                except OSError:
                    pass
    emit(f"Caches Python nettoyés: {removed_dirs} dossiers, {removed_files} fichiers.")


def preferred_venv_launcher() -> list[str]:
    py = shutil.which("py.exe") or shutil.which("py")
    if py and run_probe([py, "-3.13", "-c", "import sys; print(sys.version)"], REPO_ROOT):
        return [py, "-3.13"]
    return [sys.executable]


def venv_python() -> Path:
    windows = VENV_ROOT / "Scripts" / "python.exe"
    posix = VENV_ROOT / "bin" / "python"
    return windows if windows.exists() else posix


def ensure_python_env(emit) -> Path:
    if not REQUIREMENTS.exists():
        raise RuntimeError(f"Fichier absent: {REQUIREMENTS.name}")
    python = venv_python()
    if not python.exists():
        launcher = preferred_venv_launcher()
        emit("Création de .venv avec " + subprocess.list2cmdline(launcher) + "...")
        run_command(launcher + ["-m", "venv", str(VENV_ROOT)], REPO_ROOT, emit, timeout=180)
        python = venv_python()
    if not python.exists():
        raise RuntimeError(".venv créé mais python.exe introuvable.")

    if run_probe([str(python), "-c", PYTHON_IMPORT_CHECK], REPO_ROOT):
        emit("Python .venv: dépendances de test OK.")
        return python

    emit("Python .venv incomplet -> installation requirements-dev.txt...")
    run_command([str(python), "-m", "pip", "install", "--upgrade", "pip"], REPO_ROOT, emit, timeout=600)
    run_command([str(python), "-m", "pip", "install", "-r", str(REQUIREMENTS)], REPO_ROOT, emit, timeout=1200)
    if not run_probe([str(python), "-c", PYTHON_IMPORT_CHECK], REPO_ROOT):
        raise RuntimeError("La pile Python de test reste incomplète après installation.")
    emit("Python .venv réparé.")
    return python


def publish_governed_artifacts(python: Path, emit) -> None:
    emit("Publication des artefacts gouvernés...")
    for label, relative in PUBLISHERS:
        script = REPO_ROOT / relative
        if not script.exists():
            emit(f"  {label}: absent -> skip")
            continue
        emit(f"  {label}...")
        run_command([str(python), str(script)], REPO_ROOT, emit, timeout=240)


def run_python_tests(python: Path, emit) -> None:
    emit("Validation Python / repository...")
    run_command([str(python), "-m", "pytest", "-q"], REPO_ROOT, emit, timeout=1200)


def ensure_node_modules(emit) -> None:
    if not shutil.which("node"):
        raise RuntimeError("Node.js introuvable dans PATH.")
    if not (shutil.which("npm.cmd") or shutil.which("npm")):
        raise RuntimeError("npm introuvable dans PATH.")
    marker = WEB_ROOT / "node_modules" / "maplibre-gl" / "package.json"
    if marker.exists():
        emit("node_modules / MapLibre: OK")
        return
    command = ["npm.cmd" if shutil.which("npm.cmd") else "npm", "ci" if (WEB_ROOT / "package-lock.json").exists() else "install"]
    emit("Dépendances frontend absentes -> " + " ".join(command) + "...")
    run_command(command, WEB_ROOT, emit, timeout=1200)
    if not marker.exists():
        raise RuntimeError("maplibre-gl absent après installation npm.")


def run_web_checks(emit) -> None:
    npm = "npm.cmd" if shutil.which("npm.cmd") else "npm"
    emit("TypeScript typecheck...")
    run_command([npm, "run", "typecheck"], WEB_ROOT, emit, timeout=900)
    emit("Next.js production build...")
    run_command([npm, "run", "build"], WEB_ROOT, emit, timeout=1200)


def start_imagery_server(record: ImageryRecord, emit) -> None:
    tilejson = f"http://127.0.0.1:{PORT_IMAGERY}/{record.id}.json"
    if url_ok(tilejson):
        emit("Serveur PMTiles local déjà actif.")
        return
    if port_open(PORT_IMAGERY):
        raise RuntimeError(f"Port {PORT_IMAGERY} occupé mais {record.id}.json inaccessible.")
    if not IMAGERY_SERVER_SCRIPT.exists():
        raise RuntimeError(f"Script absent: {IMAGERY_SERVER_SCRIPT.name}")
    if not PMTILES_EXE.exists():
        emit("PMTiles local non installé -> imagerie locale ignorée.")
        return
    emit("Démarrage du serveur PMTiles local...")
    subprocess.Popen(
        [find_pwsh(), "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(IMAGERY_SERVER_SCRIPT)],
        cwd=str(REPO_ROOT),
        creationflags=NEW_CONSOLE,
    )
    deadline = time.time() + 20
    while time.time() < deadline:
        if url_ok(tilejson, 1.5):
            emit(f"PMTiles OK: {tilejson}")
            return
        time.sleep(0.5)
    raise RuntimeError(f"TileJSON ne répond pas: {tilejson}")


def register_imagery(record: ImageryRecord, emit) -> None:
    if not REGISTER_SCRIPT.exists() or not PMTILES_EXE.exists():
        return
    emit(f"Réenregistrement imagerie locale: {record.label}")
    command = [
        find_pwsh(), "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(REGISTER_SCRIPT),
        "-Id", record.id,
        "-Title", f"Sentinel-2 — {record.place}",
        "-Source", record.source,
        "-Acquired", record.acquired[:10] if record.acquired else "",
        "-Attribution", record.attribution,
    ]
    run_command(command, REPO_ROOT, emit, timeout=60)


def start_web(emit) -> None:
    npm = "npm.cmd" if shutil.which("npm.cmd") else "npm"
    emit("Démarrage npm run dev...")
    # cmd /k keeps the dev-server console available for the user.
    subprocess.Popen(
        ["cmd.exe", "/k", npm, "run", "dev"],
        cwd=str(WEB_ROOT),
        creationflags=NEW_CONSOLE,
    )
    deadline = time.time() + 60
    while time.time() < deadline:
        try:
            page = http_text("http://127.0.0.1:3000/", 2).lower()
            if "kristal farms" in page or "northern atlas" in page or "observatory" in page:
                emit("Observatory prêt: http://localhost:3000")
                return
        except Exception:
            pass
        time.sleep(0.75)
    raise RuntimeError("Observatory n'a pas répondu dans les 60 secondes.")


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Kristal Farms Observatory — Rebuild + Due Process")
        self.root.geometry("860x650")
        self.root.minsize(760, 560)
        self.events: queue.Queue = queue.Queue()
        self.running = False
        self.records = load_records()

        outer = ttk.Frame(root, padding=16)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="Kristal Farms Observatory", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(
            outer,
            text="REBUILD + DUE PROCESS · publish → clean → tests → typecheck → build → start",
        ).pack(anchor="w", pady=(2, 14))

        if not (WEB_ROOT / "package.json").exists():
            ttk.Label(outer, text="ERREUR: place ce .pyw à la racine du repo Kristal.").pack(anchor="w")
            return

        row = ttk.Frame(outer)
        row.pack(fill="x", pady=(0, 10))
        ttk.Label(row, text="Local imagery (optional)").pack(side="left")
        labels = ["(none / keep governed manifest)"] + [record.label for record in self.records]
        self.selected = tk.StringVar(value=labels[1] if len(labels) > 1 else labels[0])
        self.combo = ttk.Combobox(row, textvariable=self.selected, values=labels, state="readonly", width=66)
        self.combo.pack(side="left", fill="x", expand=True, padx=(12, 0))

        self.clean_var = tk.BooleanVar(value=True)
        self.browser_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(outer, text="Clean generated caches before validation", variable=self.clean_var).pack(anchor="w")
        ttk.Checkbutton(outer, text="Open Observatory after successful validation", variable=self.browser_var).pack(anchor="w", pady=(0, 10))

        ttk.Label(
            outer,
            text=(
                "The tool may create/repair .venv and install requirements-dev.txt. "
                "It never deletes node_modules, .venv, source data, research, or Git history."
            ),
            wraplength=810,
        ).pack(anchor="w", pady=(0, 12))

        controls = ttk.Frame(outer)
        controls.pack(fill="x", pady=(0, 10))
        self.rebuild_btn = ttk.Button(controls, text="REBUILD + VERIFY + START", command=self.start)
        self.rebuild_btn.pack(side="left")
        ttk.Button(controls, text="Refresh imagery list", command=self.refresh).pack(side="left", padx=(8, 0))
        ttk.Button(controls, text="Open log", command=self.open_log).pack(side="left", padx=(8, 0))

        self.progress = ttk.Progressbar(outer, mode="indeterminate")
        self.progress.pack(fill="x", pady=(0, 10))
        self.logbox = tk.Text(outer, height=25, wrap="word", font=("Consolas", 9))
        self.logbox.pack(fill="both", expand=True)
        self.root.after(150, self.poll)

    def refresh(self) -> None:
        self.records = load_records()
        labels = ["(none / keep governed manifest)"] + [record.label for record in self.records]
        self.combo.configure(values=labels)
        self.selected.set(labels[1] if len(labels) > 1 else labels[0])

    def selected_record(self) -> ImageryRecord | None:
        label = self.selected.get()
        for record in self.records:
            if record.label == label:
                return record
        return None

    def open_log(self) -> None:
        ensure_data_dirs()
        if not LOG_PATH.exists():
            LOG_PATH.write_text("", encoding="utf-8")
        os.startfile(str(LOG_PATH))

    def emit(self, message) -> None:
        text = str(message)
        self.events.put(("log", text))
        log_line(text)

    def start(self) -> None:
        if self.running:
            return
        record = self.selected_record()
        steps = (
            "• stop the current Kristal dev server if needed\n"
            "• clean generated caches (if checked)\n"
            "• create/repair .venv dependencies\n"
            "• regenerate governed public artifacts\n"
            "• run the full pytest suite\n"
            "• run npm typecheck + production build\n"
            "• start Observatory only if all checks pass"
        )
        if record:
            steps += f"\n• refresh local imagery: {record.label}"
        if not messagebox.askyesno("Kristal Farms Observatory", "Run controlled rebuild?\n\n" + steps):
            return
        self.running = True
        self.rebuild_btn.configure(state="disabled")
        self.progress.start(10)
        self.logbox.delete("1.0", "end")
        threading.Thread(target=self.worker, args=(record,), daemon=True).start()

    def worker(self, record: ImageryRecord | None) -> None:
        try:
            ensure_data_dirs()
            self.emit("=" * 76)
            self.emit("KRISTAL FARMS OBSERVATORY — REBUILD + DUE PROCESS")
            self.emit(f"Repo: {REPO_ROOT}")
            self.emit("")
            stop_existing_web(self.emit)
            if self.clean_var.get():
                clean_generated(self.emit)
            python = ensure_python_env(self.emit)
            publish_governed_artifacts(python, self.emit)
            run_python_tests(python, self.emit)
            ensure_node_modules(self.emit)
            run_web_checks(self.emit)
            if record:
                start_imagery_server(record, self.emit)
                register_imagery(record, self.emit)
            start_web(self.emit)
            self.emit("")
            self.emit("DUE PROCESS PASSED — OBSERVATORY STARTED")
            self.events.put(("done", None))
        except Exception as exc:
            self.emit("")
            self.emit("FAILED: " + str(exc))
            self.emit(traceback.format_exc())
            self.events.put(("error", str(exc)))

    def poll(self) -> None:
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
                    if self.browser_var.get():
                        webbrowser.open("http://localhost:3000")
                    messagebox.showinfo(
                        "Kristal Farms Observatory",
                        "Rebuild and due process passed.\n\nObservatory is running at:\nhttp://localhost:3000",
                    )
                elif kind == "error":
                    self.running = False
                    self.progress.stop()
                    self.rebuild_btn.configure(state="normal")
                    messagebox.showerror(
                        "Kristal Farms Observatory — validation failed",
                        payload + f"\n\nObservatory was not started.\nLog:\n{LOG_PATH}",
                    )
        except queue.Empty:
            pass
        self.root.after(150, self.poll)


def main() -> None:
    ensure_data_dirs()
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
