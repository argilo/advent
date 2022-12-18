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
import dijkstar

data = aocd.get_data(day=18, year=2022)
# data = """2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5"""

cubes = set()
for line in data.split("\n"):
    x, y, z = [int(n) for n in line.split(",")]
    cubes.add((x, y, z))

area = 0
for x, y, z in cubes:
    for dx, dy, dz in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
        if (x + dx, y + dy, z + dz) not in cubes:
            area += 1
print(area)


min_x, max_x = 1000, -1000
min_y, max_y = 1000, -1000
min_z, max_z = 1000, -1000

for x, y, z in cubes:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    min_z = min(min_z, z)
    max_z = max(max_z, z)

graph = dijkstar.Graph()

for x in range(min_x - 1, max_x + 2):
    for y in range(min_y - 1, max_y + 2):
        for z in range(min_z - 1, max_z + 2):
            for dx, dy, dz in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
                if ((x, y, z) not in cubes) and ((x + dx, y + dy, z + dz) not in cubes):
                    graph.add_edge((x, y, z), (x + dx, y + dy, z + dz), 1)
                    graph.add_edge((x + dx, y + dy, z + dz), (x, y, z), 1)

interior = set()
for x in range(min_x - 1, max_x + 2):
    for y in range(min_y - 1, max_y + 2):
        for z in range(min_z - 1, max_z + 2):
            if (x, y, z) not in cubes:
                try:
                    dijkstar.find_path(graph, (min_x - 1, min_y - 1, min_z - 1), (x, y, z))
                except dijkstar.algorithm.NoPathError:
                    interior.add((x, y, z))

area = 0
for x, y, z in cubes:
    for dx, dy, dz in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
        if ((x + dx, y + dy, z + dz) not in cubes) and ((x + dx, y + dy, z + dz) not in interior):
            area += 1
print(area)
