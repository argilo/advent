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

data = aocd.get_data(day=2, year=2024)

# data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

ans = 0
for line in data.splitlines():
    report = [int(n) for n in line.split()]
    safe = True

    diffs = []
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        diffs.append(diff)
        if diff not in [-3, -2, -1, 1, 2, 3]:
            safe = False

    if safe:
        if min(diffs) > 0 or max(diffs) < 0:
            ans += 1

print(ans)
# aocd.submit(ans, part="a", day=2, year=2024)


def is_safe(report):
    safe = True

    diffs = []
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        diffs.append(diff)
        if diff not in [-3, -2, -1, 1, 2, 3]:
            safe = False

    if safe:
        if min(diffs) > 0 or max(diffs) < 0:
            return True
    
    return False


ans = 0
for line in data.splitlines():
    report = [int(n) for n in line.split()]
    safe = is_safe(report)
    if (safe):
        ans += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                ans += 1
                break

print(ans)
# aocd.submit(ans, part="b", day=2, year=2024)
