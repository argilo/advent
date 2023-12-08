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
import math

data = aocd.get_data(day=8, year=2023)

net = {}
for i, line in enumerate(data.splitlines()):
    if i == 0:
        instructions = line
        continue
    if i == 1:
        continue

    el = line[0:3]
    left = line[7:10]
    right = line[12:15]
    net[el] = (left, right)

current = "AAA"
steps = 0
while current != "ZZZ":
    direction = instructions[steps % len(instructions)]
    if direction == "L":
        current = net[current][0]
    else:
        current = net[current][1]
    steps += 1

print(steps)
# aocd.submit(steps, part="a", day=8, year=2023)


ans = 1
for el in net.keys():
    if el.endswith("A"):
        current = el
        steps = 0
        while not current.endswith("Z"):
            direction = instructions[steps % len(instructions)]
            if direction == "L":
                current = net[current][0]
            else:
                current = net[current][1]
            steps += 1
        ans = math.lcm(ans, steps)

print(ans)
# aocd.submit(ans, part="b", day=8, year=2023)
