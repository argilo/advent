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

with open("03-input.txt") as f:
    data = f.read().rstrip()

presents = {(0, 0): 1}
x, y = 0, 0
for char in data:
    if char == "<":
        x -= 1
    elif char == ">":
        x += 1
    elif char == "^":
        y -= 1
    elif char == "v":
        y += 1
    presents[(x, y)] = presents.get((x, y), 0)
print(len(presents))

presents = {(0, 0): 2}
x, y = 0, 0
for char in data[0::2]:
    if char == "<":
        x -= 1
    elif char == ">":
        x += 1
    elif char == "^":
        y -= 1
    elif char == "v":
        y += 1
    presents[(x, y)] = presents.get((x, y), 0)
x, y = 0, 0
for char in data[1::2]:
    if char == "<":
        x -= 1
    elif char == ">":
        x += 1
    elif char == "^":
        y -= 1
    elif char == "v":
        y += 1
    presents[(x, y)] = presents.get((x, y), 0)
print(len(presents))
