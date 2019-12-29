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

import copy


def life(board):
    new_board = copy.deepcopy(board)
    for row in range(1, len(board)-1):
        for col in range(1, len(board[row])-1):
            neighbours = 0
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if (r, c) != (0, 0):
                        neighbours += board[row+r][col+c]
            if board[row][col] == 0 and neighbours == 3:
                new_board[row][col] = 1
            if board[row][col] == 1 and neighbours not in [2, 3]:
                new_board[row][col] = 0
    return new_board


board = [[0 for _ in range(102)] for _ in range(102)]


for row, line in enumerate(open("18-input.txt"), start=1):
    for col, char in enumerate(line.rstrip(), start=1):
        board[row][col] = 1 if char == "#" else 0

for _ in range(100):
    board = life(board)
print(sum(sum(row) for row in board))


for row, line in enumerate(open("18-input.txt"), start=1):
    for col, char in enumerate(line.rstrip(), start=1):
        board[row][col] = 1 if char == "#" else 0

for _ in range(100):
    board[1][1] = 1
    board[1][-2] = 1
    board[-2][1] = 1
    board[-2][-2] = 1
    board = life(board)
board[1][1] = 1
board[1][-2] = 1
board[-2][1] = 1
board[-2][-2] = 1
print(sum(sum(row) for row in board))
