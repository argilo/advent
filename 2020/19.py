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
import lark
import re

data = aocd.get_data(day=19, year=2020)
grammar, strings = data.split("\n\n")
grammar = re.sub(r"\b(\d+)\b", r"n\1", grammar)
grammar = grammar.replace("n0", "start")

p = lark.Lark(grammar, parser='earley')

total = 0
for line in strings.splitlines():
    try:
        p.parse(line)
        total += 1
    except lark.exceptions.LarkError:
        pass
print(total)


data = aocd.get_data(day=19, year=2020)
grammar, strings = data.split("\n\n")
grammar = grammar.replace("8: 42", "8: 42 | 42 8")
grammar = grammar.replace("11: 42 31", "11: 42 31 | 42 11 31")
grammar = re.sub(r"\b(\d+)\b", r"n\1", grammar)
grammar = grammar.replace("n0", "start")

p = lark.Lark(grammar, parser='earley')

total = 0
for line in strings.splitlines():
    try:
        p.parse(line)
        total += 1
    except lark.exceptions.LarkError:
        pass
print(total)
