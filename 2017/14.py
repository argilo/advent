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

import dijkstar


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


def knot_hash(inp):
    sparse_hash = permute((list(inp) + [17, 31, 73, 47, 23]) * 64)
    dense_hash = []
    for i in range(16):
        xor = 0
        for j in range(i*16, i*16 + 16):
            xor ^= sparse_hash[j]
        dense_hash.append(xor)
    return bytes(dense_hash)


with open("14-input.txt") as f:
    key = f.read().rstrip()

sum = 0
board = []
for n in range(128):
    row = [int(n) for n in "".join([f"{n:08b}" for n in knot_hash(f"{key}-{n}".encode())])]
    board.append(row)
    sum += row.count(1)
print(sum)

graph = dijkstar.Graph()
vertices = set()
for x in range(128):
    for y in range(128):
        if board[x][y]:
            vertices.add((x, y))
            for (x2, y2) in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
                if 0 <= x2 < 128 and 0 <= y2 < 128 and board[x2][y2]:
                    graph.add_edge((x, y), (x2, y2), 1)
components = 0
while len(vertices) > 0:
    target = min(vertices)
    for n in vertices.copy():
        try:
            dijkstar.find_path(graph, target, n).total_cost
            vertices.remove(n)
        except dijkstar.algorithm.NoPathError:
            pass
    components += 1
print(components)
