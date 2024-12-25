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
import itertools

data = aocd.get_data(day=25, year=2024)

# data = """#####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####"""

schematics = data.split("\n\n")

ans = 0
for s1, s2 in itertools.permutations(schematics, 2):
    s1_lines = s1.splitlines()
    s2_lines = s2.splitlines()
    if s1_lines[0] == "#####" and s2_lines[0] == ".....":
        good = True
        for r1, r2 in zip(s1_lines[1:-1], s2_lines[1:-1]):
            for c1, c2 in zip(r1, r2):
                if c1 == "#" and c2 == "#":
                    good = False
        if good:
            ans += 1

print(ans)
# aocd.submit(ans, part="a", day=25, year=2024)
