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


def say(s):
    s += "x"
    last_char = None
    seq_len = 0
    output = ""
    for char in s:
        if char == last_char:
            seq_len += 1
        else:
            if last_char is not None:
                output += f"{seq_len}{last_char}"
            seq_len = 1
        last_char = char
    return output


with open("10-input.txt") as f:
    data = f.read().rstrip()

for _ in range(40):
    data = say(data)
print(len(data))

for _ in range(10):
    data = say(data)
print(len(data))
