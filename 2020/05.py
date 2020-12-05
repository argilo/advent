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

ids = []
for line in open("05-input.txt"):
    line = line.rstrip()
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    id = row*8 + col
    ids.append(id)
ids.sort()

print(ids[-1])

for x in range(ids[0], ids[-1] + 1):
    if x not in ids:
        print(x)
