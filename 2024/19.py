#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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

data = aocd.get_data(day=19, year=2024)

# data = """r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""

available = data.splitlines()[0].split(", ")


@functools.cache
def check(desired):
    if len(desired) == 0:
        return True

    for towel in available:
        if desired.startswith(towel):
            if check(desired[len(towel):]):
                return True

    return False


ans = 0
for desired in data.splitlines()[2:]:
    if check(desired):
        ans += 1

print(ans)
# aocd.submit(ans, part="a", day=19, year=2024)


@functools.cache
def check2(desired):
    if len(desired) == 0:
        return 1

    total = 0
    for towel in available:
        if desired.startswith(towel):
            total += check2(desired[len(towel):])

    return total


ans = 0
for desired in data.splitlines()[2:]:
    ans += check2(desired)

print(ans)
# aocd.submit(ans, part="b", day=19, year=2024)
