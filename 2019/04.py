#!/usr/bin/env python3

# Copyright 2019 Clayton Smith
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

with open("04-input.txt") as f:
    begin, end = [int(n) for n in f.read().rstrip().split("-")]

ans1 = 0
ans2 = 0
for n in range(begin, end+1):
    digits = [int(d) for d in str(n)]
    if digits == sorted(digits):
        counts = [digits.count(n) for n in range(10)]
        if max(counts) >= 2:
            ans1 += 1
        if 2 in counts:
            ans2 += 1
print(ans1)
print(ans2)
