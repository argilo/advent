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

data = aocd.get_data(day=10, year=2023)
# data = """7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ"""
# data = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""
# data = """...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........
# """

board = data.splitlines()
graph = nx.Graph()

for r, row in enumerate(board):
    prev_r = r-1 if r > 0 else None
    next_r = r+1 if r < len(board)-1 else None
    for c, square in enumerate(row):
        prev_c = c-1 if c > 0 else None
        next_c = c+1 if c < len(row)-1 else None

        if square == "|":
            if prev_r and board[prev_r][c] in ("|", "7", "F"):
                graph.add_edge((prev_r, c), (r, c))
            if next_r and board[next_r][c] in ("|", "L", "J"):
                graph.add_edge((next_r, c), (r, c))
        if square == "-":
            if prev_c and board[r][prev_c] in ("-", "L", "F"):
                graph.add_edge((r, prev_c), (r, c))
            if next_c and board[r][next_c] in ("-", "J", "7"):
                graph.add_edge((r, next_c), (r, c))
        if square == "L":
            if prev_r and board[prev_r][c] in ("|", "7", "F"):
                graph.add_edge((prev_r, c), (r, c))
            if next_c and board[r][next_c] in ("-", "J", "7"):
                graph.add_edge((r, next_c), (r, c))
        if square == "J":
            if prev_r and board[prev_r][c] in ("|", "7", "F"):
                graph.add_edge((prev_r, c), (r, c))
            if prev_c and board[r][prev_c] in ("-", "L", "F"):
                graph.add_edge((r, prev_c), (r, c))
        if square == "7":
            if next_r and board[next_r][c] in ("|", "L", "J"):
                graph.add_edge((next_r, c), (r, c))
            if prev_c and board[r][prev_c] in ("-", "L", "F"):
                graph.add_edge((r, prev_c), (r, c))
        if square == "F":
            if next_r and board[next_r][c] in ("|", "L", "J"):
                graph.add_edge((next_r, c), (r, c))
            if next_c and board[r][next_c] in ("-", "J", "7"):
                graph.add_edge((r, next_c), (r, c))
        if square == ".":
            pass
        if square == "S":
            start_r = r
            start_c = c

if board[start_r - 1][start_c] in ("|", "L", "J"):
    graph.add_edge((start_r - 1, start_c), (start_r, start_c))
if board[start_r + 1][start_c] in ("|", "7", "F"):
    graph.add_edge((start_r + 1, start_c), (start_r, start_c))
if board[start_r][start_c - 1] in ("-", "J", "7"):
    graph.add_edge((start_r, start_c - 1), (start_r, start_c))
if board[start_r][start_c + 1] in ("-", "L", "F"):
    graph.add_edge((start_r, start_c + 1), (start_r, start_c))

for comp in nx.connected_components(graph):
    if (start_r, start_c) in comp:
        break

print(len(comp) // 2)
# aocd.submit(ans, part="a", day=10, year=2023)

bc = {
    "|": "│",
    "-": "─",
    "L": "└",
    "J": "┘",
    "7": "┐",
    "F": "┌",
    "S": "S",
}

ans = 0
for r in range(len(board)):
    inside = False
    for c in range(len(board[0])):
        if (r, c) in comp:
            print(bc[board[r][c]], end="")
            if board[r][c] in ("|", "L", "J", "S"):
                inside = not inside
        else:
            print("*" if inside else ".", end="")
            if inside:
                ans += 1
    print()

print(ans)
# aocd.submit(ans, part="b", day=10, year=2023)
