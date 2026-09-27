# IRL™ Language Specification — 2.1 (frozen)

**IRL™ — the .irl language.** *Python's words with C's braces.* Easy like
Python, honest about being its own language. This document is the frozen
2.1 specification: implementations (bootstrap Python engine today, native
backend tomorrow) must satisfy it exactly.

**Differences from Python at a glance:**

| Concept | Python | .irl 2.1 |
|---|---|---|
| Blocks | indentation + `:` | braces `{}` |
| Variables | `x = 5` (no keyword) | `var x = 5` |
| Conditions | `if age > 18:` | `if (age > 18) { }` — parens required |
| Booleans / None | `True` / `False` / `None` | `true` / `false` / `none` |
| Comments | `#` only | `#` and `//` |
| Statement end | newline | newline (optional `;`) |
| Everything else | — | **the same words, the same behavior** |

---

## 1. Syntax

### 1.1 Statements
- A statement ends at a **newline** or an optional **`;`** (both allowed, mix freely).
- Newlines inside `(...)`, `[...]` and `{...}` literals/calls are ignored.
- Comments: `// line` and `# line`.
- Shebang (`#!/usr/bin/env irl`) is a comment — scripts are executable.

### 1.2 Programs
```js
// hello.irl
var name = input("Name: ")
print(f"hello {name}")
```
Run it: `irl hello.irl` (or `irl lang run hello.irl`).

## 2. Variables & types

- Declare with `var` (aliases: `let`; legacy: `snag`). Assignment to an
  undeclared name is an error.
- Types are exactly Python's at runtime, and `type(x)` prints Python-exact:
  `<class 'int'>`, `<class 'float'>`, `<class 'str'>`, `<class 'bool'>`,
  `<class 'list'>`, `<class 'dict'>`, `<class 'function'>`, `<class 'NoneType'>`.
- Numbers: integers are **arbitrary-precision**; floats are IEEE doubles
  printed shortest-repr (`2.5`, `0.1`); `/` is true division (`10 / 4` → `2.5`).
- Truthiness is Python's: `false`, `0`, `0.0`, `""`, `[]`, `{}`, `none` are
  falsey; everything else is truthy.

## 3. Operators

`+ - * / ** == != < > <= >= and or not in not in`, unary `-`/`+`/`not`.
Precedence: `or` < `and` < `not` < comparisons < `+ -` < `* /` < `**` <
postfix (calls/index/slices/methods) < primary. `**` is right-associative
(`2 ** 3 ** 2` → `512`). `and`/`or` short-circuit and **return the operand
value** (Python semantics). `+` does NOT auto-convert: mixing str and number
is an error — convert with `str()` / `int()`.

## 4. Control flow

```js
if (score >= 90) {
    print("A")
} elif (score >= 80) {
    print("B")
} else {
    print("keep grinding")
}

while (lives > 0) {
    lives = lives - 1
    if (lives == 2) { continue }
    if (lives == 0) { break }
}

for (item in inventory) {
    print(item)
}

for (i in range(0, 10, 2)) {
    print(i)
}
```

`for (name in iterable)` iterates lists, dict **keys**, strings (chars),
and `range(...)`. `break` / `continue` work in both loops. `return` exits a
function (a top-level `return` ends the program).

## 5. Data structures

```js
var scores = [91, 77, 85]
scores.append(100)              // method (legacy builtin push(list, x) also works)
print(scores[0], scores[-1], scores[1:3])

var ages = {"anika": 24, "sam": 19}
ages["kim"] = 15
print(ages.keys(), ages.values(), "sam" in ages)
```

Lists have reference semantics (`var b = a` aliases the same list). Dicts
iterate keys. Indexing a missing key raises; slicing never does.

**String methods:** `upper lower strip lstrip rsplit split replace startswith
endswith join find count isdigit isalpha title capitalize zfill`
**List methods:** `append reverse sort pop insert remove extend index count`
**Dict methods:** `keys values items get pop`

## 6. Strings & f-strings

Double-quoted; escapes `\n \t \r \" \\ \{ \}`. F-strings interpolate any
expression: `f"{name} is {age + 1}"`; literal braces are `{{` and `}}`.

## 7. Functions

```js
function fib(n) {
    if (n < 2) { return n }
    return fib(n - 1) + fib(n - 2)
}

memo function fib_fast(n) {     // auto-cached across calls
    if (n < 2) { return n }
    return fib_fast(n - 1) + fib_fast(n - 2)
}
```

- `function` (aliases `def`, `fn`; legacy `task`). Params positional only.
- Functions see **globals + their params** (no closures in 2.1).
- `memo` caches every call (unhashable arguments skip the cache safely).
- Recursion is capped at 200 nested calls with a clear error.

## 8. Imports

```js
import math                      // stdlib (capability allowlist)
import random
import "utils.irl"               // local module: top-level names merge
```

**Allowed stdlib modules (2.1):** `math`, `random`, `time`, `datetime`,
`json`, `string`, `statistics`. Anything else is refused — this is a
security boundary, not an oversight. Attribute and method access on
modules works: `math.sqrt(16)`, `math.pi`, `random.randint(1, 6)`.

## 9. Builtins

`print` (multi-arg, `sep=`, `end=`) · `input` · `int` · `float` · `str` ·
`len` · `range` · `sum` · `min` · `max` · `abs` · `round` · `sorted` ·
`type` · `isinstance` · `append(list, x)`.

## 10. Errors

Syntax errors carry line + column and render with a caret:
```
[IRL_ERROR] line 2, col 5: Expected a variable name, got '='.
      var = 5
          ^
```
Runtime errors: `[IRL_RUNTIME_ERROR] (line N) message`.

## 11. Tooling (per invocation)

| Command | What |
|---|---|
| `irl file.irl` | run (shebang-friendly) |
| `irl lang run <f>` | run via subcommand |
| `irl lang build <f> [-O0/1/2] [--run] [--emit-ir] [--emit-py] [-v] [-o out]` | compile to CPython bytecode |
| `irl lang check <f> [--json]` | validate, exit code 0/1 |
| `irl lang spec [--json]` | grammar + keywords |
| `irl lang bench` | interpreter vs compiled vs CPython |
| `irl notebook [f.irlnb]` | cells + persistent kernel |
| `irl lang repl` | persistent kernel REPL |

## 12. Legacy aliases (run on 2.x, removed in 3.0)

`snag`→`var` · `spill`→`print` (the 2.0 `💦` prefix is gone) ·
`ask`→`input` · `bet`/`cap`→`if`/`else` · `grind`→`while` · `brb`→`return` ·
`task`→`function` · `fax`/`fake`→`true`/`false` · `fr`/`nah`→`and`/`not` ·
`push`→`append`.

## 13. What 2.1 deliberately does not have

Classes, try/except, tuples/sets, lambdas, closures, generics, modules-as-
objects, `async`. Roadmap and reasoning: see DESIGN.md §2 and §16.
