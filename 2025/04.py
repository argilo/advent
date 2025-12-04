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
DAY = 4

data = aocd.get_data(day=DAY, year=YEAR)
# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

# height = len(data.splitlines())
# width = len(data.splitlines()[0])

rolls = set()
for r, row in enumerate(data.splitlines()):
    for c, col in enumerate(row):
        if col == "@":
            rolls.add((r, c))

ans = 0
for r, c in rolls:
    adj = -1
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (r+dr, c+dc) in rolls:
                adj += 1
    if adj < 4:
        ans += 1

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


rolls = set()
for r, row in enumerate(data.splitlines()):
    for c, col in enumerate(row):
        if col == "@":
            rolls.add((r, c))

ans = 0
while True:
    remove = []
    for r, c in rolls:
        adj = -1
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if (r+dr, c+dc) in rolls:
                    adj += 1
        if adj < 4:
            remove.append((r, c))
            ans += 1

    if not remove:
        break

    for r, c in remove:
        rolls.remove((r, c))

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
