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


def possible(a, b, c):
    return a < b + c and b < a + c and c < a + b


sum = 0
seq1 = []
seq2 = []
seq3 = []
for line in open("03-input.txt"):
    a, b, c = [int(n) for n in line.rstrip().split()]
    if possible(a, b, c):
        sum += 1
    seq1.append(a)
    seq2.append(b)
    seq3.append(c)
print(sum)

seq = seq1 + seq2 + seq3
sum = 0
for x in range(0, len(seq), 3):
    a, b, c = seq[x:x+3]
    if possible(a, b, c):
        sum += 1
print(sum)
