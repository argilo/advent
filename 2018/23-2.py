#!/usr/bin/env python3

import collections
import re
import z3

Nanobot = collections.namedtuple("Nanobot", ["x", "y", "z", "r"])
nanobots = []
for line in open("23-input.txt"):
    match = re.compile(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)").match(line)
    nanobots.append(Nanobot(int(match[1]), int(match[2]), int(match[3]), int(match[4])))


def zabs(x):
    return z3.If(x >= 0, x, -x)


x, y, z = z3.Int("x"), z3.Int("y"), z3.Int("z")
in_ranges = [z3.Int(f"in_range_{i}") for i in range(len(nanobots))]
range_count = z3.Int("range_count")
dist_from_zero = z3.Int("dist_from_zero")

o = z3.Optimize()

for i, bot in enumerate(nanobots):
    o.add(in_ranges[i] == z3.If(zabs(x - bot.x) + zabs(y - bot.y) + zabs(z - bot.z) <= bot.r, 1, 0))

o.add(range_count == sum(in_ranges))
o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))

h1 = o.maximize(range_count)
h2 = o.minimize(dist_from_zero)
o.check()
print(o.model()[x], o.model()[y], o.model()[z])
print(o.model()[range_count])
print(o.model()[dist_from_zero])
