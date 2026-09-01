# -*- coding: utf-8 -*-
"""
INSTALL_PMTILES.pyw
Kristal Farms - Windows PMTiles installer

Double-click this file.

Actions:
- Detect Windows architecture (x64 / arm64)
- Fetch the latest official protomaps/go-pmtiles release from GitHub
- Download the matching Windows archive/executable
- Install to C:\KristalData\bin\pmtiles.exe
- Add C:\KristalData\bin to the current USER Path
- Create Kristal imagery directories
- Verify pmtiles.exe
- Write C:\KristalData\pmtiles-install.log

No administrator privileges should be required for the default paths.
"""

from __future__ import annotations

import ctypes
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

API_URL = "https://api.github.com/repos/protomaps/go-pmtiles/releases/latest"
USER_AGENT = "Kristal-Farms-PMTiles-Installer/1.1"

KRISTAL_DATA = Path(r"C:\KristalData")
BIN_DIR = KRISTAL_DATA / "bin"
EXE_PATH = BIN_DIR / "pmtiles.exe"
LOG_PATH = KRISTAL_DATA / "pmtiles-install.log"

IMAGERY_SOURCE = KRISTAL_DATA / "imagery" / "source"
IMAGERY_PMTILES = KRISTAL_DATA / "imagery" / "pmtiles"
TOOLS_DIR = KRISTAL_DATA / "tools"


def log(message: str) -> None:
    KRISTAL_DATA.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(message.rstrip() + "\n")


def http_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=180) as response:
        with destination.open("wb") as output:
            shutil.copyfileobj(response, output)


def architecture_tokens() -> tuple[str, ...]:
    machine = platform.machine().lower()

    if machine in {"amd64", "x86_64", "x64"}:
        return ("windows_x86_64", "windows_amd64", "win64", "windows-x86_64")

    if machine in {"arm64", "aarch64"}:
        return ("windows_arm64", "windows_aarch64", "windows-arm64")

    raise RuntimeError(
        "Architecture Windows non supportée automatiquement : "
        f"{platform.machine()}"
    )


def select_release_asset(release: dict) -> dict:
    assets = release.get("assets") or []
    tokens = architecture_tokens()

    # Prefer ZIP releases, but accept a direct executable if upstream changes.
    for extension in (".zip", ".exe"):
        for asset in assets:
            name = str(asset.get("name") or "")
            normalized = name.lower().replace("-", "_")
            if normalized.endswith(extension) and any(
                token.replace("-", "_") in normalized for token in tokens
            ):
                return asset

    available = "\n".join(
        f"  - {asset.get('name', '')}" for asset in assets
    ) or "  (aucun asset)"

    raise RuntimeError(
        "Aucun binaire Windows compatible trouvé dans la dernière release.\n\n"
        f"Architecture détectée : {platform.machine()}\n"
        f"Assets disponibles :\n{available}"
    )


def extract_pmtiles(downloaded: Path, destination: Path) -> None:
    if downloaded.suffix.lower() == ".exe":
        shutil.copy2(downloaded, destination)
        return

    if not zipfile.is_zipfile(downloaded):
        raise RuntimeError("Le téléchargement n'est pas une archive ZIP valide.")

    with tempfile.TemporaryDirectory(prefix="kristal-pmtiles-extract-") as tmp:
        extracted = Path(tmp)
        with zipfile.ZipFile(downloaded, "r") as archive:
            archive.extractall(extracted)

        matches = list(extracted.rglob("pmtiles.exe"))
        if not matches:
            raise RuntimeError(
                "L'archive a été extraite, mais pmtiles.exe est introuvable."
            )

        shutil.copy2(matches[0], destination)


def add_user_path(directory: Path) -> bool:
    import winreg

    target = os.path.normcase(os.path.normpath(str(directory)))

    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Environment",
        0,
        winreg.KEY_READ | winreg.KEY_WRITE,
    ) as key:
        try:
            current, value_type = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current = ""
            value_type = winreg.REG_EXPAND_SZ

        parts = [part.strip() for part in str(current).split(";") if part.strip()]
        normalized = {
            os.path.normcase(os.path.normpath(part))
            for part in parts
        }

        if target in normalized:
            return False

        new_path = ";".join(parts + [str(directory)])
        winreg.SetValueEx(key, "Path", 0, value_type, new_path)

    # Broadcast environment change to Windows.
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x001A
    SMTO_ABORTIFHUNG = 0x0002

    try:
        result = ctypes.c_ulong()
        ctypes.windll.user32.SendMessageTimeoutW(
            HWND_BROADCAST,
            WM_SETTINGCHANGE,
            0,
            "Environment",
            SMTO_ABORTIFHUNG,
            5000,
            ctypes.byref(result),
        )
    except Exception:
        # Not fatal; new shells will still get the persistent user Path.
        pass

    return True


