# IRL™ 🌱 - Software for Humans
# Copyright (C) 2026 Anika Mukherjee
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""The .irl grammar, machine-readable.

One regular, unambiguous grammar with one way to say everything — the
property that makes the language reliable for LLM code generation and
tooling. `irl lang spec [--json]` prints this.
"""

GRAMMAR_EBNF = """\
program        = { statement } ;
statement      = var_decl | function_def | if_stmt | while_stmt
               | for_stmt | "break" | "continue" | return_stmt
               | import_stmt | assignment | expr_stmt ;

var_decl       = "var" IDENT "=" expr ;
function_def   = [ "memo" ] "function" IDENT "(" [ param { "," param } ] ")" block ;
if_stmt        = "if" "(" expr ")" block { "elif" "(" expr ")" block } [ "else" block ] ;
while_stmt     = "while" "(" expr ")" block ;
for_stmt       = "for" "(" IDENT "in" expr ")" block ;
return_stmt    = "return" [ expr ] ;
import_stmt    = "import" ( IDENT { "." IDENT } | STRING ) ;
assignment     = target "=" expr ;
target         = IDENT | postfix "[" expr_or_slice "]" ;
expr_stmt      = expr ;

block          = "{" { statement } "}" ;

expr           = or_expr ;
or_expr        = and_expr { "or" and_expr } ;
and_expr       = not_expr { "and" not_expr } ;
not_expr       = "not" not_expr | comparison ;
comparison     = term { ( "==" | "!=" | "<" | ">" | "<=" | ">=" | "in" | "not" "in" ) term } ;
term           = factor { ( "+" | "-" ) factor } ;
factor         = power { ( "*" | "/" ) power } ;
power          = postfix [ "**" unary ] ;
unary          = ( "-" | "+" | "not" ) unary | postfix ;
postfix        = primary { "(" call_args ")" | "[" expr_or_slice "]" | "." IDENT [ "(" call_args ")" ] } ;
primary        = NUMBER | STRING | FSTRING | "true" | "false" | "none"
               | IDENT | array | dict | "(" expr ")" ;
array          = "[" [ expr { "," expr } [ "," ] ] "]" ;
dict           = "{" [ pair { "," pair } [ "," ] ] "}" ;
pair           = expr ":" expr ;

call_args      = [ ( expr | IDENT "=" expr ) { "," ( expr | IDENT "=" expr ) } ] ;
expr_or_slice  = [ expr ] ":" [ expr ] [ ":" [ expr ] ] | expr ;

(* Lexical: statements end at a NEWLINE or an optional ";". *)
(* Comments: "//" and "#" to end of line. Strings escape \n \t \" \\. *)
(* F-strings: f"...{expr}..." with {{ }} for literal braces. *)
"""

KEYWORD_TABLE = {
    "var": ["var", "let", "snag (legacy)"],
    "function": ["function", "def", "fn", "task (legacy)"],
    "if": ["if", "bet (legacy)"],
    "elif": ["elif"],
    "else": ["else", "cap (legacy)"],
    "while": ["while", "grind (legacy)"],
    "for": ["for"],
    "in": ["in"],
    "break": ["break"],
    "continue": ["continue"],
    "return": ["return", "brb (legacy)"],
    "true": ["true", "fax (legacy)"],
    "false": ["false", "fake (legacy)"],
    "none": ["none"],
    "and": ["and", "fr (legacy)"],
    "or": ["or"],
    "not": ["not", "nah (legacy)"],
    "memo": ["memo"],
    "import": ["import"],
    "print()": ["print", "spill (legacy)"],
    "input()": ["input", "ask (legacy)"],
    "list.append()": ["append", "push (legacy)"],
}
