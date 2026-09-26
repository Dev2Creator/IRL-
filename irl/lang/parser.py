from .lexer import Token, IrlSyntaxError

class ASTNode: pass

class Program(ASTNode):
    def __init__(self, statements): self.statements = statements

class Block(ASTNode):
    def __init__(self, statements): self.statements = statements

class FunctionDef(ASTNode):
    def __init__(self, name, params, block):
        self.name = name
        self.params = params
        self.block = block

class VarDecl(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Assign(ASTNode):
    def __init__(self, target, value):
        self.target = target
        self.value = value

class IfStmt(ASTNode):
    def __init__(self, condition, true_block, false_block):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

class WhileStmt(ASTNode):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class SpillStmt(ASTNode):
    def __init__(self, value): self.value = value

class ReturnStmt(ASTNode):
    def __init__(self, value): self.value = value

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(ASTNode):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

class IndexExpr(ASTNode):
    def __init__(self, array_expr, index_expr):
        self.array_expr = array_expr
        self.index_expr = index_expr

class Array(ASTNode):
    def __init__(self, elements):
        self.elements = elements

class Number(ASTNode):
    def __init__(self, value): self.value = value

class String(ASTNode):
    def __init__(self, value): self.value = value

class Boolean(ASTNode):
    def __init__(self, value): self.value = value

class Identifier(ASTNode):
    def __init__(self, name): self.name = name

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens): return self.tokens[self.pos]
        return self.tokens[-1]

    def eat(self, token_type):
        tok = self.current_token()
        if tok.type == token_type:
            self.pos += 1
            return tok
        raise IrlSyntaxError(f"Expected {token_type}, got {tok.type} ('{tok.value}'). Are you even trying?", tok.line, tok.column)

    def parse(self):
        statements = []
        while self.current_token().type != 'EOF':
            statements.append(self.parse_statement())
        return Program(statements)

    def parse_statement(self):
        tok = self.current_token()
        if tok.type == 'KEYWORD':
            if tok.value == 'snag': return self.parse_var_decl()
            elif tok.value == 'spill': return self.parse_spill()
            elif tok.value == 'bet': return self.parse_if()
            elif tok.value == 'grind': return self.parse_while()
            elif tok.value == 'brb': return self.parse_return()
            elif tok.value == 'task': return self.parse_function_def()
        
        # It could be an assignment or a function call as a statement
        expr = self.parse_expr()
        if self.current_token().type == 'ASSIGN':
            self.eat('ASSIGN')
            value = self.parse_expr()
            self.eat('SEMI')
            return Assign(expr, value)
        else:
            self.eat('SEMI')
            return expr # FunctionCall or other expr acting as statement

    def parse_block(self):
        self.eat('LBRACE')
        statements = []
        while self.current_token().type != 'RBRACE' and self.current_token().type != 'EOF':
            statements.append(self.parse_statement())
        self.eat('RBRACE')
        return Block(statements)

    def parse_function_def(self):
        self.eat('KEYWORD') # 'task'
        name_tok = self.eat('IDENT')
        self.eat('LPAREN')
        params = []
        if self.current_token().type != 'RPAREN':
            params.append(self.eat('IDENT').value)
            while self.current_token().type == 'COMMA':
                self.eat('COMMA')
                params.append(self.eat('IDENT').value)
        self.eat('RPAREN')
        block = self.parse_block()
        return FunctionDef(name_tok.value, params, block)

    def parse_var_decl(self):
        self.eat('KEYWORD') # 'snag'
        name_tok = self.eat('IDENT')
        self.eat('ASSIGN')
        value = self.parse_expr()
        self.eat('SEMI')
        return VarDecl(name_tok.value, value)

    def parse_spill(self):
        self.eat('KEYWORD') # 'spill'
        self.eat('LPAREN')
        value = self.parse_expr()
        self.eat('RPAREN')
        self.eat('SEMI')
        return SpillStmt(value)

    def parse_return(self):
        self.eat('KEYWORD') # 'brb'
        value = None
        if self.current_token().type != 'SEMI':
            value = self.parse_expr()
        self.eat('SEMI')
        return ReturnStmt(value)

    def parse_if(self):
        self.eat('KEYWORD') # 'bet'
        self.eat('LPAREN')
        condition = self.parse_expr()
        self.eat('RPAREN')
        true_block = self.parse_block()
        false_block = None
        
        if self.current_token().type == 'KEYWORD' and self.current_token().value == 'cap':
            self.eat('KEYWORD') # 'cap'
            false_block = self.parse_block()
            
        return IfStmt(condition, true_block, false_block)

    def parse_while(self):
        self.eat('KEYWORD') # 'grind'
        self.eat('LPAREN')
        condition = self.parse_expr()
        self.eat('RPAREN')
        block = self.parse_block()
        return WhileStmt(condition, block)

    def parse_expr(self):
        return self.parse_logic_or()

    def parse_logic_or(self):
        node = self.parse_logic_and()
        while self.current_token().type == 'KEYWORD' and self.current_token().value == 'or':
            op = self.eat('KEYWORD').value
            right = self.parse_logic_and()
            node = BinOp(node, op, right)
        return node

    def parse_logic_and(self):
        node = self.parse_comparison()
        while self.current_token().type == 'KEYWORD' and self.current_token().value == 'fr':
            op = self.eat('KEYWORD').value
            right = self.parse_comparison()
            node = BinOp(node, op, right)
        return node

    def parse_comparison(self):
        node = self.parse_term()
        while self.current_token().type in ('EQEQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE'):
            op = self.current_token()
            self.eat(op.type)
            right = self.parse_term()
            node = BinOp(node, op.value, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_token().type in ('PLUS', 'MINUS'):
            op = self.current_token()
            self.eat(op.type)
            right = self.parse_factor()
            node = BinOp(node, op.value, right)
        return node

    def parse_factor(self):
        node = self.parse_unary()
        while self.current_token().type in ('MUL', 'DIV'):
            op = self.current_token()
            self.eat(op.type)
            right = self.parse_unary()
            node = BinOp(node, op.value, right)
        return node

    def parse_unary(self):
        if self.current_token().type == 'KEYWORD' and self.current_token().value == 'nah':
            self.eat('KEYWORD')
            return UnaryOp('nah', self.parse_unary())
        return self.parse_index_call()

    def parse_index_call(self):
        node = self.parse_primary()
        while self.current_token().type in ('LPAREN', 'LBRACKET'):
            tok = self.current_token()
            if tok.type == 'LPAREN':
                self.eat('LPAREN')
                args = []
                if self.current_token().type != 'RPAREN':
                    args.append(self.parse_expr())
                    while self.current_token().type == 'COMMA':
                        self.eat('COMMA')
                        args.append(self.parse_expr())
                self.eat('RPAREN')
                # If node is Identifier, it's a standard function call
                if isinstance(node, Identifier):
                    node = FunctionCall(node.name, args)
                else:
                    raise IrlSyntaxError("Can only call functions by name.", tok.line, tok.column)
            elif tok.type == 'LBRACKET':
                self.eat('LBRACKET')
                index_expr = self.parse_expr()
                self.eat('RBRACKET')
                node = IndexExpr(node, index_expr)
        return node

    def parse_primary(self):
        tok = self.current_token()
        if tok.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(int(tok.value))
        elif tok.type == 'STRING':
            self.eat('STRING')
            return String(tok.value)
        elif tok.type == 'IDENT':
            self.eat('IDENT')
            return Identifier(tok.value)
        elif tok.type == 'KEYWORD' and tok.value in ('fax', 'fake'):
            self.eat('KEYWORD')
            return Boolean(True if tok.value == 'fax' else False)
        elif tok.type == 'LBRACKET':
            self.eat('LBRACKET')
            elements = []
            if self.current_token().type != 'RBRACKET':
                elements.append(self.parse_expr())
                while self.current_token().type == 'COMMA':
                    self.eat('COMMA')
                    elements.append(self.parse_expr())
            self.eat('RBRACKET')
            return Array(elements)
        elif tok.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.parse_expr()
            self.eat('RPAREN')
            return node
            
        raise IrlSyntaxError(f"I was expecting a value but found '{tok.value}'. Absolutely tragic.", tok.line, tok.column)

def parse(tokens):
    parser = Parser(tokens)
    return parser.parse()
