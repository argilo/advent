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

data = aocd.get_data(day=10, year=2022)

X = 1
cycle = 0
ans = 0


def check():
    global X, cycle, ans
    if cycle in (20, 60, 100, 140, 180, 220):
        ans += cycle * X


for line in data.split("\n"):
    if line.startswith("addx"):
        op = int(line.split(" ")[1])

        cycle += 1
        check()
        cycle += 1
        check()
        X += op

    elif line == "noop":
        cycle += 1
        check()

print(ans)


X = 1
cycle = 0


def check():
    global X, cycle
    col = (cycle - 1) % 40
    if abs(X - col) <= 1:
        print("#", end="")
    else:
        print(".", end="")
    if col == 39:
        print()


for line in data.split("\n"):
    if line.startswith("addx"):
        op = int(line.split(" ")[1])

        cycle += 1
        check()
        cycle += 1
        check()
        X += op

    elif line == "noop":
        cycle += 1
        check()
