"""IRL Notebook — kernel, format, and HTTP server tests (all in-process)."""

import json
import threading
import urllib.request

import pytest

from irl.notebook import (
    IrlKernel,
    export_script,
    load_notebook,
    save_notebook,
)


def test_kernel_captures_print_output():
    k = IrlKernel()
    res = k.run('print("hello", 42)')
    assert res["ok"] is True
    assert "hello 42" in res["output"]
    assert res["error"] is None


def test_kernel_state_is_persistent():
    k = IrlKernel()
    k.run("var total = 40")
    res = k.run("total + 2")
    assert res["ok"] is True
    assert "42" in res["output"]


def test_kernel_functions_persist():
    k = IrlKernel()
    k.run("function double(x) { return x * 2 }")
    res = k.run("print(double(21))")
    assert "42" in res["output"]


def test_kernel_reports_syntax_errors():
    k = IrlKernel()
    res = k.run("var = 5")
    assert res["ok"] is False
    assert "IRL_ERROR" in res["error"]


def test_kernel_reports_runtime_errors():
    k = IrlKernel()
    k.run("var x = 1")
    res = k.run("print(ghost)")
    assert res["ok"] is False
    assert "ghost" in res["error"]


def test_kernel_error_does_not_kill_session():
    k = IrlKernel()
    k.run("var broken = ")  # syntax error
    res = k.run('print("still alive")')
    assert res["ok"] is True


def test_notebook_default_structure():
    nb = load_notebook(None)
    assert nb["irl_notebook"] == 1
    assert isinstance(nb["cells"], list) and len(nb["cells"]) >= 1


def test_save_load_round_trip(tmp_path):
    path = str(tmp_path / "nb.irlnb")
    cells = [
        {"type": "markdown", "source": "# Title"},
        {"type": "code", "source": 'print("hi")'},
    ]
    save_notebook(path, cells)
    loaded = load_notebook(path)
    assert loaded["cells"] == cells


def test_export_script_only_code_cells():
    cells = [
        {"type": "markdown", "source": "# note"},
        {"type": "code", "source": "var x = 1"},
        {"type": "code", "source": "print(x)"},
        {"type": "code", "source": "   "},
    ]
    script = export_script(cells)
    assert "# note" not in script
    assert "var x = 1" in script and "print(x)" in script


@pytest.fixture()
def server_url():
    from irl.notebook import NotebookHandler, ThreadingHTTPServer

    NotebookHandler.kernel = IrlKernel()
    NotebookHandler.notebook_path = None
    srv = ThreadingHTTPServer(("127.0.0.1", 0), NotebookHandler)
    thread = threading.Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()


def test_http_serves_notebook_page(server_url):
    html = urllib.request.urlopen(server_url + "/", timeout=10).read().decode()
    assert "IRL™ Notebook" in html and "initial" in html


def test_http_run_endpoint(server_url):
    req = urllib.request.Request(
        server_url + "/run",
        data=json.dumps({"code": 'print("via http")'}).encode(),
        headers={"Content-Type": "application/json"},
    )
    payload = json.loads(urllib.request.urlopen(req, timeout=10).read())
    assert payload["ok"] is True and "via http" in payload["output"]


def test_http_save_endpoint(tmp_path, server_url):
    from irl import notebook as nb_mod

    nb_mod.NotebookHandler.notebook_path = str(tmp_path / "nb.irlnb")
    req = urllib.request.Request(
        server_url + "/save",
        data=json.dumps({"file": "kept.irlnb", "cells": [{"type": "code", "source": "var a = 1"}]}).encode(),
        headers={"Content-Type": "application/json"},
    )
    payload = json.loads(urllib.request.urlopen(req, timeout=10).read())
    assert payload["ok"] is True
    saved = json.loads((tmp_path / "kept.irlnb").read_text())
    assert saved["cells"][0]["source"] == "var a = 1"


def test_http_export_endpoint(server_url):
    req = urllib.request.Request(
        server_url + "/export",
        data=json.dumps({"cells": [{"type": "code", "source": "print(1)"}]}).encode(),
        headers={"Content-Type": "application/json"},
    )
    body = urllib.request.urlopen(req, timeout=10).read().decode()
    assert "print(1)" in body
