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

data = aocd.get_data(day=2, year=2021)

x = 0
y = 0

for line in data.splitlines():
    dir, n = line.split()
    n = int(n)
    if dir == "down":
        y += n
    elif dir == "up":
        y -= n
    elif dir == "forward":
        x += n
print(x*y)

# aocd.submit(x*y, part="a", day=2, year=2021)

aim = 0
x = 0
y = 0

for line in data.splitlines():
    dir, n = line.split()
    n = int(n)
    if dir == "down":
        aim += n
    elif dir == "up":
        aim -= n
    elif dir == "forward":
        x += n
        y += aim * n
print(x*y)

# aocd.submit(x*y, part="b", day=2, year=2021)
