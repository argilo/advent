#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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

data = aocd.get_data(day=10, year=2020)
nums = [int(n) for n in data.splitlines()]
nums.sort()
nums = [0] + nums + [nums[-1] + 3]

ones = 0
threes = 0
for x in range(len(nums)-1):
    if nums[x+1] - nums[x] == 1:
        ones += 1
    elif nums[x+1] - nums[x] == 3:
        threes += 1
ans = ones * threes
print(ans)

# aocd.submit(ans, part="a", day=10, year=2020)

d = {}


def arrangements(ar):
    t = tuple(ar)
    if t in d:
        return d[t]

    if len(ar) == 1:
        return 1

    total = 0
    if len(ar) >= 2:
        total += arrangements(ar[1:])
    if len(ar) >= 3 and ar[2] - ar[0] <= 3:
        total += arrangements(ar[2:])
    if len(ar) >= 4 and ar[3] - ar[0] <= 3:
        total += arrangements(ar[3:])
    d[t] = total
    return total


ans = arrangements(nums)
print(ans)

# aocd.submit(ans, part="b", day=10, year=2020)
