# IRL™ Language — Architecture & Evolution Design (DESIGN.md)

**Mission:** *"Easy to write like Python, powerful like a systems language, fast
enough for serious workloads, AI-friendly by design, CI/CD-friendly, and without
turning into another C++."*

Maintainer: Anika Mukherjee · License: AGPL-3.0-or-later · This document is the
compiler/architecture contract for .irl 2.x → 2030.

---

## 0. The Bootstrap Principle (architectural law)

Python is the **bootstrap implementation**, never the permanent mother
implementation. The 2.1 Python-based engine ships as the stable **reference
implementation** — and every component is isolated behind interfaces so the
same frontend can later drive native backends.

```
                 IRL source (.irl)
                        ↓
                 IRL frontend
            (lexer / parser / AST — frozen spec)
                        ↓
                 IRL IR  "SEESEMBLY"   ← the stable contract
                    ↓               ↓
        bootstrap backend      native backend
          (Python)                 (Zig)
             ↓                       ↓
         CPython               native runtime
                                    ↓
                             bytecode / native
```

**Long term:** IRL source → IRL compiler → self-hosted core → native
IR/bytecode → runtime. Python becomes an optional **ecosystem bridge**, not
the foundation.

**Migration plan (in order, no skipping):**
1. Freeze the IRL 2.1 language specification (LANG.md = the frozen spec)
2. Keep frontend strictly separate from backend (already true: `irl/lang/`
   lexer+parser produce AST; `interpreter.py` and `builder.py` are both
   *backends* of the same AST)
3. Define the stable IR (SEESEMBLY, §3) with a versioned text+binary format
4. Separate compiler from runtime (the notebook/kernel/runner talk to the
   language only through `lex/parse/evaluate/build` — no internals)
5. Define the native ABI/runtime boundary (§11.3)
6. Implement the Zig/native backend **incrementally** (per-opcode parity
   tests against the bootstrap implementation)
7. Self-host the compiler in .irl **only after** the native toolchain is
   stable (2.4+, never before)

**What Python is used for during bootstrap (and stays isolated behind
interfaces):** the bootstrap backend, the notebook prototype, testing, tooling,
and the ecosystem bridge. None of these may leak CPython assumptions into the
AST/IR contract.

---

## 1. Revised architecture (component boundaries)

| Component | 2.1 home | Contract | Native reimplementation |
|---|---|---|---|
| Lexer | `irl/lang/lexer.py` | source → `Token` stream | 2.2 (C/Zig, table-driven) |
| Parser | `irl/lang/parser.py` | tokens → AST | 2.2 |
| AST | `irl/lang/parser.py` node classes | 27 node types, `line` on nodes | frozen spec, JSON-dumpable |
| IR (SEESEMBLY) | `irl/lang/seesembly.py` (2.2) | AST → typed register code | the permanent target |
| Interpreter backend | `irl/lang/interpreter.py` | AST/IR → execution | replaced by native eval core |
| Compiler backend | `irl/lang/builder.py` | AST/IR → CPython bytecode | IR → Zig → native objects |
| Runtime | CPython (bootstrap) | builtins + env + object model | `irlrt` native runtime (2.3) |
| Tools | `irl/` (notebook, runner, bench) | CLI + JSON protocols | mostly stay Python — tooling is not the hot path |

**Rule:** tools and backends may depend on Python; the **frontend + IR
contract may not**. Anything with CPython semantics baked in (truthiness,
string coercion rules, display formats) is written down in LANG.md so native
implementations target a spec, not the reference code.

## 2. Language design (frozen 2.1 core)

Shipped in 2.1 (see LANG.md for the full frozen spec): `var`/`let`,
`function`/`def`/`fn`, `if`/`elif`/`else`, `while`, `for (x in iterable)`,
`break`/`continue`, `return`, `true`/`false`/`none`, `memo function`,
`import <stdlib>` + `import "file.irl"`, floats, escapes, f-strings, dicts,
lists with slicing, methods, `print` with `sep=`/`end=`, `type`/`isinstance`,
optional semicolons, braces, `#`/`//` comments. Legacy slang (snag/spill/bet/
cap/grind/brb/task/fax/fake/fr/nah) runs as aliases through the 2.x series,
removed in 3.0.

