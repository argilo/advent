#!/usr/bin/env python3

# Copyright 2019 Clayton Smith
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

board = []
for line in open("19-input.txt"):
    board.append(list(line.rstrip("\n")))

y, x = 0, board[0].index("|")
dir_y, dir_x = 1, 0

str = ""
steps = 0
while True:
    char = board[y][x]
    if ord("A") <= ord(char) <= ord("Z"):
        str += char
    elif char == "+":
        dir_y, dir_x = dir_x, dir_y
        if board[y+dir_y][x+dir_x] == " ":
            dir_y, dir_x = -dir_y, -dir_x
    elif char == " ":
        break
    steps += 1
    y += dir_y
    x += dir_x
print(str)
print(steps)
