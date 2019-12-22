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

with open("05-input.txt") as f:
    door_id = f.read().rstrip()

number = 0
password = ""
while len(password) < 8:
    hash = hashlib.md5(f"{door_id}{number}".encode()).hexdigest()
    if hash[0:5] == "00000":
        password += hash[5]
    number += 1
print(password)

number = 0
password = [None] * 8
while None in password:
    hash = hashlib.md5(f"{door_id}{number}".encode()).hexdigest()
    if hash[0:5] == "00000":
        pos = hash[5]
        if pos in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            if password[int(pos)] is None:
                password[int(pos)] = hash[6]
    number += 1
print("".join(password))
