#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=2, year=2022)

games = []
for row in data.split("\n"):
    a = ord(row[0]) - ord("A") + 1
    b = ord(row[2]) - ord("X") + 1
    games.append((a, b))


def score(a, b):
    tot = 0
    if (a, b) in ((1, 2), (2, 3), (3, 1)):
        tot += 6
    elif (a, b) in ((2, 1), (3, 2), (1, 3)):
        tot += 0
    else:
        tot += 3
    tot += b
    return tot


ans = 0
for a, b in games:
    ans += score(a, b)
print(ans)

# aocd.submit(ans, part="a", day=2, year=2022)


def score2(a, out):
    if out == 1:
        b = a - 1
        if b == 0:
            b = 3
    elif out == 2:
        b = a
    else:
        b = a + 1
        if b == 4:
            b = 1

    tot = 0
    if (a, b) in ((1, 2), (2, 3), (3, 1)):
        tot += 6
    elif (a, b) in ((2, 1), (3, 2), (1, 3)):
        tot += 0
    else:
        tot += 3
    tot += b
    return tot


ans = 0
for a, b in games:
    ans += score2(a, b)
print(ans)

# aocd.submit(ans, part="b", day=2, year=2022)
