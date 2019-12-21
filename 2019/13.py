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

import curses
import intcode
import sys

CHARS = [" ", "█", "■", "━", "●"]

with open("13-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]


machine = intcode.execute(prog)
count = 0
while True:
    try:
        x, y, tile_id = next(machine), next(machine), next(machine)
        if tile_id == 2:
            count += 1
    except StopIteration:
        break
print(count)


prog[0] = 2
board = [[0 for _ in range(24)] for _ in range(42)]
score = 0
machine = intcode.execute(prog)
paddle_x = 0
ball_x = 0
stdscr = curses.initscr()
while True:
    try:
        x = next(machine)
        if x is None:
            stdscr.addstr(0, 0, f"Score: {score}")
            for y in range(24):
                for x in range(42):
                    stdscr.addch(y + 1, x, CHARS[board[x][y]])
            stdscr.refresh()

            if paddle_x > ball_x:
                x = machine.send(1)
            elif paddle_x < ball_x:
                x = machine.send(-1)
            else:
                x = machine.send(0)
        y = next(machine)
        tile_id = next(machine)
        if (x, y) == (-1, 0):
            score = tile_id
        else:
            board[x][y] = tile_id
            if tile_id == 3:
                ball_x = x
            elif tile_id == 4:
                paddle_x = x
    except (StopIteration, KeyboardInterrupt):
        break
curses.endwin()
print(score)
