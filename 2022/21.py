#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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
import os

data = aocd.get_data(day=21, year=2022)

monkeys = {}
for line in data.split("\n"):
    parts = line.split(" ")
    m1 = parts[0][:4]

    if len(parts) == 2:
        monkeys[m1] = int(parts[1])
    else:
        m2, op, m3 = parts[1], parts[2], parts[3]
        monkeys[m1] = (m2, op, m3)


def traverse(monkey):
    x = monkeys[monkey]
    if isinstance(x, int):
        return x
    else:
        m2, op, m3 = x
        if op == "+":
            return traverse(m2) + traverse(m3)
        elif op == "-":
            return traverse(m2) - traverse(m3)
        elif op == "*":
            return traverse(m2) * traverse(m3)
        elif op == "/":
            return traverse(m2) // traverse(m3)
        else:
            print("error")


ans = traverse("root")
print(ans)


left = monkeys["root"][0]
right = monkeys["root"][2]


def expression(monkey):
    x = monkeys[monkey]
    if isinstance(x, int):
        if monkey == "humn":
            return "x"
        else:
            return str(x)
    else:
        m2, op, m3 = x
        if op == "+":
            return f"({expression(m2)} + {expression(m3)})"
        elif op == "-":
            return f"({expression(m2)} - {expression(m3)})"
        elif op == "*":
            return f"({expression(m2)} * {expression(m3)})"
        elif op == "/":
            return f"({expression(m2)} / {expression(m3)})"
        else:
            print("error")


os.system(f"sage -c 'print(solve({expression(left)} == {expression(right)}, x)[0].rhs())'")
