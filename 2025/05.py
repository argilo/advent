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
DAY = 5

data = aocd.get_data(day=DAY, year=YEAR)
# data = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""

fresh, avail = data.split("\n\n")

ranges = []
for line in fresh.splitlines():
    a, b = [int(n) for n in line.split("-")]
    ranges.append((a, b))

ans = 0
for line in avail.splitlines():
    n = int(line)
    if any((n in range(a, b+1)) for a, b in ranges):
        ans += 1

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


ranges = []
for line in fresh.splitlines():
    a, b = [int(n) for n in line.split("-")]
    ranges.append((a, b))
ranges.sort()

ans = 0
highest = 0
for a, b in ranges:
    if a > highest:
        ans += (b - a + 1)
    else:
        if b < highest:
            pass
        else:
            ans += (b - highest)
    highest = max(highest, b)

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
