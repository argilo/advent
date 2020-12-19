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

nums = [int(line) for line in aocd.get_data(day=1, year=2020).splitlines()]

for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(nums[i] * nums[j])

for i in range(len(nums) - 2):
    for j in range(i+1, len(nums) - 1):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
