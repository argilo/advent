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

data = aocd.get_data(day=1, year=2023)

sum = 0
for line in data.splitlines():
    digits = []
    for c in line:
        if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            digits.append(int(c))
    sum += digits[0] * 10 + digits[-1]
print(sum)


dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum = 0
for line in data.splitlines():
    digits = []
    i = 0
    while i < len(line):
        if line[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            digits.append(int(line[i]))
            i += 1
            continue

        found = False
        for text, val in dic.items():
            if line[i:i+len(text)] == text:
                digits.append(val)
                i += 1
                found = True
                break
        if found:
            continue

        i += 1

    sum += digits[0] * 10 + digits[-1]
print(sum)
