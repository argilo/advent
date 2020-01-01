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

import hashlib


def doors(s):
    h = hashlib.md5(s.encode()).hexdigest()[0:4]
    return ["b" <= c <= "f" for c in h]


dir_chr = ["U", "D", "L", "R"]
dir_xy = [(0, -1), (0, 1), (-1, 0), (1, 0)]

with open("17-input.txt") as f:
    passcode = f.read().rstrip()

queue = [(0, 0, "")]
first = None
longest = 0
while queue:
    new_queue = []
    for x, y, seq in queue:
        if (x, y) == (3, 3):
            longest = len(seq)
            if first is None:
                first = seq
        else:
            dir_doors = doors(passcode + seq)
            for dir in range(4):
                if not dir_doors[dir]:
                    continue
                delta_x, delta_y = dir_xy[dir]
                new_x, new_y = x + delta_x, y + delta_y
                if 0 <= new_x < 4 and 0 <= new_y < 4:
                    new_queue.append((new_x, new_y, seq + dir_chr[dir]))
    queue = new_queue
print(first)
print(longest)
