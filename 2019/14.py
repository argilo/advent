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


def parse_piece(piece):
    quant, chem = piece.split(" ")
    return (int(quant), chem)


def produce(quant, chem):
    if chem == "ORE":
        return quant

    if chem == "FUEL":
        for c in leftovers:
            leftovers[c] = 0

    reaction = reactions[chem]
    leftover = leftovers[chem]

    if leftover >= quant:
        leftovers[chem] -= quant
        return 0
    else:
        quant -= leftover
        leftovers[chem] = 0

    out_quant, inputs = reaction[0], reaction[1]
    times = (quant + (out_quant - 1)) // out_quant
    leftovers[chem] += (out_quant * times) - quant

    total = 0
    for input in inputs:
        total += produce(input[0] * times, input[1])
    return total


reactions = {}
leftovers = {}
for line in open("14-input.txt"):
    left, right = line.rstrip().split(" => ")
    left = [parse_piece(piece) for piece in left.split(", ")]
    right = parse_piece(right)
    reactions[right[1]] = (right[0], left)
    leftovers[right[1]] = 0


print(produce(1, "FUEL"))


lower = 0
upper = 1000000000000
while lower < upper:
    mid = (lower + upper) // 2
    if produce(mid, "FUEL") > 1000000000000:
        upper = mid - 1
    else:
        lower = mid
    if produce(mid + 1, "FUEL") > 1000000000000:
        upper = mid
print(lower)
