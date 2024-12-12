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

data = aocd.get_data(day=12, year=2024)

# data = """AAAA
# BBCD
# BBCC
# EEEC"""

# data = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

# data = """EEEEE
# EXXXX
# EEEEE
# EXXXX
# EEEEE"""

# data = """AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA"""


board = data.splitlines()
height = len(board)
width = len(board[0])

graph = nx.Graph()

for r in range(height):
    for c in range(width):
        graph.add_node((r, c))
        if r < height - 1 and board[r][c] == board[r+1][c]:
            graph.add_edge((r, c), (r+1, c))
        if c < width - 1 and board[r][c] == board[r][c+1]:
            graph.add_edge((r, c), (r, c+1))

ans = 0
for component in nx.connected_components(graph):
    area = 0
    perimeter = 0
    for (r, c) in component:
        area += 1
        for diff_r, diff_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (r + diff_r, c + diff_c) not in component:
                perimeter += 1
    ans += area * perimeter

print(ans)
# aocd.submit(ans, part="a", day=12, year=2024)


ans = 0
for component in nx.connected_components(graph):
    area = 0
    perimeter = set()
    for (r, c) in component:
        area += 1
        for diff_r, diff_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (r + diff_r, c + diff_c) not in component:
                perimeter.add((diff_r, diff_c, r*2 + diff_r, c*2 + diff_c))
    per_graph = nx.Graph()
    for diff_r, diff_c, r, c in perimeter:
        per_graph.add_node((diff_r, diff_c, r, c))
        if diff_r != 0 and diff_c == 0 and (diff_r, diff_c, r, c+2) in perimeter:
            per_graph.add_edge((diff_r, diff_c, r, c), (diff_r, diff_c, r, c+2))
        if diff_r == 0 and diff_c != 0 and (diff_r, diff_c, r+2, c) in perimeter:
            per_graph.add_edge((diff_r, diff_c, r, c), (diff_r, diff_c, r+2, c))
    cost = 0
    for component in nx.connected_components(per_graph):
        cost += 1
    ans += area * cost

print(ans)
# aocd.submit(ans, part="b", day=12, year=2024)
