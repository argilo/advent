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

SIZE=29

data = aocd.get_data(day=19, year=2022)
# data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

@functools.cache
def explore(robots, stock, time):
    global costs

    best = 0
    success = False
    for i, cost in enumerate(costs):
        if cost[0] <= stock[0] and cost[1] <= stock[1] and cost[2] <= stock[2]:
            if i == 0:
                success = True
            if i == 3:
                success = True
            new_stock = tuple(s+r-c for s, r, c in zip(stock, robots, cost))
            if i == 3:
                result = (explore(robots, new_stock, time+1) if time<(SIZE-1) else 0) + (SIZE - time - 1)
            else:
                rl = list(robots)
                rl[i] += 1
                new_robots = tuple(rl)
                result = explore(new_robots, new_stock, time+1) if time<(SIZE-1) else 0
            best = max(result, best)

    if not success:
        result = explore(robots, tuple(s+r for s, r in zip(stock, robots)), time+1) if time<(SIZE-1) else 0
        best = max(result, best)

    return best


total = 0
costs = tuple()
for line in data.split("\n")[0:3]:
    explore.cache_clear()
    parts = line.split(" ")
    bp = int(parts[1][:-1])
    costs = (
        (int(parts[6]), 0, 0),
        (int(parts[12]), 0, 0),
        (int(parts[18]), int(parts[21]), 0),
        (int(parts[27]), 0, int(parts[30])),
    )
    result = explore((1, 0, 0), (0, 0, 0), 0)
    print(bp, result)
    total += (bp * result)
print(total)


# aocd.submit(ans, part="a", day=19, year=2022)


# aocd.submit(ans, part="b", day=19, year=2022)
