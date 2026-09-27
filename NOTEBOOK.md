# IRL™ Notebook 📓🌱

A Jupyter-style notebook for the .irl language — **zero dependencies**.
Code cells, markdown notes, one persistent kernel, save/load as `.irlnb`,
export to plain `.irl`.

## Quickstart

```zsh
irl notebook                  # fresh notebook
irl notebook my.irlnb         # open an existing one
```

Your browser opens at `http://127.0.0.1:<port>` (localhost only).

## Using it

- **Shift+Enter** runs the current cell (▶ button works too)
- The **kernel is persistent**: define a function in cell 1, use it in cell 7
- **+ code / + note** adds cells; ↑ ↓ reorder; ✕ deletes
- **Save** writes the `.irlnb` file (JSON: `{"irl_notebook": 1, "cells": [...]}`)
- **Export .irl** concatenates all code cells into a runnable script

## The format

```json
{
  "irl_notebook": 1,
  "cells": [
    {"type": "markdown", "source": "# Notes"},
    {"type": "code", "source": "var x = 42\nprint(x)"}
  ]
}
```

## Good to know

- The server binds **127.0.0.1 only** — nothing is exposed to the network
- Kernel imports follow the language allowlist (`math`, `random`, `time`,
  `datetime`, `json`, `string`, `statistics`) — see LANG.md §8
- Kernel state is per-server-run: close with Ctrl-C, reopen fresh
- Errors render inline in red with line info — no tracebacks
