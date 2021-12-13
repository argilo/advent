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

data = aocd.get_data(day=13, year=2021)
#print(data)
# data = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5"""

board = set()

lines = data.splitlines()
mid = lines.index("")

for n in range(mid):
    x, y = [int(x) for x in lines[n].split(",")]
    board.add((x, y))

for n in range(mid+1, len(lines)):
    instr = lines[n].split(" ")[2]
    dir, coord = instr.split("=")
    coord = int(coord)

    new_board = set()
    if dir == "y":
        for x, y in board:
            if y > coord:
                new_board.add((x, coord - (y-coord)))
            else:
                new_board.add((x, y))
    if dir == "x":
        for x, y in board:
            if x > coord:
                new_board.add((coord - (x-coord), y))
            else:
                new_board.add((x, y))
    board = new_board
    print(len(board))

    for y in range(6):
        for x in range(40):
            print("#" if (x, y) in board else ".", end="")
        print()
    print()
