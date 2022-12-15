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

data = aocd.get_data(day=15, year=2022)


dat = []
for line in data.split("\n"):
    parts = line.split(" ")
    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])
    dat.append((sx, sy, bx, by))

ty = 2000000

cannot = set()
for sx, sy, bx, by in dat:
    dist = abs(bx-sx) + abs(by-sy)
    disty = abs(ty-sy)
    if disty <= dist:
        minx = sx - (dist - disty)
        maxx = sx + (dist - disty)
        for x in range(minx, maxx+1):
            if ty == by and x == bx:
                continue
            cannot.add(x)
ans = len(cannot)
print(ans)


limit = 4000000

for ty in range(limit + 1):
    cannot_intervals = []
    for sx, sy, bx, by in dat:
        dist = abs(bx-sx) + abs(by-sy)
        disty = abs(ty-sy)
        if disty <= dist:
            minx = max(sx - (dist - disty), 0)
            maxx = min(sx + (dist - disty), limit)
            cannot_intervals.append((minx, maxx))
    cannot_intervals.sort()

    current = -1
    highest = -1
    for s, e in cannot_intervals:
        if s > highest+1:
            print(ty + 4000000*(current+1))
            exit()
        highest = max(highest, e)
        current = e
