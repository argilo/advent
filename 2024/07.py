#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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
import itertools

data = aocd.get_data(day=7, year=2024)

# data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

ans = 0
for line in data.splitlines():
    ls, rs = line.split(": ")
    ls = int(ls)
    rs = [int(n) for n in rs.split()]

    for ops in itertools.product((0, 1), repeat=len(rs) - 1):
        val = rs[0]
        for op, n in zip(ops, rs[1:]):
            if op == 0:
                val += n
            elif op == 1:
                val *= n
        if val == ls:
            ans += ls
            break

print(ans)
# aocd.submit(ans, part="a", day=7, year=2024)


ans = 0
for line in data.splitlines():
    ls, rs = line.split(": ")
    ls = int(ls)
    rs = [int(n) for n in rs.split()]

    for ops in itertools.product((0, 1, 2), repeat=len(rs) - 1):
        val = rs[0]
        for op, n in zip(ops, rs[1:]):
            if op == 0:
                val += n
            elif op == 1:
                val *= n
            elif op == 2:
                val = int(str(val) + str(n))
        if val == ls:
            ans += ls
            break

print(ans)
# aocd.submit(ans, part="b", day=7, year=2024)
