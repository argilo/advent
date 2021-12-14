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
import numpy

data = aocd.get_data(day=14, year=2021)

lines = data.splitlines()
template = lines[0]

rules = {}
for line in lines[2:]:
    a, b = line.split(" -> ")
    rules[a] = (a[0] + b, b + a[1])

keys = list(rules.keys())
n_keys = len(keys)
matrix = numpy.zeros((n_keys, n_keys), dtype=int)

for k, v in rules.items():
    index_k = keys.index(k)
    matrix[index_k][keys.index(v[0])] = 1
    matrix[index_k][keys.index(v[1])] = 1

vector = numpy.zeros(n_keys, dtype=int)
for i in range(len(template)-1):
    vector[keys.index(template[i:i+2])] += 1

for n in (10, 40):
    result = vector.dot(numpy.linalg.matrix_power(matrix, n))

    letter_count = {}
    for i, key in enumerate(keys):
        letter_count[key[0]] = letter_count.get(key[0], 0) + result[i]
        letter_count[key[1]] = letter_count.get(key[1], 0) + result[i]
    letter_count[template[0]] += 1
    letter_count[template[-1]] += 1

    max_count = max(letter_count.values()) // 2
    min_count = min(letter_count.values()) // 2
    print(n, max_count - min_count)
