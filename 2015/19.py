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

import random
import re

el = re.compile(r"([A-Z][a-z]?|e)")


def elements(s):
    return list(el.findall(s))


def outputs(s, replacements):
    result = set()
    for left, rights in replacements.items():
        for m in re.finditer(left, s):
            for right in rights:
                new = s[0:m.start()] + right + s[m.end():]
                result.add(new)
    return result


def search(s, n, target, replacements):
    if s == target:
        return n
    else:
        out = outputs(s, replacements)
        if out:
            return search(random.choice(list(out)), n+1, target, replacements)
        else:
            return None


replacements1 = {}
replacements2 = {}
with open("19-input.txt") as f:
    seen_l, seen_r = [], []
    while True:
        line = f.readline().rstrip()
        if not line:
            break
        left, right = line.split(" => ")
        if left not in replacements1:
            replacements1[left] = []
        if right not in replacements2:
            replacements2[right] = []
        replacements1[left].append(right)
        replacements2[right].append(left)
    target = f.readline().rstrip()

print(len(outputs(target, replacements1)))

steps = None
while not steps:
    steps = search(target, 0, "e", replacements2)
print(steps)
