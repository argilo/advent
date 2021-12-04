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

data = aocd.get_data(day=4, year=2021)
#print(data)

# data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
#
#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6
#
# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""

# nums = [int(line) for line in data.splitlines()]
# print(nums)

lines = data.splitlines()

boards = []
boards_checked = []
nums = [int(n) for n in lines[0].split(",")]
print(nums)

for x in range(2, len(lines), 6):
    board = []
    board_checked = []
    for y in range(5):
        board.append([int(n) for n in lines[x + y].split()])
        board_checked.append([False] * 5)
    boards.append(board)
    boards_checked.append(board_checked)

boards_won = [False] * len(boards)
for num in nums:
    print(num)
    i = 0
    for board, board_checked in zip(boards, boards_checked):
        for row in range(5):
            for col in range(5):
                if board[row][col] == num:
                    board_checked[row][col] = True
        for row in range(5):
            tot = sum(board_checked[row])
            if tot == 5:
                win = 0
                for r in range(5):
                    for c in range(5):
                        if not board_checked[r][c]:
                            win += board[r][c]
                if not boards_won[i]:
                    print("won board", i, win * num)
                    boards_won[i] = True
        for col in range(5):
            tot = 0
            for row in range(5):
                if board_checked[row][col]:
                    tot += 1
            if tot == 5:
                win = 0
                for r in range(5):
                    for c in range(5):
                        if not board_checked[r][c]:
                            win += board[r][c]
                if not boards_won[i]:
                    print("won board", i, win * num)
                    boards_won[i] = True
        i += 1

# aocd.submit(ans, part="a", day=4, year=2021)


# aocd.submit(ans, part="b", day=4, year=2021)
