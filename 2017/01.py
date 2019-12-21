#!/usr/bin/env python3

# Copyright 2019 Clayton Smith
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

with open("01-input.txt") as f:
    data = f.read().rstrip()

data = [int(char) for char in data]

sum = 0
for i in range(len(data)):
    if data[i] == data[(i+1) % len(data)]:
        sum += data[i]
print(sum)

sum = 0
for i in range(len(data)):
    if data[i] == data[(i+len(data)//2) % len(data)]:
        sum += data[i]
print(sum)
