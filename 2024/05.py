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
from functools import cmp_to_key

data = aocd.get_data(day=5, year=2024)

# data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

first = True
rules = []
ans = 0
for line in data.splitlines():
    if line == "":
        first = False
        continue

    if first:
        parts = line.split("|")
        a, b = int(parts[0]), int(parts[1])
        rules.append((a, b))

    else:
        pages = [int(n) for n in line.split(",")]
        for a, b in rules:
            try:
                ia = pages.index(a)
                ib = pages.index(b)
                if ia > ib:
                    break
            except ValueError:
                pass
        else:
            ans += pages[(len(pages) - 1) // 2]

print(ans)
# aocd.submit(ans, part="a", day=5, year=2024)


first = True
rules = set()


def compare(a, b):
    if (a, b) in rules:
        return -1
    else:
        return 1


ans = 0
for line in data.splitlines():
    if line == "":
        first = False
        continue

    if first:
        parts = line.split("|")
        a, b = int(parts[0]), int(parts[1])
        rules.add((a, b))

    else:
        pages = [int(n) for n in line.split(",")]
        for a, b in rules:
            try:
                ia = pages.index(a)
                ib = pages.index(b)
                if ia > ib:
                    pages.sort(key=cmp_to_key(compare))
                    ans += pages[(len(pages) - 1) // 2]
            except ValueError:
                pass

print(ans)
# aocd.submit(ans, part="b", day=5, year=2024)
