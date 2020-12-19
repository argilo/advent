#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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
import dijkstar

data = aocd.get_data(day=7, year=2020)

lines = data.splitlines()

dict = {}
for line in lines:
    parts = line.split()
    outer = (parts[0], parts[1])

    if parts[4] == "no":
        dict[outer] = []
    else:
        inners = []
        for x in range(4, len(parts), 4):
            inner = (int(parts[x]), (parts[x+1], parts[x+2]))
            inners.append(inner)
        dict[outer] = inners

graph = dijkstar.Graph()

for outer, inners in dict.items():
    for num, inner in inners:
        graph.add_edge(outer, inner, num)

ans = 0
for outer in dict:
    try:
        cost = dijkstar.find_path(graph, outer, ("shiny", "gold")).total_cost
        ans += 1
    except dijkstar.algorithm.NoPathError:
        pass
print(ans-1)


def weight(outer):
    w = 1
    inners = dict[outer]
    for num, inner in inners:
        w += num * weight(inner)
    return w


ans = weight(("shiny", "gold"))
print(ans-1)
