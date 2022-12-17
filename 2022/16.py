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
import functools
import itertools
import dijkstar

data = aocd.get_data(day=16, year=2022)

graph = dijkstar.Graph()

valves = {}
num_valves = 0
interesting_valves = []
for line in data.split("\n"):
    parts = line.split(" ")
    valve = parts[1]
    rate = int(parts[4][5:-1])
    if rate > 0:
        num_valves += 1
        interesting_valves.append(valve)
    outs = [out.replace(",", "") for out in parts[9:]]
    valves[valve] = (rate, outs)
    for out in outs:
        graph.add_edge(valve, out, 1)


@functools.cache
def foo(time, loc, open):
    if time == 30:
        return 0

    score = 0
    for valve in open:
        score += valves[valve][0]

    rate = valves[loc][0]
    outs = valves[loc][1]

    best = 0
    if rate > 0 and loc not in open:
        best = foo(time+1, loc, open + (loc,))

    for valve in outs:
        new_score = foo(time+1, valve, open)
        if new_score > best:
            best = new_score

    return score + best


print(foo(0, "AA", tuple()))


@functools.cache
def ccc(start, end):
    return dijkstar.find_path(graph, start, end).total_cost + 1


paths = set()


def foo(time, path, valves):
    paths.add(path)
    pos = path[-1]
    for valve in valves:
        cost = ccc(pos, valve)
        if time + cost <= 26:
            new_valves = tuple(v for v in valves if v != valve)
            foo(time + cost, path + (valve,), new_valves)


foo(0, ("AA",), tuple(interesting_valves))

good_paths = []
for path in paths:
    score = 0
    time = 0
    for a, b in itertools.pairwise(path):
        time += ccc(a, b)
        score += (26 - time) * valves[b][0]
    if score > 800:
        good_paths.append((score, path))

best = 0
for path1 in good_paths:
    for path2 in good_paths:
        if set(path1[1][1:]) & set(path2[1][1:]):
            continue
        else:
            score = path1[0] + path2[0]
            if score > best:
                best = score

print(best)
