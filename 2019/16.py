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

with open("16-input.txt") as f:
    input = [int(n) for n in list(f.read().rstrip())]

fft_seqs = []
for n in range(1, len(input) + 1):
    seq = []
    while len(seq) < len(input) + 1:
        seq += [0]*n + [1]*n + [0]*n + [-1]*n
    seq = seq[1:len(input) + 1]
    fft_seqs.append(seq)

for phase in range(100):
    input = [abs(sum([a * b for a, b in zip(input, fft_seqs[n])])) % 10 for n in range(len(fft_seqs))]

print("".join([str(d) for d in input[:8]]))


with open("16-input.txt") as f:
    input = [int(n) for n in list(f.read().rstrip())] * 10000

skip = int("".join([str(d) for d in input[0:7]]))
input = input[skip:]

for phase in range(100):
    output = [0]*len(input)
    sum = 0
    for i in range(len(input)-1, -1, -1):
        sum += input[i]
        output[i] = abs(sum) % 10
    input = output

print("".join([str(d) for d in input[:8]]))
