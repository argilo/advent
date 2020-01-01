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


def checksum(s, target_len):
    while len(s) < target_len:
        s = s + "0" + "".join(str(int(c) ^ 1) for c in s[::-1])
    s = s[:target_len]
    while len(s) % 2 == 0:
        s = "".join([str(int(a == b)) for a, b in zip(s[0::2], s[1::2])])
    return s


with open("16-input.txt") as f:
    s = f.read().rstrip()

print(checksum(s, 272))
print(checksum(s, 35651584))
