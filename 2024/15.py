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

data = aocd.get_data(day=15, year=2024)

# data = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# data = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""

# data = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^"""

board = data.split("\n\n")[0].split("\n")
board = [list(row) for row in board]

commands = data.split("\n\n")[1].replace("\n", "")

height = len(board)
width = len(board[0])

dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

for r, row in enumerate(board):
    for c, col in enumerate(row):
        if col == "@":
            robot_r = r
            robot_c = c

for command in commands:
    dir_r, dir_c = dirs[command]

    target_robot_r = robot_r + dir_r
    target_robot_c = robot_c + dir_c

    boxes = 0
    if board[target_robot_r][target_robot_c] == "#":
        new_robot_r = robot_r
        new_robot_c = robot_c
    elif board[target_robot_r][target_robot_c] == ".":
        new_robot_r = target_robot_r
        new_robot_c = target_robot_c
    else:
        box_r = robot_r + dir_r
        box_c = robot_c + dir_c
        while board[box_r][box_c] == "O":
            box_r += dir_r
            box_c += dir_c
            boxes += 1
        if board[box_r][box_c] == "#":
            new_robot_r = robot_r
            new_robot_c = robot_c
        else:
            new_robot_r = target_robot_r
            new_robot_c = target_robot_c

    if (new_robot_r, new_robot_c) != (robot_r, robot_c):
        # print(robot_r, robot_c, new_robot_r, new_robot_c)
        board[robot_r][robot_c] = "."
        board[new_robot_r][new_robot_c] = "@"
        if boxes > 0:
            board[robot_r + dir_r * (boxes + 1)][robot_c + dir_c * (boxes + 1)] = "O"

    robot_r = new_robot_r
    robot_c = new_robot_c

    # print(command)
    # for row in board:
    #     for col in row:
    #         print(col, end="")
    #     print()
    # print()

ans = 0
for r, row in enumerate(board):
    for c, col in enumerate(row):
        if col == "O":
            ans += 100 * r + c

print(ans)
# aocd.submit(ans, part="a", day=15, year=2024)


data = data.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")

board = data.split("\n\n")[0].split("\n")
board = [list(row) for row in board]

commands = data.split("\n\n")[1].replace("\n", "")

height = len(board)
width = len(board[0])

dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

for r, row in enumerate(board):
    for c, col in enumerate(row):
        if col == "@":
            robot_r = r
            robot_c = c

for command in commands:
    dir_r, dir_c = dirs[command]

    target_robot_r = robot_r + dir_r
    target_robot_c = robot_c + dir_c

    boxes_moved = set()
    if board[target_robot_r][target_robot_c] == "#":
        new_robot_r = robot_r
        new_robot_c = robot_c
    elif board[target_robot_r][target_robot_c] == ".":
        new_robot_r = target_robot_r
        new_robot_c = target_robot_c
    else:
        box_r = robot_r + dir_r
        box_c = robot_c + dir_c
        if board[box_r][box_c] == "]":
            box_c -= 1

        if dir_r == 0:
            while board[box_r][box_c] == "[":
                boxes_moved.add((box_r, box_c))
                box_c += dir_c * 2
            if (dir_c == 1 and board[box_r][box_c] == "#") or (dir_c == -1 and board[box_r][box_c + 1] == "#"):
                new_robot_r = robot_r
                new_robot_c = robot_c
            else:
                new_robot_r = target_robot_r
                new_robot_c = target_robot_c
        else:
            new_robot_r = target_robot_r
            new_robot_c = target_robot_c
            boxes_current_row = set([(box_r, box_c)])

            done = False
            while not done:
                boxes_moved = boxes_moved.union(boxes_current_row)
                # print("foo", boxes_moved)
                boxes_next_row = set()
                for box_r, box_c in boxes_current_row:
                    if board[box_r + dir_r][box_c] == "#" or board[box_r + dir_r][box_c + 1] == "#":
                        new_robot_r = robot_r
                        new_robot_c = robot_c
                        done = True
                        break

                    if board[box_r + dir_r][box_c] == "[":
                        boxes_next_row.add((box_r + dir_r, box_c))
                    elif board[box_r + dir_r][box_c] == "]":
                        boxes_next_row.add((box_r + dir_r, box_c - 1))

                    if board[box_r + dir_r][box_c + 1] == "[":
                        boxes_next_row.add((box_r + dir_r, box_c + 1))

                if len(boxes_next_row) == 0:
                    break
                else:
                    boxes_current_row = boxes_next_row

    if (new_robot_r, new_robot_c) != (robot_r, robot_c):
        # print(robot_r, robot_c, new_robot_r, new_robot_c, boxes_moved)
        for box_r, box_c in boxes_moved:
            board[box_r][box_c] = "."
            board[box_r][box_c + 1] = "."
        for box_r, box_c in boxes_moved:
            board[box_r + dir_r][box_c + dir_c] = "["
            board[box_r + dir_r][box_c + dir_c + 1] = "]"
        board[robot_r][robot_c] = "."
        board[new_robot_r][new_robot_c] = "@"

    robot_r = new_robot_r
    robot_c = new_robot_c

    # print(command)
    # for row in board:
    #     for col in row:
    #         print(col, end="")
    #     print()
    # print()

ans = 0
for r, row in enumerate(board):
    for c, col in enumerate(row):
        if col == "[":
            ans += 100 * r + c

print(ans)
aocd.submit(ans, part="b", day=15, year=2024)
