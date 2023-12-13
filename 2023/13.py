#!/usr/bin/env python3

# Copyright 2023 Clayton Smith
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

data = aocd.get_data(day=13, year=2023)

ans = 0
for puzzle in data.strip().split("\n\n"):
    rows = puzzle.splitlines()
    width = len(rows[0])
    for c in range(1, width):
        room = min(c, width - c)
        for row in rows:
            if row[c-room:c] != row[c:c+room][::-1]:
                break
        else:
            ans += c

    height = len(rows)
    for r in range(1, height):
        room = min(r, height - r)
        for n in range(room):
            if rows[r - 1 - n] != rows[r + n]:
                break
        else:
            ans += 100*r

print(ans)
# aocd.submit(ans, part="a", day=13, year=2023)


def solve(rows, bad=None):
    width = len(rows[0])
    for c in range(1, width):
        room = min(c, width - c)
        for row in rows:
            if row[c-room:c] != row[c:c+room][::-1]:
                break
        else:
            if c != bad:
                return c

    height = len(rows)
    for r in range(1, height):
        room = min(r, height - r)
        for n in range(room):
            if rows[r - 1 - n] != rows[r + n]:
                break
        else:
            if 100*r != bad:
                return 100*r

    return None


ans = 0
for puzzle in data.strip().split("\n\n"):
    rows = [list(r) for r in puzzle.splitlines()]
    bad = solve(rows)
    done = False
    for r in range(len(rows)):
        for c in range(len(rows[0])):
            old = rows[r][c]
            rows[r][c] = "#" if old == "." else "."
            foo = solve(rows, bad)
            if foo and not done:
                ans += foo
                done = True
            rows[r][c] = old

print(ans)
# aocd.submit(ans, part="b", day=13, year=2023)
