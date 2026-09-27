# IRL™ Package System & Library Standards 📦

**Frozen-language contract:** the package system is TOOLING + DATA
FORMATS. It never changes the language. The language is the foundation;
these libraries are the ecosystem built on top of it.

## 1. Package identity

| Kind | Naming | Import |
|---|---|---|
| First-party ecosystem lib | `irl_iron`, `irl_wire`, `irl_forge` | `import irl_iron` |
| Community package | `irl_<name>` (reserved prefix, registry-validated) | `import irl_<name>` |
| Bridge modules (private) | `_bridge/*.py` | never imported from .irl directly |

- Package directories expose `.irl` entry via `lib/__init__.irl`
- Distribution: **pip wheels/sdists on PyPI** (`pip install irl_iron`) —
  IRL is a good citizen of the Python ecosystem by design (DESIGN.md §11);
  `irl pkg` is a friendly front-end, not a parallel universe
- `pkg.json` metadata (see §4) lives inside every package

## 2. `irl pkg` CLI (ships with irl-pkg 2.2)

```zsh
irl pkg install irl_iron          # latest, from PyPI
irl pkg install irl_iron==1.0.0   # pinned
irl pkg remove irl_iron
irl pkg list                       # installed + versions
irl pkg search numeric             # PyPI search filtered to irl-* packages
irl pkg lock                       # write irl.lock (exact pins, hashes)
irl pkg install --locked           # CI: reproducible from irl.lock
```

- **Lockfile `irl.lock`:** name, version, sha256 of the artifact, and the
  interpreter target. CI installs `--locked` or fails.
- **Determinism:** same lock + same PyPI state ⇒ same install, verified
  in CI by hash comparison.
- **Security:** sha256 verification of every artifact; `irl pkg publish`
  (2.2) signs with sigstore-style attestation; bridge modules are
  stdlib-only by policy (auditable in one file).

## 3. Library standards (every package MUST have)

1. **Documented public API** — human docs + `api.json` (machine-readable
   signature table; versioned schema)
2. **Tests** — `.irl` tests + bridge conformance tests; run by `irl test`
   and CI
3. **Examples** — every example passes `irl lang check`
4. **Error behavior** — all runtime errors prefixed `[<package>]`;
   documented error table per function
5. **Versioning** — SemVer; MAJOR bump may break API, MINOR adds, PATCH
   fixes; the frozen IRL 2.1 semantics are the compatibility ceiling
6. **Package metadata** — `pkg.json`:
   ```json
   {
     "name": "irl_iron",
     "version": "1.0.0",
     "irl": ">=2.1,<2.2",
     "description": "Numerical computing for .irl",
     "entry": "lib/__init__.irl",
     "bridge": "_bridge/numpy_bridge.py",
     "bridge_deps": {"numpy": "optional"},
     "license": "AGPL-3.0-or-later"
   }
   ```
7. **CI coverage** — each package repo runs: `irl lang check` on all
   sources/examples, the package test suite, bridge-parity tests (with
   and without optional Python deps), and builds on 3 OS
8. **Compatibility notes** — a matrix: IRL version × backend (bootstrap /
   native) × optional accelerators
9. **Native-backend compatibility plan** — which parts are permanent .irl
   (logic/API) vs bridge (to be replaced by Zig runtime); no package may
   depend on undocumented interpreter quirks (enforced by review + the
   parity suite)

## 4. The bridge-module pattern (the native seam)

Every package that needs host capabilities (HTTP, storage, crypto, SIMD)
ships a **bridge**: a single stdlib-only Python module with a narrow
contract, behind a pure-.irl public API.

```
.irl public API  (the contract — permanent)
      ↓
package logic in .irl (routing tables, schemas, validation)
      ↓
narrow bridge call  (documented dict-in/dict-out)
      ↓
_bridge/*.py  (bootstrap implementation — swappable)
      ↓
native runtime (2.3+): same contract, Zig implementation
```

Rules: bridges never leak Python objects into .irl values; every bridge
function takes/returns JSON-able dicts; bridge behavior is fully covered
by conformance fixtures so the native replacement is drop-in.

## 5. AI-friendliness requirements (per package)

- One canonical spelling per operation; no aliases in new packages
- Explicit arguments everywhere; kwargs only where documented
- Deterministic behavior (seeded randomness, stable iteration order for
  dicts where order matters)
- `api.json` consumed by `irl doc` (2.2) and by LLM agents directly
- The ideal loop, enforced by CI:
  `AI writes .irl → irl lang check --json → structured error → fix →
   irl test → run`

## 6. Implementation order (GLM / contributor phases)

| Phase | Contents | Gate |
|---|---|---|
| E1 | `irl_iron` full spec → implementation | parity + bench tables published |
| E2 | `irl_wire` core (routes/responses/middleware/static + bridge) | conformance fixtures green |
| E3 | `irl pkg` CLI + lockfile + PyPI publishing of E1/E2 | reproducible install in CI |
| E4 | `irl_forge` phase 1 (scaffold, views, irltmpl, models, migrations) | example blog passes `irl web test` |
| E5 | `irl_forge` batteries (forms/sessions/auth/admin) + `irl web test` runner | docs + api.json complete |

**Standing rule for every phase:** the frozen IRL 2.1 specification
(LANG.md) is not modified, weakened, or reinterpreted. Missing
expressiveness is solved with DATA and TOOLING — never with new syntax.
