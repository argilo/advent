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

data = aocd.get_data(day=10, year=2024)

# data = """0123
# 1234
# 8765
# 9876"""

# data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

board = [[int(n) for n in row] for row in data.splitlines()]

height = len(board)
width = len(board[0])

ans = 0
for r in range(height):
    for c in range(width):
        if board[r][c] == 0:
            positions = set([(r, c)])
            for n in range(1, 10):
                new_positions = set()
                for cur_r, cur_c in positions:
                    for dir_r, dir_c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        new_r, new_c = cur_r + dir_r, cur_c + dir_c
                        if 0 <= new_r < height and 0 <= new_c < width and board[new_r][new_c] == n:
                            new_positions.add((new_r, new_c))
                positions = new_positions
            ans += len(positions)

print(ans)
# aocd.submit(ans, part="a", day=10, year=2024)


ans = 0
for r in range(height):
    for c in range(width):
        if board[r][c] == 0:
            positions = set([(r, c)])
            for n in range(1, 10):
                new_positions = []
                for cur_r, cur_c in positions:
                    for dir_r, dir_c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        new_r, new_c = cur_r + dir_r, cur_c + dir_c
                        if 0 <= new_r < height and 0 <= new_c < width and board[new_r][new_c] == n:
                            new_positions.append((new_r, new_c))
                positions = new_positions
            ans += len(positions)

print(ans)
# aocd.submit(ans, part="b", day=10, year=2024)
