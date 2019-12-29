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

people = set()
pairs = {}
for line in open("13-input.txt"):
    parts = line.split()
    a = parts[0]
    gain = int(parts[3])
    if parts[2] == "lose":
        gain = -gain
    b = parts[10][:-1]
    people.add(a)
    pairs[(a, b)] = gain


def find_best(people, pairs):
    best = 0
    for sitting in itertools.permutations(people):
        sum = 0
        for i in range(len(sitting)):
            j = (i+1) % len(sitting)
            sum += pairs[(sitting[i], sitting[j])]
            sum += pairs[(sitting[j], sitting[i])]
        if sum > best:
            best = sum
    return(best)


print(find_best(people, pairs))

people.add("me")
for person in people:
    pairs["me", person] = 0
    pairs[person, "me"] = 0
print(find_best(people, pairs))
