from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path
from tkinter import Tk, messagebox

APP_URL = "http://localhost:3000/"


def notify(title: str, message: str, error: bool = False) -> None:
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    try:
        (messagebox.showerror if error else messagebox.showinfo)(title, message, parent=root)
    finally:
        root.destroy()


def http_json(url: str, timeout: float = 2.0):
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def check_app() -> int:
    with urllib.request.urlopen(APP_URL, timeout=8) as response:
        return int(response.status)


def find_browser() -> Path | None:
    env = os.environ
    candidates = [
        Path(env.get("PROGRAMFILES", "")) / "Google/Chrome/Application/chrome.exe",
        Path(env.get("PROGRAMFILES(X86)", "")) / "Google/Chrome/Application/chrome.exe",
        Path(env.get("LOCALAPPDATA", "")) / "Google/Chrome/Application/chrome.exe",
        Path(env.get("PROGRAMFILES", "")) / "Microsoft/Edge/Application/msedge.exe",
        Path(env.get("PROGRAMFILES(X86)", "")) / "Microsoft/Edge/Application/msedge.exe",
    ]
    return next((p for p in candidates if p.is_file()), None)


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def normalize_issue(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    except Exception:
        return str(value).strip()


def main() -> None:
    root_dir = Path(__file__).resolve().parents[2]
    out_path = root_dir / "next-devtools-issues.txt"
    raw_path = root_dir / "next-devtools-issues.raw.json"

    try:
        status = check_app()
    except Exception as exc:
        notify(
            "Kristal Observatory diagnostic",
            f"Observatory ne répond pas sur {APP_URL}\n\n"
            f"Démarre START_OBSERVATORY.bat puis relance ce fichier.\n\n{exc}",
            error=True,
        )
        return

    browser = find_browser()
    if browser is None:
        notify("Kristal Observatory diagnostic", "Chrome ou Edge n'a pas été trouvé.", error=True)
        return

    node = shutil.which("node")
    if not node:
        notify("Kristal Observatory diagnostic", "Node.js n'est pas disponible dans PATH.", error=True)
        return

    port = free_port()
    profile_dir = Path(tempfile.mkdtemp(prefix="kristal-observatory-cdp-"))
    node_file = Path(tempfile.mkstemp(prefix="kristal-observatory-diag-", suffix=".mjs")[1])

    node_source = r'''
const wsUrl = process.argv[2];
const ws = new WebSocket(wsUrl);
let nextId = 1;
const pending = new Map();
const consoleEntries = [];
const exceptions = [];
const logEntries = [];

const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function stringifyRemote(obj) {
  if (!obj) return "";
  if (Object.prototype.hasOwnProperty.call(obj, "value")) {
    if (typeof obj.value === "string") return obj.value;
    try { return JSON.stringify(obj.value); } catch { return String(obj.value); }
  }
  return obj.description || obj.className || obj.type || "";
}

function call(method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = nextId++;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
}

ws.addEventListener("message", (event) => {
  let msg;
  try { msg = JSON.parse(String(event.data)); } catch { return; }

  if (msg.id && pending.has(msg.id)) {
    const { resolve, reject } = pending.get(msg.id);
    pending.delete(msg.id);
    if (msg.error) reject(new Error(JSON.stringify(msg.error)));
    else resolve(msg.result);
    return;
  }

  if (msg.method === "Runtime.consoleAPICalled") {
    consoleEntries.push({
      type: msg.params?.type || "console",
      text: (msg.params?.args || []).map(stringifyRemote).filter(Boolean).join(" "),
      timestamp: msg.params?.timestamp || null,
    });
  } else if (msg.method === "Runtime.exceptionThrown") {
    const d = msg.params?.exceptionDetails || {};
    exceptions.push({
      text: d.text || stringifyRemote(d.exception) || "Runtime exception",
      exception: stringifyRemote(d.exception),
      url: d.url || null,
      lineNumber: d.lineNumber ?? null,
      columnNumber: d.columnNumber ?? null,
    });
  } else if (msg.method === "Log.entryAdded") {
    const e = msg.params?.entry || {};
    logEntries.push({
      level: e.level || "log",
      source: e.source || null,
      text: e.text || "",
      url: e.url || null,
    });
  }
});

await new Promise((resolve, reject) => {
  ws.addEventListener("open", resolve, { once: true });
  ws.addEventListener("error", reject, { once: true });
});

await call("Runtime.enable");
await call("Log.enable");
await call("Page.enable");
await call("Page.reload", { ignoreCache: true });
await wait(5500);

const pageInfo = await call("Runtime.evaluate", {
  expression: `({ href: window.location.href, title: document.title })`,
  returnByValue: true,
});

const nextInfo = await call("Runtime.evaluate", {
  expression: `
(async () => {
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  const portal = document.querySelector("nextjs-portal");
  if (!portal?.shadowRoot) return { available: false };
  const root = portal.shadowRoot;

  const issueButton =
    root.querySelector('[aria-label="Open issues overlay"]') ||
    root.querySelector('[data-issues-open]') ||
    [...root.querySelectorAll("button")].find((b) => /Issues?/i.test(b.textContent || ""));

  const badge = issueButton?.textContent?.trim() || null;
  issueButton?.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, composed: true }));
  await wait(700);

  const dialogTexts = [...root.querySelectorAll('[role="dialog"], dialog')]
    .map((d) => (d.innerText || d.textContent || "").trim())
    .filter(Boolean);

  const buttons = [...root.querySelectorAll("button")].map((b) => ({
    text: (b.innerText || b.textContent || "").trim(),
    aria: b.getAttribute("aria-label"),
    title: b.getAttribute("title"),
  }));

  return { available: true, badge, dialogTexts, buttons };
})()
`,
  returnByValue: true,
  awaitPromise: true,
});

console.log(JSON.stringify({
  capturedAt: new Date().toISOString(),
  page: pageInfo?.result?.value || null,
  consoleEntries,
  exceptions,
  logEntries,
  next: nextInfo?.result?.value || null,
}, null, 2));

ws.close();
'''
    node_file.write_text(node_source, encoding="utf-8")

    browser_process = None
    try:
        browser_args = [
            str(browser),
            "--headless=new",
            f"--remote-debugging-port={port}",
            f"--user-data-dir={profile_dir}",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-extensions",
            "--disable-gpu",
            APP_URL,
        ]
        creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
        browser_process = subprocess.Popen(
            browser_args,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=creationflags,
        )

        target = None
        endpoint = f"http://127.0.0.1:{port}/json"
        for _ in range(60):
            time.sleep(0.2)
            try:
                targets = http_json(endpoint, timeout=1)
                target = next(
                    (
                        item for item in targets
                        if item.get("type") == "page" and str(item.get("url", "")).startswith(APP_URL.rstrip("/"))
                    ),
                    None,
                )
                if target:
                    break
            except Exception:
                pass

        if not target or not target.get("webSocketDebuggerUrl"):
            raise RuntimeError("Impossible de connecter le diagnostic au navigateur headless.")

        result = subprocess.run(
            [node, str(node_file), target["webSocketDebuggerUrl"]],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            creationflags=creationflags,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Le collecteur Node a échoué.")

        payload = json.loads(result.stdout)
        raw_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

        candidates: list[str] = []
        for item in payload.get("consoleEntries", []):
            if item.get("type") in {"error", "warning", "assert"}:
                candidates.append(normalize_issue(item.get("text")))
        for item in payload.get("exceptions", []):
            candidates.append(normalize_issue(item.get("exception") or item.get("text")))
        for item in payload.get("logEntries", []):
            if item.get("level") in {"error", "warning"}:
                candidates.append(normalize_issue(item.get("text")))
        for text in (payload.get("next") or {}).get("dialogTexts", []):
            candidates.append(normalize_issue(text))

        unique: list[str] = []
        seen = set()
        for issue in candidates:
            issue = issue.strip()
            if not issue:
                continue
            key = " ".join(issue.split())
            if key not in seen:
                seen.add(key)
                unique.append(issue)

        page = payload.get("page") or {}
        next_info = payload.get("next") or {}
        lines = [
            "==================================================",
            "KRISTAL OBSERVATORY - DIAGNOSTIC",
            f"Captured: {payload.get('capturedAt', '')}",
            "==================================================",
            "",
            f"HTTP: {status}",
            f"URL: {page.get('href', APP_URL)}",
            f"Title: {page.get('title', '')}",
            f"Next badge: {next_info.get('badge') or 'not reported'}",
            f"Unique captured issues: {len(unique)}",
            "",
        ]

        if unique:
            for index, issue in enumerate(unique, 1):
                lines.extend([
                    f"---------------- ISSUE {index} ----------------",
                    issue,
                    "",
                ])
        else:
            lines.extend([
                "No console/runtime issues were captured during the diagnostic reload.",
                "",
            ])

        out_path.write_text("\n".join(lines), encoding="utf-8")

        notify(
            "Kristal Observatory diagnostic",
            f"Diagnostic terminé.\n\n"
            f"Issues uniques capturées : {len(unique)}\n\n"
            f"Rapport :\n{out_path}",
        )
    except Exception as exc:
        out_path.write_text(
            "KRISTAL OBSERVATORY DIAGNOSTIC FAILED\n\n" + repr(exc),
            encoding="utf-8",
        )
        notify(
            "Kristal Observatory diagnostic",
            f"Le diagnostic a échoué.\n\n{exc}\n\nRapport : {out_path}",
            error=True,
        )
    finally:
        try:
            if browser_process and browser_process.poll() is None:
                browser_process.terminate()
                try:
                    browser_process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    browser_process.kill()
        except Exception:
            pass
        try:
            node_file.unlink(missing_ok=True)
        except Exception:
            pass
        try:
            shutil.rmtree(profile_dir, ignore_errors=True)
        except Exception:
            pass


if __name__ == "__main__":
    main()
