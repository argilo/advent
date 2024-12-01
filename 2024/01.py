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

data = aocd.get_data(day=1, year=2024)

# data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

aa = []
bb = []
for line in data.splitlines():
    a, b = line.split()
    a = int(a)
    b = int(b)
    aa.append(a)
    bb.append(b)

aa.sort()
bb.sort()

ans = 0
for a, b in zip(aa, bb):
    ans += abs(a-b)
print(ans)

# aocd.submit(ans, part="a", day=1, year=2024)


ans = 0
for a in aa:
    ans += a * bb.count(a)
print(ans)

# aocd.submit(ans, part="b", day=1, year=2024)
