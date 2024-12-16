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

data = aocd.get_data(day=16, year=2024)

# data = """###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############"""

board = data.splitlines()
board = [list(row) for row in board]

height = len(board)
width = len(board[0])

for r, row in enumerate(board):
    for c, col in enumerate(row):
        if col == "S":
            start_r = r
            start_c = c
        if col == "E":
            end_r = r
            end_c = c

board[start_r][start_c] = "."
board[end_r][end_c] = "."

graph = nx.DiGraph()
for r in range(1, height - 1):
    for c in range(1, width - 1):
        if board[r][c] == ".":
            graph.add_edge((0, r, c), (1, r, c), weight=1000)
            graph.add_edge((1, r, c), (2, r, c), weight=1000)
            graph.add_edge((2, r, c), (3, r, c), weight=1000)
            graph.add_edge((3, r, c), (0, r, c), weight=1000)

            graph.add_edge((0, r, c), (3, r, c), weight=1000)
            graph.add_edge((1, r, c), (0, r, c), weight=1000)
            graph.add_edge((2, r, c), (1, r, c), weight=1000)
            graph.add_edge((3, r, c), (2, r, c), weight=1000)

            if board[r][c+1] == ".":
                graph.add_edge((0, r, c), (0, r, c+1), weight=1)
                graph.add_edge((2, r, c+1), (2, r, c), weight=1)
            if board[r][c-1] == ".":
                graph.add_edge((2, r, c), (2, r, c-1), weight=1)
                graph.add_edge((0, r, c-1), (0, r, c), weight=1)
            if board[r+1][c] == ".":
                graph.add_edge((1, r, c), (1, r+1, c), weight=1)
                graph.add_edge((3, r+1, c), (3, r, c), weight=1)
            if board[r-1][c] == ".":
                graph.add_edge((3, r, c), (3, r-1, c), weight=1)
                graph.add_edge((1, r-1, c), (1, r, c), weight=1)

lens = [nx.shortest_path_length(graph, source=(0, start_r, start_c), target=(dir, end_r, end_c), weight="weight") for dir in range(4)]
ans = min(lens)

print(ans)
# aocd.submit(ans, part="a", day=16, year=2024)


shortest = ans
sitting = set()
for dir in range(4):
    for path in nx.all_shortest_paths(graph, source=(0, start_r, start_c), target=(dir, end_r, end_c), weight="weight"):
        if nx.path_weight(graph, path, weight="weight") == shortest:
            for dir, r, c in path:
                sitting.add((r, c))
ans = len(sitting)

print(ans)
# aocd.submit(ans, part="b", day=16, year=2024)
