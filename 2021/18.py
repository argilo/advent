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

data = aocd.get_data(day=18, year=2021)


def paths(num):
    if isinstance(num, int):
        return [[]]

    arr = []
    left, right = num
    for path in paths(left):
        arr.append([0] + path)
    for path in paths(right):
        arr.append([1] + path)
    return arr


def mag(num):
    if isinstance(num, int):
        return num
    else:
        left, right = num
        return 3*mag(left) + 2*mag(right)


def explode(num):
    p = paths(num)
    for x in range(len(p)-1):
        if len(p[x]) == len(p[x+1]) == 5 and p[x][0:4] == p[x+1][0:4]:

            prev_pointer = None
            pointer = num
            for dir in p[x][0:4]:
                prev_pointer = pointer
                pointer = pointer[dir]
            left, right = pointer

            prev_pointer[dir] = 0

            if x > 0:
                prev_pointer = None
                pointer = num
                for dir in p[x-1]:
                    prev_pointer = pointer
                    pointer = pointer[dir]
                prev_pointer[dir] += left

            if x+2 < len(p):
                prev_pointer = None
                pointer = num
                for dir in p[x+2]:
                    prev_pointer = pointer
                    pointer = pointer[dir]
                prev_pointer[dir] += right

            return True
    return False


def split(num):
    for path in paths(num):
        prev_pointer = None
        pointer = num
        for dir in path:
            prev_pointer = pointer
            pointer = pointer[dir]
        if pointer >= 10:
            prev_pointer[dir] = [pointer // 2, pointer - (pointer // 2)]
            return True
    return False


lines = data.splitlines()
num = eval(lines[0])
while explode(num) or split(num):
    pass

for line in lines[1:]:
    num = [num, eval(line)]

    while explode(num) or split(num):
        pass

print(mag(num))


best = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            continue
        num = [eval(lines[i]), eval(lines[j])]
        while explode(num) or split(num):
            pass
        new_mag = mag(num)
        if new_mag > best:
            best = new_mag
print(best)
