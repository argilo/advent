#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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
import itertools
import networkx as nx

data = aocd.get_data(day=21, year=2024)

# data = """029A
# 980A
# 179A
# 456A
# 379A"""

numeric = ["789", "456", "123", " 0A"]
h_num, w_num = len(numeric), len(numeric[0])
directional = [" ^A", "<v>"]
h_dir, w_dir = len(directional), len(directional[0])

direction_symbol = {
    (-1, 0): "^",
    (1, 0): "v",
    (0, -1): "<",
    (0, 1): ">"
}

num_graph = nx.grid_2d_graph(h_num, w_num)
num_coords = {}
for r, row in enumerate(numeric):
    for c, col in enumerate(row):
        if col == " ":
            num_graph.remove_node((r, c))
        else:
            num_coords[col] = (r, c)

dir_graph = nx.grid_2d_graph(h_dir, w_dir)
dir_coords = {}
for r, row in enumerate(directional):
    for c, col in enumerate(row):
        if col == " ":
            dir_graph.remove_node((r, c))
        else:
            dir_coords[col] = (r, c)


def gen_paths(keypad_graph, keypad_coords, target):
    pos_r, pos_c = keypad_coords["A"]
    piece_choices = []
    for symbol in target:
        choices = []
        target_r, target_c = keypad_coords[symbol]

        for path in nx.all_shortest_paths(keypad_graph, source=(pos_r, pos_c), target=(target_r, target_c)):
            seq = []
            for (r1, c1), (r2, c2) in itertools.pairwise(path):
                seq.append(direction_symbol[(r2-r1, c2-c1)])
            if seq in (sorted(seq), sorted(seq, reverse=True)):
                choices.append("".join(seq + ["A"]))

        if keypad_coords == dir_coords:
            if (pos_r, pos_c, target_r, target_c) == (0, 1, 1, 2):
                choices = ['v>A', '>vA'][0:1]
            if (pos_r, pos_c, target_r, target_c) == (0, 2, 1, 1):
                choices = ['v<A', '<vA'][1:2]
            if (pos_r, pos_c, target_r, target_c) == (1, 1, 0, 2):
                choices = ['^>A', '>^A'][0:1]
            if (pos_r, pos_c, target_r, target_c) == (1, 2, 0, 1):
                choices = ['^<A', '<^A'][1:2]

        piece_choices.append(choices)
        pos_r, pos_c = target_r, target_c

    return itertools.product(*piece_choices)


ans = 0
for code in data.splitlines():
    shortest = 1000000
    for path1 in gen_paths(num_graph, num_coords, code):
        target1 = "".join(path1)
        for path2 in gen_paths(dir_graph, dir_coords, target1):
            target2 = "".join(path2)
            for path3 in gen_paths(dir_graph, dir_coords, target2):
                target3 = "".join(path3)
                if len(target3) < shortest:
                    shortest = len(target3)
    ans += shortest * int(code[0:3])

print(ans)
# aocd.submit(ans, part="a", day=21, year=2024)

ans = 0
for code in data.splitlines():
    shortest = 100000000000000000
    for path1 in gen_paths(num_graph, num_coords, code):
        c = collections.Counter()
        for piece in path1:
            c[piece] += 1

        for _ in range(25):
            new_c = collections.Counter()
            for piece, count in c.items():
                path2 = list(gen_paths(dir_graph, dir_coords, piece))[0]
                for piece2 in path2:
                    new_c[piece2] += count
            c = new_c
    
        total = 0
        for piece, count in c.items():
            total += len(piece) * count
        if total < shortest:
            shortest = total
    
    ans += shortest * int(code[0:3])

print(ans)
# aocd.submit(ans, part="b", day=21, year=2024)
