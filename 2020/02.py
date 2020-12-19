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

total = 0
for line in open("02-input.txt"):
    line = line.rstrip().split()
    low, high = [int(n) for n in line[0].split("-")]
    letter = line[1].split(":")[0]
    password = line[2]
    if low <= password.count(letter) <= high:
        total += 1
print(total)

total = 0
for line in open("02-input.txt"):
    line = line.rstrip().split()
    first, second = [int(n) for n in line[0].split("-")]
    letter = line[1].split(":")[0]
    password = line[2]
    if (password[first-1] == letter) ^ (password[second-1] == letter):
        total += 1
print(total)
