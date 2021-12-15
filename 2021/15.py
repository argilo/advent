#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=15, year=2021)
# data = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""

graph = dijkstar.Graph()

board = []
for line in data.splitlines():
    board.append([int(n) for n in line])

height = len(board)
width = len(board[0])

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for row in range(height):
    for col in range(width):
        for dir in dirs:
            other_row, other_col = row + dir[0], col + dir[1]
            if 0 <= other_row < height and 0 <= other_col < width:
                #print(other_row, other_col, row, col)
                graph.add_edge((other_row, other_col), (row, col), board[row][col])

cost = dijkstar.find_path(graph, (0, 0), (height-1, width-1)).total_cost
print(cost)

# aocd.submit(cost, part="a", day=15, year=2021)

board2 = [[0 for _ in range(width*5)] for _ in range(height*5)]
for row in range(height * 5):
    base_row = row % height
    copy_row = row // height

    for col in range(width * 5):
        base_col = col % width
        copy_col = col // width

        board2[row][col] = board[base_row][base_col] + copy_row + copy_col
        while board2[row][col] > 9:
            board2[row][col] -= 9

graph = dijkstar.Graph()

for row in range(height * 5):
    for col in range(width * 5):
        for dir in dirs:
            other_row, other_col = row + dir[0], col + dir[1]
            if 0 <= other_row < height*5 and 0 <= other_col < width*5:
                #print(other_row, other_col, row, col)
                graph.add_edge((other_row, other_col), (row, col), board2[row][col])

cost = dijkstar.find_path(graph, (0, 0), (height*5-1, width*5-1)).total_cost
print(cost)

# aocd.submit(cost, part="b", day=15, year=2021)
