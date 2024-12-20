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

full_time = nx.shortest_path_length(graph, source=(start_r, start_c), target=(end_r, end_c))

ans = 0
for rr in range(1, height - 1):
    for cc in range(1, width - 1):
        if board[rr][cc] == "#":
            added = False
            if board[rr+1][cc] == ".":
                graph.add_edge((rr, cc), (rr+1, cc))
                added = True
            if board[rr-1][cc] == ".":
                graph.add_edge((rr, cc), (rr-1, cc))
                added = True
            if board[rr][cc+1] == ".":
                graph.add_edge((rr, cc), (rr, cc+1))
                added = True
            if board[rr][cc-1] == ".":
                graph.add_edge((rr, cc), (rr, cc-1))
                added = True
            if not added:
                continue

            cheat_time = nx.shortest_path_length(graph, source=(start_r, start_c), target=(end_r, end_c))
            if cheat_time <= full_time - 100:
                ans += 1

            graph.remove_node((rr, cc))

print(ans)
# aocd.submit(ans, part="a", day=20, year=2024)


full_path = nx.shortest_path(graph, source=(start_r, start_c), target=(end_r, end_c))
index = {}
for i, node in enumerate(full_path):
    index[node] = i

max_cheat = 20
ans = 0
for r in range(height):
    for c in range(width):
        if board[r][c] == ".":
            for d_r in range(-max_cheat, max_cheat+1):
                for d_c in range(-max_cheat, max_cheat+1):
                    if 2 <= abs(d_r) + abs(d_c) <= max_cheat and (d_r, d_c) > (0, 0):
                        if 0 < r+d_r < height - 1 and 0 < c+d_c < width - 1:
                            if board[r+d_r][c+d_c] == ".":
                                if (r, c) in index and (r+d_r, c+d_c) in index:
                                    improvement = abs(index[(r, c)] - index[(r+d_r, c+d_c)]) - abs(d_r) - abs(d_c)
                                    if improvement >= 100:
                                        ans += 1

print(ans)
# aocd.submit(ans, part="b", day=20, year=2024)
