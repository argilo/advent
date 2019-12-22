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


def calc(kit, out):
    if out in cache:
        return cache[out]

    try:
        result = int(out)
    except ValueError:
        op, arg1, arg2 = kit[out]
        if op is None:
            result = calc(kit, arg2)
        elif op == "NOT":
            result = calc(kit, arg2) ^ 0xffff
        elif op == "AND":
            result = calc(kit, arg1) & calc(kit, arg2)
        elif op == "OR":
            result = calc(kit, arg1) | calc(kit, arg2)
        elif op == "LSHIFT":
            result = (calc(kit, arg1) << calc(kit, arg2)) & 0xffff
        elif op == "RSHIFT":
            result = (calc(kit, arg1) >> calc(kit, arg2)) & 0xffff

    cache[out] = result
    return result


pattern = re.compile(r"(([a-z0-9]*) )?(([A-Z]*) )?([a-z0-9]*) -> ([a-z]*)")
kit = {}
cache = {}
for line in open("07-input.txt"):
    match = pattern.match(line.rstrip())
    arg1, op, arg2, out = match[2], match[4], match[5], match[6]
    kit[out] = (op, arg1, arg2)
a_out = calc(kit, "a")
print(a_out)

cache = {}
kit["b"] = (None, None, str(a_out))
print(calc(kit, "a"))
