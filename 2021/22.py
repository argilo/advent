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

data = aocd.get_data(day=22, year=2021)
lines = data.splitlines()

space = set()
for line in lines:
    state, rest = line.split()
    coords = []
    for part in rest.split(","):
        start, end = [int(n) for n in part.split("=")[1].split("..")]
        coords.append((start, end))
    if coords[0][0] < -50 or coords[0][0] > 50:
        continue
    for x in range(coords[0][0], coords[0][1]+1):
        for y in range(coords[1][0], coords[1][1]+1):
            for z in range(coords[2][0], coords[2][1]+1):
                if state == "on":
                    space.add((x, y, z))
                else:
                    if (x, y, z) in space:
                        space.remove((x, y, z))
ans = len(space)
print(ans)

# aocd.submit(ans, part="a", day=22, year=2021)

change_loc = [[] for _ in range(3)]

for line in lines:
    state, rest = line.split()
    coords = []
    for i, part in enumerate(rest.split(",")):
        start, end = [int(n) for n in part.split("=")[1].split("..")]
        coords.append((start, end))
        change_loc[i].append(start)
        change_loc[i].append(end+1)
for i in range(3):
    change_loc[i].sort()

space = set()
for line in lines:
    state, rest = line.split()
    coords = []
    for i, part in enumerate(rest.split(",")):
        start, end = [int(n) for n in part.split("=")[1].split("..")]
        coords.append((change_loc[i].index(start), change_loc[i].index(end+1)))

    for x in range(coords[0][0], coords[0][1]):
        for y in range(coords[1][0], coords[1][1]):
            for z in range(coords[2][0], coords[2][1]):
                if state == "on":
                    space.add((x, y, z))
                else:
                    if (x, y, z) in space:
                        space.remove((x, y, z))

ans = 0
for (x, y, z) in space:
    x_size = change_loc[0][x+1] - change_loc[0][x]
    y_size = change_loc[1][y+1] - change_loc[1][y]
    z_size = change_loc[2][z+1] - change_loc[2][z]
    ans += x_size * y_size * z_size
print(ans)

# aocd.submit(ans, part="b", day=22, year=2021)
