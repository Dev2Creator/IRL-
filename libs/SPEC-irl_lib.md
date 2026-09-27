# SPEC-irl_lib — The .irl Standard Library 🧰

**Status:** Specification v1.0 (implementation target: ecosystem phase 1 —
ships alongside `irlglass`)
**Frozen-language contract:** IRL 2.1 semantics only. No new syntax.
**Named plainly because it IS the plain one:** everything a .irl program
needs that the language core doesn't ship — strings, collections, paths,
time, parsing, logging. The numpy-class power lives in `irlglass`; this
is the everyday toolbox.

## 1. Identity

- Package: `irl_lib` — submodules via local imports:
  `import "irl_lib/str.irl"` etc. (2.1 has no package-qualified imports;
  the loader merge semantics make submodule files work — PACKAGING.md §4)
- Pure .irl wherever possible; **bridges only for real I/O** (files,
  process env) — the same bridge law as every ecosystem package
- Zero dependencies on other ecosystem packages

## 2. Modules & public API

### `str.irl` — string toolkit
| Function | Notes |
|---|---|
| `title_case(s)` / `snake_case(s)` / `kebab_case(s)` / `camel_case(s)` | deterministic conversions |
| `pad_left(s, n, ch)` / `pad_right(s, n, ch)` | explicit fill char |
| `truncate(s, n, suffix="...")` | |
| `count_words(s)` / `word_wrap(s, width)` | |
| `starts_any(s, prefixes)` / `strip_any(s, cuts)` | list-based |
| `is_blank(s)` | whitespace-only |
| `repeat(s, n)` | |
| `replace_many(s, pairs)` | dict of → replacements, one pass |

### `coll.irl` — collections
| Function | Notes |
|---|---|
| `unique(items)` | order-preserving |
| `freq(items)` | dict value → count |
| `group_by(items, keyfn)` | dict key → list |
| `sort_by(items, keyfn)` / `sort_desc(items, keyfn)` | stable |
| `zip_lists(a, b)` | list of `[a_i, b_i]` pairs, stops at shorter |
| `flatten_one(items)` | one level |
| `chunks(items, n)` | list of n-sized lists |
| `take(items, n)` / `drop(items, n)` | |
| `first(items)` / `last(items)` | none on empty |
| `range_step` notes | builtin `range` covers it — no duplicate here |

### `path.irl` — files & paths (bridge-backed)
| Function | Notes |
|---|---|
| `join(parts)` | platform-correct join (pure .irl over bridge sep) |
| `exists(p)` / `is_file(p)` / `is_dir(p)` | bridge stat |
| `read_text(p)` / `write_text(p, s)` / `append_text(p, s)` | utf-8 always |
| `read_lines(p)` | list, newline-stripped |
| `list_dir(p)` | names only |
| `mkdir(p)` | parents ok |
| `remove(p)` / `remove_dir(p)` | file / empty dir |
| `home()` / `cwd()` | |
| **Sandbox law:** the bridge resolves every path; env var
  `IRL_LIB_ROOT` (set at runtime start) confines all operations —
  outside it, error `[irl_lib] path escapes sandbox` | security by
  default, matches notebook/allowlist philosophy |

### `time.irl` — dates & time (bridge for clocks, .irl math for calendars)
| Function | Notes |
|---|---|
| `now()` | epoch seconds float (bridge) |
| `today_str()` / `now_str()` | `YYYY-MM-DD` / ISO datetime (pure .irl civil-calendar math) |
| `epoch_to_str(e)` / `str_to_epoch(s)` | ISO round-trip |
| `add_days(e, n)` / `diff_days(a, b)` | civil calendar, no DST traps |
| `weekday(e)` | 0=Mon |
| `sleep(s)` | bridge (the interpreter core never sleeps) |

### `parse.irl` — structured data helpers
| Function | Notes |
|---|---|
| `parse_csv(text)` | → list of dicts (header row); quoted fields supported |
| `to_csv(rows)` | inverse; deterministic column order (first-seen) |
| `parse_kv(lines, sep=":")` | config-style lines → dict |
| `parse_bool(s)` | `"true/yes/1/on"` → true (case-insensitive), else error |
| `parse_int_safe(s)` / `parse_float_safe(s)` | none on failure — no exceptions for expected cases |

### `log.irl` — logging
| Function | Notes |
|---|---|
| `log_info(msg)` / `log_warn(msg)` / `log_error(msg)` | `LEVEL: msg` to stderr via bridge, ISO timestamp prefix |
| `log_set_level(level)` | `"debug" | "info" | "warn" | "error"` |
| `log_debug(msg)` | hidden unless debug level |
Deterministic format — machine-greppable, AI-readable.

## 3. Errors

All prefixed `[irl_lib]`, with the module named:
`[irl_lib/path] path escapes sandbox: /etc/passwd` ·
`[irl_lib/parse] parse_bool: 'maybe' is not a boolean`.
`parse_*_safe` variants return `none` instead of raising (documented per
function — the safe/raising split is explicit, never implicit).

## 4. Package layout

```
irl_lib/
├── lib/
│   ├── str.irl  coll.irl  parse.irl  log.irl   # pure .irl
│   └── path.irl  time.irl                      # thin .irl over bridge
├── _bridge/
│   └── io_bridge.py    # file/clock/env — sandboxed, stdlib-only
├── tests/
├── examples/
├── api.json
└── pkg.json
```

## 5. Test plan

1. String conversions round-trips (`snake→camel→snake` identity)
2. Collections: order preservation, stability, empty-input behavior
3. `parse_csv` with quotes/commas/newlines-in-quotes
4. Path sandbox: escape attempts rejected; normal ops pass
5. Calendar math across month/year boundaries (2026-02-28 + 1 day)
6. Logging format snapshot; level filtering
7. Everything passes `irl lang check`; examples run clean

## 6. Compatibility

- IRL 2.1 bootstrap: everything above
- Native runtime: `.irl` modules permanent; `io_bridge` replaced by
  runtime syscalls (sandbox law preserved); calendar math already pure
- No dependencies; the dependency OTHER packages have
