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


def is_wall(x, y, fav):
    num = x*x + 3*x + 2*x*y + y + y*y + fav
    return f"{num:b}".count("1") % 2


with open("13-input.txt") as f:
    fav = int(f.read().rstrip())

graph = dijkstar.Graph()
for y in range(100):
    for x in range(100):
        if not is_wall(x, y, fav):
            for (x2, y2) in ((x+1, y), (x, y+1)):
                if not is_wall(x2, y2, fav):
                    graph.add_edge((x, y), (x2, y2), 1)
                    graph.add_edge((x2, y2), (x, y), 1)
print(dijkstar.find_path(graph, (1, 1), (31, 39)).total_cost)

sum = 0
for y in range(60):
    for x in range(60):
        try:
            cost = dijkstar.find_path(graph, (1, 1), (x, y)).total_cost
            if cost <= 50:
                sum += 1
        except dijkstar.algorithm.NoPathError:
            pass
print(sum)
