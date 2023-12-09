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

data = aocd.get_data(day=9, year=2023)


def next_nums(nums):
    new_nums = []
    for i in range(len(nums)-1):
        new_nums.append(nums[i+1] - nums[i])
    return new_nums


ans = 0
for line in data.splitlines():
    nums = [int(n) for n in line.split()]
    table = [nums]
    while True:
        new_nums = next_nums(nums)
        table.append(new_nums)
        if new_nums.count(0) == len(new_nums):
            break
        nums = new_nums

    table[-1].append(0)
    for r in range(len(table)-2, -1, -1):
        table[r].append(table[r][-1] + table[r+1][-1])
    ans += table[0][-1]

print(ans)
# aocd.submit(ans, part="a", day=9, year=2023)


ans = 0
for line in data.splitlines():
    nums = [int(n) for n in line.split()]
    table = [nums]
    while True:
        new_nums = next_nums(nums)
        table.append(new_nums)
        if new_nums.count(0) == len(new_nums):
            break
        nums = new_nums

    table[-1].insert(0, 0)
    for r in range(len(table)-2, -1, -1):
        table[r].insert(0, table[r][0] - table[r+1][0])
    ans += table[0][0]

print(ans)
# aocd.submit(ans, part="b", day=9, year=2023)
