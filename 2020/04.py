#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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

import aocd
import re

valid = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

present = set()
num_valid = 0
for line in aocd.get_data(day=4, year=2020).splitlines():
    if line == "":
        if valid.issubset(present):
            num_valid += 1
        present = set()
    pieces = line.split()
    fields = [piece.split(":")[0] for piece in pieces]
    for field in fields:
        present.add(field)
if valid.issubset(present):
    num_valid += 1
print(num_valid)


present = set()
num_valid = 0
for line in aocd.get_data(day=4, year=2020).splitlines():
    if line == "":
        if valid.issubset(present):
            num_valid += 1
        present = set()
    pieces = line.split()
    fields = [piece.split(":")[0] for piece in pieces]
    values = [piece.split(":")[1] for piece in pieces]
    for field, value in zip(fields, values):
        if field == "byr" and len(value) == 4 and (1920 <= int(value) <= 2002):
            present.add(field)
        elif field == "iyr" and len(value) == 4 and (2010 <= int(value) <= 2020):
            present.add(field)
        elif field == "eyr" and len(value) == 4 and (2020 <= int(value) <= 2030):
            present.add(field)
        elif field == "hgt":
            if value.endswith("cm") and (150 <= int(value[0:-2]) <= 193):
                present.add(field)
            elif value.endswith("in") and (59 <= int(value[0:-2]) <= 76):
                present.add(field)
        elif field == "hcl" and re.match(r"^#[0-9a-f]{6}$", value):
            present.add(field)
        elif field == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            present.add(field)
        elif field == "pid" and re.match(r"^\d{9}$", value):
            present.add(field)
if valid.issubset(present):
    num_valid += 1
print(num_valid)
