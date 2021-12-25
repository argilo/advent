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

data = aocd.get_data(day=25, year=2021)
# data = """v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>"""

lines = data.splitlines()

board = []
for line in lines:
    board.append(list(line))
height = len(board)
width = len(board[0])

def print_board(board):
    for row in board:
        print("".join(row))
    print()

ans = 0
while True:
    changed = False
    for row in range(height):
        can_move = []
        for col in range(width):
            if board[row][col] == ">" and board[row][(col+1) % width] == ".":
                changed = True
                can_move.append(True)
            else:
                can_move.append(False)
        for col in range(width):
            if can_move[col]:
                board[row][col] = "."
                board[row][(col+1) % width] = ">"

    for col in range(width):
        can_move = []
        for row in range(height):
            if board[row][col] == "v" and board[(row+1) % height][col] == ".":
                changed = True
                can_move.append(True)
            else:
                can_move.append(False)
        for row in range(height):
            if can_move[row]:
                board[row][col] = "."
                board[(row+1) % height][col] = "v"

    ans += 1
    if not changed:
        break

print(ans)
