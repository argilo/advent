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


def new_board(board):
    nb = [[0]*7 for _ in range(7)]
    for row in range(1, 6):
        for col in range(1, 6):
            adjacents = board[row][col-1], board[row][col+1], board[row-1][col], board[row+1][col]
            if board[row][col] == 1 and adjacents.count(1) == 1:
                nb[row][col] = 1
            if board[row][col] == 0 and adjacents.count(1) in (1, 2):
                nb[row][col] = 1
    return nb


def score(board):
    score = 0
    for row in range(1, 6):
        for col in range(1, 6):
            if board[row][col] == 1:
                score += 1 << (5*(row-1) + (col-1))
    return score


board = []
board.append([0]*7)
for line in open("24-input.txt"):
    board.append([0] + [1 if char == "#" else 0 for char in list(line.rstrip())] + [0])
board.append([0]*7)

seen = set()
while True:
    sc = score(board)
    if sc in seen:
        break
    seen.add(sc)
    board = new_board(board)
print(sc)


def new_board2(board):
    nb = [[[0]*5 for _ in range(5)] for _ in range(len(board))]
    for depth in range(1, len(board)-1):
        for row in range(5):
            for col in range(5):
                if (row, col) == (2, 2):
                    continue
                adjacents = []
                for r, c in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]:
                    if r == -1:
                        adjacents.append(board[depth-1][1][2])
                    elif r == 5:
                        adjacents.append(board[depth-1][3][2])
                    elif c == -1:
                        adjacents.append(board[depth-1][2][1])
                    elif c == 5:
                        adjacents.append(board[depth-1][2][3])
                    elif (r, c) == (2, 2):
                        if (row, col) == (1, 2):
                            for cc in range(5):
                                adjacents.append(board[depth+1][0][cc])
                        if (row, col) == (3, 2):
                            for cc in range(5):
                                adjacents.append(board[depth+1][4][cc])
                        if (row, col) == (2, 1):
                            for rr in range(5):
                                adjacents.append(board[depth+1][rr][0])
                        if (row, col) == (2, 3):
                            for rr in range(5):
                                adjacents.append(board[depth+1][rr][4])
                    else:
                        adjacents.append(board[depth][r][c])

                if board[depth][row][col] == 1 and adjacents.count(1) == 1:
                    nb[depth][row][col] = 1
                if board[depth][row][col] == 0 and adjacents.count(1) in (1, 2):
                    nb[depth][row][col] = 1

    return nb


board = [[[0]*5 for _ in range(5)] for _ in range(500)]
row = 0
for line in open("24-input.txt"):
    for col in range(5):
        board[250][row][col] = 1 if line[col] == "#" else 0
    row += 1

for _ in range(200):
    board = new_board2(board)

sum = 0
for depth in range(len(board)):
    for row in range(5):
        for col in range(5):
            sum += board[depth][row][col]
print(sum)
