#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=7, year=2021)
#data = "16,1,2,0,4,2,7,1,2,14"
nums = [int(n) for n in data.split(",")]
nums.sort()

best = 1000000000

for i in range(min(nums), max(nums)+1):
    tot = 0
    for num in nums:
        tot += abs(num-i)
    if tot < best:
        print(i, tot)
        best = tot


def cost(a, b):
    dist = abs(a-b)
    return dist * (dist+1) // 2

best = 1000000000000

for i in range(min(nums), max(nums)+1):
    tot = 0
    for num in nums:
        tot += cost(num, i)
    if tot < best:
        print(i, tot)
        best = tot