def verify() -> str:
    attempts = (
        [str(EXE_PATH), "version"],
        [str(EXE_PATH), "--version"],
        [str(EXE_PATH), "--help"],
    )

    errors: list[str] = []

    for command in attempts:
        try:
            completed = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=20,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            output = (completed.stdout or "").strip()

            if completed.returncode == 0:
                if output:
                    return output.splitlines()[0]
                return "pmtiles.exe répond correctement."

            errors.append(
                f"{command[-1]} -> code {completed.returncode}: {output}"
            )
        except Exception as exc:
            errors.append(f"{command[-1]} -> {exc}")

    raise RuntimeError(
        "pmtiles.exe a été copié mais n'a pas passé la vérification.\n\n"
        + "\n".join(errors)
    )


def main() -> None:
    root = tk.Tk()
    root.withdraw()

    try:
        KRISTAL_DATA.mkdir(parents=True, exist_ok=True)
        BIN_DIR.mkdir(parents=True, exist_ok=True)
        IMAGERY_SOURCE.mkdir(parents=True, exist_ok=True)
        IMAGERY_PMTILES.mkdir(parents=True, exist_ok=True)
        TOOLS_DIR.mkdir(parents=True, exist_ok=True)

        log("")
        log("=" * 72)
        log("Kristal Farms - INSTALL_PMTILES.pyw")
        log(f"Python: {sys.version.split()[0]}")
        log(f"Windows architecture: {platform.machine()}")

        if EXE_PATH.exists():
            answer = messagebox.askyesno(
                "Kristal Farms — PMTiles",
                "PMTiles est déjà présent ici :\n\n"
                f"{EXE_PATH}\n\n"
                "Télécharger et installer la dernière release par-dessus ?",
            )
        else:
            answer = messagebox.askyesno(
                "Kristal Farms — PMTiles",
                "Installer le CLI officiel PMTiles ?\n\n"
                f"Destination :\n{EXE_PATH}\n\n"
                "Le programme téléchargera la dernière release Windows officielle "
                "depuis protomaps/go-pmtiles sur GitHub.\n\n"
                "Continuer ?",
            )

        if not answer:
            log("Installation annulée.")
            return

        release = http_json(API_URL)
        version = str(
            release.get("tag_name")
            or release.get("name")
            or "latest"
        )
        log(f"Release: {version}")

        asset = select_release_asset(release)
        asset_name = str(asset.get("name"))
        asset_url = str(asset.get("browser_download_url"))

        if not asset_url:
            raise RuntimeError("L'asset GitHub ne contient pas d'URL de téléchargement.")

        log(f"Asset: {asset_name}")
        log(f"URL: {asset_url}")

        with tempfile.TemporaryDirectory(prefix="kristal-pmtiles-download-") as tmp:
            downloaded = Path(tmp) / asset_name
            download(asset_url, downloaded)

            log(f"Downloaded bytes: {downloaded.stat().st_size}")

            if EXE_PATH.exists():
                backup = EXE_PATH.with_suffix(".exe.bak")
                try:
                    shutil.copy2(EXE_PATH, backup)
                    log(f"Backup: {backup}")
                except Exception:
                    pass

            extract_pmtiles(downloaded, EXE_PATH)

        if not EXE_PATH.exists():
            raise RuntimeError(
                f"L'installation n'a pas créé {EXE_PATH}"
            )

        path_changed = add_user_path(BIN_DIR)
        verification = verify()

        log(f"Installed: {EXE_PATH}")
        log(f"Verify: {verification}")
        log(f"User PATH changed: {path_changed}")
        log("SUCCESS")

        note = (
            "\n\nC:\\KristalData\\bin a été ajouté au PATH utilisateur."
            if path_changed
            else "\n\nC:\\KristalData\\bin était déjà dans le PATH utilisateur."
        )

        messagebox.showinfo(
            "Kristal Farms — PMTiles installé",
            "Installation réussie.\n\n"
            f"Version/reponse : {verification}\n\n"
            f"Exécutable :\n{EXE_PATH}"
            f"{note}\n\n"
            "Les dossiers d'imagerie ont aussi été créés :\n"
            r"C:\KristalData\imagery\source"
            "\n"
            r"C:\KristalData\imagery\pmtiles"
            "\n\n"
            "IMPORTANT : ouvre une NOUVELLE fenêtre PowerShell avant "
            "d'utiliser simplement la commande 'pmtiles'.\n\n"
            "Test :\n"
            r"C:\KristalData\bin\pmtiles.exe version",
        )

    except Exception as exc:
        log(f"ERROR: {type(exc).__name__}: {exc}")
        messagebox.showerror(
            "Kristal Farms — Échec installation PMTiles",
            "L'installation a échoué.\n\n"
            f"{exc}\n\n"
            f"Journal :\n{LOG_PATH}",
        )
    finally:
        try:
            root.destroy()
        except Exception:
            pass


if __name__ == "__main__":
    main()
