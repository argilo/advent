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

data = aocd.get_data(day=23, year=2020)
cups = [int(n) for n in list(data)]

for _ in range(100):
    current_cup = cups[0]
    left = cups[0:1] + cups[4:]

    dest_cup = current_cup
    while True:
        dest_cup -= 1
        if dest_cup < 1:
            dest_cup = 9
        if dest_cup in left:
            break

    index = left.index(dest_cup)
    cups = left[:index+1] + cups[1:4] + left[index+1:]
    cups = cups[1:] + cups[:1]

index = cups.index(1)
cups = cups[index:] + cups[:index]
print("".join(str(n) for n in cups[1:]))


data = aocd.get_data(day=23, year=2020)
cups = [int(n) for n in list(data)] + list(range(10, 1000001))

dict = {}
prev = cups[-1]
for cup in cups:
    dict[prev] = cup
    prev = cup

current_cup = cups[0]
for _ in range(10000000):
    taken = (dict[current_cup], dict[dict[current_cup]], dict[dict[dict[current_cup]]])
    dict[current_cup] = dict[dict[dict[dict[current_cup]]]]

    dest_cup = current_cup
    while True:
        dest_cup -= 1
        if dest_cup < 1:
            dest_cup = 1000000
        if dest_cup not in taken:
            break

    dict[taken[2]] = dict[dest_cup]
    dict[dest_cup] = taken[0]
    current_cup = dict[current_cup]

print(dict[1] * dict[dict[1]])
