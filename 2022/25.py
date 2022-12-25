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

data = aocd.get_data(day=25, year=2022)


def from_snafu(num):
    ans = 0
    for d in num:
        ans *= 5
        if d == "0":
            ans += 0
        if d == "1":
            ans += 1
        if d == "2":
            ans += 2
        if d == "-":
            ans -= 1
        if d == "=":
            ans -= 2
    return ans


def to_snafu(num):
    ans = ""
    while num > 0:
        d = num % 5
        if d == 3:
            d = -2
            ch = "="
        elif d == 4:
            d = -1
            ch = "-"
        else:
            ch = str(d)
        ans = ch + ans
        num = (num - d) // 5
    return ans


tot = 0
for line in data.split("\n"):
    tot += from_snafu(line)
print(to_snafu(tot))
