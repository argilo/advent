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


def redist(banks):
    max_len = 0
    max_i = 0
    for i, bank in enumerate(banks):
        if bank > max_len:
            max_len = bank
            max_i = i
    banks[max_i] = 0
    for i in range(max_i + 1, max_i + max_len + 1):
        banks[i % len(banks)] += 1


with open("06-input.txt") as f:
    banks = [int(n) for n in f.read().rstrip().split()]

seen = set()
while tuple(banks) not in seen:
    seen.add(tuple(banks))
    redist(banks)
print(len(seen))

seen = set()
while tuple(banks) not in seen:
    seen.add(tuple(banks))
    redist(banks)
print(len(seen))
