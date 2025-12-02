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
DAY = 2

data = aocd.get_data(day=DAY, year=YEAR)
# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

ans = 0
for range_str in data.split(","):
    start, end = [int(n) for n in range_str.split("-")]
    for n in range(start, end+1):
        n_str = str(n)
        l = len(n_str)
        if l % 2 == 1:
            continue
        if n_str[:l//2] == n_str[l//2:]:
            ans += n

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


ans = 0
for range_str in data.split(","):
    start, end = [int(n) for n in range_str.split("-")]
    for n in range(start, end+1):
        n_str = str(n)
        l = len(n_str)
        match = False
        for d in range(1, l):
            if l % d == 0:
                part1 = n_str[:d]
                for x in range(d, l, d):
                    if n_str[x:x+d] != part1:
                        break
                else:
                    match = True
        if match:
            ans += n

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
