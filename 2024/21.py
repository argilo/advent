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
import functools
import itertools
import networkx as nx

data = aocd.get_data(day=21, year=2024)

# data = """029A
# 980A
# 179A
# 456A
# 379A"""

numeric = ["789", "456", "123", " 0A"]
num_graph = nx.grid_2d_graph(len(numeric), len(numeric[0]))
num_coords = {}
for r, row in enumerate(numeric):
    for c, col in enumerate(row):
        if col == " ":
            num_graph.remove_node((r, c))
        else:
            num_coords[col] = (r, c)

directional = [" ^A", "<v>"]
dir_graph = nx.grid_2d_graph(len(directional), len(directional[0]))
dir_coords = {}
for r, row in enumerate(directional):
    for c, col in enumerate(row):
        if col == " ":
            dir_graph.remove_node((r, c))
        else:
            dir_coords[col] = (r, c)

direction_symbol = {
    (-1, 0): "^",
    (1, 0): "v",
    (0, -1): "<",
    (0, 1): ">"
}


@functools.cache
def path_cost(depth, max_depth, target):
    if depth == max_depth:
        return len(target)

    if depth == 0:
        keypad_graph = num_graph
        keypad_coords = num_coords
    else:
        keypad_graph = dir_graph
        keypad_coords = dir_coords

    cost = 0
    for source_key, target_key in itertools.pairwise("A" + target):
        option_costs = []
        for path in nx.all_shortest_paths(keypad_graph,
                                          source=keypad_coords[source_key],
                                          target=keypad_coords[target_key]):
            new_target = []
            for (r1, c1), (r2, c2) in itertools.pairwise(path):
                new_target.append(direction_symbol[(r2-r1, c2-c1)])
            new_target = "".join(new_target) + "A"
            option_costs.append(path_cost(depth+1, max_depth, new_target))
        cost += min(option_costs)

    return cost


ans = sum(path_cost(0, 3, code) * int(code[0:3]) for code in data.splitlines())

print(ans)
# aocd.submit(ans, part="a", day=21, year=2024)

ans = sum(path_cost(0, 26, code) * int(code[0:3]) for code in data.splitlines())

print(ans)
# aocd.submit(ans, part="b", day=21, year=2024)
