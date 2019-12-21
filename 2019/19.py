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

import intcode

with open("19-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]


def pulled(x, y):
    machine = intcode.execute(prog)
    next(machine)
    machine.send(x)
    return machine.send(y)


sum = 0
for y in range(50):
    for x in range(50):
        if pulled(x, y):
            sum += 1
print(sum)

y = 3
ends = [0] * y
start = 0
while True:
    x = start
    while not pulled(x, y):
        x += 1
    start = x
    while pulled(x, y):
        x += 1
    end = x-1
    ends.append(end)

    if y >= 99:
        if start + 99 <= ends[y-99]:
            print(start*10000 + (y-99))
            break

    y += 1
