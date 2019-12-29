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

with open("17-input.txt") as f:
    containers = [int(n) for n in f.read().split()]

size = len(containers)
ways = []
for choose in itertools.product((0, 1), repeat=size):
    summ = 0
    for i in range(size):
        if choose[i] == 1:
            summ += containers[i]
    if summ == 150:
        ways.append(choose)

print(len(ways))
lens = [sum(way) for way in ways]
best = min(lens)
print(lens.count(best))
