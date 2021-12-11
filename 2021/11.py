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

data = aocd.get_data(day=11, year=2021)
# data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

oct = []
for line in data.splitlines():
    oct.append([int(n) for n in line])

flashes = 0
for step in range(1000):
    new_flashes = 0
    new_oct = [[None] * 10 for _ in range(10)]
    flashed = [[False] * 10 for _ in range(10)]
    for row in range(10):
        for col in range(10):
            new_oct[row][col] = oct[row][col] + 1
    while True:
        new_flash = False
        for row in range(10):
            for col in range(10):
                if not flashed[row][col] and new_oct[row][col] >= 10:
                    flashes += 1
                    new_flashes += 1
                    flashed[row][col] = True
                    new_flash = True
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if dr == dc == 0:
                                continue
                            if 0 <= row+dr < 10 and 0 <= col+dc < 10:
                                new_oct[row+dr][col+dc] += 1
        if not new_flash:
            break
    for row in range(10):
        for col in range(10):
            if new_oct[row][col] >= 10:
                new_oct[row][col] = 0
    oct = new_oct
    if new_flashes == 100:
        print(step+1)
        break
    if step+1 == 100:
        print(flashes)
