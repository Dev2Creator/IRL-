import re
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int

class IrlSyntaxError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"\n[IRL_ERROR] ☠️ BRUH. {message} (Line {line}, Col {column})")

# Token definitions
TOKEN_SPEC = [
    ('COMMENT',   r'//.*'),
    ('NUMBER',    r'\d+'),
    ('STRING',    r'"[^"]*"'),
    ('KEYWORD',   r'\b(snag|spill|bet|cap|grind|brb|fax|fake|task|fr|or|nah)\b'),
    ('IDENT',     r'[a-zA-Z_]\w*'),
    ('EQEQ',      r'=='),
    ('NEQ',       r'!='),
    ('LTE',       r'<='),
    ('GTE',       r'>='),
    ('ASSIGN',    r'='),
    ('LT',        r'<'),
    ('GT',        r'>'),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('MUL',       r'\*'),
    ('DIV',       r'/'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('LBRACE',    r'\{'),
    ('RBRACE',    r'\}'),
    ('LBRACKET',  r'\['),
    ('RBRACKET',  r'\]'),
    ('SEMI',      r';'),
    ('COMMA',     r','),
    ('NEWLINE',   r'\n'),
    ('SKIP',      r'[ \t]+'),
    ('MISMATCH',  r'.'),
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
get_token = re.compile(tok_regex).match

def lex(code: str) -> List[Token]:
    line_num = 1
    line_start = 0
    tokens = []
    mo = get_token(code)
    
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group(kind)
        column = mo.start() - line_start + 1
        
        if kind == 'NUMBER':
            tokens.append(Token(kind, value, line_num, column))
        elif kind == 'STRING':
            tokens.append(Token(kind, value.strip('"'), line_num, column))
        elif kind == 'IDENT':
            tokens.append(Token(kind, value, line_num, column))
        elif kind == 'KEYWORD':
            tokens.append(Token(kind, value, line_num, column))
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind in ('SKIP', 'COMMENT'):
            pass
        elif kind == 'MISMATCH':
            raise IrlSyntaxError(f"What even is '{value}'? Learn to type.", line_num, column)
        else:
            tokens.append(Token(kind, value, line_num, column))
            
        mo = get_token(code, mo.end())
        
    tokens.append(Token('EOF', '', line_num, 0))
    return tokens
