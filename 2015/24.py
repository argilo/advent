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

import itertools

with open("24-input.txt") as f:
    weights = set(int(n) for n in f.read().split())

target = sum(weights) // 3
best = 100000000000000000000
for s in itertools.combinations(weights, 6):
    if sum(s) == target:
        remaining = tuple(weights - set(s))
        for choose in itertools.product((0, 1), repeat=22):
            summ = 0
            for i in range(22):
                if choose[i] == 1:
                    summ += remaining[i]
            if summ == target:
                prod = 1
                for n in s:
                    prod *= n
                if prod < best:
                    best = prod
                break
print(best)

target = sum(weights) // 4
best = 100000000000000000000
for s in itertools.combinations(weights, 5):
    if sum(s) == target:
        remaining = tuple(weights - set(s))
        for choose in itertools.product((0, 1), repeat=22):
            summ = 0
            for i in range(22):
                if choose[i] == 1:
                    summ += remaining[i]
            if summ == target:
                prod = 1
                for n in s:
                    prod *= n
                if prod < best:
                    best = prod
                break
print(best)
