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
    for rw in range(1, 6):
        for cl in range(1, 6):
            adj = board[rw][cl-1], board[rw][cl+1], \
                board[rw-1][cl], board[rw+1][cl]
            if board[rw][cl] == 1 and adj.count(1) == 1:
                nb[rw][cl] = 1
            if board[rw][cl] == 0 and adj.count(1) in (1, 2):
                nb[rw][cl] = 1
    return nb


def score(board):
    score = 0
    for rw in range(1, 6):
        for cl in range(1, 6):
            if board[rw][cl] == 1:
                score += 1 << (5*(rw-1) + (cl-1))
    return score


board = []
board.append([0]*7)
for line in open("24-input.txt"):
    board.append([0] + [int(ch == "#") for ch in list(line.rstrip())] + [0])
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
        for rw in range(5):
            for cl in range(5):
                if (rw, cl) == (2, 2):
                    continue
                adj = []
                for r, c in (rw, cl+1), (rw, cl-1), (rw+1, cl), (rw-1, cl):
                    if r == -1:
                        adj.append(board[depth-1][1][2])
                    elif r == 5:
                        adj.append(board[depth-1][3][2])
                    elif c == -1:
                        adj.append(board[depth-1][2][1])
                    elif c == 5:
                        adj.append(board[depth-1][2][3])
                    elif (r, c) == (2, 2):
                        if (rw, cl) == (1, 2):
                            for cc in range(5):
                                adj.append(board[depth+1][0][cc])
                        if (rw, cl) == (3, 2):
                            for cc in range(5):
                                adj.append(board[depth+1][4][cc])
                        if (rw, cl) == (2, 1):
                            for rr in range(5):
                                adj.append(board[depth+1][rr][0])
                        if (rw, cl) == (2, 3):
                            for rr in range(5):
                                adj.append(board[depth+1][rr][4])
                    else:
                        adj.append(board[depth][r][c])

                if board[depth][rw][cl] == 1 and adj.count(1) == 1:
                    nb[depth][rw][cl] = 1
                if board[depth][rw][cl] == 0 and adj.count(1) in (1, 2):
                    nb[depth][rw][cl] = 1

    return nb


board = [[[0]*5 for _ in range(5)] for _ in range(500)]
rw = 0
for line in open("24-input.txt"):
    for cl in range(5):
        board[250][rw][cl] = 1 if line[cl] == "#" else 0
    rw += 1

for _ in range(200):
    board = new_board2(board)

sum = 0
for depth in range(len(board)):
    for rw in range(5):
        for cl in range(5):
            sum += board[depth][rw][cl]
print(sum)
