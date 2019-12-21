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

import intcode
import dijkstar

with open("15-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

NEXT_DIRECTIONS = {
    1: [4, 1, 3, 2],
    2: [3, 2, 4, 1],
    3: [1, 3, 2, 4],
    4: [2, 4, 1, 3],
}

x, y = 0, 0
min_x, max_x, min_y, max_y = 0, 0, 0, 0
last_direction = 1
board = {(0, 0): "."}
graph = dijkstar.Graph()
machine = intcode.execute(prog)

done = False
while not done:
    for direction in NEXT_DIRECTIONS[last_direction]:
        if board.get((x, y), " ") == "#":
            continue

        next(machine)
        status = machine.send(direction)

        next_x, next_y = x, y
        if direction == 1:
            next_y -= 1
        elif direction == 2:
            next_y += 1
        elif direction == 3:
            next_x -= 1
        elif direction == 4:
            next_x += 1

        if next_x < min_x:
            min_x = next_x
        if next_x > max_x:
            max_x = next_x
        if next_y < min_y:
            min_y = next_y
        if next_y > max_y:
            max_y = next_y

        moved = False
        if status == 0:
            board[(next_x, next_y)] = "#"
        elif status == 1:
            board[(next_x, next_y)] = "."
            graph.add_edge((x, y), (next_x, next_y), 1)
            graph.add_edge((next_x, next_y), (x, y), 1)
            x, y = next_x, next_y
            moved = True
            last_direction = direction
        elif status == 2:
            board[(next_x, next_y)] = "O"
            graph.add_edge((x, y), (next_x, next_y), 1)
            graph.add_edge((next_x, next_y), (x, y), 1)
            oxygen_x, oxygen_y = next_x, next_y
            x, y = next_x, next_y
            moved = True
            last_direction = direction

        if moved:
            break

    done = True
    for screen_x, screen_y in board:
        if board[(screen_x, screen_y)] == ".":
            if (screen_x+1, screen_y) not in board:
                done = False
            if (screen_x-1, screen_y) not in board:
                done = False
            if (screen_x, screen_y+1) not in board:
                done = False
            if (screen_x, screen_y-1) not in board:
                done = False

for screen_y in range(min_y, max_y + 1):
    for screen_x in range(min_x, max_x + 1):
        print(board.get((screen_x, screen_y), " "), end="")
    print()

print(dijkstar.find_path(graph, (0, 0), (oxygen_x, oxygen_y)).total_cost)

max_minutes = 0
for screen_y in range(min_y, max_y + 1):
    for screen_x in range(min_x, max_x + 1):
        if board.get((screen_x, screen_y), " ") == ".":
            minutes = dijkstar.find_path(graph, (oxygen_x, oxygen_y), (screen_x, screen_y)).total_cost
            if minutes > max_minutes:
                max_minutes = minutes
print(max_minutes)
