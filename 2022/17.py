#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=17, year=2022)
#data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

pieces = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]


tower = []
piece_num = 0
move_num = 0
for _ in range(2022):
    piece = pieces[piece_num]
    piece_num = (piece_num + 1) % len(pieces)

    r, c = len(tower) + 3, 2

    while True:
        move = data[move_num]
        move_num = (move_num + 1) % len(data)

        if move == ">":
            next_c = c+1
        elif move == "<":
            next_c = c-1

        for pr, pc in piece:
            if next_c + pc < 0 or next_c + pc >= 7:
                next_c = c
                break
            if r + pr < len(tower) and tower[r + pr][next_c + pc] == 1:
                next_c = c
                break

        c = next_c

        next_r = r-1
        stopped = False
        if next_r < 0:
            next_r = r
            stopped = True
        else:
            for pr, pc in piece:
                if next_r + pr < len(tower) and tower[next_r + pr][c + pc] == 1:
                    next_r = r
                    stopped = True
                    break

        r = next_r

        if stopped:
            for pr, pc in piece:
                if len(tower) < r + pr + 1:
                    tower.append([0] * 7)
                tower[r + pr][c + pc] = 1
            break

print(len(tower))

# aocd.submit(ans, part="a", day=17, year=2022)

# formula:
# >>> ((1000000000000 - 3407) // 1700) * 2642
# 1554117641464 + 5305 + 2964 - 2663 = 1554117647070


tower = []
piece_num = 0
move_num = 0
#print(len(data))
last_ans = 0
for z in range(1707+193):
    if move_num == 2:
        print(z, piece_num, len(tower), len(tower) - last_ans)
        last_ans = len(tower)

    piece = pieces[piece_num]
    piece_num = (piece_num + 1) % len(pieces)

    r, c = len(tower) + 3, 2

    while True:
        move = data[move_num]
        move_num = (move_num + 1) % len(data)

        if move == ">":
            next_c = c+1
        elif move == "<":
            next_c = c-1

        for pr, pc in piece:
            if next_c + pc < 0 or next_c + pc >= 7:
                next_c = c
                break
            if r + pr < len(tower) and tower[r + pr][next_c + pc] == 1:
                next_c = c
                break

        c = next_c

        next_r = r-1
        stopped = False
        if next_r < 0:
            next_r = r
            stopped = True
        else:
            for pr, pc in piece:
                if next_r + pr < len(tower) and tower[next_r + pr][c + pc] == 1:
                    next_r = r
                    stopped = True
                    break

        r = next_r

        if stopped:
            for pr, pc in piece:
                if len(tower) < r + pr + 1:
                    tower.append([0] * 7)
                tower[r + pr][c + pc] = 1
            break

print(len(tower))

# aocd.submit(ans, part="b", day=17, year=2022)
