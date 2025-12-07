#!/usr/bin/env python3

# Copyright 2025 Clayton Smith
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

YEAR = 2025
DAY = 7

data = aocd.get_data(day=DAY, year=YEAR)
# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

board = data.splitlines()
beams = {board[0].index("S")}

ans = 0
for row in board[1:]:
    for beam in list(beams):
        if row[beam] == "^":
            ans += 1
            beams.remove(beam)
            beams.add(beam - 1)
            beams.add(beam + 1)

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


beams = {}
beams[board[0].index("S")] = 1

for row in board[1:]:
    for beam, n in beams.copy().items():
        if row[beam] == "^":
            ans += n
            del beams[beam]
            beams[beam - 1] = beams.get(beam - 1, 0) + n
            beams[beam + 1] = beams.get(beam + 1, 0) + n

ans = sum(n for n in beams.values())

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
