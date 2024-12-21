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
import itertools
import networkx as nx

data = aocd.get_data(day=20, year=2024)

# data = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""

board = [list(row) for row in data.splitlines()]
height = len(board)
width = len(board[0])

graph = nx.grid_2d_graph(height, width)
for r, row in enumerate(board):
    for c, col in enumerate(row):
        if col == "#":
            graph.remove_node((r, c))
        if col == "S":
            start_r, start_c = r, c
        elif col == "E":
            end_r, end_c = r, c

board[start_r][start_c] = "."
board[end_r][end_c] = "."

full_path = nx.shortest_path(graph, source=(start_r, start_c), target=(end_r, end_c))
index = {node: i for i, node in enumerate(full_path)}

ans = 0
for ((r1, c1), (r2, c2)) in itertools.combinations(full_path, 2):
    cheat_len = abs(r1 - r2) + abs(c1 - c2)
    if cheat_len <= 2:
        if abs(index[(r1, c1)] - index[(r2, c2)]) - cheat_len >= 100:
            ans += 1

print(ans)
# aocd.submit(ans, part="a", day=20, year=2024)


ans = 0
for ((r1, c1), (r2, c2)) in itertools.combinations(full_path, 2):
    cheat_len = abs(r1 - r2) + abs(c1 - c2)
    if cheat_len <= 20:
        if abs(index[(r1, c1)] - index[(r2, c2)]) - cheat_len >= 100:
            ans += 1

print(ans)
# aocd.submit(ans, part="b", day=20, year=2024)
