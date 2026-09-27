# SPEC-irl_citadel — Batteries-included web framework for .irl 🏗️

**Status:** Specification v0.9 (progressive: core in phase 1, batteries in
phases 2–3). **Frozen-language contract:** IRL 2.1 semantics only — no
decorators, no classes, no closures; scaffolding is TOOLING (`irl web …`),
not language syntax. Built ON TOP of `irl_pulse`'s bridge pattern, not on
Django internals.

## 1. Identity

- Package: `irl_citadel` — batteries-included web framework, .irl-native.
- Philosophy: **project structure is files, configuration is .irl data,
  views are functions, models are schema dicts.** Nothing requires
  language features 2.1 lacks; phases upgrade as the language does.

## 2. Developer experience (tooling, not syntax)

```text
irl web create mysite          # scaffold (CLI: a irl subcommand)
cd mysite
irl web create-app users       # adds users/ app directory + registers it
irl web migrate                # apply model schemas to the data store
irl web run                    # dev server (bridge-backed)
irl web check                  # validate project (routing, templates, models)
```

Generated project layout:

```text
mysite/
├── main.irl            # imports apps, registers routes, calls run
├── settings.irl        # dict: DEBUG, SECRET, APPS, DATABASE, STATIC
├── urls.irl            # top-level route table (registered via irl_pulse.route)
├── users/
│   ├── routes.irl      # url → view wiring for this app
│   ├── views.irl       # view functions
│   ├── models.irl      # model schema dicts
│   └── templates/      # app templates
├── templates/          # project templates
└── static/
```

## 3. Core (phase 1)

### Views & routing
Plain functions receiving an explicit `request` dict; return the same
six response forms as irl_pulse (§ shared response contract — one
implementation, `irl_citadel.views` re-exports it).

```js
// users/views.irl
function profile(request, username) {
    var user = models_get("users", {"name": username})
    if (user == none) {
        return error(404, "no such user")
    }
    return render("users/profile.html", {"user": user})
}
```

### Templates — `irltmpl`
A tiny deterministic template language (spec'd fully in this package —
NOT Jinja2):
- `{{ expr }}` — substitution (dot-paths into the context dict only:
  `{{ user.name }}`; no arbitrary code, ever — AI-safety by construction)
- `{% if expr %}…{% elif %}…{% else %}…{% endif %}` — truthiness of
  context dot-paths / literals
- `{% for item in list_path %}…{% endfor %}`
- `{% include "partial.html" %}`
- Unknown tags/paths are **compile-time errors** of the render call
- Filters (explicit, closed set): `upper lower trim first last length`
  used as `{{ name | upper }}` — no custom filters in v1

### Settings
`settings.irl` returns one dict. The framework reads it once at start:
`DEBUG`, `SECRET`, `APPS` (list), `DATABASE` ({"engine": "json"} in
phase 1), `STATIC`, `TEMPLATES`. Unknown keys are warnings (`irl web
check` reports them).

### Models & data (phase 1 storage: JSON store)
Models are schema dicts — no DSL, no magic:

```js
// users/models.irl
var users = {
    "fields": {
        "name": {"type": "str", "required": true, "unique": true},
        "age": {"type": "int", "required": false},
    }
}
```

API (explicit CRUD, no ORM magic):
`models_register(name, schema)` · `models_get(table, match)` ·
`models_all(table)` · `models_insert(table, data)` (validates against
schema) · `models_update(table, match, changes)` ·
`models_delete(table, match)` · `models_count(table)`.
Storage: append-only JSON file + in-memory index (bootstrap); the
storage driver is a bridge interface (phase 3: sqlite bridge, native
store later).

### Migrations
`irl web migrate` diffs registered schemas against the store's manifest
(`.irldata/manifest.json`), writes additive migrations (add field /
add table); destructive changes require `--force`. Migrations are
replayable JSON — deterministic and CI-friendly.

## 4. Batteries (phases 2–3, each gated on language milestones)

| Feature | Phase | 2.1-expressible design |
|---|---|---|
| Forms | 2 | schema dicts for fields; `forms_validate(schema, data)` → `{"ok": bool, "errors": {...}, "clean": {...}}` |
| Sessions | 2 | signed cookie (HMAC via the bridge) + `sessions_get/set` API |
| Auth | 2 | `auth_register/login/logout/current` over users model + salted hash via bridge |
| Admin-style inspector | 2 | `irl web admin` — local, read-only table browser generated from schemas |
| Middleware | 1 | irl_pulse before/after hooks at project level |
| Static assets | 1 | irl_pulse static_dir per app + project |
| Testing | 2 | `irl web test` — in-process request/response fixtures against views |
| Native store | 3 | storage bridge → Zig runtime table store |
| Production deploy | 3 | `irl web serve --production` (native HTTP) + compiled app via `irl lang build` |

## 5. Package layout

```
irl_citadel/
├── lib/                    # .irl framework code (router, views, templates,
│   │                       #  models, forms, sessions, auth)
├── _bridge/
│   ├── http_bridge.py      # shared pattern with irl_pulse
│   └── storage_bridge.py   # JSON store, later sqlite/native
├── scaffolds/              # templates for `irl web create`
├── tests/
├── examples/               # a full demo blog project
├── api.json
└── pkg.json
```

## 6. Layer split for native backends

| Concern | Layer | Native replacement target |
|---|---|---|
| Routing, views, middleware, template **logic** | .irl | none — permanent .irl |
| Template rendering core | .irl (v1) → SEESEMBLY kernel (2.3+) | speed only |
| HTTP I/O | bridge | Zig runtime |
| Storage | bridge | Zig store |
| Crypto (HMAC/hash) | bridge | Zig runtime (constant-time) |

## 7. Test plan

1. Scaffold → `irl web check` clean → `irl web run` boots (fixture request)
2. Template language: every tag/filter, plus error cases (unknown tag,
   unknown filter, bad dot-path)
3. Models: schema validation, unique constraint, CRUD round-trip
4. Migrations: additive replay, destructive requires --force
5. Sessions: sign/verify/tamper rejection
6. Auth: register/login/logout/current + wrong-password path
7. End-to-end: the example blog passes `irl web test`

## 8. Compatibility

- IRL 2.1 bootstrap: phases 1–2 fully expressible (no closures needed —
  state lives in the data store and settings dict)
- Native backend: public .irl API identical; bridges swap out
- Explicitly OUT of scope until the language admits it: ORM relations
  with lazy loading (needs closures/classes), admin auto-edit UI
  (needs 2.2 forms), async anything
