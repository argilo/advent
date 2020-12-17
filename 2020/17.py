#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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
import copy

data = aocd.get_data(day=17, year=2020)

cycles = 6
lines = data.splitlines()

width = len(lines[0]) + cycles * 2 + 2
height = len(lines) + cycles * 2 + 2
depth = 1 + cycles * 2 + 2

board = [[[0]*width for _ in range(height)] for _ in range(depth)]

for row, line in enumerate(data.splitlines()):
    for col, c in enumerate(line):
        if c == "#":
            board[cycles+1][row+cycles+1][col+cycles+1] = 1

for _ in range(cycles):
    new_board = copy.deepcopy(board)
    for z in range(1, len(board)-1):
        for r in range(1, len(board[0])-1):
            for c in range(1, len(board[0][0])-1):
                neighbours = 0
                for dz in range(-1, 2):
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if dz == dr == dc == 0:
                                continue
                            if board[z+dz][r+dr][c+dc] == 1:
                                neighbours += 1
                if board[z][r][c] == 1:
                    if neighbours not in [2, 3]:
                        new_board[z][r][c] = 0
                else:
                    if neighbours == 3:
                        new_board[z][r][c] = 1
    board = new_board

total = 0
for slice in board:
    for row in slice:
        for col in row:
            if col == 1:
                total += 1
print(total)


data = aocd.get_data(day=17, year=2020)

cycles = 6
lines = data.splitlines()

width = len(lines[0]) + cycles * 2 + 2
height = len(lines) + cycles * 2 + 2
depth = 1 + cycles * 2 + 2
depth2 = 1 + cycles * 2 + 2

board = [[[[0]*width for _ in range(height)] for _ in range(depth)] for _ in range(depth2)]

for row, line in enumerate(data.splitlines()):
    for col, c in enumerate(line):
        if c == "#":
            board[cycles+1][cycles+1][row+cycles+1][col+cycles+1] = 1

for _ in range(cycles):
    new_board = copy.deepcopy(board)
    for z2 in range(1, len(board)-1):
        for z in range(1, len(board[0])-1):
            for r in range(1, len(board[0][0])-1):
                for c in range(1, len(board[0][0][0])-1):
                    neighbours = 0
                    for dz2 in range(-1, 2):
                        for dz in range(-1, 2):
                            for dr in range(-1, 2):
                                for dc in range(-1, 2):
                                    if dz2 == dz == dr == dc == 0:
                                        continue
                                    if board[z2+dz2][z+dz][r+dr][c+dc] == 1:
                                        neighbours += 1
                    if board[z2][z][r][c] == 1:
                        if neighbours not in [2, 3]:
                            new_board[z2][z][r][c] = 0
                    else:
                        if neighbours == 3:
                            new_board[z2][z][r][c] = 1
    board = new_board

total = 0
for slice2 in board:
    for slice in slice2:
        for row in slice:
            for col in row:
                if col == 1:
                    total += 1
print(total)
