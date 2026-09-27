# SPEC-irlcu — Parallel & GPU computing for .irl 🎮

**Status:** Specification v0.9 (design now; GPU targets gated on the native
runtime — CPU-parallelism ships first)
**Frozen-language contract:** IRL 2.1 semantics only. No new syntax.
**Named after CUDA** — .irl's device/parallel-computing layer.

## 1. Identity & the honest roadmap

`irlcu` = .irl's parallel-computing layer: CUDA's mental model (kernels,
device data) with .irl approachability. The name is the ambition; the
phases are the honesty:

| Phase | Backend | What actually runs |
|---|---|---|
| cu-1 (bootstrap) | CPU bridge | threads/processes pool in `_bridge`; GIL-honest: parallel I/O + process-based CPU work benefit today |
| cu-2 (2.3 native runtime) | CPU native | M:N green threads over all cores — real parallelism, identical API |
| cu-3 (2.4+) | GPU | Zig/CUDA/Vulkan kernels for numeric work; `irlglass` arrays become device-resident |

## 2. Public API (module functions, explicit args — 2.1-expressible)

### Device model
No `device` object exists in 2.1 — the "device" is module state:

| Function | Signature | Notes |
|---|---|---|
| `workers(n)` | set pool size | default: core count via bridge |
| `mode(m)` | `"threads"` or `"processes"` (bootstrap) | native runtime ignores; always M:N |
| `stats()` | dict | workers, mode, tasks run, failures |

### Parallel map / filter / reduce
| Function | Signature | Notes |
|---|---|---|
| `pmap(fn, items)` | list → list, parallel | order-preserving, deterministic |
| `pfilter(fn, items)` | parallel filter | order-preserving |
| `preduce(fn, items, initial)` | parallel fold | correctness always; speedups need an associative fn |
| `pchunks(fn, items, n)` | chunked map | fewer bridge crossings for big jobs |

### Kernels (surface designed now; real GPU in cu-3)
| Function | Notes |
|---|---|
| `kernel(fn)` | declare a **pure** function as a kernel — checked: no imports, no I/O inside |
| `launch(k, grid, args)` | run kernel over grid; bootstrap = loop, native = GPU |
| `device_array(shape, fill)` | `irlglass`-compatible array marked device-resident |
| `to_host(arr)` / `to_device(arr)` | explicit transfers — never implicit (AI-friendly) |
| `synchronize()` | barrier; bootstrap is synchronous anyway |

**Kernel purity rules (enforced by `kernel()`):** pure .irl functions
only — no `import`, no `print`/`input`, no I/O; args in, return out.
This is what makes real GPU compilation (cu-3) possible without breaking
anyone's code.

### Determinism
Same inputs + same worker count ⇒ same result, always. `pmap`/`pfilter`
preserve order; `preduce` combines chunks in order.

## 3. Errors (all prefixed `[irlcu]`)

- `[irlcu] kernel 'k' is not pure: contains print`
- `[irlcu] grid must be positive, got 0`
- `[irlcu] worker pool exhausted — task raised in all workers`
Task failures surface with the original .irl error text plus the failing
item index.

## 4. Package layout

```
irlcu/
├── lib/
│   ├── __init__.irl
│   ├── pool.irl          # workers/mode/stats, scheduling
│   ├── parallel.irl      # pmap/pfilter/preduce/pchunks
│   └── kernel.irl        # purity checking, launch, transfers
├── _bridge/
│   └── pool_bridge.py    # threads/processes pool; GPU in cu-3
├── tests/
├── examples/             # pmap log-cleaning, preduce wordcount, kernel demo
├── api.json
└── pkg.json
```

## 5. Layer split (native seams)

| Concern | Layer | Native future |
|---|---|---|
| Purity checks, scheduling policy, ordering | **.irl** | permanent .irl |
| Pool/worker execution | **bridge** | threads → Zig M:N green threads (cu-2) |
| Kernel compilation | **bridge stub** | Zig → GPU kernels (cu-3) |
| Device memory | **bridge** | runtime-managed (cu-3) |

## 6. Test plan

1. `pmap` order preservation (threads and processes modes)
2. `preduce` correct with associative AND non-associative fns
   (non-associative = sequential fallback — slower, never wrong)
3. Worker crash propagation + pool recovery
4. `kernel()` purity rejection matrix (import/print/input/IO)
5. Determinism: same inputs/workers ⇒ byte-identical output
6. Bridge parity: threads == processes == sequential results

## 7. Compatibility

- IRL 2.1 bootstrap: cu-1 (CPU-parallel, GIL-honest docs)
- Native runtime (2.3): cu-2 — same API, real parallelism
- GPU (2.4+): cu-3 — kernels compile to device code; the API is frozen
  now so nothing breaks later
- Interops with `irlglass` arrays for device transfers
