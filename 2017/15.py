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

with open("15-input.txt") as f:
    a = int(f.readline().rstrip().split()[-1])
    b = int(f.readline().rstrip().split()[-1])

total = 0
for _ in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if (a & 0xffff) == (b & 0xffff):
        total += 1
print(total)

with open("15-input.txt") as f:
    a = int(f.readline().rstrip().split()[-1])
    b = int(f.readline().rstrip().split()[-1])

total = 0
for _ in range(5000000):
    while True:
        a = (a * 16807) % 2147483647
        if a & 3 == 0:
            break
    while True:
        b = (b * 48271) % 2147483647
        if b & 7 == 0:
            break
    if (a & 0xffff) == (b & 0xffff):
        total += 1
print(total)
