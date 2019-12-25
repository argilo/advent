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

import dijkstar

graph = dijkstar.Graph()
for line in open("12-input.txt"):
    parts = line.rstrip().split(" <-> ")
    left = int(parts[0])
    rights = [int(n) for n in parts[1].split(", ")]
    for right in rights:
        graph.add_edge(left, right, 1)

remaining = set(range(2000))
components = 0
while len(remaining) > 0:
    target = min(remaining)
    sum = 0
    for n in remaining.copy():
        try:
            dijkstar.find_path(graph, target, n).total_cost
            remaining.remove(n)
            sum += 1
        except dijkstar.algorithm.NoPathError:
            pass
    if target == 0:
        print(sum)
    components += 1
print(components)
