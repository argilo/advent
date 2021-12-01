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

data = aocd.get_data(day=1, year=2021)
# print(data)

nums = [int(line) for line in data.splitlines()]
# print(nums)

ans = 0
for x in range(0, len(nums)-1):
    if nums[x+1] > nums[x]:
        ans += 1

print(ans)
# aocd.submit(ans, part="a", day=1, year=2021)

ans = 0
for x in range(0, len(nums)-3):
    if nums[x+1] + nums[x+2] + nums[x+3] > nums[x] + nums[x+1] + nums[x+2]:
        ans += 1

print(ans)
# aocd.submit(ans, part="b", day=1, year=2021)
