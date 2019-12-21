#!/usr/bin/env python3

# Copyright 2018 Clayton Smith
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


def reduce(str):
    stack = []
    for byte in str:
        if len(stack) > 0 and stack[-1] == byte ^ 0x20:
            stack.pop()
        else:
            stack.append(byte)
    return len(stack)


with open("05-input.txt", "rb") as f:
    input = f.read().rstrip()

print(reduce(input))

min = len(input)
for byte in range(ord("A"), ord("Z") + 1):
    length = reduce(input.replace(bytes([byte]), bytes())
                         .replace(bytes([byte ^ 0x20]), bytes()))
    if length < min:
        min = length
print(min)
