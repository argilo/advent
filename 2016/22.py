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

import itertools


nodes = {}
size_x, size_y = 0, 0
for line in open("22-input.txt"):
    if line.startswith("/dev/grid/"):
        parts = line.split()
        x, y = [int(s[1:]) for s in parts[0].split("-")[1:]]
        size, used = int(parts[1][:-1]), int(parts[2][:-1])
        nodes[(x, y)] = (size, used)
        if x+1 > size_x:
            size_x = x+1
        if y+1 > size_y:
            size_y = y+1

viable = 0
for a, b in itertools.permutations(nodes.values(), 2):
    if 0 < a[1] <= (b[0] - b[1]):
        viable += 1
print(viable)

print()
for y in range(size_y):
    for x in range(size_x):
        size, used = nodes[(x, y)]
        print(f"{used:3}/{size:3} ", end="")
    print()
print(12 + 14 + 32 + 5*31)
