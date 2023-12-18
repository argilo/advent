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

data = aocd.get_data(day=18, year=2023)
# data = """R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)"""

dirs = {
    "D": (1, 0),
    "U": (-1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

pos_r, pos_c = 0, 0
dug = set()
dug.add((pos_r, pos_c))
for line in data.splitlines():
    dir, num, _ = line.split()
    num = int(num)

    for _ in range(num):
        dir_r, dir_c = dirs[dir]
        pos_r += dir_r
        pos_c += dir_c
        dug.add((pos_r, pos_c))

min_r = 1000000
max_r = -1000000
min_c = 1000000
max_c = -1000000
for dug_r, dug_c in dug:
    min_r = min(min_r, dug_r)
    max_r = max(max_r, dug_r)
    min_c = min(min_c, dug_c)
    max_c = max(max_c, dug_c)

area = 0
for r in range(min_r, max_r + 1):
    inside = False
    for c in range(min_c, max_c + 1):
        if (r, c) in dug:
            print("#", end="")
            area += 1
            if (r-1, c) in dug and (r+1, c) in dug:
                inside = not inside
            if (r, c-1) in dug and (r-1, c) in dug:
                inside = not inside
            if (r, c+1) in dug and (r-1, c) in dug:
                inside = not inside
        else:
            if inside:
                print("*", end="")
                area += 1
            else:
                print(".", end="")
    print()
print(area)

# aocd.submit(area, part="a", day=18, year=2023)

dirs = {
    1: (1, 0),
    3: (-1, 0),
    0: (0, 1),
    2: (0, -1)
}

pos_r, pos_c = 0, 0
dug = []
for line in data.splitlines():
    old_dir, num, _ = line.split()
    num = int(num)

    if old_dir == "R":
        dir = 0
    elif old_dir == "D":
        dir = 1
    elif old_dir == "L":
        dir = 2
    elif old_dir == "U":
        dir = 3

    _, _, col = line.split()
    num = int(col[2:-2], 16)
    dir = int(col[-2:-1], 16)

    dug.append([pos_r, pos_c, dir])

    dir_r, dir_c = dirs[dir]
    pos_r += dir_r * num
    pos_c += dir_c * num

for i in range(len(dug)):
    dug_r, dug_c, dug_dir = dug[i][0:3]
    dug[(i+1) % len(dug)].append(dug_dir ^ 2)

dug = [tuple(d) for d in dug]
dug_s = sorted(dug)
# print(dug)
# print(dug_s)

min_r = 1000000000
max_r = -1000000000
min_c = 1000000000
max_c = -1000000000
for dug_r, dug_c, _, _ in dug:
    min_r = min(min_r, dug_r)
    max_r = max(max_r, dug_r)
    min_c = min(min_c, dug_c)
    max_c = max(max_c, dug_c)
print(min_r, max_r, min_c, max_c)

row_lists = {}

for point in dug_s:
    dug_r = point[0]
    dug_c = point[1]
    if dug_r not in row_lists:
        row_lists[dug_r] = []
    row_lists[dug_r].append(point[1:])

# print(row_lists)


area = 0
walls = set()
for r in range(min_r, max_r + 1):
    if r in row_lists:
        rl = row_lists[r]
        for point in rl:
            dug_c, dir1, dir2 = point
            dirs_s = sorted([dir1, dir2])
            if dirs_s == [0, 3]:
                walls.remove((dug_c,))
            if dirs_s == [2, 3]:
                walls.remove((dug_c,))

        points = sorted(list(walls) + rl)
    else:
        points = sorted(list(walls))
    # print(r, points)

    inside = False
    last_c = None

    for point in points:
        if len(point) == 3:
            dug_c, dir1, dir2 = point
            dirs_s = sorted([dir1, dir2])
            if dirs_s == [0, 1]:
                if inside:
                    # print("inside", dug_c, last_c, dug_c - last_c - 1)
                    area += (dug_c - last_c - 1)

                area += 1
                walls.add((dug_c,))
            if dirs_s == [1, 2]:
                area += dug_c - last_c
                walls.add((dug_c,))
            if dirs_s == [0, 3]:
                if inside:
                    # print("inside", dug_c, last_c, dug_c - last_c - 1)
                    area += (dug_c - last_c - 1)

                area += 1
                inside = not inside
            if dirs_s == [2, 3]:
                area += dug_c - last_c
                inside = not inside


            last_c = dug_c

        if len(point) == 1:
            dug_c = point[0]
            if not inside:
                area += 1
            else:
                area += dug_c - last_c

            inside = not inside

            last_c = dug_c

        # print(point, inside)
    # print(area)

print(area)

aocd.submit(area, part="b", day=18, year=2023)
