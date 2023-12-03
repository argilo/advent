#!/usr/bin/env python3

# Copyright 2023 Clayton Smith
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
import re

data = aocd.get_data(day=3, year=2023)
# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
data = data.split()

ans = 0
for y, line in enumerate(data):
    for m in re.compile(r"\d+").finditer(line):
        include = False
        for x in range(m.start(), m.end()):
            for y2 in range(y-1, y+2):
                if y2 < 0 or y2 >= len(data):
                    continue
                for x2 in range(x-1, x+2):
                    if x2 < 0 or x2 >= len(line):
                        continue
                    if data[y2][x2] not in (".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        include = True
        if include:
            ans += int(m.group())
print(ans)

# aocd.submit(ans, part="a", day=3, year=2023)

adjacents = {}
ans = 0
for y, line in enumerate(data):
    for m in re.compile(r"\d+").finditer(line):
        for x in range(m.start(), m.end()):
            for y2 in range(y-1, y+2):
                if y2 < 0 or y2 >= len(data):
                    continue
                for x2 in range(x-1, x+2):
                    if x2 < 0 or x2 >= len(line):
                        continue
                    if data[y2][x2] not in (".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        if (y2, x2) not in adjacents:
                            adjacents[(y2, x2)] = set()
                        adjacents[(y2, x2)].add((y, m.start(), int(m.group())))

ans = 0
for coords, dat in adjacents.items():
    if len(dat) == 2:
        prod = 1
        for item in dat:
            prod *= item[2]
        ans += prod
print(ans)

# aocd.submit(ans, part="b", day=3, year=2023)
