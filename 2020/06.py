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

lines = aocd.get_data(day=6, year=2020).splitlines() + [""]

total = 0
s = set()
for line in lines:
    if line == "":
        total += len(s)
        s = set()
        continue
    for letter in line:
        s.add(letter)
print(total)

total = 0
s = set([chr(n) for n in range(97, 97+26)])
for line in lines:
    if line == "":
        total += len(s)
        s = set([chr(n) for n in range(97, 97+26)])
        continue
    s2 = set()
    for letter in line:
        s2.add(letter)
    s = s.intersection(s2)
print(total)
