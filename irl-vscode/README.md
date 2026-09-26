# IRL Language Support

Syntax highlighting and snippets for the **.irl** toy language — the
chaotic little language that ships with [irl-pkg](https://pypi.org/project/irl-pkg/)
(`pip install irl-pkg`, then `irl lang demo`).

Keywords: `snag` (declare), `spill` (print), `bet`/`cap` (if/else),
`grind` (while), `brb` (return), `task` (function), with the truth
values `fax` and `fake` and logic operators `fr`, `or`, `nah`.

## Features

- TextMate grammar for the full language surface
- Snippets for tasks, conditionals and loops
- Bracket and comment rules for .irl files

## Running .irl files

```bash
pip install irl-pkg
irl lang run myfile.irl
irl lang repl
```

## License

AGPL-3.0-or-later — see [LICENSE](../LICENSE) in the repository root.
