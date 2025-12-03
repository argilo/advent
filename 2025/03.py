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
import itertools
import functools

YEAR = 2025
DAY = 3

data = aocd.get_data(day=DAY, year=YEAR)
# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

ans = 0
for line in data.splitlines():
    ans += max(int(a)*10 + int(b) for a, b in itertools.combinations(line, 2))

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


@functools.cache
def best(bank, num):
    if num == 1:
        return max(bank)

    highest = 0
    for i in range(len(bank) - num + 1):
        current = bank[i] * (10**(num-1)) + best(bank[i+1:], num - 1)
        highest = max(current, highest)
    return highest


ans = 0
for line in data.splitlines():
    bank = tuple(int(n) for n in line)
    ans += best(bank, 12)

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
