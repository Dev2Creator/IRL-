"""IRL language parser — 2.1 "Full Language Edition".

Recursive descent over the canonical token stream. Statements end at a
newline or optional `;`. Blocks use braces. Supports elif chains, for-in,
break/continue, dicts, method/attribute calls, slicing, f-strings, kwargs,
imports and memo functions. Legacy slang never reaches this module — the
lexer already canonicalized it.
"""

from .lexer import IrlSyntaxError, lex


class ASTNode:
    pass


class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements
        self.line = 1


class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements
        self.line = 0


class FunctionDef(ASTNode):
    def __init__(self, name, params, block, memo=False, line=0):
        self.name = name
        self.params = params
        self.block = block
        self.memo = memo
        self.line = line


class VarDecl(ASTNode):
    def __init__(self, name, value, line=0):
        self.name = name
        self.value = value
        self.line = line


class Assign(ASTNode):
    def __init__(self, target, value, line=0):
        self.target = target
        self.value = value
        self.line = line


class IfStmt(ASTNode):
    def __init__(self, condition, true_block, false_block, line=0):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block
        self.line = line


class WhileStmt(ASTNode):
    def __init__(self, condition, block, line=0):
        self.condition = condition
        self.block = block
        self.line = line


class ForStmt(ASTNode):
    def __init__(self, var_name, iter_expr, block, line=0):
        self.var_name = var_name
        self.iter_expr = iter_expr
        self.block = block
        self.line = line


class BreakStmt(ASTNode):
    def __init__(self, line=0):
        self.line = line


class ContinueStmt(ASTNode):
    def __init__(self, line=0):
        self.line = line


class ReturnStmt(ASTNode):
    def __init__(self, value, line=0):
        self.value = value
        self.line = line


class ImportStmt(ASTNode):
    def __init__(self, module, path=None, line=0):
        self.module = module
        self.path = path
        self.line = line


class FunctionCall(ASTNode):
    def __init__(self, name, args, kwargs=None, line=0):
        self.name = name
        self.args = args
        self.kwargs = kwargs or {}
        self.line = line


class MethodCall(ASTNode):
    def __init__(self, obj, name, args, kwargs=None, line=0):
        self.obj = obj
        self.name = name
        self.args = args
        self.kwargs = kwargs or {}
        self.line = line


class Attribute(ASTNode):
    def __init__(self, obj, name, line=0):
        self.obj = obj
        self.name = name
        self.line = line


class BinOp(ASTNode):
    def __init__(self, left, op, right, line=0):
        self.left = left
        self.op = op
        self.right = right
        self.line = line


class UnaryOp(ASTNode):
    def __init__(self, op, expr, line=0):
        self.op = op
        self.expr = expr
        self.line = line


class IndexExpr(ASTNode):
    def __init__(self, array_expr, index_expr, line=0):
        self.array_expr = array_expr
        self.index_expr = index_expr
        self.line = line


class Slice(ASTNode):
    def __init__(self, start, stop, step=None, line=0):
        self.start = start
        self.stop = stop
        self.step = step
        self.line = line


class Array(ASTNode):
    def __init__(self, elements, line=0):
        self.elements = elements
        self.line = line


class DictLit(ASTNode):
    def __init__(self, pairs, line=0):
        self.pairs = pairs
        self.line = line


class FString(ASTNode):
    def __init__(self, parts, line=0):
        self.parts = parts
        self.line = line


class Number(ASTNode):
    def __init__(self, value, line=0):
        self.value = value
        self.line = line


class String(ASTNode):
    def __init__(self, value, line=0):
        self.value = value
        self.line = line


class Boolean(ASTNode):
    def __init__(self, value, line=0):
        self.value = value
        self.line = line


class NoneLiteral(ASTNode):
    def __init__(self, line=0):
        self.line = line


class Identifier(ASTNode):
    def __init__(self, name, line=0):
        self.name = name
        self.line = line


