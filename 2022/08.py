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

data = aocd.get_data(day=8, year=2022)

data = [[int(n) for n in row] for row in data.split("\n")]
height = len(data)
width = len(data[0])

visible = [[0 for _ in range(width)] for _ in range(height)]

for row in range(height):
    tallest = -1
    for col in range(width):
        if data[row][col] > tallest:
            visible[row][col] = 1
            tallest = data[row][col]

    tallest = -1
    for col in range(width-1, -1, -1):
        if data[row][col] > tallest:
            visible[row][col] = 1
            tallest = data[row][col]

for col in range(width):
    tallest = -1
    for row in range(height):
        if data[row][col] > tallest:
            visible[row][col] = 1
            tallest = data[row][col]

    tallest = -1
    for row in range(height-1, -1, -1):
        if data[row][col] > tallest:
            visible[row][col] = 1
            tallest = data[row][col]

print(sum(sum(row) for row in visible))


best_score = 0
for row in range(height):
    for col in range(width):
        current = data[row][col]

        right = 0
        for new_col in range(col+1, width):
            right += 1
            if data[row][new_col] >= current:
                break

        left = 0
        for new_col in range(col-1, -1, -1):
            left += 1
            if data[row][new_col] >= current:
                break

        down = 0
        for new_row in range(row+1, height):
            down += 1
            if data[new_row][col] >= current:
                break

        up = 0
        for new_row in range(row-1, -1, -1):
            up += 1
            if data[new_row][col] >= current:
                break

        score = left * right * up * down
        if score > best_score:
            best_score = score
print(best_score)
