"""IRL language interpreter — 2.1 "Full Language Edition".

Tree-walking evaluator with a precomputed dispatch table (no per-node
getattr string building), Python-exact semantics and display, builtins,
methods on str/list/dict, stdlib imports, memo functions, slicing,
f-strings and a friendly recursion limit.
"""

import importlib
import os
import types

from .lexer import lex  # noqa: F401  (re-exported)
from .parser import (  # noqa: F401  (re-exported)
    Array,
    Assign,
    Attribute,
    BinOp,
    Block,
    Boolean,
    BreakStmt,
    ContinueStmt,
    DictLit,
    ForStmt,
    FString,
    FunctionCall,
    FunctionDef,
    Identifier,
    IfStmt,
    ImportStmt,
    IndexExpr,
    MethodCall,
    NoneLiteral,
    Number,
    Program,
    ReturnStmt,
    Slice,
    String,
    UnaryOp,
    VarDecl,
    WhileStmt,
    parse,  # noqa: F401  (re-exported)
)


class IrlRuntimeError(Exception):
    def __init__(self, message, line=None):
        self.message = message
        self.line = line
        where = f" (line {line})" if line else ""
        super().__init__(f"[IRL_RUNTIME_ERROR]{where} {message}")


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


class BreakException(Exception):
    pass


class ContinueException(Exception):
    pass


MAX_RECURSION = 200

STDLIB_ALLOWLIST = (
    "math",
    "random",
    "time",
    "datetime",
    "json",
    "string",
    "statistics",
)

STRING_METHODS = {
    "upper",
    "lower",
    "strip",
    "lstrip",
    "rstrip",
    "split",
    "rsplit",
    "replace",
    "startswith",
    "endswith",
    "join",
    "find",
    "count",
    "isdigit",
    "isalpha",
    "title",
    "capitalize",
    "zfill",
}
LIST_METHODS = {
    "append",
    "reverse",
    "sort",
    "pop",
    "insert",
    "remove",
    "extend",
    "index",
    "count",
}
DICT_METHODS = {"keys", "values", "items", "get", "pop"}


class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def declare(self, name, value):
        self.vars[name] = value

    def get(self, name):
        env = self
        while env is not None:
            if name in env.vars:
                return env.vars[name]
            env = env.parent
        raise IrlRuntimeError(f"'{name}' is not defined. Declare it first: var {name} = ...")

    def assign(self, name, value):
        env = self
        while env is not None:
            if name in env.vars:
                env.vars[name] = value
                return
            env = env.parent
        raise IrlRuntimeError(f"Assigning to '{name}' before declaring it. Use: var {name} = ...")


class IrlFunction:
    def __init__(self, definition, interpreter):
        self.definition = definition
        self.interpreter = interpreter
        self.cache = {} if definition.memo else None

    def __call__(self, *args, **kwargs):
        defn = self.definition
        if kwargs:
            raise IrlRuntimeError(
                f"{defn.name}() does not take named arguments yet.",
                defn.line,
            )
        if len(args) != len(defn.params):
            raise IrlRuntimeError(
                f"{defn.name}() takes {len(defn.params)} argument(s), got {len(args)}.",
                defn.line,
            )
        if self.cache is not None:
            try:
                if args in self.cache:
                    return self.cache[args]
            except TypeError:
                pass  # unhashable args (e.g. lists) — compute, don't cache
        local = Environment(self.interpreter.global_env)
        for param, arg in zip(defn.params, args):
            local.declare(param, arg)
        self.interpreter._depth += 1
        if self.interpreter._depth > MAX_RECURSION:
            self.interpreter._depth = 0
            raise IrlRuntimeError(
                f"Recursion went {MAX_RECURSION} calls deep in {defn.name}(). Give it a base case that fires, or use a loop instead.",
                defn.line,
            )
        try:
            self.interpreter.run_scoped(defn.block, local)
            result = None
        except ReturnException as ret:
            result = ret.value
        except RecursionError:
            raise IrlRuntimeError(
                f"Recursion went too deep in {defn.name}(). Give it a base case that fires, or use a loop instead.",
                defn.line,
            )
        finally:
            self.interpreter._depth -= 1
        if self.cache is not None:
            try:
                self.cache[args] = result
            except TypeError:
                pass  # unhashable args — skip caching
        return result


