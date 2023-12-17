#!/usr/bin/env python3

# Copyright 2023 Clayton Smith
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
import networkx as nx

data = aocd.get_data(day=17, year=2023)

board = [[int(n) for n in line] for line in data.splitlines()]
height = len(board)
width = len(board[0])

# directions
# 0 = down
# 1 = up
# 2 = right
# 3 = left

graph = nx.DiGraph()
for r in range(height):
    if r == 0:
        blocked1 = set([1])
    elif r == height - 1:
        blocked1 = set([0])
    else:
        blocked1 = set()

    for c in range(width):
        if c == 0:
            blocked2 = set([3])
        elif c == width - 1:
            blocked2 = set([2])
        else:
            blocked2 = set()

        for dir in range(4):
            blocked3 = set([dir ^ 1])

            blocked4 = blocked1 | blocked2 | blocked3
            for hist in range(4):
                if hist == 3:
                    blocked4.add(dir)

                for new_dir in range(4):
                    if new_dir not in blocked4:
                        new_r, new_c = r, c
                        if new_dir == 0:
                            new_r += 1
                        elif new_dir == 1:
                            new_r -= 1
                        elif new_dir == 2:
                            new_c += 1
                        elif new_dir == 3:
                            new_c -= 1

                        if new_dir == dir:
                            graph.add_edge((r, c, dir, hist), (new_r, new_c, new_dir, hist+1), weight=board[new_r][new_c])
                        else:
                            graph.add_edge((r, c, dir, hist), (new_r, new_c, new_dir, 1), weight=board[new_r][new_c])

best = 1000000
for dir in range(4):
    for hist in range(4):
        try:
            weight = nx.shortest_path_length(graph, source=(0, 0, 0, 0), target=(height-1, width-1, dir, hist), weight="weight")
            if weight < best:
                best = weight
        except nx.NetworkXNoPath:
            pass
print(best)

# aocd.submit(best, part="a", day=17, year=2023)

graph = nx.DiGraph()
for r in range(height):
    print(r)
    if r == 0:
        blocked1 = set([1])
    elif r == height - 1:
        blocked1 = set([0])
    else:
        blocked1 = set()

    for c in range(width):
        if c == 0:
            blocked2 = set([3])
        elif c == width - 1:
            blocked2 = set([2])
        else:
            blocked2 = set()

        for dir in range(4):
            blocked3 = set([dir ^ 1])

            blocked4 = blocked1 | blocked2 | blocked3
            for hist in range(11):
                if hist == 10:
                    blocked4.add(dir)

                if hist < 4:
                    new_dir = dir
                    if new_dir not in blocked4:
                        new_r, new_c = r, c
                        if new_dir == 0:
                            new_r += 1
                        elif new_dir == 1:
                            new_r -= 1
                        elif new_dir == 2:
                            new_c += 1
                        elif new_dir == 3:
                            new_c -= 1

                        if new_dir == dir:
                            graph.add_edge((r, c, dir, hist), (new_r, new_c, new_dir, hist+1), weight=board[new_r][new_c])
                        else:
                            graph.add_edge((r, c, dir, hist), (new_r, new_c, new_dir, 1), weight=board[new_r][new_c])

                else:
                    for new_dir in range(4):
                        if new_dir not in blocked4:
                            new_r, new_c = r, c
                            if new_dir == 0:
                                new_r += 1
                            elif new_dir == 1:
                                new_r -= 1
                            elif new_dir == 2:
                                new_c += 1
                            elif new_dir == 3:
                                new_c -= 1

                            if new_dir == dir:
                                graph.add_edge((r, c, dir, hist), (new_r, new_c, new_dir, hist+1), weight=board[new_r][new_c])
                            else:
                                graph.add_edge((r, c, dir, hist), (new_r, new_c, new_dir, 1), weight=board[new_r][new_c])

best = 1000000
for dir in range(4):
    print("dir=", dir)
    for hist in range(1, 11):
        print("hist=", hist)
        try:
            weight = nx.shortest_path_length(graph, source=(0, 0, 0, 0), target=(height-1, width-1, dir, hist), weight="weight")
            if weight < best:
                best = weight
        except nx.NetworkXNoPath:
            pass
        try:
            weight = nx.shortest_path_length(graph, source=(0, 0, 2, 0), target=(height-1, width-1, dir, hist), weight="weight")
            if weight < best:
                best = weight
        except nx.NetworkXNoPath:
            pass
print(best)

# aocd.submit(best, part="b", day=17, year=2023)
