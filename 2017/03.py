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


def spiral(n):
    if n == 1:
        return (0, 0)
    layer = int((((n - 0.5)**0.5) + 1) / 2)
    side_len = layer * 2
    layer_start = (1 + 2*layer)**2 - (4 * side_len) + 1
    side = (n - layer_start) // side_len
    side_pos = (n - layer_start) % side_len

    if side == 0:
        return layer, 1 - layer + side_pos
    elif side == 1:
        return layer - 1 - side_pos, layer
    elif side == 2:
        return -layer, layer - 1 - side_pos
    elif side == 3:
        return 1 - layer + side_pos, -layer
    return layer, side_len, layer_start, side, side_pos


with open("03-input.txt") as f:
    data = int(f.read().rstrip())

x, y = spiral(data)
print(abs(x) + abs(y))

memory = {}
n = 1
x, y = spiral(n)
memory[(x, y)] = 1
while memory[(x, y)] < data:
    x, y = spiral(n)
    sum = 0
    for other_x in range(x-1, x+2):
        for other_y in range(y-1, y+2):
            sum += memory.get((other_x, other_y), 0)
    memory[(x, y)] = sum
    n += 1
print(memory[(x, y)])
