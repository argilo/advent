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

import re

grid1 = [[0 for _ in range(1000)] for _ in range(1000)]
grid2 = [[0 for _ in range(1000)] for _ in range(1000)]
pattern = re.compile(r"(.*) (\d+),(\d+) through (\d+),(\d+)")
for line in open("06-input.txt"):
    match = pattern.match(line.rstrip())
    command = match[1]
    x1, y1 = int(match[2]), int(match[3])
    x2, y2 = int(match[4]), int(match[5])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if command == "turn on":
                grid1[x][y] = 1
                grid2[x][y] += 1
            elif command == "turn off":
                grid1[x][y] = 0
                grid2[x][y] = max(grid2[x][y] - 1, 0)
            elif command == "toggle":
                grid1[x][y] ^= 1
                grid2[x][y] += 2

sum1 = 0
sum2 = 0
for x in range(1000):
    for y in range(1000):
        sum1 += grid1[x][y]
        sum2 += grid2[x][y]
print(sum1)
print(sum2)
