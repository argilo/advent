#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=9, year=2021)
# data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""

m = []
for line in data.splitlines():
    m.append([int(n) for n in line])

rows = len(m)
cols = len(m[0])

tot = 0
lows = []
for row in range(rows):
    for col in range(cols):
        neighbours = []
        if row > 0:
            neighbours.append(m[row-1][col])
        if row < rows-1:
            neighbours.append(m[row+1][col])
        if col > 0:
            neighbours.append(m[row][col-1])
        if col < cols-1:
            neighbours.append(m[row][col+1])
        if m[row][col] < min(neighbours):
            risk = m[row][col]+1
            lows.append((row, col))
            tot += risk

print(tot)
#aocd.submit(tot, part="a", day=9, year=2021)

basins = []
for low in lows:
    found = set()
    found.add(low)
    while True:
        new_found = found.copy()
        for row, col in found:
            if row > 0:
                if m[row-1][col] != 9:
                    new_found.add((row-1, col))
            if row < rows-1:
                if m[row+1][col] != 9:
                    new_found.add((row+1, col))
            if col > 0:
                if m[row][col-1] != 9:
                    new_found.add((row, col-1))
            if col < cols-1:
                if m[row][col+1] != 9:
                    new_found.add((row, col+1))
        if len(found) == len(new_found):
            break
        found = new_found
    basins.append(len(found))
basins.sort()
ans = basins[-3] * basins[-2] * basins[-1]

print(ans)
# aocd.submit(ans, part="b", day=9, year=2021)
