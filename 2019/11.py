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

import intcode
import itertools

with open("11-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]


seen_panels = {}
direction = 0
x, y = 0, 0
machine = intcode.execute(prog)

while True:
    try:
        next(machine)
    except StopIteration:
        break
    colour = machine.send(seen_panels.get((x, y), 0))
    turn = next(machine)

    seen_panels[(x, y)] = colour
    if turn == 1:
        direction = (direction + 1) % 4
    elif turn == 0:
        direction = (direction + 3) % 4

    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x -= 1
print(len(seen_panels))


seen_panels = {(0, 0): 1}
direction = 0
x, y = 0, 0
min_x, max_x, min_y, max_y = 0, 0, 0, 0
machine = intcode.execute(prog)

while True:
    try:
        next(machine)
    except StopIteration:
        break
    colour = machine.send(seen_panels.get((x, y), 0))
    turn = next(machine)

    seen_panels[(x, y)] = colour
    if turn == 1:
        direction = (direction + 1) % 4
    elif turn == 0:
        direction = (direction + 3) % 4

    if direction == 0:
        y -= 1
        if y < min_y:
            min_y = y
    elif direction == 1:
        x += 1
        if x > max_x:
            max_x = x
    elif direction == 2:
        y += 1
        if y > max_y:
            max_y = y
    elif direction == 3:
        x -= 1
        if x < min_x:
            min_x = x

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        print("█" if seen_panels.get((x, y), 0) == 1 else " ", end="")
    print()
