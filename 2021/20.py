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

data = aocd.get_data(day=20, year=2021)
# data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
# #..#.
# #....
# ##..#
# ..#..
# ..###"""

iter = 50

lines = data.splitlines()
alg = [0 if c == "." else 1 for c in lines[0]]

image = set()
for row, line in enumerate(data.splitlines()[2:]):
    for col, c in enumerate(line):
        if c == "#":
            image.add((row, col))
min_row = 0 - iter*4
max_row = row + iter*4
min_col = 0 - iter*4
max_col = col + iter*4

for nn in range(iter):
    min_row -= 1
    max_row += 1
    min_col -= 1
    max_col += 1
    new_image = set()
    for row in range(min_row, max_row+1):
        for col in range(min_col, max_col+1):
            num = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    num = num * 2 + ((row + dr, col + dc) in image)
            if alg[num] == 1:
                new_image.add((row, col))
    image = new_image

    tot = 0
    for row in range(min_row + iter*2, max_row - iter*2 + 1):
        for col in range(min_col + iter*2, max_col - iter*2 + 1):
            if (row, col) in image:
                tot += 1
    if nn + 1 in (2, 50):
        print(tot)
