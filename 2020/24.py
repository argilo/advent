#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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

data = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
data = aocd.get_data(day=24, year=2020)

black = set()
for line in data.splitlines():
    x, y = 0, 0

    dir = ""
    for c in line:
        dir += c
        if dir == "e":
            x += 1
            dir = ""
        elif dir == "w":
            x -= 1
            dir = ""
        elif dir == "ne":
            y -= 1
            x += 1
            dir = ""
        elif dir == "nw":
            y -= 1
            dir = ""
        elif dir == "se":
            y += 1
            dir = ""
        elif dir == "sw":
            y += 1
            x -= 1
            dir = ""

    if (x, y) in black:
        black.remove((x, y))
    else:
        black.add((x, y))
print(len(black))


for _ in range(100):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    new_black = set()

    for (x, y) in black:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            num_adj = 0
            adj = [(x+1, y), (x-1, y), (x+1, y-1), (x, y-1), (x, y+1), (x-1, y+1)]
            for a in adj:
                if a in black:
                    num_adj += 1
            if (x, y) in black:
                if num_adj == 0 or num_adj > 2:
                    pass
                else:
                    new_black.add((x, y))
            else:
                if num_adj == 2:
                    new_black.add((x, y))
                else:
                    pass
    black = new_black
print(len(black))
