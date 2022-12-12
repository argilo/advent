#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=12, year=2022)
# data = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi"""

sr, sc = -1, -1
er, ec = -1, -1
board = []
for row, s in enumerate(data.split("\n")):
    vals = []
    for col, c in enumerate(s):
        if c == "S":
            height = 0
            sr, sc = row, col
        elif c == "E":
            height = 25
            er, ec = row, col
        else:
            height = ord(c) - ord("a")
        vals.append(height)
    board.append(vals)

graph = dijkstar.Graph()
for r, row in enumerate(board):
    for c, height in enumerate(row):
        if c > 0 and board[r][c-1] <= height + 1:
            graph.add_edge((r, c), (r, c-1), 1)
        if c < len(row)-1 and board[r][c+1] <= height + 1:
            graph.add_edge((r, c), (r, c+1), 1)
        if r > 0 and board[r-1][c] <= height + 1:
            graph.add_edge((r, c), (r-1, c), 1)
        if r < len(board)-1 and board[r+1][c] <= height + 1:
            graph.add_edge((r, c), (r+1, c), 1)

print(dijkstar.find_path(graph, (sr, sc), (er, ec)).total_cost)


best = 1000000
for r, row in enumerate(board):
    for c, height in enumerate(row):
        if height == 0:
            try:
                cost = dijkstar.find_path(graph, (r, c), (er, ec)).total_cost
            except dijkstar.algorithm.NoPathError:
                continue
            if cost < best:
                best = cost

print(best)
