#!/usr/bin/env python3

# Copyright 2025 Clayton Smith
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

YEAR = 2025
DAY = 8

data = aocd.get_data(day=DAY, year=YEAR)
# data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""

boxes = []
for line in data.splitlines():
    x, y, z = [int(n) for n in line.split(",")]
    boxes.append([x, y, z])

count = len(boxes)

dists = []
for i in range(count - 1):
    for j in range(i + 1, count):
        x1, y1, z1 = boxes[i]
        x2, y2, z2 = boxes[j]
        dist = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
        dists.append((dist, i, j))
dists.sort()

graph = nx.Graph()
for i in range(count):
    graph.add_node(i)

n = 0
for _, i, j in dists:
    if j in graph.neighbors(i):
        continue
    else:
        graph.add_edge(i, j)
        n += 1
        if n == 1000:
            break

comps = list(sorted(nx.connected_components(graph), key=len, reverse=True))
ans = len(comps[0]) * len(comps[1]) * len(comps[2])

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


graph = nx.Graph()
for i in range(count):
    graph.add_node(i)

for _, i, j in dists:
    if j in graph.neighbors(i):
        continue
    else:
        graph.add_edge(i, j)
        if len(list(nx.connected_components(graph))) == 1:
            ans = boxes[i][0] * boxes[j][0]
            break

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
