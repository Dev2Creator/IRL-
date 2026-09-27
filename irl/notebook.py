# IRL™ 🌱 - Software for Humans
# Copyright (C) 2026 Anika Mukherjee
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""IRL™ Notebook — Jupyter-style cell notebook for the .irl language.

`irl notebook [file.irlnb]` starts a local server (127.0.0.1 only),
opens the browser, and gives you code cells + markdown cells with a
persistent kernel (one interpreter session across all cells), save/load
as JSON .irlnb, and export to a plain .irl script.

Zero dependencies: stdlib http.server + one vanilla-JS page.
"""

import contextlib
import io
import json
import os
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from irl.lang import Interpreter, IrlRuntimeError, lex, parse
from irl.lang.lexer import IrlSyntaxError

NOTEBOOK_VERSION = 1


class IrlKernel:
    """One persistent interpreter session with captured output."""

    def __init__(self, source_dir=None):
        self.interpreter = Interpreter(source_dir=source_dir)
        self._lock = threading.Lock()

    def run(self, code):
        """Execute a cell. Returns {ok, output, error} — never raises."""
        with self._lock:
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    result = self.interpreter.interpret(parse(lex(code)))
                out = buf.getvalue()
                if result is not None:
                    out += repr(result) + "\n"
                return {"ok": True, "output": out, "error": None}
            except IrlSyntaxError as exc:
                return {"ok": False, "output": buf.getvalue(), "error": str(exc)}
            except IrlRuntimeError as exc:
                return {"ok": False, "output": buf.getvalue(), "error": str(exc)}
            except RecursionError:
                return {"ok": False, "output": buf.getvalue(), "error": "[IRL_RUNTIME_ERROR] Recursion too deep."}
            except Exception as exc:  # pragma: no cover - defensive
                return {"ok": False, "output": buf.getvalue(), "error": f"[IRL_CRITICAL] {exc}"}


def load_notebook(path):
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        if isinstance(data, dict) and "cells" in data:
            return data
    return {
        "irl_notebook": NOTEBOOK_VERSION,
        "cells": [
            {"type": "markdown", "source": "# IRL™ Notebook\n\nCells run in one persistent kernel. Shift+Enter to run."},
            {"type": "code", "source": 'var name = "world"\nprint(f"hello {name}")'},
        ],
    }


def save_notebook(path, cells):
    data = {"irl_notebook": NOTEBOOK_VERSION, "cells": cells}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
    return data


def export_script(cells):
    parts = ["// Exported from an IRL™ Notebook"]
    for cell in cells:
        if cell.get("type") == "code" and cell.get("source", "").strip():
            parts.append(cell["source"].strip())
    return "\n\n".join(parts) + "\n"


def page_html(title):
    return PAGE_TEMPLATE.replace("__TITLE__", title)


PAGE_TEMPLATE = r"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<style>
  :root { --bg:#0d1117; --panel:#161b22; --edge:#30363d; --fg:#e6edf3;
          --green:#3fb950; --dim:#8b949e; --red:#f85149; --purple:#bc8cff; }
  * { box-sizing:border-box; }
  body { background:var(--bg); color:var(--fg);
         font-family:"SF Mono",Consolas,monospace; margin:0; padding:24px; }
  header { display:flex; align-items:center; gap:12px; margin-bottom:18px; }
  header h1 { font-size:18px; margin:0; color:var(--green); }
  header .spacer { flex:1; }
  button { background:var(--panel); color:var(--fg); border:1px solid var(--edge);
           border-radius:6px; padding:6px 12px; cursor:pointer; font-family:inherit; }
  button:hover { border-color:var(--green); color:var(--green); }
  .cell { background:var(--panel); border:1px solid var(--edge); border-radius:8px;
          margin-bottom:12px; padding:10px; }
  .cell .bar { display:flex; gap:8px; align-items:center; margin-bottom:6px; }
  .cell .tag { font-size:11px; color:var(--dim); }
  .cell .grow { flex:1; }
  textarea { width:100%; min-height:70px; background:var(--bg); color:var(--fg);
             border:1px solid var(--edge); border-radius:6px; padding:10px;
             font-family:inherit; font-size:14px; resize:vertical; }
  .out { white-space:pre-wrap; border-top:1px dashed var(--edge); margin-top:8px;
         padding-top:8px; font-size:13px; color:var(--green); display:none; }
  .out.err { color:var(--red); }
  .md { color:var(--purple); }
  .add { width:100%; padding:10px; border-style:dashed; }
</style>
</head>
<body>
<header>
  <h1>🌱 IRL™ Notebook</h1>
  <span class="tag" id="kstat">kernel: ready</span>
  <span class="spacer"></span>
  <button onclick="saveNb()">Save</button>
  <button onclick="exportNb()">Export .irl</button>
  <button onclick="addCell('code')">+ code</button>
  <button onclick="addCell('markdown')">+ note</button>
</header>
<div id="cells"></div>
<button class="add" onclick="addCell('code')">+ add cell</button>
<script>
let cells = [];
const $ = (id) => document.getElementById(id);

function render() {
  const host = $('cells');
  host.innerHTML = '';
  cells.forEach((cell, i) => {
    const div = document.createElement('div');
    div.className = 'cell';
    const bar = document.createElement('div');
    bar.className = 'bar';
    bar.innerHTML = `<span class="tag ${cell.type==='markdown'?'md':''}">[${i}] ${cell.type}</span>
                     <span class="grow"></span>
                     <button onclick="runCell(${i})">▶ run</button>
                     <button onclick="moveCell(${i},-1)">↑</button>
                     <button onclick="moveCell(${i},1)">↓</button>
                     <button onclick="delCell(${i})">✕</button>`;
    const ta = document.createElement('textarea');
    ta.value = cell.source;
    ta.spellcheck = false;
    ta.oninput = () => { cell.source = ta.value; };
    ta.onkeydown = (e) => {
      if (e.key === 'Enter' && e.shiftKey) { e.preventDefault(); runCell(i); }
    };
    const out = document.createElement('div');
    out.className = 'out';
    out.id = 'out' + i;
    div.append(bar, ta, out);
    host.append(div);
  });
}

function addCell(type) { cells.push({type, source:''}); render(); }
function delCell(i) { cells.splice(i, 1); render(); }
function moveCell(i, d) {
  const j = i + d;
  if (j < 0 || j >= cells.length) return;
  [cells[i], cells[j]] = [cells[j], cells[i]];
  render();
}

async function runCell(i) {
  const cell = cells[i];
  const out = $('out' + i);
  out.style.display = 'block';
  out.className = 'out';
  out.textContent = cell.type === 'markdown'
    ? '(note cell — nothing to run)' : 'running…';
  if (cell.type !== 'code') return;
  $('kstat').textContent = 'kernel: running';
  const res = await fetch('/run', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({code: cell.source})
  }).then(r => r.json());
  out.className = 'out' + (res.ok ? '' : ' err');
  let text = res.output || '';
  if (res.error) text += (text ? '\n' : '') + res.error;
  out.textContent = text || '(no output)';
  $('kstat').textContent = 'kernel: ready';
}

async function saveNb() {
  const name = prompt('Save as (.irlnb):', NOTEBOOK_FILE || 'notebook.irlnb');
  if (!name) return;
  const res = await fetch('/save', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({file: name, cells})
  }).then(r => r.json());
  alert(res.ok ? 'Saved to ' + res.file : 'Save failed: ' + res.error);
}

async function exportNb() {
  const res = await fetch('/export', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({cells})
  });
  const blob = await res.blob();
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'notebook.irl';
  a.click();
}

const initial = __INITIAL__;
cells = initial.cells;
render();
</script>
</body>
</html>
"""


