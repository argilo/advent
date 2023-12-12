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
import functools

data = aocd.get_data(day=12, year=2023)


@functools.cache
def explore(cond, nums):
    num = nums[0]
    l = len(cond)
    ans = 0
    for i in range(l - num + 1):
        if "#" not in cond[:i] and "." not in cond[i:i+num]:
            if len(nums) > 1 and i+num+1 < len(cond) and cond[i+num] != "#":
                ans += explore(cond[i+num+1:], nums[1:])
            elif len(nums) == 1 and "#" not in cond[i+num:]:
                ans += 1
    return ans


ans = 0
for line in data.splitlines():
    cond, nums = line.split()
    nums = tuple([int(n) for n in nums.split(",")])
    e = explore(cond, nums)
    ans += e
print(ans)

# aocd.submit(ans, part="a", day=12, year=2023)

ans = 0
for line in data.splitlines():
    cond, nums = line.split()
    nums = tuple([int(n) for n in nums.split(",")])
    cond = cond + "," + cond + "," + cond + "," + cond + "," + cond
    nums = nums * 5
    e = explore(cond, nums)
    ans += e
print(ans)

# aocd.submit(ans, part="b", day=12, year=2023)
