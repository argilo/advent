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
import re

data = aocd.get_data(day=3, year=2024)

#data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
#data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

ans = 0
for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", data):
    a = int(m[1])
    b = int(m[2])
    ans += a*b

print(ans)
#aocd.submit(ans, part="a", day=3, year=2024)


ans = 0
enabled = True
for m in re.finditer(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", data):
    if m[0].startswith("mul"):
        if enabled:
            a = int(m[2])
            b = int(m[3])
            ans += a*b
    elif m[0] == "do()":
        enabled = True
    elif m[0] == "don't()":
        enabled = False

print(ans)
# aocd.submit(ans, part="b", day=3, year=2024)
