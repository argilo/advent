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

nice = 0
pair = re.compile(r"(.)\1")
for line in open("05-input.txt"):
    line = line.rstrip()
    vowels = line.count("a") + line.count("e") + line.count("i") \
        + line.count("o") + line.count("u")
    bad = line.count("ab") + line.count("cd") + line.count("pq") \
        + line.count("xy")
    if vowels < 3 or bad > 0:
        continue
    if pair.search(line):
        nice += 1
print(nice)

nice = 0
pair = re.compile(r"(..).*\1")
aba = re.compile(r"(.).\1")
for line in open("05-input.txt"):
    if pair.search(line) and aba.search(line):
        nice += 1
print(nice)
