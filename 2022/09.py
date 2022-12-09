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

data = aocd.get_data(day=9, year=2022)
# data = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""

visited = set()

hx, hy = 0, 0
tx, ty = 0, 0

dirs = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

for row in data.split("\n"):
    dir, num = row.split(" ")
    num = int(num)

    mx, my = dirs[dir]
    for _ in range(num):
        hx += mx
        hy += my

        if hx == tx:
            if hy == ty + 2:
                ty += 1
            elif hy == ty - 2:
                ty -= 1

        if hy == ty:
            if hx == tx + 2:
                tx += 1
            elif hx == tx - 2:
                tx -= 1

        if (hx == tx + 1 and hy == ty + 2) or (hx == tx + 2 and hy == ty + 1):
            tx += 1
            ty += 1

        if (hx == tx + 1 and hy == ty - 2) or (hx == tx + 2 and hy == ty - 1):
            tx += 1
            ty -= 1

        if (hx == tx - 1 and hy == ty + 2) or (hx == tx - 2 and hy == ty + 1):
            tx -= 1
            ty += 1

        if (hx == tx - 1 and hy == ty - 2) or (hx == tx - 2 and hy == ty - 1):
            tx -= 1
            ty -= 1

        visited.add((tx, ty))

print(len(visited))


positions = [[0, 0] for _ in range(10)]
visited = set()

for row in data.split("\n"):
    dir, num = row.split(" ")
    num = int(num)

    mx, my = dirs[dir]

    for _ in range(num):
        positions[0][0] += mx
        positions[0][1] += my

        for n in range(9):

            if positions[n][0] == positions[n+1][0]:
                if positions[n][1] == positions[n+1][1] + 2:
                    positions[n+1][1] += 1
                elif positions[n][1] == positions[n+1][1] - 2:
                    positions[n+1][1] -= 1

            elif positions[n][1] == positions[n+1][1]:
                if positions[n][0] == positions[n+1][0] + 2:
                    positions[n+1][0] += 1
                elif positions[n][0] == positions[n+1][0] - 2:
                    positions[n+1][0] -= 1

            elif (positions[n][0] == positions[n+1][0] + 1 and positions[n][1] == positions[n+1][1] + 2) or (positions[n][0] == positions[n+1][0] + 2 and positions[n][1] == positions[n+1][1] + 1) or (positions[n][0] == positions[n+1][0] + 2 and positions[n][1] == positions[n+1][1] + 2):
                positions[n+1][0] += 1
                positions[n+1][1] += 1

            elif (positions[n][0] == positions[n+1][0] + 1 and positions[n][1] == positions[n+1][1] - 2) or (positions[n][0] == positions[n+1][0] + 2 and positions[n][1] == positions[n+1][1] - 1) or (positions[n][0] == positions[n+1][0] + 2 and positions[n][1] == positions[n+1][1] - 2):
                positions[n+1][0] += 1
                positions[n+1][1] -= 1

            elif (positions[n][0] == positions[n+1][0] - 1 and positions[n][1] == positions[n+1][1] + 2) or (positions[n][0] == positions[n+1][0] - 2 and positions[n][1] == positions[n+1][1] + 1) or (positions[n][0] == positions[n+1][0] - 2 and positions[n][1] == positions[n+1][1] + 2):
                positions[n+1][0] -= 1
                positions[n+1][1] += 1

            elif (positions[n][0] == positions[n+1][0] - 1 and positions[n][1] == positions[n+1][1] - 2) or (positions[n][0] == positions[n+1][0] - 2 and positions[n][1] == positions[n+1][1] - 1) or (positions[n][0] == positions[n+1][0] - 2 and positions[n][1] == positions[n+1][1] - 2):
                positions[n+1][0] -= 1
                positions[n+1][1] -= 1

        visited.add((positions[9][0], positions[9][1]))

print(len(visited))