COMPARISON_OPS = ("EQEQ", "NEQ", "LT", "GT", "LTE", "GTE")


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # -- token plumbing ---------------------------------------------------

    def current(self):
        return self.tokens[min(self.pos, len(self.tokens) - 1)]

    def peek(self, offset=1):
        return self.tokens[min(self.pos + offset, len(self.tokens) - 1)]

    def eat(self, token_type, what=None):
        tok = self.current()
        if tok.type == token_type:
            self.pos += 1
            return tok
        expected = what or token_type
        raise IrlSyntaxError(f"Expected {expected}, got '{tok.value or tok.type}'.", tok.line, tok.column)

    def match(self, token_type):
        if self.current().type == token_type:
            tok = self.current()
            self.pos += 1
            return tok
        return None

    def at_keyword(self, *words):
        tok = self.current()
        return tok.type == "KEYWORD" and tok.value in words

    def eat_newlines(self):
        while self.match("NEWLINE"):
            pass

    def end_statement(self):
        while self.current().type in ("SEMI", "NEWLINE"):
            self.pos += 1

    # -- program & statements ---------------------------------------------

    def parse(self):
        statements = []
        self.eat_newlines()
        while self.current().type != "EOF":
            statements.append(self.parse_statement())
            self.end_statement()
            self.eat_newlines()
        return Program(statements)

    def parse_statement(self):
        tok = self.current()
        if tok.type == "KEYWORD":
            word = tok.value
            if word == "var":
                return self.parse_var_decl()
            if word == "function":
                return self.parse_function_def(memo=False)
            if word == "memo":
                self.eat("KEYWORD")
                return self.parse_function_def(memo=True)
            if word == "if":
                return self.parse_if()
            if word == "while":
                return self.parse_while()
            if word == "for":
                return self.parse_for()
            if word == "break":
                self.eat("KEYWORD")
                return BreakStmt(tok.line)
            if word == "continue":
                self.eat("KEYWORD")
                return ContinueStmt(tok.line)
            if word == "return":
                self.eat("KEYWORD")
                value = None
                if self.current().type not in ("SEMI", "NEWLINE", "RBRACE", "EOF"):
                    value = self.parse_expr()
                return ReturnStmt(value, tok.line)
            if word == "import":
                return self.parse_import()

        line = tok.line
        expr = self.parse_expr()
        if self.match("ASSIGN"):
            if not isinstance(expr, (Identifier, IndexExpr)):
                raise IrlSyntaxError("Invalid assignment target.", line, tok.column)
            value = self.parse_expr()
            return Assign(expr, value, line)
        return expr

    def parse_block(self):
        self.eat("LBRACE", "'{'")
        statements = []
        self.eat_newlines()
        while self.current().type not in ("RBRACE", "EOF"):
            statements.append(self.parse_statement())
            self.end_statement()
            self.eat_newlines()
        self.eat("RBRACE", "'}'")
        return Block(statements)

    def parse_var_decl(self):
        tok = self.eat("KEYWORD")  # 'var'
        name_tok = self.eat("IDENT", "a variable name")
        self.eat("ASSIGN", "'='")
        value = self.parse_expr()
        return VarDecl(name_tok.value, value, tok.line)

    def parse_function_def(self, memo):
        tok = self.eat("KEYWORD")  # 'function'
        name_tok = self.eat("IDENT", "a function name")
        self.eat("LPAREN", "'('")
        params = []
        self.eat_newlines()
        if self.current().type != "RPAREN":
            params.append(self.eat("IDENT", "a parameter name").value)
            self.eat_newlines()
            while self.match("COMMA"):
                self.eat_newlines()
                params.append(self.eat("IDENT", "a parameter name").value)
                self.eat_newlines()
        self.eat("RPAREN", "')'")
        block = self.parse_block()
        return FunctionDef(name_tok.value, params, block, memo=memo, line=tok.line)

    def parse_if(self):
        tok = self.eat("KEYWORD")  # 'if'
        self.eat("LPAREN", "'('")
        condition = self.parse_expr()
        self.eat("RPAREN", "')'")
        true_block = self.parse_block()
        false_block = None
        self.eat_newlines()
        if self.at_keyword("elif"):
            self.eat("KEYWORD")
            # 'elif' has already been consumed; parse the rest as an if
            self.eat("LPAREN", "'('")
            elif_cond = self.parse_expr()
            self.eat("RPAREN", "')'")
            elif_block = self.parse_block()
            nested = IfStmt(elif_cond, elif_block, None, tok.line)
            self.eat_newlines()
            while self.at_keyword("elif"):
                self.eat("KEYWORD")
                self.eat("LPAREN", "'('")
                c2 = self.parse_expr()
                self.eat("RPAREN", "')'")
                b2 = self.parse_block()
                innermost = nested
                while innermost.false_block is not None:
                    innermost = innermost.false_block.statements[0]
                innermost.false_block = Block([IfStmt(c2, b2, None, tok.line)])
                self.eat_newlines()
            if self.at_keyword("else"):
                self.eat("KEYWORD")
                else_block = self.parse_block()
                innermost = nested
                while innermost.false_block is not None:
                    innermost = innermost.false_block.statements[0]
                innermost.false_block = else_block
            false_block = Block([nested])
        elif self.at_keyword("else"):
            self.eat("KEYWORD")
            false_block = self.parse_block()
        return IfStmt(condition, true_block, false_block, tok.line)

    def parse_while(self):
        tok = self.eat("KEYWORD")  # 'while'
        self.eat("LPAREN", "'('")
        condition = self.parse_expr()
        self.eat("RPAREN", "')'")
        block = self.parse_block()
        return WhileStmt(condition, block, tok.line)

    def parse_for(self):
        tok = self.eat("KEYWORD")  # 'for'
        self.eat("LPAREN", "'('")
        var_tok = self.eat("IDENT", "a loop variable")
        self.eat("KEYWORD", "'in'")
        iter_expr = self.parse_expr()
        self.eat("RPAREN", "')'")
        block = self.parse_block()
        return ForStmt(var_tok.value, iter_expr, block, tok.line)

    def parse_import(self):
        tok = self.eat("KEYWORD")  # 'import'
        if self.current().type == "STRING":
            path = self.current().value
            self.eat("STRING")
            return ImportStmt(path, path=path, line=tok.line)
        parts = [self.eat("IDENT", "a module name").value]
        while self.match("DOT"):
            parts.append(self.eat("IDENT", "a module name").value)
        return ImportStmt(".".join(parts), line=tok.line)

    # -- expressions --------------------------------------------------------

    def parse_expr(self):
        return self.parse_or()

    def parse_or(self):
        node = self.parse_and()
        while self.at_keyword("or"):
            tok = self.eat("KEYWORD")
            node = BinOp(node, "or", self.parse_and(), tok.line)
        return node

    def parse_and(self):
        node = self.parse_not()
        while self.at_keyword("and"):
            tok = self.eat("KEYWORD")
            node = BinOp(node, "and", self.parse_not(), tok.line)
        return node

    def parse_not(self):
        if self.at_keyword("not"):
            tok = self.eat("KEYWORD")
            return UnaryOp("not", self.parse_not(), tok.line)
        return self.parse_comparison()

    def parse_comparison(self):
        node = self.parse_term()
        while True:
            tok = self.current()
            if tok.type in COMPARISON_OPS:
                self.eat(tok.type)
                node = BinOp(node, tok.value, self.parse_term(), tok.line)
            elif self.at_keyword("in"):
                self.eat("KEYWORD")
                node = BinOp(node, "in", self.parse_term(), tok.line)
            elif self.at_keyword("not") and self.peek().type == "KEYWORD" and self.peek().value == "in":
                self.eat("KEYWORD")
                self.eat("KEYWORD")
                node = BinOp(node, "not in", self.parse_term(), tok.line)
            else:
                return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current().type in ("PLUS", "MINUS"):
            tok = self.eat(self.current().type)
            node = BinOp(node, tok.value, self.parse_factor(), tok.line)
        return node

    def parse_factor(self):
        node = self.parse_unary()
        while self.current().type in ("MUL", "DIV"):
            tok = self.eat(self.current().type)
            node = BinOp(node, tok.value, self.parse_unary(), tok.line)
        return node

    def parse_power(self):
        node = self.parse_postfix()
        if self.match("POWER"):
            tok = self.tokens[self.pos - 1]
            return BinOp(node, "**", self.parse_unary(), tok.line)
        return node

    def parse_unary(self):
        tok = self.current()
        if self.at_keyword("not"):
            self.eat("KEYWORD")
            return UnaryOp("not", self.parse_unary(), tok.line)
        if tok.type in ("MINUS", "PLUS"):
            self.eat(tok.type)
            return UnaryOp(tok.value, self.parse_unary(), tok.line)
        return self.parse_power()

    def parse_postfix(self):
        node = self.parse_primary()
        while True:
            tok = self.current()
            if tok.type == "LPAREN":
                self.eat("LPAREN")
                args, kwargs = self.parse_call_args()
                self.eat("RPAREN", "')'")
                if isinstance(node, Identifier):
                    node = FunctionCall(node.name, args, kwargs, tok.line)
                elif isinstance(node, Attribute):
                    node = MethodCall(node.obj, node.name, args, kwargs, tok.line)
                else:
                    raise IrlSyntaxError(
                        "Only named functions and methods can be called.",
                        tok.line,
                        tok.column,
                    )
            elif tok.type == "LBRACKET":
                self.eat("LBRACKET")
                index = self.parse_slice()
                self.eat("RBRACKET", "']'")
                node = IndexExpr(node, index, tok.line)
            elif tok.type == "DOT":
                self.eat("DOT")
                name_tok = self.eat("IDENT", "an attribute or method name")
                if self.current().type == "LPAREN":
                    self.eat("LPAREN")
                    args, kwargs = self.parse_call_args()
                    self.eat("RPAREN", "')'")
                    node = MethodCall(node, name_tok.value, args, kwargs, tok.line)
                else:
                    node = Attribute(node, name_tok.value, tok.line)
            else:
                return node

    def parse_call_args(self):
        args, kwargs = [], {}
        self.eat_newlines()
        if self.current().type != "RPAREN":
            while True:
                self.eat_newlines()
                if self.current().type == "IDENT" and self.peek().type == "ASSIGN":
                    key = self.eat("IDENT").value
                    self.eat("ASSIGN")
                    kwargs[key] = self.parse_expr()
                else:
                    args.append(self.parse_expr())
                self.eat_newlines()
                if not self.match("COMMA"):
                    break
                self.eat_newlines()
        return args, kwargs

    def parse_slice(self):
        self.eat_newlines()
        start = stop = step = None
        if self.current().type != "COLON":
            start = self.parse_expr()
        if self.match("COLON"):
            self.eat_newlines()
            if self.current().type not in ("COLON", "RBRACKET"):
                stop = self.parse_expr()
            if self.match("COLON"):
                self.eat_newlines()
                if self.current().type != "RBRACKET":
                    step = self.parse_expr()
            return Slice(start, stop, step, self.current().line)
        return start

    def parse_primary(self):
        tok = self.current()
        if tok.type == "NUMBER":
            self.eat("NUMBER")
            value = float(tok.value) if "." in tok.value else int(tok.value)
            return Number(value, tok.line)
        if tok.type == "STRING":
            self.eat("STRING")
            return String(tok.value, tok.line)
        if tok.type == "FSTRING":
            self.eat("FSTRING")
            return self.parse_fstring(tok)
        if tok.type == "IDENT":
            self.eat("IDENT")
            return Identifier(tok.value, tok.line)
        if self.at_keyword("true"):
            self.eat("KEYWORD")
            return Boolean(True, tok.line)
        if self.at_keyword("false"):
            self.eat("KEYWORD")
            return Boolean(False, tok.line)
        if self.at_keyword("none"):
            self.eat("KEYWORD")
            return NoneLiteral(tok.line)
        if tok.type == "LPAREN":
            self.eat("LPAREN")
            self.eat_newlines()
            node = self.parse_expr()
            self.eat_newlines()
            self.eat("RPAREN", "')'")
            return node
        if tok.type == "LBRACKET":
            return self.parse_array()
        if tok.type == "LBRACE":
            return self.parse_dict()
        raise IrlSyntaxError(
            f"Expected a value, found '{tok.value or tok.type}'.",
            tok.line,
            tok.column,
        )

    def parse_array(self):
        tok = self.eat("LBRACKET")
        elements = []
        self.eat_newlines()
        if self.current().type != "RBRACKET":
            while True:
                self.eat_newlines()
                elements.append(self.parse_expr())
                self.eat_newlines()
                if not self.match("COMMA"):
                    break
                self.eat_newlines()
        self.eat("RBRACKET", "']'")
        return Array(elements, tok.line)

    def parse_dict(self):
        tok = self.eat("LBRACE")
        pairs = []
        self.eat_newlines()
        if self.current().type != "RBRACE":
            while True:
                self.eat_newlines()
                key = self.parse_expr()
                self.eat("COLON", "':'")
                self.eat_newlines()
                value = self.parse_expr()
                pairs.append((key, value))
                self.eat_newlines()
                if not self.match("COMMA"):
                    break
                self.eat_newlines()
        self.eat("RBRACE", "'}'")
        return DictLit(pairs, tok.line)

    def parse_fstring(self, tok):
        """Split raw f-string text into literal and expression parts."""
        raw = tok.value
        parts = []
        buf = []
        i = 0
        depth = 0
        expr_start = 0
        while i < len(raw):
            ch = raw[i]
            if ch == "\\" and i + 1 < len(raw):
                from .lexer import ESCAPES

                buf.append(ESCAPES.get(raw[i + 1], "\\" + raw[i + 1]))
                i += 2
                continue
            if ch == "{" and i + 1 < len(raw) and raw[i + 1] == "{":
                buf.append("{")
                i += 2
                continue
            if ch == "}" and i + 1 < len(raw) and raw[i + 1] == "}":
                buf.append("}")
                i += 2
                continue
            if ch == "{" and depth == 0:
                if buf:
                    parts.append(("text", "".join(buf)))
                    buf = []
                depth = 1
                expr_start = i + 1
                i += 1
                continue
            if ch == "{" and depth > 0:
                depth += 1
                i += 1
                continue
            if ch == "}" and depth > 0:
                depth -= 1
                if depth == 0:
                    expr_text = raw[expr_start:i].strip()
                    if not expr_text:
                        raise IrlSyntaxError("Empty {} in f-string.", tok.line, tok.column)
                    inner = Parser(lex(expr_text))
                    parts.append(("expr", inner.parse_expr()))
                i += 1
                continue
            if depth > 0:
                i += 1
                continue
            buf.append(ch)
            i += 1
        if depth > 0:
            raise IrlSyntaxError("Unclosed '{' in f-string.", tok.line, tok.column)
        if buf:
            parts.append(("text", "".join(buf)))
        return FString(parts, tok.line)


def parse(tokens):
    return Parser(tokens).parse()
