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
DAY = 12

data = aocd.get_data(day=DAY, year=YEAR)

lines = data.splitlines()
shapes = []
for i in range(6):
    shapes.append(lines[i*5 + 1:i*5 + 4])

counts = [sum(line.count("#") for line in shape) for shape in shapes]

ans = 0
for line in lines[30:]:
    size, nums = line.split(": ")
    width, length = [int(n) for n in size.split("x")]
    nums = [int(n) for n in nums.split()]

    area = width * length
    occupied = sum(num * count for num, count in zip(nums, counts))
    if occupied > area:
        continue

    area_33 = (width // 3) * (length // 3)
    if sum(nums) <= area_33:
        ans += 1
        continue

    raise Exception("Oh no!")

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


# aocd.submit(ans, part="b", day=DAY, year=YEAR)
