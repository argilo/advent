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

with open("09-input.txt") as f:
    data = f.read().rstrip()

in_garbage = False
canceled = False
garbage_chars = 0
score = 0
total_score = 0

for char in data:
    if canceled:
        canceled = False
    elif in_garbage:
        if char == ">":
            in_garbage = False
        elif char == "!":
            canceled = True
        else:
            garbage_chars += 1
    else:
        if char == "{":
            score += 1
            total_score += score
        elif char == "}":
            score -= 1
        elif char == "<":
            in_garbage = True
print(total_score)
print(garbage_chars)
