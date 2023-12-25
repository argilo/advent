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
import itertools
import networkx as nx

data = aocd.get_data(day=25, year=2023)

graph = nx.Graph()
for line in data.splitlines():
    ls, rs = line.split(": ")
    part1 = ls
    for part2 in rs.split(" "):
        graph.add_edge(part1, part2)

for edge in nx.minimum_edge_cut(graph):
    graph.remove_edge(edge[0], edge[1])

prod = 1
for comp in nx.connected_components(graph):
    prod *= len(comp)
print(prod)
