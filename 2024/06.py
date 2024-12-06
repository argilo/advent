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

data = aocd.get_data(day=6, year=2024)

# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

board = data.splitlines()

height = len(board)
width = len(board[0])

for r, row in enumerate(board):
    c = row.find("^")
    if c >= 0:
        gr = r
        gc = c
        break

board[gr] = board[gr][:gc] + '.' + board[gr][gc+1:]

visited = set()
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
while True:
    visited.add((gr, gc))
    dr, dc = dirs[dir]
    next_gr = gr + dr
    next_gc = gc + dc
    if 0 <= next_gr < height and 0 <= next_gc < width:
        if board[next_gr][next_gc] == "#":
            dir = (dir + 1) % 4
        else:
            gr = next_gr
            gc = next_gc
    else:
        break


ans = len(visited)
print(ans)
# aocd.submit(ans, part="a", day=6, year=2024)


board = data.splitlines()

height = len(board)
width = len(board[0])

for r, row in enumerate(board):
    c = row.find("^")
    if c >= 0:
        gr = r
        gc = c
        break

board[gr] = board[gr][:gc] + '.' + board[gr][gc+1:]

orig_board = board[:]
orig_gr = gr
orig_gc = gc

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0
for new_r in range(height):
    for new_c in range(width):
        if new_r == orig_gr and new_c == orig_gc:
            continue
        if orig_board[new_r][new_c] == "#":
            continue

        board = orig_board[:new_r] + [orig_board[new_r][:new_c] + "#" + orig_board[new_r][new_c + 1:]] + orig_board[new_r + 1:]
        gr = orig_gr
        gc = orig_gc

        visited = set()
        dir = 0
        while True:
            visited.add((gr, gc, dir))
            dr, dc = dirs[dir]
            next_gr = gr + dr
            next_gc = gc + dc
            if 0 <= next_gr < height and 0 <= next_gc < width:
                if board[next_gr][next_gc] == "#":
                    dir = (dir + 1) % 4
                    if (gr, gc, dir) in visited:
                        ans += 1
                        break
                else:
                    gr = next_gr
                    gc = next_gc
                    if (gr, gc, dir) in visited:
                        ans += 1
                        break
            else:
                break

print(ans)
# aocd.submit(ans, part="b", day=6, year=2024)
