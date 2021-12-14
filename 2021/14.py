#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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
import collections

data = aocd.get_data(day=14, year=2021)
# data = """NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

lines = data.splitlines()

template = lines[0]

rules = {}
for line in lines[2:]:
    a, b = line.split(" -> ")
    rules[a] = b

quantities = {}
for i in range(len(template)-1):
    pair = template[i:i+2]
    quantities[pair] = quantities.get(pair, 0) + 1

for n in range(40):
    new_quantities = {}
    for k, v in quantities.items():
        pair1 = k[0]
        pair2 = k[1]
        mid = rules[k]
        new_quantities[pair1 + mid] = new_quantities.get(pair1 + mid, 0) + quantities[k]
        new_quantities[mid + pair2] = new_quantities.get(mid + pair2, 0) + quantities[k]
    quantities = new_quantities

    letter_quantities = {}
    for k, v in quantities.items():
        pair1 = k[0]
        pair2 = k[1]
        letter_quantities[pair1] = letter_quantities.get(pair1, 0) + v
        letter_quantities[pair2] = letter_quantities.get(pair2, 0) + v

    max_count = 0
    min_count = 1000000000000000
    for k, v in letter_quantities.items():
        if v > max_count:
            max_count = v
        if v < min_count:
            min_count = v
    print(n+1, (max_count+1) // 2 - (min_count+1) // 2)
