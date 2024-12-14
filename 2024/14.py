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
import time as tm

data = aocd.get_data(day=14, year=2024)
width, height = 101, 103

# data = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""
# width, height = 11, 7

time = 100
quads = [0, 0, 0, 0]
for line in data.splitlines():
    parts = line.split(" ")
    px, py = [int(n) for n in parts[0][2:].split(",")]
    vx, vy = [int(n) for n in parts[1][2:].split(",")]

    after_x = (px + time * vx) % width
    after_y = (py + time * vy) % height

    if after_x < (width - 1) // 2 and after_y < (height - 1) // 2:
        quads[0] += 1
    elif after_x > (width - 1) // 2 and after_y < (height - 1) // 2:
        quads[1] += 1
    elif after_x < (width - 1) // 2 and after_y > (height - 1) // 2:
        quads[2] += 1
    elif after_x > (width - 1) // 2 and after_y > (height - 1) // 2:
        quads[3] += 1

print(quads[0], quads[1], quads[2], quads[3])
ans = quads[0] * quads[1] * quads[2] * quads[3]

print(ans)
# aocd.submit(ans, part="a", day=14, year=2024)


for time in range(97, 10000, 101):
    result = set()
    for line in data.splitlines():
        parts = line.split(" ")
        px, py = [int(n) for n in parts[0][2:].split(",")]
        vx, vy = [int(n) for n in parts[1][2:].split(",")]

        after_x = (px + time * vx) % width
        after_y = (py + time * vy) % height

        result.add((after_x, after_y))

    print(time)
    for y in range(height):
        for x in range(width):
            print("*" if (x, y) in result else "-", end="")
        print()
    print()
    tm.sleep(0.1)

# aocd.submit(ans, part="b", day=14, year=2024)