class NotebookHandler(BaseHTTPRequestHandler):
    kernel = None
    notebook_path = None

    def log_message(self, fmt, *args):  # quiet
        pass

    def _json(self, payload, code=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length <= 0 or length > 8 * 1024 * 1024:
            return None
        return json.loads(self.rfile.read(length).decode("utf-8"))

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            page = (
                page_html("IRL™ Notebook")
                .replace("__INITIAL__", json.dumps(load_notebook(self.notebook_path), ensure_ascii=False))
                .replace(
                    "__NOTEBOOK_FILE__",
                    json.dumps(self.notebook_path or ""),
                )
            )
            # NOTEBOOK_FILE is referenced by the save handler
            page = page.replace(
                "const initial = __INITIAL__;",
                f"const NOTEBOOK_FILE = {json.dumps(self.notebook_path or '')};\nconst initial = {json.dumps(load_notebook(self.notebook_path), ensure_ascii=False)};",
            )
            body = page.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self._json({"error": "not found"}, 404)

    def do_POST(self):
        if self.path == "/run":
            data = self._read_json()
            if data is None or "code" not in data:
                self._json({"ok": False, "error": "bad request"}, 400)
                return
            self._json(self.kernel.run(data["code"]))
            return
        if self.path == "/save":
            data = self._read_json()
            try:
                name = os.path.basename(data.get("file") or "notebook.irlnb")
                if not name.endswith(".irlnb"):
                    name += ".irlnb"
                target = name if not self.notebook_path else os.path.join(os.path.dirname(self.notebook_path), name)
                save_notebook(target, data.get("cells", []))
                self._json({"ok": True, "file": target})
            except Exception as exc:
                self._json({"ok": False, "error": str(exc)})
            return
        if self.path == "/export":
            data = self._read_json()
            script = export_script(data.get("cells", [])).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/x-irl; charset=utf-8")
            self.send_header("Content-Disposition", "attachment; filename=notebook.irl")
            self.send_header("Content-Length", str(len(script)))
            self.end_headers()
            self.wfile.write(script)
            return
        self._json({"error": "not found"}, 404)


def serve(path=None, port=0, open_browser=True):
    """Start the notebook server. Returns the bound port (blocks)."""
    here = os.path.dirname(os.path.abspath(path)) if path else os.getcwd()
    NotebookHandler.kernel = IrlKernel(source_dir=here)
    NotebookHandler.notebook_path = os.path.abspath(path) if path else None
    server = ThreadingHTTPServer(("127.0.0.1", port), NotebookHandler)
    bound = server.server_address[1]
    url = f"http://127.0.0.1:{bound}"
    print(f"🌱 IRL™ Notebook — {url}  (Ctrl-C to stop)")
    if open_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nlater. 🌱")
    finally:
        server.server_close()
    return bound
