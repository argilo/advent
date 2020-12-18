#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import aocd
import ply.lex as lex
import ply.yacc as yacc


tokens = (
    "NUMBER",
    "PLUS",
    "TIMES",
    "LPAREN",
    "RPAREN",
)

t_PLUS = r"\+"
t_TIMES = r"\*"
t_LPAREN = r"\("
t_RPAREN = r"\)"

t_ignore = " "


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


precedence = (
    ("left", "PLUS", "TIMES"),
)


def p_expression_binop(t):
    """expression : expression PLUS expression
                  | expression TIMES expression"""
    if t[2] == "+":
        t[0] = t[1] + t[3]
    elif t[2] == "*":
        t[0] = t[1] * t[3]


def p_expression_group(t):
    "expression : LPAREN expression RPAREN"
    t[0] = t[2]


def p_expression_number(t):
    "expression : NUMBER"
    t[0] = t[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


parser = yacc.yacc(debug=0)


total = 0
data = aocd.get_data(day=18, year=2020)
for line in data.splitlines():
    total += parser.parse(line)
print(total)


precedence = (
    ("left", "TIMES"),
    ("left", "PLUS"),
)
parser = yacc.yacc(debug=0)


total = 0
for line in data.splitlines():
    total += parser.parse(line)
print(total)
