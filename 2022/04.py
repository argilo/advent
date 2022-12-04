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

data = aocd.get_data(day=4, year=2022)

ans = 0
for row in data.split("\n"):
    part1, part2 = row.split(",")
    a, b = [int(n) for n in part1.split("-")]
    c, d = [int(n) for n in part2.split("-")]

    if c >= a and d <= b:
        ans += 1
    elif a >= c and b <= d:
        ans += 1
print(ans)

# aocd.submit(ans, part="a", day=4, year=2022)

ans = 0
for row in data.split("\n"):
    part1, part2 = row.split(",")
    a, b = [int(n) for n in part1.split("-")]
    c, d = [int(n) for n in part2.split("-")]

    if a <= c <= b or a <= d <= b:
        ans += 1
    elif c <= a <= d or c <= b <= d:
        ans += 1
print(ans)

# aocd.submit(ans, part="b", day=4, year=2022)
