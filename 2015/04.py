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

import hashlib

with open("04-input.txt") as f:
    secret = f.read().rstrip()

number = 1
while True:
    hash = hashlib.md5(f"{secret}{number}".encode()).hexdigest()
    if hash[0:5] == "00000":
        break
    number += 1
print(number)

number = 1
while True:
    hash = hashlib.md5(f"{secret}{number}".encode()).hexdigest()
    if hash[0:6] == "000000":
        break
    number += 1
print(number)
