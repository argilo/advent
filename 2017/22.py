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

infected = set()
for row, line in enumerate(open("22-input.txt")):
    line = line.rstrip()
    width = len(line)
    for col, char in enumerate(line):
        if char == "#":
            infected.add((row, col))

row, col = width//2, width//2
dir = 0
count = 0
for _ in range(10000):
    if (row, col) in infected:
        dir = (dir + 1) % 4
        infected.remove((row, col))
    else:
        dir = (dir - 1) % 4
        infected.add((row, col))
        count += 1
    if dir == 0:
        row -= 1
    elif dir == 1:
        col += 1
    elif dir == 2:
        row += 1
    elif dir == 3:
        col -= 1
print(count)


infected = {}
for row, line in enumerate(open("22-input.txt")):
    line = line.rstrip()
    width = len(line)
    for col, char in enumerate(line):
        if char == "#":
            infected[(row, col)] = 2

row, col = width//2, width//2
dir = 0
count = 0
for _ in range(10000000):
    state = infected.get((row, col), 0)
    if state == 0:
        dir = (dir - 1) % 4
        infected[(row, col)] = 1
    elif state == 1:
        infected[(row, col)] = 2
        count += 1
    elif state == 2:
        dir = (dir + 1) % 4
        infected[(row, col)] = 3
    elif state == 3:
        dir = (dir + 2) % 4
        infected[(row, col)] = 0

    if dir == 0:
        row -= 1
    elif dir == 1:
        col += 1
    elif dir == 2:
        row += 1
    elif dir == 3:
        col -= 1
print(count)
