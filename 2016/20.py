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

rules = []
for line in open("20-input.txt"):
    start, end = [int(n) for n in line.rstrip().split("-")]
    rules.append([start, end])
rules.sort()

simplified_rules = []
cur_start, cur_end = rules[0]
for start, end in rules[1:]:
    if start <= cur_end + 1 and end > cur_end:
        cur_end = end
    if start > cur_end + 1:
        simplified_rules.append([cur_start, cur_end])
        cur_start, cur_end = start, end
simplified_rules.append([cur_start, cur_end])

print(simplified_rules[0][1] + 1)

allowed = 1 << 32
for start, end in simplified_rules:
    allowed -= (end - start + 1)
print(allowed)
