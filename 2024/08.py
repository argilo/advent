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

data = aocd.get_data(day=8, year=2024)

# data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

height = len(data.splitlines())
width = len(data.splitlines()[0])

antennas = {}
for r, line in enumerate(data.splitlines()):
    for c, letter in enumerate(line):
        if letter == ".":
            continue
        if letter not in antennas:
            antennas[letter] = []
        antennas[letter].append((r, c))

antinodes = {}
for letter, positions in antennas.items():
    for (r1, c1), (r2, c2) in itertools.combinations(positions, 2):
        dr = r2 - r1
        dc = c2 - c1

        ar1 = r1 - dr
        ac1 = c1 - dc

        ar2 = r2 + dr
        ac2 = c2 + dc

        for (ar, ac) in ((ar1, ac1), (ar2, ac2)):
            if 0 <= ar < height and 0 <= ac < width:
                if (ar, ac) not in antinodes:
                    antinodes[(ar, ac)] = []
                antinodes[(ar, ac)].append(letter)

ans = len(antinodes)
print(ans)
# aocd.submit(ans, part="a", day=8, year=2024)


antinodes = {}
for letter, positions in antennas.items():
    for (r1, c1), (r2, c2) in itertools.combinations(positions, 2):
        dr = r2 - r1
        dc = c2 - c1

        for mult in range(height + 1):
            ar1 = r1 - dr * mult
            ac1 = c1 - dc * mult

            ar2 = r2 + dr * mult
            ac2 = c2 + dc * mult

            for (ar, ac) in ((ar1, ac1), (ar2, ac2)):
                if 0 <= ar < height and 0 <= ac < width:
                    if (ar, ac) not in antinodes:
                        antinodes[(ar, ac)] = []
                    antinodes[(ar, ac)].append(letter)

ans = len(antinodes)
print(ans)
# aocd.submit(ans, part="b", day=8, year=2024)
