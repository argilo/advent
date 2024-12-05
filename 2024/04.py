#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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

data = aocd.get_data(day=4, year=2024)

# data = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""

board = data.splitlines()

height = len(board)
width = len(board[0])

ans = 0
for r in range(height):
    for c in range(width):
        for dr in (-1, 0, 1):
            if 0 <= r + dr*3 < height:
                for dc in (-1, 0, 1):
                    if (dr, dc) == (0, 0):
                        continue
                    if 0 <= c + dc*3 < width:
                        word = board[r][c] + board[r+dr][c+dc] + board[r+dr*2][c+dc*2] + board[r+dr*3][c+dc*3]
                        if word == "XMAS":
                            ans += 1
print(ans)
# aocd.submit(ans, part="a", day=4, year=2024)


ans = 0
for r in range(1, height - 1):
    for c in range(1, width - 1):
        if board[r][c] != "A":
            continue
        if (board[r-1][c-1], board[r+1][c+1]) in (("M", "S"), ("S", "M")) and (board[r-1][c+1], board[r+1][c-1]) in (("M", "S"), ("S", "M")):
            ans += 1

print(ans)
# aocd.submit(ans, part="b", day=4, year=2024)
