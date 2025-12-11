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
DAY = 11

data = aocd.get_data(day=DAY, year=YEAR)
# data = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out"""

graph = nx.DiGraph()
ways = {}
for line in data.splitlines():
    start, ends = line.split(": ")
    ends = ends.split()
    for end in ends:
        graph.add_edge(start, end)
    ways[start] = 0

for v in nx.topological_sort(graph):
    if v == "you":
        ways[v] = 1
    else:
        ways[v] = sum(ways[i] for i in graph.predecessors(v))
ans = ways["out"]

print(ans)
# aocd.submit(ans, part="a", day=DAY, year=YEAR)


def num_ways(a, b):
    ways = {}
    for v in nx.topological_sort(graph):
        if v == a:
            ways[v] = 1
        else:
            ways[v] = sum(ways[i] for i in graph.predecessors(v))
    return ways[b]


ans = num_ways("svr", "fft") * num_ways("fft", "dac") * num_ways("dac", "out")

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
