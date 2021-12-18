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


def bits(num):
    if isinstance(num, int):
        return [""]

    arr = []
    left, right = num
    for b in bits(left):
        arr.append("0" + b)
    for b in bits(right):
        arr.append("1" + b)
    return arr


def mag(num):
    if isinstance(num, int):
        return num
    else:
        left, right = num
        return 3*mag(left) + 2*mag(right)


def explode(num):
    bts = bits(num)
    for x in range(len(bts)-1):
        if len(bts[x]) == len(bts[x+1]) == 5 and bts[x][0:4] == bts[x+1][0:4]:

            prev_pointer = None
            pointer = num
            for dir in bts[x][0:4]:
                prev_pointer = pointer
                pointer = pointer[int(dir)]
            left, right = pointer

            prev_pointer[int(dir)] = 0

            if x > 0:
                prev_pointer = None
                pointer = num
                for dir in bts[x-1]:
                    prev_pointer = pointer
                    pointer = pointer[int(dir)]
                prev_pointer[int(dir)] += left

            if x+2 < len(bts):
                prev_pointer = None
                pointer = num
                for dir in bts[x+2]:
                    prev_pointer = pointer
                    pointer = pointer[int(dir)]
                prev_pointer[int(dir)] += right

            return True
    return False


def split(num):
    for b in bits(num):
        prev_pointer = None
        pointer = num
        for dir in b:
            prev_pointer = pointer
            pointer = pointer[int(dir)]
        if pointer >= 10:
            prev_pointer[int(dir)] = [pointer // 2, pointer - (pointer // 2)]
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
