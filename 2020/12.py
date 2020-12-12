#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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

data = aocd.get_data(day=12, year=2020)

x, y = 0, 0
dir = 90
for line in data.splitlines():
    cmd = line[0]
    num = int(line[1:])
    print(cmd, num)
    if cmd == "N":
        y -= num
    if cmd == "S":
        y += num
    if cmd == "W":
        x -= num
    if cmd == "E":
        x += num
    if cmd == "R":
        dir = (dir + num) % 360
    if cmd == "L":
        dir = (dir + 360 - num) % 360
    if cmd == "F":
        if dir == 0:
            y -= num
        if dir == 180:
            y += num
        if dir == 270:
            x -= num
        if dir == 90:
            x += num
    print("",  x, y, dir)
ans = abs(x) + abs(y)
print(ans)

x, y = 0, 0
wx, wy = 10, -1
for line in data.splitlines():
    cmd = line[0]
    num = int(line[1:])
    print(cmd, num)
    if cmd == "N":
        wy -= num
    if cmd == "S":
        wy += num
    if cmd == "W":
        wx -= num
    if cmd == "E":
        wx += num
    if cmd == "R":
        diffx = wx - x
        diffy = wy - y
        if num == 90:
            wx = x - diffy
            wy = y + diffx
        if num == 180:
            wx = x - diffx
            wy = y - diffy
        if num == 270:
            wx = x + diffy
            wy = y - diffx
    if cmd == "L":
        diffx = wx - x
        diffy = wy - y
        if num == 270:
            wx = x - diffy
            wy = y + diffx
        if num == 180:
            wx = x - diffx
            wy = y - diffy
        if num == 90:
            wx = x + diffy
            wy = y - diffx
    if cmd == "F":
        diffx = wx - x
        diffy = wy - y
        x += diffx * num
        wx += diffx * num
        y += diffy * num
        wy += diffy * num
    print("",  x, y, wx, wy)
ans = abs(x) + abs(y)
print(ans)
