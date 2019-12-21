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
import copy

board = []
for line in open("18-input.txt"):
    row = list(line.rstrip())
    board.append(row)


def to_graph(board):
    starts = []
    keys = {}
    doors = {}
    graph = dijkstar.Graph()
    for r in range(1, len(board) - 1):
        row = board[r]
        for c in range(1, len(row) - 1):
            if board[r][c] == "@":
                starts.append((r, c))
            if "a" <= board[r][c] <= "z":
                keys[board[r][c]] = (r, c)
            if "A" <= board[r][c] <= "Z":
                doors[board[r][c].lower()] = (r, c)
            if board[r][c] in ["@", "."]:
                for r2, c2 in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if board[r2][c2] in ["@", "."]:
                        graph.add_edge((r, c), (r2, c2), 1)
                        graph.add_edge((r2, c2), (r, c), 1)
                    elif "a" <= board[r2][c2] <= "z":
                        graph.add_edge((r, c), (r2, c2), 1)
    return graph, tuple(starts), keys, doors


cache = {}


def pathlen(board):
    graph, starts, keys, doors = to_graph(board)
    if len(keys) == 0:
        return 0
    lookup_key = (starts, "".join(sorted(keys.keys())))
    if lookup_key in cache:
        return cache[lookup_key]

    min_path = 1000000
    for start in starts:
        for key, key_pos in keys.items():
            try:
                path = dijkstar.find_path(graph, start, key_pos)
                new_board = copy.deepcopy(board)

                start_r, start_c = start
                new_board[start_r][start_c] = "."

                key_r, key_c = key_pos
                new_board[key_r][key_c] = "@"

                if key in doors:
                    door_r, door_c = doors[key]
                    new_board[door_r][door_c] = "."

                new_pathlen = path.total_cost + pathlen(new_board)
                if new_pathlen < min_path:
                    min_path = new_pathlen
            except dijkstar.NoPathError:
                pass
    cache[lookup_key] = min_path
    return min_path


print(pathlen(board))

for rr in range(1, len(board) - 1):
    for cc in range(1, len(row) - 1):
        if board[rr][cc] == "@":
            r, c = rr, cc

board[r][c] = "#"
board[r][c-1] = "#"
board[r][c+1] = "#"
board[r-1][c] = "#"
board[r+1][c] = "#"
board[r-1][c-1] = "@"
board[r-1][c+1] = "@"
board[r+1][c-1] = "@"
board[r+1][c+1] = "@"

print(pathlen(board))
