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

data = aocd.get_data(day=3, year=2021)
#print(data)

# data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""

# nums = [int(line) for line in data.splitlines()]
# print(nums)

data = data.splitlines()
ans = ""
ans2 = ""
for x in range(len(data[0])):
    zeroes = 0
    ones = 0
    for row in data:
        if row[x] == "0":
            zeroes += 1
        else:
            ones += 1
    if ones > zeroes:
        ans += "1"
        ans2 += "0"
    else:
        ans += "0"
        ans2 += "1"

ans = int(ans, 2)
ans2 = int(ans2, 2)
print(ans * ans2)
# aocd.submit(ans, part="a", day=3, year=2021)

oxygen_data = data[:]
co2_data = data[:]

for x in range(len(data[0])):
    zeroes = 0
    ones = 0
    for row in oxygen_data:
        if row[x] == "0":
            zeroes += 1
        else:
            ones += 1
    if ones >= zeroes:
        # keep ones for oxygen
        oxygen_data = [row for row in oxygen_data if row[x] == "1"]
    else:
        # keep zeroes for oxygen
        oxygen_data = [row for row in oxygen_data if row[x] == "0"]
    print(oxygen_data)
    if len(oxygen_data) == 1:
        print(oxygen_data)
        ans = int(oxygen_data[0], 2)
        break

for x in range(len(data[0])):
    zeroes = 0
    ones = 0
    for row in co2_data:
        if row[x] == "0":
            zeroes += 1
        else:
            ones += 1
    if ones >= zeroes:
        # keep ones for oxygen
        co2_data = [row for row in co2_data if row[x] == "0"]
    else:
        # keep zeroes for oxygen
        co2_data = [row for row in co2_data if row[x] == "1"]
    print(co2_data)
    if len(co2_data) == 1:
        print(co2_data)
        ans2 = int(co2_data[0], 2)
        break

print(ans, ans2, ans*ans2)
# aocd.submit(ans, part="b", day=3, year=2021)
