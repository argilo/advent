#!/usr/bin/env python3

# Copyright 2023 Clayton Smith
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

data = aocd.get_data(day=4, year=2023)
# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

ans = 0
for line in data.splitlines():
    part1, part2 = line.split(": ")
    wins, haves = part2.split(" | ")
    wins = [int(n) for n in wins.split()]
    haves = [int(n) for n in haves.split()]

    match = 0
    for have in haves:
        if have in wins:
            match += 1
    if match >= 1:
        ans += 2**(match - 1)
print(ans)

# aocd.submit(ans, part="a", day=4, year=2023)

copies = [1] * 198
n = 0
for line in data.splitlines():
    part1, part2 = line.split(": ")
    wins, haves = part2.split(" | ")
    wins = [int(n) for n in wins.split()]
    haves = [int(n) for n in haves.split()]

    match = 0
    for have in haves:
        if have in wins:
            match += 1
    for i in range(n+1, n+1+match):
        copies[i] += copies[n]

    n += 1

ans = sum(copies[:n])
print(ans)

# aocd.submit(ans, part="b", day=4, year=2023)
