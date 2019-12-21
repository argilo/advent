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

keypad1 = {
    (-1, -1): "1",
    (-1, 0): "2",
    (-1, 1): "3",
    (0, -1): "4",
    (0, 0): "5",
    (0, 1): "6",
    (1, -1): "7",
    (1, 0): "8",
    (1, 1): "9",
}

keypad2 = {
    (-2, 0): "1",
    (-1, -1): "2",
    (-1, 0): "3",
    (-1, 1): "4",
    (0, -2): "5",
    (0, -1): "6",
    (0, 0): "7",
    (0, 1): "8",
    (0, 2): "9",
    (1, -1): "A",
    (1, 0): "B",
    (1, 1): "C",
    (2, 0): "D",
}


def code(keypad):
    row, col = 0, 0
    for line in open("02-input.txt"):
        for char in line.rstrip():
            new_row, new_col = row, col
            if char == "U":
                new_row -= 1
            if char == "D":
                new_row += 1
            if char == "L":
                new_col -= 1
            if char == "R":
                new_col += 1
            if (new_row, new_col) in keypad:
                row, col = new_row, new_col
        print(keypad[(row, col)], end="")
    print()


code(keypad1)
code(keypad2)
