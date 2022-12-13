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
import functools

data = aocd.get_data(day=13, year=2022)


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0
    elif isinstance(l, list) and isinstance(r, list):
        while len(l) > 0 and len(r) > 0:
            cmp = compare(l[0], r[0])
            if cmp != 0:
                return cmp
            else:
                l = l[1:]
                r = r[1:]
        if len(l) == 0 and len(r) > 0:
            return -1
        elif len(l) > 0 and len(r) == 0:
            return 1
        else:
            return 0
    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])


n = 1
ans = 0
for pair in data.split("\n\n"):
    l, r = pair.split("\n")
    l = eval(l)
    r = eval(r)
    cmp = compare(l, r)
    if cmp == -1:
        ans += n
    n += 1

print(ans)


packets = [
    [[2]],
    [[6]]
]
for line in data.split("\n"):
    if line != "":
        packets.append(eval(line))
packets.sort(key=functools.cmp_to_key(compare))
n1 = packets.index([[2]]) + 1
n2 = packets.index([[6]]) + 1
ans = n1*n2

print(ans)
