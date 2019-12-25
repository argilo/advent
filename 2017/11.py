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

with open("11-input.txt") as f:
    steps = f.read().rstrip().split(",")

x, y = 0, 0
max_dist = 0
for step in steps:
    if step == "n":
        y += 1
    elif step == "s":
        y -= 1
    elif step == "se":
        x += 1
    elif step == "nw":
        x -= 1
    elif step == "ne":
        x += 1
        y += 1
    elif step == "sw":
        x -= 1
        y -= 1
    if max(x, y) > max_dist:
        max_dist = max(x, y)
print(max(x, y))
print(max_dist)
