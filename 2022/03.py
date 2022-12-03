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

data = aocd.get_data(day=3, year=2022)
# data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""
print(data)

ans = 0
for line in data.split("\n"):
    items = len(line)
    first = line[:items//2]
    second = line[items//2:]
    fs = set(list(first))
    ss = set(list(second))
    common = list(fs & ss)[0]
    if ord('a') <= ord(common) <= ord('z'):
        pri = ord(common) - ord('a') + 1
    elif ord('A') <= ord(common) <= ord('Z'):
        pri = ord(common) - ord('A') + 27
    ans += pri

print(ans)

# aocd.submit(ans, part="a", day=3, year=2022)

lines = data.split("\n")
ans = 0
for n in range(0, len(lines), 3):
    common = set(lines[n]) & set(lines[n+1]) & set(lines[n+2])
    common = list(common)[0]
    if ord('a') <= ord(common) <= ord('z'):
        pri = ord(common) - ord('a') + 1
    elif ord('A') <= ord(common) <= ord('Z'):
        pri = ord(common) - ord('A') + 27
    ans += pri

print(ans)

# aocd.submit(ans, part="b", day=3, year=2022)
