#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=24, year=2022)

lines = data.split("\n")
height = len(lines) - 2
width = len(lines[0]) - 2

blizzards = []
for r, line in enumerate(lines):
    for c, chr in enumerate(line):
        bz = None
        if chr == ">":
            bz = (r-1, c-1, 0, 1)
        elif chr == "<":
            bz = (r-1, c-1, 0, -1)
        elif chr == "^":
            bz = (r-1, c-1, -1, 0)
        elif chr == "v":
            bz = (r-1, c-1, 1, 0)

        if bz is not None:
            blizzards.append(bz)

occupied = set()
for bz in blizzards:
    occupied.add(bz[0:2])

graph = nx.DiGraph()

for time in range(1000):
    new_blizzards = []
    for bz in blizzards:
        r, c, dr, dc = bz
        new_bz = ((r+dr) % height, (c+dc) % width, dr, dc)
        new_blizzards.append(new_bz)

    new_occupied = set()
    for bz in new_blizzards:
        new_occupied.add(bz[0:2])

    graph.add_edge((-1, 0, time), (-1, 0, time+1))
    if (0, 0) not in occupied:
        graph.add_edge((0, 0, time), (-1, 0, time+1))
    if (0, 0) not in new_occupied:
        graph.add_edge((-1, 0, time), (0, 0, time+1))

    for r in range(height):
        for c in range(width):
            if c < width-1 and (r, c) not in occupied and (r, c+1) not in new_occupied:
                graph.add_edge((r, c, time), (r, c+1, time+1))
            if c > 0 and (r, c) not in occupied and (r, c-1) not in new_occupied:
                graph.add_edge((r, c, time), (r, c-1, time+1))
            if r < height-1 and (r, c) not in occupied and (r+1, c) not in new_occupied:
                graph.add_edge((r, c, time), (r+1, c, time+1))
            if r > 0 and (r, c) not in occupied and (r-1, c) not in new_occupied:
                graph.add_edge((r, c, time), (r-1, c, time+1))
            if (r, c) not in occupied and (r, c) not in new_occupied:
                graph.add_edge((r, c, time), (r, c, time+1))

    if (height-1, width-1) not in occupied:
        graph.add_edge((height-1, width-1, time), (height, width-1, time+1))
    if (height-1, width-1) not in new_occupied:
        graph.add_edge((height, width-1, time), (height-1, width-1, time+1))

    try:
        path = nx.shortest_path(graph, source=(-1, 0, 0), target=(height, width-1, time+1))
        print(time+1)
        blizzards = new_blizzards
        occupied = new_occupied
        break
    except:
        blizzards = new_blizzards
        occupied = new_occupied


success_time = time+1
graph = nx.DiGraph()

while True:
    time += 1
    new_blizzards = []
    for bz in blizzards:
        r, c, dr, dc = bz
        new_bz = ((r+dr) % height, (c+dc) % width, dr, dc)
        new_blizzards.append(new_bz)

    new_occupied = set()
    for bz in new_blizzards:
        new_occupied.add(bz[0:2])

    graph.add_edge((-1, 0, time), (-1, 0, time+1))
    if (0, 0) not in occupied:
        graph.add_edge((0, 0, time), (-1, 0, time+1))
    if (0, 0) not in new_occupied:
        graph.add_edge((-1, 0, time), (0, 0, time+1))

    for r in range(height):
        for c in range(width):
            if c < width-1 and (r, c) not in occupied and (r, c+1) not in new_occupied:
                graph.add_edge((r, c, time), (r, c+1, time+1))
            if c > 0 and (r, c) not in occupied and (r, c-1) not in new_occupied:
                graph.add_edge((r, c, time), (r, c-1, time+1))
            if r < height-1 and (r, c) not in occupied and (r+1, c) not in new_occupied:
                graph.add_edge((r, c, time), (r+1, c, time+1))
            if r > 0 and (r, c) not in occupied and (r-1, c) not in new_occupied:
                graph.add_edge((r, c, time), (r-1, c, time+1))
            if (r, c) not in occupied and (r, c) not in new_occupied:
                graph.add_edge((r, c, time), (r, c, time+1))

    if (height-1, width-1) not in occupied:
        graph.add_edge((height-1, width-1, time), (height, width-1, time+1))
    if (height-1, width-1) not in new_occupied:
        graph.add_edge((height, width-1, time), (height-1, width-1, time+1))
    graph.add_edge((height, width-1, time), (height, width-1, time+1))

    try:
        path = nx.shortest_path(graph, source=(height, width-1, success_time), target=(-1, 0, time+1))
        blizzards = new_blizzards
        occupied = new_occupied
        break
    except:
        blizzards = new_blizzards
        occupied = new_occupied

success_time = time+1
graph = nx.DiGraph()

while True:
    time += 1
    new_blizzards = []
    for bz in blizzards:
        r, c, dr, dc = bz
        new_bz = ((r+dr) % height, (c+dc) % width, dr, dc)
        new_blizzards.append(new_bz)

    new_occupied = set()
    for bz in new_blizzards:
        new_occupied.add(bz[0:2])

    graph.add_edge((-1, 0, time), (-1, 0, time+1))
    if (0, 0) not in occupied:
        graph.add_edge((0, 0, time), (-1, 0, time+1))
    if (0, 0) not in new_occupied:
        graph.add_edge((-1, 0, time), (0, 0, time+1))

    for r in range(height):
        for c in range(width):
            if c < width-1 and (r, c) not in occupied and (r, c+1) not in new_occupied:
                graph.add_edge((r, c, time), (r, c+1, time+1))
            if c > 0 and (r, c) not in occupied and (r, c-1) not in new_occupied:
                graph.add_edge((r, c, time), (r, c-1, time+1))
            if r < height-1 and (r, c) not in occupied and (r+1, c) not in new_occupied:
                graph.add_edge((r, c, time), (r+1, c, time+1))
            if r > 0 and (r, c) not in occupied and (r-1, c) not in new_occupied:
                graph.add_edge((r, c, time), (r-1, c, time+1))
            if (r, c) not in occupied and (r, c) not in new_occupied:
                graph.add_edge((r, c, time), (r, c, time+1))

    if (height-1, width-1) not in occupied:
        graph.add_edge((height-1, width-1, time), (height, width-1, time+1))
    if (height-1, width-1) not in new_occupied:
        graph.add_edge((height, width-1, time), (height-1, width-1, time+1))
    graph.add_edge((height, width-1, time), (height, width-1, time+1))

    try:
        path = nx.shortest_path(graph, source=(-1, 0, success_time), target=(height, width-1, time+1))
        print(time+1)
        blizzards = new_blizzards
        occupied = new_occupied
        break
    except:
        blizzards = new_blizzards
        occupied = new_occupied
