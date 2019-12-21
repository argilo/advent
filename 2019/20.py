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
import itertools

board = []
for line in open("20-input.txt"):
    row = list(line.rstrip("\n"))
    board.append(row)

graph = dijkstar.Graph()
portals = {}
for r in range(2, len(board)-2):
    row = board[r]
    for c in range(2, len(row) - 2):
        if board[r][c] == ".":
            for dir_r, dir_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r2, c2 = r + dir_r, c + dir_c
                r3, c3 = r2 + dir_r, c2 + dir_c
                if board[r2][c2] == ".":
                    graph.add_edge((r, c), (r2, c2), 1)
                    graph.add_edge((r2, c2), (r, c), 1)
                elif "A" <= board[r2][c2] <= "Z":
                    if (r2, c2) < (r3, c3):
                        portal_name = board[r2][c2] + board[r3][c3]
                    else:
                        portal_name = board[r3][c3] + board[r2][c2]
                    portals[portal_name] = portals.get(portal_name, [])
                    portals[portal_name].append((r, c))
for portal_name, squares in portals.items():
    if len(squares) == 2:
        graph.add_edge(squares[0], squares[1], 1)
        graph.add_edge(squares[1], squares[0], 1)

print(dijkstar.find_path(graph, portals["AA"][0], portals["ZZ"][0]).total_cost)


LAYERS = 50
graph = dijkstar.Graph()
portals = {}
vertices = []
for r in range(2, len(board)-2):
    row = board[r]
    for c in range(2, len(row) - 2):
        if board[r][c] == ".":
            for dir_r, dir_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r2, c2 = r + dir_r, c + dir_c
                r3, c3 = r2 + dir_r, c2 + dir_c
                if board[r2][c2] == ".":
                    for layer in range(LAYERS):
                        graph.add_edge((r, c)+(layer,), (r2, c2)+(layer,), 1)
                        graph.add_edge((r2, c2)+(layer,), (r, c)+(layer,), 1)
                elif "A" <= board[r2][c2] <= "Z":
                    vertices.append((r, c))
                    if (r2, c2) < (r3, c3):
                        portal_name = board[r2][c2] + board[r3][c3]
                    else:
                        portal_name = board[r3][c3] + board[r2][c2]
                    portals[portal_name] = portals.get(portal_name, [])
                    portals[portal_name].append((r, c))
for portal_name, squares in portals.items():
    if len(squares) == 2:
        r, c = squares[0]
        if r in (2, len(board)-3) or c in (2, len(board[0])-3):
            inner, outer = squares[1], squares[0]
        else:
            inner, outer = squares[0], squares[1]
        for layer in range(LAYERS-1):
            graph.add_edge(inner + (layer,), outer + (layer+1,), 1)
            graph.add_edge(outer + (layer+1,), inner + (layer,), 1)

print(dijkstar.find_path(graph,
                         portals["AA"][0] + (0,),
                         portals["ZZ"][0] + (0,)).total_cost)
