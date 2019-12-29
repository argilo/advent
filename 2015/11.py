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

import re


def succ(s):
    carry = True
    output = [None] * len(s)
    for i in range(len(s)-1, -1, -1):
        c = ord(s[i])
        if carry:
            c += 1
        if c > ord("z"):
            carry = True
            c = ord("a")
        else:
            carry = False
        output[i] = chr(c)
    return "".join(output)


with open("11-input.txt") as f:
    s = f.read().rstrip()

pairs = re.compile(r"(.)\1.*(.)\2")
straight = re.compile(r"(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)")
found = 0
while found < 2:
    s = succ(s)
    if "i" in s or "o" in s or "l" in s:
        continue
    if not pairs.search(s):
        continue
    if not straight.search(s):
        continue
    print(s)
    found += 1
