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
import copy
import sys

data = aocd.get_data(day=14, year=2023)
# data = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

rows = [list(row) for row in data.splitlines()]
while True:
    new_rows = copy.deepcopy(rows)
    for r in range(1, len(rows)):
        for c in range(len(rows)):
            if rows[r-1][c] == "." and rows[r][c] == "O":
                rows[r-1][c] = "O"
                rows[r][c] = "."

    if new_rows == rows:
        break

load = len(rows)
ans = 0
for row in rows:
    ans += row.count("O") * load
    load -= 1
print(ans)

# aocd.submit(ans, part="a", day=14, year=2023)

def cycle(rows):
    while True:
        new_rows = copy.deepcopy(rows)
        for r in range(1, len(rows)):
            for c in range(len(rows)):
                if rows[r-1][c] == "." and rows[r][c] == "O":
                    rows[r-1][c] = "O"
                    rows[r][c] = "."

        if new_rows == rows:
            break

    while True:
        new_rows = copy.deepcopy(rows)
        for c in range(1, len(rows)):
            for r in range(len(rows)):
                if rows[r][c-1] == "." and rows[r][c] == "O":
                    rows[r][c-1] = "O"
                    rows[r][c] = "."

        if new_rows == rows:
            break

    while True:
        new_rows = copy.deepcopy(rows)
        for r in range(len(rows) - 1, 0, -1):
            for c in range(len(rows)):
                if rows[r][c] == "." and rows[r-1][c] == "O":
                    rows[r][c] = "O"
                    rows[r-1][c] = "."

        if new_rows == rows:
            break

    while True:
        new_rows = copy.deepcopy(rows)
        for c in range(len(rows) - 1, 0, -1):
            for r in range(len(rows)):
                if rows[r][c] == "." and rows[r][c-1] == "O":
                    rows[r][c] = "O"
                    rows[r][c-1] = "."

        if new_rows == rows:
            break

    return rows


def calc_load(rows):
    load = len(rows)
    ans = 0
    for row in rows:
        ans += row.count("O") * load
        load -= 1
    return ans


rows = [list(row) for row in data.splitlines()]

for n in range(1, 301):
    cycle(rows)
    print(n, calc_load(rows))

# after ~200 spin cycles, we enter into a 14-cycle loop.
# submit the correct number mod 14