**Feature admission policy** (no feature-list envy): a feature enters only
with a written answer to — *Why does it exist? What problem? Performance
impact? Complexity cost? Which layer owns it (language / SEESEMBLY /
bytecode / runtime / tooling)?* Deferred by this policy in 2.1: classes
(2.2 — largest single feature), try/except (2.2), tuples/sets (2.2),
lambdas (2.3), generics (3.0), macros (never — they break deterministic
parsing and AI-friendliness).

## 3. SEESEMBLY — the stable IR

Not another syntax layer: it is the **optimization surface and the backend
contract**. The frontend lowers AST → SEESEMBLY once; every backend consumes
SEESEMBLY; every optimization pass runs on it; `--emit-ir` shows it to humans.

**Instruction model:** linear, register-based, SSA-lite (each temp assigned
once per block), one operation per line, typed opcodes.

```
# fib.irl → fib.seea  (text form; ships alongside packed .seeab)
fn fib(n: ANY) -> ANY:
    t0 = LT   n, 2
    jf  t0, L1
    ret n
L1:
    t1 = SUB  n, 1
    t2 = CALL fib, [t1]
    t3 = SUB  n, 2
    t4 = CALL fib, [t3]
    t5 = ADD  t2, t4
    ret t5
```

**Types:** `I64, F64, BOOL, STR, LIST, DICT, ANY, FN`. Dynamic semantics are
preserved by `ANY`; typed ops (`ADD_I64` vs `ADD_ANY`) let the optimizer
specialize where annotations or inference prove types. Overflow on `I64`
promotes to `ANY`/bigint — .irl numerics stay Python-exact (arbitrary
precision).

