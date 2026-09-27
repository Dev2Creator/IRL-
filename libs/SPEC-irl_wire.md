# SPEC-irl_wire — Web micro-framework for .irl 🌐

**Status:** Specification v1.0 (implementation target: ecosystem phase 1)
**Frozen-language contract:** builds ONLY on IRL 2.1 semantics (LANG.md).

## 1. Identity & design law

- Package: `irl_wire` · Flask-*like*, but designed for what .irl 2.1 can
  actually express.
- **No decorators** (not in frozen 2.1 — never invent `@route`).
- **No classes, no closures** (not in frozen 2.1) → there is no `App()`
  object. The framework is a **module with module-level registration**:

```js
import irl_wire

function home() {
    return "Hello from IRL"
}

function user(name) {
    return irl_wire.json_response({"name": name})
}

irl_wire.route("/", home)
irl_wire.route("/api/user/<name>", user, methods=["GET", "POST"])

irl_wire.run(host="127.0.0.1", port=8000)
```

- **One app per program** (module state is global — documented limitation,
  revisit if 2.2 adds modules-as-objects).

## 2. Public API

### Routing
| Function | Signature | Notes |
|---|---|---|
| `route(path, handler, methods=["GET"])` | register; path params as `<name>` | duplicate path+method = error |
| `path_params()` | dict of current request's path params | inside handler |
| `default(handler)` | 404 handler override | |

### Request (explicit, no magic injection)
`request_method()` → str · `request_path()` → str ·
`request_query()` → dict (parsed `?a=1&b=2`) · `request_headers()` → dict ·
`request_body()` → str · `request_form()` → dict (urlencoded body) ·
`request_json()` → parsed dict (error if body isn't JSON)

### Responses
Handler return value rules (predictable, ordered):
1. **str** → `200`, body = str, `Content-Type: text/plain; charset=utf-8`
2. **dict/list** → `200` JSON-encoded, `application/json`
3. **`response(body, status=200, headers={})`** → full control
4. **`json_response(data, status=200)`** → explicit JSON
5. **`redirect(location, status=302)`** → redirect
6. **`error(status, message)`** → structured error page

### Middleware
`before_request(fn)` / `after_request(fn)` — module-level registration,
executed in registration order. `before` may return a response (short-
circuit); `after` receives the response text + status and may modify.
(Real hooks — implemented as plain .irl function lists in module state.)

### Static files
`static_dir(path="static", url_prefix="/static")` — serves files under
the directory; path traversal is rejected (the bridge resolves and
validates every path against the declared root).

### Server
`run(host="127.0.0.1", port=8000)` — blocking development server.
`config(key, value)` / `config_get(key)` — app settings dict.

## 3. Layer split (native-backend seams)

| Concern | Lives in | Bootstrap impl | Native future |
|---|---|---|---|
| Routing table + match | **.irl** (this package) | dict + match fn | same .irl |
| Middleware chain | **.irl** | list walk | same .irl |
| Response building | **.irl** | string/json building | same .irl |
| Socket I/O + HTTP parsing | **bridge** | `_bridge/http_bridge.py` (stdlib http.server) | Zig runtime (2.3) |
| Static file IO | **bridge** | os.path + validation | Zig runtime |

**Bridge contract:** `serve(config, handler)` — the bridge receives a
config dict and ONE .irl callback `handle(request_dict) → response_dict`;
all framework logic stays in .irl. The bridge is replaceable without
touching the public API (this is the native-backend seam).

## 4. Errors

- Handler raises → bridge returns `500` with structured body
  `{"error": "...", "status": 500}` (no tracebacks to clients)
- `route()` on a taken path → `[irl_wire] route already registered: GET /`
- Unknown path → registered default (404 JSON by default)
- Bad path param conversion → 400

## 5. Package layout

```
irl_wire/
├── lib/
│   ├── __init__.irl
│   ├── router.irl          # table, matching, path params
│   ├── request.irl         # request_* accessors
│   ├── response.irl        # response builders + middleware
│   └── app.irl             # run/config glue
├── _bridge/
│   └── http_bridge.py      # stdlib-only dev server (the only .py)
├── tests/
├── examples/               # hello.irl, api.irl, forms.irl, static.irl
├── api.json
└── pkg.json
```

## 6. AI-friendliness

- Return-value rules are a total function of the handler's return (no
  implicit contexts, no thread-locals, no globals the AI can't see —
  request accessors read the CURRENT request, set by the runner before
  each dispatch; single-threaded dev server in v1, documented)
- `api.json` signature table; every example passes `irl lang check`
- Deterministic routing: first registered match wins; ties are errors

## 7. Test plan

1. Route registration + duplicate rejection
2. Path params (`<name>`, `<int:id>`)
3. All six response forms
4. before/after middleware order + short-circuit
5. Query/form/JSON body parsing (hand-built requests)
6. 404 default + custom default
7. Static serving + traversal rejection (`../`)
8. Bridge-vs-spec conformance: request dict → response dict fixtures

## 8. Compatibility & roadmap

- Bootstrap: stdlib http.server bridge (dev-grade; document loudly —
  not for production)
- 2.3 native: bridge replaced by the Zig runtime's HTTP layer; .irl API
  unchanged
- Production path (2.4+): compile the app with `irl lang build`, run
  behind a real reverse proxy; WSGI-style production bridge as an option
