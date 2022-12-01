#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=1, year=2022)

elves = []
elf = []
for line in data.splitlines():
    if len(line) > 1:
        cal = int(line)
        elf.append(cal)
    else:
        elves.append(elf)
        elf = []
elves.append(elf)

print(max(sum(elf) for elf in elves))

sums = [sum(elf) for elf in elves]
sums.sort()
print(sum(sums[-3:]))
