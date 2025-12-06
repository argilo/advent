#!/usr/bin/env python3

# Copyright 2025 Clayton Smith
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

YEAR = 2025
DAY = 6

data = aocd.get_data(day=DAY, year=YEAR)
# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """

lines = data.splitlines()
ops = lines[-1].split()
accs = [0 if op == "+" else 1 for op in ops]

for line in lines[:-1]:
    parts = [int(n) for n in line.split()]
    for i, (op, part) in enumerate(zip(ops, parts)):
        if op == "+":
            accs[i] += part
        else:
            accs[i] *= part
ans = sum(accs)

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


lines = data.splitlines()
ans = 0
acc = -1
for c in range(len(lines[0])):
    op = lines[-1][c]
    if op != " ":
        if acc != -1:
            ans += acc
        current_op = op
        acc = 0 if op == "+" else 1
    try:
        num = int("".join(lines[r][c] for r in range(len(lines) - 1)))
        if current_op == "+":
            acc += num
        else:
            acc *= num
    except ValueError:
        pass
ans += acc

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
