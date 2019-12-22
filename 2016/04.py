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
import string


def checksum(s):
    counts = [(s.count(char), 256-ord(char), char) for char in string.ascii_lowercase]
    counts.sort(reverse=True)
    return "".join([count[2] for count in counts[0:5]])


def decrypt(s, sector):
    plaintext = ""
    for char in s:
        if char == "-":
            plaintext += "-"
        else:
            plaintext += chr(((ord(char)-97 + sector) % 26) + 97)
    return plaintext


sum = 0
pattern = re.compile(r"(.*)-(\d+)\[(.....)\]")
for line in open("04-input.txt"):
    match = pattern.match(line.rstrip())
    ciphertext, sector, check = match[1], int(match[2]), match[3]
    if check == checksum(ciphertext):
        sum += sector
        plaintext = decrypt(ciphertext, sector)
        if plaintext == "northpole-object-storage":
            target_sector = sector
print(sum)
print(target_sector)
