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

data = aocd.get_data(day=9, year=2020)
lines = data.splitlines()

nums = []
for line in lines:
    nums.append(int(line))

for x in range(25, len(nums)):
    flag = False
    for a, b in itertools.combinations(nums[x-25:x], 2):
        if a+b == nums[x]:
            flag = True
    if not flag:
        ans = nums[x]
        print(ans)

for start in range(0, len(nums)-2):
    for end in range(start+2, len(nums)):
        s = sum(nums[start:end])
        if s == ans:
            print(max(nums[start:end]) + min(nums[start:end]))
