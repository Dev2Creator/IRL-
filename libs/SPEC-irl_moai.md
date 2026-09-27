# SPEC-irl_moai — Numerical computing for .irl 📐

**Status:** Specification v1.0 (implementation target: ecosystem phase 1)
**Frozen-language contract:** builds ONLY on IRL 2.1 semantics (LANG.md).
No new syntax, no operators, no language changes — ever.

## 1. Identity & scope

- Package name: `irl_moai` · import: `import irl_moai` (optionally `import irl_moai as np` **if** aliasing ships in a future language release — 2.1 has no `import as`, so docs use the full name)
- Goal: NumPy-*like* numerical computing with an **IRL-facing API**. The
  public programming model is plain .irl lists plus metadata — Python
  numpy objects are NEVER exposed to user code.
- The **`@` matrix operator does not exist in frozen 2.1** → matrix
  multiplication is `dot(a, b)`. This is a language-frozen decision.

## 2. Core data model

An "array" is a **plain .irl value**: nested lists (row-major) plus a
metadata dict. Helper `info(a)` returns `{"shape": [2, 2], "ndim": 2,
"size": 4}`. Arrays are immutable-by-convention (functions return new
lists); in-place helpers are explicit (`set_` prefixed) to keep AI
generation predictable.

## 3. Public API (complete 2.1-expressible surface)

### Construction
| Function | Signature | Notes |
|---|---|---|
| `array(data)` | nested lists → validated array | rectangularity check, error on ragged |
| `zeros(shape)` | `[2, 3]` → array | int 0 fill |
| `ones(shape)` | `[2, 3]` → array | int 1 fill |
| `full(shape, value)` | fill with any scalar | |
| `arange(start, stop, step)` | like `range` but returns list | |
| `linspace(start, stop, n)` | n evenly spaced floats | endpoints included |
| `copy(a)` | deep copy | |

### Introspection
`shape(a)` → list · `ndim(a)` → int · `size(a)` → int · `info(a)` → dict

### Reshaping
`reshape(a, shape)` · `flatten(a)` · `transpose(a)` (2-D) · `squeeze(a)` ·
`concatenate(a, b, axis=0)`

### Element-wise math (all broadcast scalars against arrays; array-array
requires equal shapes in v1 — full broadcasting lands with the native
kernel, see §6)
`add sub mul div mod pow neg abs` — `add(a, b)` etc. · `sqrt exp log
log2 log10 sin cos tan floor ceil round_elem(a, digits)`

### Reductions
`sum(a)` · `mean(a)` · `min(a)` · `max(a)` · `argmin(a)` · `argmax(a)` ·
`std(a)` · `var(a)` · `cumsum(a)` · `sum_axis(a, axis)` (v1: axis 0/1 on 2-D)

### Linear algebra
`dot(a, b)` (1-D dot, 2-D matmul) · `matmul(a, b)` (alias of dot for 2-D) ·
`transpose` doubles as `.T` · `eye(n)` · `diag(a)` · `det2(a)` (2×2), `det3(a)`
(3×3) · `inverse2(a)`, `inverse3(a)` · `matvec(a, v)`

### Random
`random_uniform(low, high, shape)` · `random_normal(mean, std, shape)` ·
`random_int(low, high, shape)` · `seed(n)` — deterministic per seed
(AI-friendly: same seed ⇒ same array, always)

### Indexing / slicing
Plain .irl indexing on the nested lists (`a[0][1]`, `a[1][:]`) is the
documented way; helpers: `row(a, i)` · `col(a, j)` · `get(a, i, j)` ·
`set_(a, i, j, value)` (returns new array)

## 4. Errors (structured, AI-friendly)

All errors are `IRL_RUNTIME_ERROR` with the prefix `[irl_moai]`:
- `[irl_moai] shape mismatch: (2, 3) vs (3, 2) — use reshape or transpose`
- `[irl_moai] ragged array: row 1 has 3 columns, row 0 has 2`
- `[irl_moai] index 5 out of bounds for axis 0 (size 2)`
Machine-readable table ships in `api.json` (§7).

## 5. Package layout

```
irl_moai/
├── lib/
│   ├── __init__.irl        # re-exports the public API
│   ├── core.irl            # array/shape/constructors
│   ├── math.irl            # element-wise + reductions
│   ├── linalg.irl          # dot/matmul/det/inverse
│   └── random.irl
├── _bridge/
│   └── numpy_bridge.py     # OPTIONAL accelerator: real numpy underneath
├── tests/                  # .irl test files run by irl test
├── examples/               # runnable .irl examples
├── api.json                # machine-readable API table
└── pkg.json                # package metadata (see PACKAGING.md)
```

**Bridge rule:** `_bridge/numpy_bridge.py` (pure Python, stdlib only)
accelerates `dot/matmul/sum/mean` on large arrays when the optional
numpy package is importable — but it is an implementation detail behind
the same .irl signatures. The Zig native backend replaces the bridge in
phase native (DESIGN.md §16) without touching the public API.

## 6. Performance plan

| Layer | Workload | Implementation |
|---|---|---|
| Bootstrap .irl | small/medium arrays (<10k elements) | pure .irl loops |
| Python bridge | large arrays, when numpy exists | delegate to numpy inside the bridge |
| Native (2.3+) | everything hot | SEESEMBLY kernels + SIMD (DESIGN.md §5); same .irl API |

Benchmark plan (per release): element-wise 100k, dot 256×256, reductions
1M — published in the package README via `irl lang bench`-style tables.

## 7. AI-friendliness

- Every function: explicit positional args, kwargs only where listed,
  zero hidden state (except `seed`)
- `api.json` — versioned machine-readable signature table consumed by
  agents/LLMs (`{"name": "dot", "args": ["a", "b"], "returns": "array", ...}`)
- Deterministic: same inputs ⇒ same outputs; `seed(n)` for reproducibility

## 8. Test plan (minimum gate)

1. Construction validation (ragged rejection, shape errors)
2. Element-wise parity vs hand-computed values
3. Reductions vs `.irl` builtin sum/min/max on 1-D
4. `dot` vs hand-computed 2×2, 3×3 matmul
5. Bridge-vs-pure parity (same outputs with and without numpy present)
6. Seed determinism
7. `irl lang check` clean on all examples

## 9. Compatibility

- IRL 2.1 bootstrap: full API
- Native backend (2.3+): full API, kernels replaced — no API change
- Python numpy: optional accelerator only, never required
