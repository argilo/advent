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

graph = {}
places = set()
for line in open("09-input.txt"):
    parts = line.rstrip().split()
    start, end, dist = parts[0], parts[2], int(parts[4])
    graph[(start, end)] = dist
    graph[(end, start)] = dist
    places.add(start)
    places.add(end)

min_dist = 1000000
max_dist = 0
for order in itertools.permutations(places):
    dist = 0
    for i in range(len(places) - 1):
        dist += graph[(order[i], order[i+1])]
    if dist < min_dist:
        min_dist = dist
    if dist > max_dist:
        max_dist = dist
print(min_dist)
print(max_dist)
