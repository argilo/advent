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

data = aocd.get_data(day=5, year=2021)
# print(data)

# nums = [int(line) for line in data.splitlines()]
# print(nums)

# data = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2"""

board = [[0 for _ in range(1000)] for _ in range(1000)]

for line in data.splitlines():
    parts = line.split(" -> ")
    x1, y1 = [int(n) for n in parts[0].split(",")]
    x2, y2 = [int(n) for n in parts[1].split(",")]
    if x1 != x2 and y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            board[y1][x] += 1

    elif y1 != y2 and x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            board[y][x1] += 1

ans = 0
for row in range(1000):
    for col in range(1000):
        if board[row][col] > 1:
            ans += 1
print(ans)
#aocd.submit(ans, part="a", day=5, year=2021)

board = [[0 for _ in range(1000)] for _ in range(1000)]

for line in data.splitlines():
    parts = line.split(" -> ")
    x1, y1 = [int(n) for n in parts[0].split(",")]
    x2, y2 = [int(n) for n in parts[1].split(",")]

    if x1 < x2:
        xinc = 1
    elif x1 > x2:
        xinc = -1
    else:
        xinc = 0

    if y1 < y2:
        yinc = 1
    elif y1 > y2:
        yinc = -1
    else:
        yinc = 0

    x = x1
    y = y1

    while True:
        board[y][x] += 1

        if x == x2 and y == y2:
            break

        x += xinc
        y += yinc

ans = 0
for row in range(1000):
    for col in range(1000):
        if board[row][col] > 1:
            ans += 1
print(ans)
#aocd.submit(ans, part="b", day=5, year=2021)