**Control flow:** explicit labels + conditional/unconditional jumps. No
exceptions in the IR (2.2's try/except lowers to handler regions).

**Memory model:** registers hold boxed values (`ANY`) or unboxed scalars;
lists/dicts are heap objects with reference semantics (matching .irl);
no address-taking in 2.x — pointer-level memory belongs to the native
runtime, not the language.

**Optimization strategy (passes, in order):** constant folding → algebraic
simplification → dead-code elimination → common-subexpression elimination
(2.2) → builtin caching → memo lowering → loop-invariant hoisting (2.2, with
dataflow) → register allocation (native backend only). Each pass reports its
transformations (`-v`) — the compiler never lies about what it did.

**Versioning:** `seea-v1` text header + `.seeab` binary with magic `SEEA`,
u16 version, feature flags. Backends declare which IR version they accept.

## 4. Bytecode

**Register-based, fixed 32-bit instructions** (Lua-lineage): `op(8) | A(8) |
B(8) | C(8)`, with wide variants for large constants. Rationale: register
bytecode does fewer dispatches and fewer stack shuffles than stack bytecode
for our expression-heavy workload; a hybrid only for calls.

**Container layout:** magic `IRLB` · u16 version · u32 feature flags ·
constant pool (sorted → deterministic output) · function table · debug map
(line table for caret errors) · body. mmap-friendly, zero-parse startup.

**Compatibility:** major version bump = old runtimes reject; feature flags =
minor extensions; the bootstrap backend today emits **CPython bytecode**
(same role, borrowed runtime); the native `IRLB` format lands with the 2.3
runtime. Version field exists from day one so tooling can detect formats.

## 5. Performance strategy

**Where the time actually goes** (measured on CPython research + our bench):
instruction dispatch (~11%), dynamic type checks (~6%), recursion-limit
checks (~8%), boxing/allocation (often dominant). Attack plan by layer:

| Layer | Optimization | Ships |
|---|---|---|
| Compiler (AOT) | constant folding, DCE, builtin caching, memo lowering, CSE (2.2), loop-invariant hoisting (2.2), inlining of small leaf functions (2.2) | 2.1 → 2.2 |
| Compiler | specialization from optional annotations (`var n: int`) → typed SEESEMBLY ops | 2.2 |
| Runtime (native, 2.3) | threaded-code dispatch, inline caches for `ANY` ops, unboxed scalar fast paths | 2.3 |
| Runtime | JIT: profile-guided re-specialization of hot functions (native only) | 2.4 |
| Runtime | SIMD via `irl.numeric` kernel (Fortran/C candidates — LAPACK heritage) | 2.4 |
| Runtime | parallelism: real threads for native runtime; hosted mode is GIL-bound (honest) | 2.4 |
| Escape analysis | belongs to the **native** backend (stack-allocate non-escaping lists) — pointless in hosted mode | 2.3 |

**Governance:** `irl lang bench` is the gate. Every optimization PR must show
a measured win on the published workloads; the README numbers are regenerated
by CI so claims never drift from reality.

## 6. Type system — gradual, inference-first

- Default: fully dynamic (`ANY`) — beginners never write a type
- Optional annotations: `var x: int = 0`, `function f(a: str) -> bool`
- The compiler **infers** local types for SEESEMBLY specialization with or
  without annotations; annotations turn inference errors into compile errors
- `check` mode (2.2) type-checks annotated code, reports unannotated
  public APIs; zero runtime cost
- No generics/traits in 2.x (roadmap 3.0); no union types yet — `ANY` covers
  it without a C++-ification spiral

## 7. Concurrency (one model, added once)

- **2.2:** `task` blocks + `chan` channels (structured concurrency: tasks
  cannot outlive their scope; channels are the only communication). On the
  bootstrap backend these map to threads (GIL-honest: concurrency ≠
  parallelism for CPU work; I/O workloads benefit immediately)
- **2.3+:** the native runtime schedules tasks M:N across cores — same
  syntax, real parallelism
- **Deliberately no** `async/await` coloring: two concurrency models is how
  languages become complicated. If the native runtime needs async internals,
  they live in the runtime, not in user syntax

## 8. Memory management

| Mode | Scheme | Why |
|---|---|---|
| Bootstrap (2.1–2.2) | CPython refcounting + GC | free, correct, already there |
| Native (2.3+) | reference counting + **arenas** per task | deterministic, simple, no moving GC pauses; arenas free per-task heaps wholesale |
| Rejected | tracing GC (runtime complexity, pause unpredictability), ownership/borrowing (breaks the approachability promise) | |

Escape analysis (native backend, 2.3) stack-allocates non-escaping lists so
most allocations never touch the RC path.

## 9. AI friendliness (design constraints, not marketing)

- **One grammar, frozen and published** (EBNF in `irl/lang/spec.py`,
  `irl lang spec --json`) — one way to say anything
- **`irl lang check --json`** — stable schema: `{ok, file, errors:[{line,
  column, message}]}` — agents parse failures and self-correct
- **`--emit-ast-json`** (2.2): the AST as JSON with stable node names —
  coding tools transform code by AST, not regex
- Deterministic formatter (`irl fmt`, 2.2): byte-identical output for the
  same input → reliable AI diffs
- Legacy aliases are machine-flaggable (`irl lint` warns) so generated code
  converges on canonical syntax

## 10. Tooling architecture

| Tool | Ships | Notes |
|---|---|---|
| `irl file.irl` / `irl lang run` | **now** | runner (bootstrap backend) |
| `irl lang build` | **now** | compiler: -O0/1/2, --emit-ir/py, -v report, .irl_cache |
| `irl lang check --json` | **now** | CI/agent validation |
| `irl lang spec --json` | **now** | grammar + keywords |
| `irl lang bench` | **now** | honest published numbers |
| `irl notebook` (`.irlnb`) | **now** | persistent kernel, cells, JSON format |
| `irl fmt` | 2.2 | deterministic formatter |
| `irl lint` | 2.2 | alias warnings + type-check of annotated code |
| `irl test` | 2.2 | file-based test runner, JSON output |
| LSP | 2.2 | hover/diagnostics/go-to-def on the AST |
| `irl pkg` | 2.2 | thin layer over pip/conda (never a parallel universe) |
| Profiler | 2.2 | cProfile passthrough + per-cell notebook profiling |
| Debugger | 2.3 | stepping via runtime tracing hooks |
| Docgen | 2.3 | from doc-comments |

## 11. Python / Conda interoperability

1. **Bootstrap mode (now):** .irl *is* hosted — every Python package is one
   bridge away; stdlib allowlist (`math`, `random`, `time`, `datetime`,
   `json`, `string`, `statistics`) is the capability boundary
2. **Native runtime, bridge mode (2.3):** runtime embeds CPython via the C
   API — .irl calls Python, Python calls compiled .irl modules through a
   generated C ABI shim (`.so`/`.pyd` with plain functions)
3. **Native runtime, standalone mode (2.3+):** pure-.irl programs run with
   zero Python installed; the Python bridge is loaded only if imported —
   "avoid requiring the entire Python runtime" is a hard 2.3 goal
4. Distribution stays pip/conda-native (wheels) — .irl is a good citizen,
   not a parallel ecosystem

## 12. CI/CD

- **Reproducible builds:** content-hash build cache (`.irl_cache/`),
  sorted constant pools, compiler version stamped in artifacts
- **Lockfile:** `irl.lock` with `irl pkg` (2.2) — pinned transitive deps
- **Determinism:** same source + same compiler version ⇒ byte-identical
  `.pyc`/`.seeab` (verified by a CI job)
- **Cross-platform:** CI matrix (3 OS × 5 Python) for the bootstrap; native
  wheels via cibuildwheel; `zig cc` as the cross-compilation driver for the
  native core from a single CI runner
- **Machine-readable everything:** check/build/bench/test all have `--json`
- **Incremental:** content-hash keyed; notebook re-runs hit the parse/IR cache

## 13. Security

- **Capability-style imports:** stdlib allowlist is the boundary; no
  filesystem/network in the language core without an explicit future grant
- **Package signing:** sigstore-style attestation on `irl pkg` (2.2)
- **Notebook sandbox:** binds 127.0.0.1 only, no arbitrary file access,
  kernel imports still allowlisted (2.1)
- **Plugins:** none in-core until 2.3, then process-isolated only
- **Reproducible builds** double as supply-chain verification

## 14. Technically questionable today — honest findings

1. **f-string lowering emits `str()` concatenation** — safe but slower and
   uglier than native f-strings. *Fix (2.2):* emit real f-strings once
   escaping edge cases are covered by parity tests.
2. **`Interpreter._env` is interpreter-global** — fine for single-threaded
   runs; the notebook's threaded server must serialize kernel access
   (one lock). *Fix:* document + lock in 2.1; make env explicitly
   per-execution-context in 2.2.
3. **`50 MB` target size** — the bootstrap wheel is ~1 MB and should stay
   tiny. The 50 MB budget belongs to the **2.3 native runtime distribution**
   (runtime + stdlib bridges + prebuilt binaries). Don't bloat the wheel
   to hit a number.
4. **Tree-walking interpreter is the slow path by design** — correct for
   bootstrap; the native eval core (2.2) and SEESEMBLY (2.2) replace it.
   Nothing in the AST/IR locks us in.
5. **Local imports merge into the importer's namespace** — simple and
   notebook-friendly, but not module semantics. *Fix (2.2):* real modules
   with `import "x.irl" as x` sugar; merge stays for compatibility.
6. **Legacy aliases double the keyword surface** — kept for zero breakage,
   but lint warns and 3.0 removes them.

## 15. Biggest technical risks (ranked)

1. **Scope creep killing the language** — every feature must pay rent
   (§2 policy); the 2.1 scope is already the largest safe increment
2. **Parity drift** between bootstrap and native backends — mitigated by
   the shared parity test suite: every test runs against every backend
3. **Native runtime maintenance burden** (Zig/C per-platform wheels) —
   mitigated by incremental opcodes, fallback to bootstrap, cibuildwheel
4. **GIL ceiling** for hosted concurrency — honest docs; parallelism is a
   native-runtime promise, not a bootstrap one
5. **One-maintainer bus factor** — AGPL, docs, and AI-friendly onboarding
   are the mitigations

## 16. Roadmap → 2030

| Release | Theme | Contents |
|---|---|---|
| **2.1** (2026) | The Full Platform | frozen spec, std keywords, imports, types, memo, compiler+optimizer, notebook, check/spec/bench, native C accelerator core, brand |
| **2.2** (2027) | Native core + tooling | SEESEMBLY IR as the real frontend output, Zig/C eval core, classes, try/except, `irl fmt/lint/test/pkg`, LSP, f-string lowering, real modules |
| **2.3** (2028) | Standalone runtime | `IRLB` bytecode, native runtime (RC+arenas), bridge/standalone modes, debugger, C-ABI exports |
| **2.4** (2029) | Serious workloads | JIT specialization, SIMD numeric kernel, parallel tasks on native runtime, early self-hosting experiments |
| **3.0** (2030) | Self-hosted | compiler written in .irl, legacy aliases removed, generics if the policy admits them |

## 17. Concrete next steps for 2.x

1. Ship 2.1 (this release): frozen spec in LANG.md, bootstrap engine,
   compiler, notebook, native accelerator, tooling
2. Extract SEESEMBLY as the real frontend output; builder consumes IR
   instead of AST (mechanical, parity-tested)
3. Native eval core opcodes one-by-one, each behind the parity suite
4. `irl fmt` first (deterministic), then lint/LSP on the same AST API
5. cibuildwheel in the release workflow for native wheels
6. Only then: self-hosting experiments (never a 2.x blocker)
