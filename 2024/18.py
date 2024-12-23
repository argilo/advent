#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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
import networkx as nx

data = aocd.get_data(day=18, year=2024)
size = 71
num_corrupted = 1024

# data = """5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0"""
# size = 7
# num_corrupted = 12

graph = nx.grid_2d_graph(size, size)

for line in data.splitlines()[:num_corrupted]:
    x, y = [int(n) for n in line.split(",")]
    graph.remove_node((x, y))

ans = nx.shortest_path_length(graph, source=(0, 0), target=(size-1, size-1))

print(ans)
# aocd.submit(ans, part="a", day=18, year=2024)


graph = nx.grid_2d_graph(size, size)

for line in data.splitlines():
    x, y = [int(n) for n in line.split(",")]
    graph.remove_node((x, y))

    if not nx.has_path(graph, source=(0, 0), target=(size-1, size-1)):
        ans = f"{x},{y}"
        break

print(ans)
# aocd.submit(ans, part="b", day=18, year=2024)
