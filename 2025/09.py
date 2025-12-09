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
import itertools

YEAR = 2025
DAY = 9

data = aocd.get_data(day=DAY, year=YEAR)
# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""

reds = []
for line in data.splitlines():
    x, y = [int(n) for n in line.split(",")]
    reds.append((x, y))

ans = 0
for (x1, y1), (x2, y2) in itertools.combinations(reds, 2):
    area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
    ans = max(ans, area)

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


edges = set()
cur_x, cur_y = reds[-1]
for x, y in reds:
    dx, dy = 0, 0
    if x < cur_x:
        dx = -1
    elif x > cur_x:
        dx = 1
    elif y < cur_y:
        dy = -1
    elif y > cur_y:
        dy = 1
    while (cur_x, cur_y) != (x, y):
        cur_x += dx
        cur_y += dy
        edges.add((cur_x, cur_y))

ans = 0
for (x1, y1), (x2, y2) in itertools.combinations(reds, 2):
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    area = (x2 - x1 + 1) * (y2 - y1 + 1)

    for x, y in edges:
        if (x1 < x < x2) and (y1 < y < y2):
            break
    else:
        ans = max(ans, area)

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
