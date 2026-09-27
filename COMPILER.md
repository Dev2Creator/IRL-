# IRL™ Compiler — how the .irl pipeline works ⚙️

The compiler is a **multi-pass pipeline with honest reporting**. It is the
first backend of the SEESEMBLY contract (DESIGN.md §3); the Zig/native
backend plugs into the same contract later.

## Pipeline

```
file.irl
   ↓  lex            (native machine-code accelerator, Python fallback)
   ↓  parse          (recursive descent → AST)
   ↓  optimize       (constant folding, dead-code elimination, memo lowering)
   ↓  transpile      (scope-aware IR → Python source)
   ↓  CPython compiler  (the back end — 30 years of optimization)
   ↓
app.pyc  (+ app.py for reading)  →  runs at full CPython speed
```

## Using it

```zsh
irl lang build app.irl                 # → app.pyc + app.py
irl lang build app.irl --run           # compile and execute immediately
irl lang build app.irl -O2 -v          # max optimization + what-it-did report
irl lang build app.irl --emit-py       # print the generated Python
irl lang build app.irl --emit-ir       # inspect the IR
irl lang build app.irl -o out          # custom output base name
```

## Optimization levels

| Level | Passes |
|---|---|
| `-O0` | none (reference codegen) |
| `-O1` (default) | constant folding, algebraic identities, dead-code elimination, `memo` lowering |
| `-O2` | everything above + builtin caching (`len`, `print`, … hoisted to locals) |

`-v` prints the report — the compiler never lies about what it did:
```
optimizer: folded 14 constant(s), removed 2 dead branch(es), memoized 1 function(s)
```

## What each pass does

- **Constant folding** — `2 + 3 * 4` becomes `14` at build time (guarded:
  division by zero and huge powers are not folded)
- **Dead-code elimination** — `if (false) { … }` and `while (false) { … }`
  are pruned, branch counted
- **Memo lowering** — `memo function` gets a cache decorator with
  unhashable-argument safety (identical semantics to the interpreter)
- **Builtin caching (`-O2`)** — builtins used in the program are hoisted to
  module-level locals, removing per-call global lookups inside loops

## Scope handling

.irl has block scoping (like the interpreter's environment chains); Python
has function scoping. The transpiler runs a **symbol-table pass** that gives
every block-level declaration a scope-aware unique name, so shadowing
behaves identically in both backends. Assign-before-declare is a **build
error**, not a runtime surprise.

## Build cache

`.irl_cache/` (next to the source) stores compiled artifacts keyed by
content hash + optimization level. Unchanged sources are cache hits —
rebuilds are instant, notebook re-runs reuse the same key.

## Parity guarantee

`tests/test_lang.py` runs identical programs through the interpreter and
the compiler and asserts byte-identical output. The two backends share one
front end and one optimizer contract.

## Host language status (bootstrap law)

Today the pipeline's implementation is Python (the **bootstrap**). The
frontend/AST/optimizer are the permanent assets; the native (Zig) backend
implements the same IR contract — see DESIGN.md §0 and §16 for the
migration law and the 2030 roadmap.
