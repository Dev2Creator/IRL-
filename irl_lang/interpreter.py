import time
from .parser import (
    Program, Block, VarDecl, Assign, IfStmt, WhileStmt, 
    SpillStmt, ReturnStmt, BinOp, UnaryOp, Number, String, Boolean, Identifier,
    FunctionDef, FunctionCall, Array, IndexExpr
)

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class IrlRuntimeError(Exception):
    def __init__(self, message):
        super().__init__(f"\n[IRL_RUNTIME_ERROR] ☠️ RIP. {message}")

class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def declare(self, name, value):
        if name in self.vars:
            raise IrlRuntimeError(f"You already snagged '{name}'. Why are you declaring it again?")
        self.vars[name] = value

    def assign(self, name, value):
        if name in self.vars:
            self.vars[name] = value
        elif self.parent:
            self.parent.assign(name, value)
        else:
            raise IrlRuntimeError(f"Trying to assign to '{name}' before snagging it. That's illegal.")

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise IrlRuntimeError(f"Variable '{name}' doesn't exist. Are you hallucinating?")

# Built-in functions
def builtin_ask(args):
    prompt = args[0] if len(args) > 0 else ""
    return input(prompt)

def builtin_len(args):
    if len(args) == 0: return 0
    return len(args[0])

def builtin_push(args):
    if len(args) < 2: raise IrlRuntimeError("push() needs an array and an item.")
    arr = args[0]
    item = args[1]
    if not isinstance(arr, list):
        raise IrlRuntimeError("You can only push to an array.")
    arr.append(item)
    return arr

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        # Add builtins
        self.global_env.declare('ask', builtin_ask)
        self.global_env.declare('len', builtin_len)
        self.global_env.declare('push', builtin_push)

    def interpret(self, node):
        return self.visit(node, self.global_env)

    def visit(self, node, env):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node, env)

    def generic_visit(self, node, env):
        raise IrlRuntimeError(f"No visit_{type(node).__name__} method defined. The dev (me) messed up.")

    def visit_Program(self, node, env):
        result = None
        try:
            for stmt in node.statements:
                result = self.visit(stmt, env)
        except ReturnException as r:
            return r.value
        return result

    def visit_Block(self, node, env):
        block_env = Environment(parent=env)
        for stmt in node.statements:
            self.visit(stmt, block_env)

    def visit_FunctionDef(self, node, env):
        env.declare(node.name, node)

    def visit_FunctionCall(self, node, env):
        func = env.get(node.name)
        args = [self.visit(arg, env) for arg in node.args]
        
        # If it's a built-in Python function
        if callable(func):
            return func(args)
            
        # If it's an IRL function
        if not isinstance(func, FunctionDef):
            raise IrlRuntimeError(f"'{node.name}' is not a task. It's a {type(func).__name__}.")
            
        if len(args) != len(func.params):
            raise IrlRuntimeError(f"Task '{node.name}' expects {len(func.params)} arguments, got {len(args)}.")
            
        func_env = Environment(parent=self.global_env) # functions capture globals
        for param, arg in zip(func.params, args):
            func_env.declare(param, arg)
            
        try:
            self.visit(func.block, func_env)
        except ReturnException as r:
            return r.value
        return None

    def visit_VarDecl(self, node, env):
        value = self.visit(node.value, env)
        env.declare(node.name, value)

    def visit_Assign(self, node, env):
        value = self.visit(node.value, env)
        if isinstance(node.target, Identifier):
            env.assign(node.target.name, value)
        elif isinstance(node.target, IndexExpr):
            array = self.visit(node.target.array_expr, env)
            index = self.visit(node.target.index_expr, env)
            if not isinstance(array, list):
                raise IrlRuntimeError("You can only index into arrays.")
            try:
                array[index] = value
            except IndexError:
                raise IrlRuntimeError(f"Index {index} is out of bounds for array of size {len(array)}.")
        else:
            raise IrlRuntimeError("Invalid assignment target.")

    def visit_SpillStmt(self, node, env):
        value = self.visit(node.value, env)
        print(f"💦 {value}")

    def visit_ReturnStmt(self, node, env):
        value = None
        if node.value:
            value = self.visit(node.value, env)
        raise ReturnException(value)

    def visit_IfStmt(self, node, env):
        condition = self.visit(node.condition, env)
        if condition:
            self.visit(node.true_block, env)
        elif node.false_block:
            self.visit(node.false_block, env)

    def visit_WhileStmt(self, node, env):
        while self.visit(node.condition, env):
            self.visit(node.block, env)
            time.sleep(0.001) 

    def visit_UnaryOp(self, node, env):
        expr = self.visit(node.expr, env)
        if node.op == 'nah':
            return not expr
        raise IrlRuntimeError(f"Unknown unary operator '{node.op}'")

    def visit_BinOp(self, node, env):
        left = self.visit(node.left, env)
        right = self.visit(node.right, env)
        
        op = node.op
        try:
            if op == '+': 
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right
            if op == '==': return left == right
            if op == '!=': return left != right
            if op == '<': return left < right
            if op == '>': return left > right
            if op == '<=': return left <= right
            if op == '>=': return left >= right
            if op == 'fr': return left and right
            if op == 'or': return left or right
        except Exception as e:
            raise IrlRuntimeError(f"Can't do '{left} {op} {right}'. You're mixing types like a madman.")
            
    def visit_Array(self, node, env):
        return [self.visit(el, env) for el in node.elements]
        
    def visit_IndexExpr(self, node, env):
        array = self.visit(node.array_expr, env)
        index = self.visit(node.index_expr, env)
        if not isinstance(array, list):
            raise IrlRuntimeError("Can only index into an array.")
        if not isinstance(index, int):
            raise IrlRuntimeError("Array index must be a braincell (integer).")
        try:
            return array[index]
        except IndexError:
            raise IrlRuntimeError(f"Index {index} is out of bounds for array of size {len(array)}.")
            
    def visit_Number(self, node, env): return node.value
    def visit_String(self, node, env): return node.value
    def visit_Boolean(self, node, env): return node.value
    def visit_Identifier(self, node, env): return env.get(node.name)

def evaluate(ast):
    interpreter = Interpreter()
    return interpreter.interpret(ast)
