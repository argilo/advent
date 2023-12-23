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
import networkx as nx

data = aocd.get_data(day=23, year=2023)
# data = """#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#"""

board = data.splitlines()
height = len(board)
width = len(board[0])

source = (0, board[0].index("."))
target = (len(board)-1, board[-1].index("."))

graph = nx.DiGraph()

for r in range(height):
    for c in range(width):
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r2 = r + dr
            c2 = c + dc
            if 0 <= r2 < height and 0 <= c2 < width:
                if board[r][c] == board[r2][c2] == ".":
                    graph.add_edge((r, c), (r2, c2))
                    graph.add_edge((r2, c2), (r, c))
                if dr == 1 and board[r][c] == "." and board[r2][c2] == "v":
                    graph.add_edge((r, c), (r2, c2))
                if dr == 1 and board[r][c] == "v" and board[r2][c2] == ".":
                    graph.add_edge((r, c), (r2, c2))
                if dr == -1 and board[r][c] == "." and board[r2][c2] == "^":
                    graph.add_edge((r2, c2), (r, c))
                if dr == -1 and board[r][c] == "^" and board[r2][c2] == ".":
                    graph.add_edge((r2, c2), (r, c))
                if dc == 1 and board[r][c] == "." and board[r2][c2] == ">":
                    graph.add_edge((r, c), (r2, c2))
                if dc == 1 and board[r][c] == ">" and board[r2][c2] == ".":
                    graph.add_edge((r, c), (r2, c2))
                if dc == -1 and board[r][c] == "." and board[r2][c2] == "<":
                    graph.add_edge((r2, c2), (r, c))
                if dc == -1 and board[r][c] == "<" and board[r2][c2] == ".":
                    graph.add_edge((r2, c2), (r, c))

ans = 0
for path in nx.all_simple_paths(graph, source=source, target=target):
    path_len = len(path) - 1
    if path_len > ans:
        ans = path_len
print(ans)
print()

# aocd.submit(ans, part="a", day=23, year=2023)

graph = nx.Graph()
for r in range(height):
    for c in range(width):
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r2 = r + dr
            c2 = c + dc
            if 0 <= r2 < height and 0 <= c2 < width:
                if board[r][c] != "#" and board[r2][c2] != "#":
                    graph.add_edge((r, c), (r2, c2))


def all_simple_paths_graph(G, source, target):
    visited = {source: True}
    stack = [iter(G[source])]
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.popitem()
        else:
            if child in visited:
                continue
            if child == target:
                yield len(visited)
            else:
                visited[child] = True
                stack.append(iter(G[child]))


ans = 0
for path_len in all_simple_paths_graph(graph, source=source, target=target):
    if path_len > ans:
        ans = path_len
        print(ans)
print(ans)

# aocd.submit(ans, part="b", day=23, year=2023)
