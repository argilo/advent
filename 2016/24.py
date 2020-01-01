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
import itertools

board = []
for line in open("24-input.txt"):
    board.append(list(line.rstrip()))

graph = dijkstar.Graph()
numbers = {}
for r in range(1, len(board)-1):
    for c in range(1, len(board[r])-1):
        if board[r][c] != "#":
            for r2, c2 in ((r, c+1), (r, c-1), (r+1, c), (r-1, c)):
                if board[r2][c2] != "#":
                    graph.add_edge((r, c), (r2, c2), 1)
        if "1" <= board[r][c] <= "9":
            numbers[int(board[r][c])] = (r, c)
        if board[r][c] == "0":
            start_r, start_c = r, c

costs = {}
all_points = ((start_r, start_c),) + tuple(numbers.values())
for a, b in itertools.combinations(all_points, 2):
    cost = dijkstar.find_path(graph, a, b).total_cost
    costs[(a, b)] = cost
    costs[(b, a)] = cost

best = 1000000
for p in itertools.permutations(numbers.values()):
    p = ((start_r, start_c),) + p
    cost = 0
    for i in range(len(numbers)):
        cost += costs[(p[i], p[i+1])]
    if cost < best:
        best = cost
print(best)

best = 1000000
for p in itertools.permutations(numbers.values()):
    p = ((start_r, start_c),) + p + ((start_r, start_c),)
    cost = 0
    for i in range(len(numbers)+1):
        cost += costs[(p[i], p[i+1])]
    if cost < best:
        best = cost
print(best)