def _append(seq, item):
    if isinstance(seq, list):
        seq.append(item)
        return seq
    raise IrlRuntimeError("append() needs a list.")


def _type_name(value):
    return type(value).__name__


class Interpreter:
    def __init__(self, source_dir=None):
        self.global_env = Environment()
        self._env = self.global_env
        self._depth = 0
        self._source_dir = source_dir
        self._imported_files = set()
        self._dispatch = {
            Program: self.visit_Program,
            Block: self.visit_Block,
            FunctionDef: self.visit_FunctionDef,
            VarDecl: self.visit_VarDecl,
            Assign: self.visit_Assign,
            IfStmt: self.visit_IfStmt,
            WhileStmt: self.visit_WhileStmt,
            ForStmt: self.visit_ForStmt,
            BreakStmt: self.visit_BreakStmt,
            ContinueStmt: self.visit_ContinueStmt,
            ReturnStmt: self.visit_ReturnStmt,
            ImportStmt: self.visit_ImportStmt,
            FunctionCall: self.visit_FunctionCall,
            MethodCall: self.visit_MethodCall,
            Attribute: self.visit_Attribute,
            BinOp: self.visit_BinOp,
            UnaryOp: self.visit_UnaryOp,
            IndexExpr: self.visit_IndexExpr,
            Slice: self.visit_Slice,
            Array: self.visit_Array,
            DictLit: self.visit_DictLit,
            FString: self.visit_FString,
            Number: self.visit_Number,
            String: self.visit_String,
            Boolean: self.visit_Boolean,
            NoneLiteral: self.visit_NoneLiteral,
            Identifier: self.visit_Identifier,
        }
        self._install_builtins()

    def _install_builtins(self):
        for name, fn in {
            "print": print,
            "input": input,
            "int": int,
            "float": float,
            "str": str,
            "len": len,
            "range": range,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
            "round": round,
            "sorted": sorted,
            "type": type,
            "isinstance": isinstance,
            "append": _append,
        }.items():
            self.global_env.declare(name, fn)

    # -- entry points ------------------------------------------------------

    def interpret(self, ast):
        return self.visit(ast)

    def visit(self, node):
        return self._dispatch[type(node)](node)

    def run_scoped(self, block, scope):
        old = self._env
        self._env = scope
        try:
            for stmt in block.statements:
                self.visit(stmt)
        finally:
            self._env = old

    # -- statements ---------------------------------------------------------

    def visit_Program(self, node):
        result = None
        try:
            for stmt in node.statements:
                result = self.visit(stmt)
        except ReturnException as ret:
            result = ret.value
        return result

    def visit_Block(self, node):
        for stmt in node.statements:
            self.visit(stmt)
        return None

    def visit_FunctionDef(self, node):
        self._env.declare(node.name, IrlFunction(node, self))
        return None

    def visit_VarDecl(self, node):
        self._env.declare(node.name, self.visit(node.value))
        return None

    def visit_Assign(self, node):
        value = self.visit(node.value)
        target = node.target
        if isinstance(target, Identifier):
            self._env.assign(target.name, value)
        elif isinstance(target, IndexExpr):
            obj = self.visit(target.array_expr)
            index = self.visit(target.index_expr)
            try:
                obj[index] = value
            except IndexError:
                raise IrlRuntimeError(f"Index {index} is out of range.", node.line)
            except TypeError as exc:
                raise IrlRuntimeError(str(exc), node.line)
        else:
            raise IrlRuntimeError("Invalid assignment target.", node.line)
        return None

    def visit_IfStmt(self, node):
        if self.visit(node.condition):
            self.run_scoped(node.true_block, Environment(self._env))
        elif node.false_block is not None:
            self.run_scoped(node.false_block, Environment(self._env))
        return None

    def visit_WhileStmt(self, node):
        while self.visit(node.condition):
            try:
                self.run_scoped(node.block, Environment(self._env))
            except BreakException:
                break
            except ContinueException:
                continue
        return None

    def visit_ForStmt(self, node):
        iterable = self.visit(node.iter_expr)
        try:
            iterator = iter(iterable)
        except TypeError:
            raise IrlRuntimeError(
                f"'{_type_name(iterable)}' is not iterable — for needs a list, dict, string or range().",
                node.line,
            )
        for item in iterator:
            scope = Environment(self._env)
            scope.declare(node.var_name, item)
            try:
                self.run_scoped(node.block, scope)
            except BreakException:
                break
            except ContinueException:
                continue
        return None

    def visit_BreakStmt(self, node):
        raise BreakException()

    def visit_ContinueStmt(self, node):
        raise ContinueException()

    def visit_ReturnStmt(self, node):
        value = self.visit(node.value) if node.value is not None else None
        raise ReturnException(value)

    def visit_ImportStmt(self, node):
        if node.path is not None:
            self._import_local(node)
            return None
        if node.module not in STDLIB_ALLOWLIST:
            raise IrlRuntimeError(
                f"Module '{node.module}' is not available. Allowed: " + ", ".join(STDLIB_ALLOWLIST),
                node.line,
            )
        try:
            module = importlib.import_module(node.module)
        except Exception as exc:  # pragma: no cover - defensive
            raise IrlRuntimeError(f"Could not import {node.module}: {exc}", node.line)
        self._env.declare(node.module, module)
        return None

    def _import_local(self, node):
        base = self._source_dir or os.getcwd()
        path = os.path.abspath(os.path.join(base, node.path))
        if not path.endswith(".irl"):
            path += ".irl"
        if not os.path.isfile(path):
            raise IrlRuntimeError(
                f"Local module '{node.path}' not found (looked for {path}).",
                node.line,
            )
        if path in self._imported_files:
            return
        self._imported_files.add(path)
        with open(path, encoding="utf-8") as fh:
            code = fh.read()
        program = parse(lex(code))
        for stmt in program.statements:
            self.visit(stmt)

    # -- expressions ---------------------------------------------------------

    def visit_FunctionCall(self, node):
        fn = self._env.get(node.name)
        args = [self.visit(a) for a in node.args]
        kwargs = {k: self.visit(v) for k, v in node.kwargs.items()}
        if isinstance(fn, IrlFunction):
            return fn(*args, **kwargs)
        if callable(fn):
            try:
                return fn(*args, **kwargs)
            except IrlRuntimeError:
                raise
            except TypeError as exc:
                raise IrlRuntimeError(f"{node.name}(): {exc}", node.line)
        raise IrlRuntimeError(
            f"'{node.name}' is not a function (it's a {_type_name(fn)}).",
            node.line,
        )

    def visit_MethodCall(self, node):
        obj = self.visit(node.obj)
        args = [self.visit(a) for a in node.args]
        kwargs = {k: self.visit(v) for k, v in node.kwargs.items()}
        if isinstance(obj, types.ModuleType):
            try:
                attr = getattr(obj, node.name)
            except AttributeError:
                raise IrlRuntimeError(f"Module has no attribute '{node.name}'.", node.line)
            if not callable(attr):
                return attr
            try:
                return attr(*args, **kwargs)
            except TypeError as exc:
                raise IrlRuntimeError(f"{node.name}(): {exc}", node.line)
        if isinstance(obj, str):
            allowed = STRING_METHODS
        elif isinstance(obj, list):
            allowed = LIST_METHODS
        elif isinstance(obj, dict):
            allowed = DICT_METHODS
        else:
            raise IrlRuntimeError(f"'{_type_name(obj)}' has no methods.", node.line)
        if node.name not in allowed:
            raise IrlRuntimeError(f"'{_type_name(obj)}' has no method '{node.name}'.", node.line)
        try:
            return getattr(obj, node.name)(*args, **kwargs)
        except (AttributeError, TypeError, ValueError) as exc:
            raise IrlRuntimeError(f"{node.name}(): {exc}", node.line)

    def visit_Attribute(self, node):
        obj = self.visit(node.obj)
        if isinstance(obj, types.ModuleType):
            try:
                return getattr(obj, node.name)
            except AttributeError:
                raise IrlRuntimeError(f"Module has no attribute '{node.name}'.", node.line)
        raise IrlRuntimeError(
            f"Attributes can only be read from modules; call methods with (): '{node.name}()'.",
            node.line,
        )

    def visit_BinOp(self, node):
        op = node.op
        if op == "and":
            left = self.visit(node.left)
            return self.visit(node.right) if left else left
        if op == "or":
            left = self.visit(node.left)
            return left if left else self.visit(node.right)
        left = self.visit(node.left)
        right = self.visit(node.right)
        ops = {
            "+": lambda: left + right,
            "-": lambda: left - right,
            "*": lambda: left * right,
            "/": lambda: left / right,
            "**": lambda: left**right,
            "==": lambda: left == right,
            "!=": lambda: left != right,
            "<": lambda: left < right,
            ">": lambda: left > right,
            "<=": lambda: left <= right,
            ">=": lambda: left >= right,
            "in": lambda: left in right,
            "not in": lambda: left not in right,
        }
        if op not in ops:
            raise IrlRuntimeError(f"Unknown operator '{op}'.", node.line)
        try:
            return ops[op]()
        except ZeroDivisionError:
            raise IrlRuntimeError("Division by zero.", node.line)
        except TypeError:
            raise IrlRuntimeError(
                f"Can't apply '{op}' to {_type_name(left)} and {_type_name(right)} — convert with str() or int().",
                node.line,
            )

    def visit_UnaryOp(self, node):
        value = self.visit(node.expr)
        try:
            if node.op == "not":
                return not value
            if node.op == "-":
                return -value
            if node.op == "+":
                return +value
        except TypeError:
            raise IrlRuntimeError(f"Can't apply '{node.op}' to {_type_name(value)}.", node.line)
        raise IrlRuntimeError(f"Unknown unary operator '{node.op}'.", node.line)

    def visit_IndexExpr(self, node):
        obj = self.visit(node.array_expr)
        index = self.visit(node.index_expr)
        try:
            return obj[index]
        except IndexError:
            raise IrlRuntimeError(f"Index {index} is out of range.", node.line)
        except KeyError:
            raise IrlRuntimeError(f"Key {index!r} is not in the dict.", node.line)
        except TypeError as exc:
            raise IrlRuntimeError(str(exc), node.line)

    def visit_Slice(self, node):
        start = self.visit(node.start) if node.start is not None else None
        stop = self.visit(node.stop) if node.stop is not None else None
        step = self.visit(node.step) if node.step is not None else None
        return slice(start, stop, step)

    def visit_Array(self, node):
        return [self.visit(el) for el in node.elements]

    def visit_DictLit(self, node):
        return {self.visit(k): self.visit(v) for k, v in node.pairs}

    def visit_FString(self, node):
        out = []
        for kind, part in node.parts:
            if kind == "text":
                out.append(part)
            else:
                value = self.visit(part)
                out.append(value if isinstance(value, str) else str(value))
        return "".join(out)

    def visit_Number(self, node):
        return node.value

    def visit_String(self, node):
        return node.value

    def visit_Boolean(self, node):
        return node.value

    def visit_NoneLiteral(self, node):
        return None

    def visit_Identifier(self, node):
        return self._env.get(node.name)


def evaluate(ast, source_dir=None):
    return Interpreter(source_dir=source_dir).interpret(ast)
