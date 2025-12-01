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

data = aocd.get_data(day=1, year=2025)
# data = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""


pos = 50
ans = 0
for line in data.splitlines():
    dir = line[:1]
    num = int(line[1:])
    if dir == "L":
        num = -num
    pos = (pos + num) % 100
    if pos == 0:
        ans += 1

print(ans)
# aocd.submit(ans, part="a", day=1, year=2025)


pos = 50
ans = 0
for line in data.splitlines():
    dir = line[:1]
    num = int(line[1:])
    for _ in range(num):
        if dir == "L":
            pos = (pos - 1) % 100
        else:
            pos = (pos + 1) % 100
        if pos == 0:
            ans += 1

print(ans)
# aocd.submit(ans, part="b", day=1, year=2025)
