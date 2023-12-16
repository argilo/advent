#!/usr/bin/env python3

# Copyright 2023 Clayton Smith
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

# entering from
LEFT = 1
RIGHT = 2
TOP = 4
BOTTOM = 8

data = aocd.get_data(day=16, year=2023)
# data = """.|...\\....
# |.-.\\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|...."""

rows = data.splitlines()

height = len(rows)
width = len(rows[0])

entering = [[0] * width for _ in range(height)]
entering[0][0] |= LEFT

while True:
    old_entering = copy.deepcopy(entering)
    for r in range(height):
        for c in range(width):
            ent = entering[r][c]
            cell = rows[r][c]

            if ent:
                if cell == ".":
                    if ent & LEFT and c+1 < width:
                        entering[r][c+1] |= LEFT
                    if ent & RIGHT and c-1 >= 0:
                        entering[r][c-1] |= RIGHT
                    if ent & TOP and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & BOTTOM and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                if cell == "|":
                    if ent & (LEFT | RIGHT):
                        if r+1 < height:
                            entering[r+1][c] |= TOP
                        if r-1 >= 0:
                            entering[r-1][c] |= BOTTOM
                    if ent & TOP and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & BOTTOM and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                if cell == "-":
                    if ent & (TOP | BOTTOM):
                        if c+1 < width:
                            entering[r][c+1] |= LEFT
                        if c-1 >= 0:
                            entering[r][c-1] |= RIGHT
                    if ent & LEFT and c+1 < width:
                        entering[r][c+1] |= LEFT
                    if ent & RIGHT and c-1 >= 0:
                        entering[r][c-1] |= RIGHT
                if cell == "/":
                    if ent & LEFT and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                    if ent & RIGHT and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & TOP and c-1 >= 0:
                        entering[r][c-1] |= RIGHT
                    if ent & BOTTOM and c+1 < width:
                        entering[r][c+1] |= LEFT
                if cell == "\\":
                    if ent & LEFT and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & RIGHT and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                    if ent & TOP and c+1 < width:
                        entering[r][c+1] |= LEFT
                    if ent & BOTTOM and c-1 >= 0:
                        entering[r][c-1] |= RIGHT
    if entering == old_entering:
        break

ans = 0
for row in entering:
    for col in row:
        if col > 0:
            ans += 1
print(ans)

# aocd.submit(ans, part="a", day=16, year=2023)

print()
def foo(rows, rr, cc, dir):
    entering = [[0] * width for _ in range(height)]
    entering[rr][cc] |= dir

    changed = []
    changed.append((rr, cc))

    while True:
        old_entering = copy.deepcopy(entering)

        for r, c in changed:
            ent = entering[r][c]
            cell = rows[r][c]

            if ent:
                if cell == ".":
                    if ent & LEFT and c+1 < width:
                        entering[r][c+1] |= LEFT
                    if ent & RIGHT and c-1 >= 0:
                        entering[r][c-1] |= RIGHT
                    if ent & TOP and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & BOTTOM and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                if cell == "|":
                    if ent & (LEFT | RIGHT):
                        if r+1 < height:
                            entering[r+1][c] |= TOP
                        if r-1 >= 0:
                            entering[r-1][c] |= BOTTOM
                    if ent & TOP and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & BOTTOM and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                if cell == "-":
                    if ent & (TOP | BOTTOM):
                        if c+1 < width:
                            entering[r][c+1] |= LEFT
                        if c-1 >= 0:
                            entering[r][c-1] |= RIGHT
                    if ent & LEFT and c+1 < width:
                        entering[r][c+1] |= LEFT
                    if ent & RIGHT and c-1 >= 0:
                        entering[r][c-1] |= RIGHT
                if cell == "/":
                    if ent & LEFT and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                    if ent & RIGHT and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & TOP and c-1 >= 0:
                        entering[r][c-1] |= RIGHT
                    if ent & BOTTOM and c+1 < width:
                        entering[r][c+1] |= LEFT
                if cell == "\\":
                    if ent & LEFT and r+1 < height:
                        entering[r+1][c] |= TOP
                    if ent & RIGHT and r-1 >= 0:
                        entering[r-1][c] |= BOTTOM
                    if ent & TOP and c+1 < width:
                        entering[r][c+1] |= LEFT
                    if ent & BOTTOM and c-1 >= 0:
                        entering[r][c-1] |= RIGHT

        if entering == old_entering:
            break
        changed = []
        for r in range(height):
            for c in range(width):
                if entering[r][c] != old_entering[r][c]:
                    changed.append((r, c))


    ans = 0
    for row in entering:
        for col in row:
            if col > 0:
                ans += 1
    return(ans)

best = 0

for rr in range(height):
    ans = foo(rows, rr, 0, LEFT)
    if ans > best:
        best = ans
        print(best)
    ans = foo(rows, rr, width-1, RIGHT)
    if ans > best:
        best = ans
        print(best)
for cc in range(width):
    ans = foo(rows, 0, cc, TOP)
    if ans > best:
        best = ans
        print(best)
    ans = foo(rows, height-1, cc, BOTTOM)
    if ans > best:
        best = ans
        print(best)


# aocd.submit(ans, part="b", day=16, year=2023)
