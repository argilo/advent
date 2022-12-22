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

data = aocd.get_data(day=22, year=2022)

rows = data.split("\n")[:-2]
path = data.split("\n")[-1]

width = max(len(row) for row in rows)
height = len(rows)
rows = [row + " " * (width - len(row)) for row in rows]

path_list = []
n = 0
for c in path:
    if ord("0") <= ord(c) <= ord("9"):
        d = ord(c) - ord("0")
        n = 10*n + d
    else:
        path_list.append(n)
        path_list.append(c)
        n = 0
path_list.append(n)


dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

cur_r = 0
cur_c = rows[0].index(".")
cur_dir = 0

for step in path_list:
    #print(step)
    if isinstance(step, int):
        times = int(step)
        mov_r, mov_c = dirs[cur_dir]

        for _ in range(times):
            next_r, next_c = (cur_r + mov_r) % height, (cur_c + mov_c) % width
            #print(cur_r, cur_c, cur_dir, next_r, next_c)
            while rows[next_r][next_c] == " ":
                next_r, next_c = (next_r + mov_r) % height, (next_c + mov_c) % width
                #print(" ", next_r, next_c)

            if rows[next_r][next_c] == "#":
                break
            else:
                cur_r, cur_c = next_r, next_c

    else:
        if step == "R":
            cur_dir = (cur_dir + 1) % 4
        else:
            cur_dir = (cur_dir + 3) % 4


ans = 1000 * (cur_r + 1) + 4 * (cur_c + 1) + cur_dir
print(ans)


def next_step(r, c, dir):
    # 1
    if dir == 0 and 150 <= r < 200 and c == 49:
        next_dir = 3
        next_r = 149
        next_c = r - 150 + 50
    elif dir == 1 and r == 149 and 50 <= c < 100:
        next_dir = 2
        next_r = c - 50 + 150
        next_c = 49

    # 2
    elif dir == 1 and r == 49 and 100 <= c < 150:
        next_dir = 2
        next_r = c - 100 + 50
        next_c = 99
    elif dir == 0 and 50 <= r < 100 and c == 99:
        next_dir = 3
        next_r = 49
        next_c = r - 50 + 100

    # 3
    elif dir == 2 and 50 <= r < 100 and c == 50:
        next_dir = 1
        next_r = 100
        next_c = r - 50
    elif dir == 3 and r == 100 and 0 <= c < 50:
        next_dir = 0
        next_r = c + 50
        next_c = 50

    # 4
    elif dir == 2 and 0 <= r < 50 and c == 50:
        next_dir = 0
        next_r = 149 - r
        next_c = 0
    elif dir == 2 and 100 <= r < 150 and c == 0:
        next_dir = 0
        next_r = 149 - r
        next_c = 50

    # 5
    elif dir == 2 and 150 <= r < 200 and c == 0:
        next_dir = 1
        next_r = 0
        next_c = r - 150 + 50
    elif dir == 3 and r == 0 and 50 <= c < 100:
        next_dir = 0
        next_r = c - 50 + 150
        next_c = 0

    # 6
    elif dir == 3 and r == 0 and 100 <= c < 150:
        next_dir = 3
        next_r = 199
        next_c = c - 100
    elif dir == 1 and r == 199 and 0 <= c < 50:
        next_dir = 1
        next_r = 0
        next_c = c + 100

    # 7
    elif dir == 0 and 0 <= r < 50 and c == 149:
        next_dir = 2
        next_r = 149 - r
        next_c = 99
    elif dir == 0 and 100 <= r < 150 and c == 99:
        next_dir = 2
        next_r = 149 - r
        next_c = 149

    else:
        mov_r, mov_c = dirs[cur_dir]
        next_r, next_c = (r + mov_r), (c + mov_c)
        next_dir = dir

    return next_r, next_c, next_dir


cur_r = 0
cur_c = rows[0].index(".")
cur_dir = 0

for step in path_list:
    if isinstance(step, int):
        times = int(step)
        mov_r, mov_c = dirs[cur_dir]

        for _ in range(times):
            next_r, next_c, next_dir = next_step(cur_r, cur_c, cur_dir)

            if rows[next_r][next_c] == "#":
                break
            else:
                cur_r, cur_c, cur_dir = next_r, next_c, next_dir

    else:
        if step == "R":
            cur_dir = (cur_dir + 1) % 4
        else:
            cur_dir = (cur_dir + 3) % 4

ans = 1000 * (cur_r + 1) + 4 * (cur_c + 1) + cur_dir
print(ans)
