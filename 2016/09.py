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


def decompress_len1(s):
    output_len = 0
    offset = 0
    while offset < len(s):
        if s[offset] == "(":
            offset += 1
            marker = ""
            while s[offset] != ")":
                marker += s[offset]
                offset += 1
            offset += 1
            parts = marker.split("x")
            chars, repeat = int(parts[0]), int(parts[1])
            output_len += chars * repeat
            offset += chars
        else:
            output_len += 1
            offset += 1
    return(output_len)


def decompress_len2(s):
    output_len = 0
    offset = 0
    while offset < len(s):
        if s[offset] == "(":
            offset += 1
            marker = ""
            while s[offset] != ")":
                marker += s[offset]
                offset += 1
            offset += 1
            parts = marker.split("x")
            chars, repeat = int(parts[0]), int(parts[1])
            output_len += decompress_len2(s[offset:offset+chars]) * repeat
            offset += chars
        else:
            output_len += 1
            offset += 1
    return(output_len)


with open("09-input.txt") as f:
    data = f.read().rstrip()

print(decompress_len1(data))
print(decompress_len2(data))
