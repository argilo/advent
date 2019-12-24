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
import re


def hash1(salt, number):
    return hashlib.md5(f"{salt}{number}".encode()).hexdigest()


def hash2(salt, number):
    hash = hashlib.md5(f"{salt}{number}".encode()).hexdigest()
    for _ in range(2016):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash


def answer(hashes):
    triple = re.compile(r"(.)\1\1")
    number = 0
    numbers = []
    while len(numbers) < 64:
        hash = hashes[number]
        m = triple.search(hash)
        if m:
            for number2 in range(number+1, number+1001):
                hash = hashes[number2]
                if m[1]*5 in hash:
                    numbers.append(number)
                    break
        number += 1
    return numbers[-1]


with open("14-input.txt") as f:
    salt = f.read().rstrip()

hashes = [hash1(salt, n) for n in range(40000)]
print(answer(hashes))
hashes = [hash2(salt, n) for n in range(25000)]
print(answer(hashes))
