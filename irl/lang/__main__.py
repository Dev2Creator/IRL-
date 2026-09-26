import os
import sys

from .interpreter import IrlRuntimeError, evaluate
from .lexer import IrlSyntaxError, lex
from .parser import parse


def main():
    if len(sys.argv) < 2:
        print("☠️  BRUH. You didn't give me a file to run.")
        print("Usage: python -m irl_lang <file.irl>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"☠️  BRUH. The file '{filepath}' literally doesn't exist.")
        sys.exit(1)

    with open(filepath, encoding="utf-8") as f:
        code = f.read()

    try:
        tokens = lex(code)
        ast = parse(tokens)
        evaluate(ast)
    except (IrlSyntaxError, IrlRuntimeError) as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"\n[IRL_CRITICAL] ☠️ Something went catastrophically wrong: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
