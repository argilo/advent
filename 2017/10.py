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


def permute(lengths):
    lst_len = 256
    lst = list(range(lst_len))
    skip_size = 0
    skipped = 0

    for length in lengths:
        lst = lst[:length][::-1] + lst[length:]
        skip = (length + skip_size) % lst_len
        lst = lst[skip:] + lst[:skip]
        skipped = (skipped + skip) % lst_len
        skip_size += 1

    return lst[-skipped % lst_len:] + lst[:-skipped % lst_len]


with open("10-input.txt") as f:
    lengths = [int(n) for n in f.read().rstrip().split(",")]

permuted = permute(lengths)
print(permuted[0] * permuted[1])


with open("10-input.txt", "rb") as f:
    lengths = (list(f.read().rstrip()) + [17, 31, 73, 47, 23]) * 64

sparse_hash = permute(lengths)
dense_hash = []
for i in range(16):
    xor = 0
    for j in range(i*16, i*16 + 16):
        xor ^= sparse_hash[j]
    dense_hash.append(xor)
print(bytes(dense_hash).hex())
