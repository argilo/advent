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
import itertools

data = aocd.get_data(day=11, year=2023)

space = []
for line in data.splitlines():
    if "#" not in line:
        space.append(line)
    space.append(line)

space2 = [[] for _ in range(len(space))]
for c in range(len(space[0])):
    column = [row[c] for row in space]
    if "#" not in column:
        for r in range(len(space)):
            space2[r].append(column[r])
    for r in range(len(space)):
        space2[r].append(column[r])

galaxies = []
for r, row in enumerate(space2):
    for c, thing in enumerate(row):
        if thing == "#":
            galaxies.append((r, c))

sum = 0
for a, b in itertools.combinations(galaxies, 2):
    r1, c1 = a
    r2, c2 = b
    sum += abs(r2 - r1) + abs(c2 - c1)
print(sum)

# aocd.submit(sum, part="a", day=11, year=2023)


expansion = 1000000
space = data.splitlines()
row_cost = [1 if "#" in row else expansion for row in space]

col_cost = []
for c in range(len(space[0])):
    for row in space:
        if row[c] == "#":
            col_cost.append(1)
            break
    else:
        col_cost.append(expansion)

galaxies = []
for r, row in enumerate(space):
    for c, thing in enumerate(row):
        if thing == "#":
            galaxies.append((r, c))

sum = 0
for a, b in itertools.combinations(galaxies, 2):
    r1, c1 = a
    r2, c2 = b
    if r2 < r1:
        r1, r2 = r2, r1
    if c2 < c1:
        c1, c2 = c2, c1
    for r in range(r1, r2):
        sum += row_cost[r]
    for c in range(c1, c2):
        sum += col_cost[c]
print(sum)

# aocd.submit(sum, part="b", day=11, year=2023)
