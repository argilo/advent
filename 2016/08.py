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

width, height = 50, 6

screen = [[0 for _ in range(width)] for _ in range(height)]
for line in open("08-input.txt"):
    parts = line.rstrip().split()
    if parts[0] == "rect":
        parts2 = parts[1].split("x")
        rect_w, rect_h = int(parts2[0]), int(parts2[1])
        for x in range(rect_w):
            for y in range(rect_h):
                screen[y][x] = 1
    elif parts[0] == "rotate":
        coord = int(parts[2].split("=")[1])
        amt = int(parts[4])
        if parts[1] == "column":
            col = [screen[i][coord] for i in range(height)]
            col = col[height-amt:] + col[:height-amt]
            for i, val in enumerate(col):
                screen[i][coord] = val
        elif parts[1] == "row":
            screen[coord] = screen[coord][width-amt:] + screen[coord][:width-amt]

pixels = 0
for y in range(height):
    for x in range(width):
        print("█" if screen[y][x] else " ", end="")
        pixels += screen[y][x]
    print()
print(pixels)
