#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=12, year=2021)
# data = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""
# #
# data = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc"""
# #
# data = """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW"""

conns = {}
tot = 0

for line in data.splitlines():
    c1, c2 = line.split("-")

    if c1 in conns:
        conns[c1].append(c2)
    else:
        conns[c1] = [c2]

    if c2 in conns:
        conns[c2].append(c1)
    else:
        conns[c2] = [c1]

def visit(start, visited):
    global tot
    if start == "end":
        tot += 1
    for c in conns[start]:
        if (c.upper() == c) or (c.lower() == c and c not in visited):
            visit(c, visited + [start])

visit("start", [])
print(tot)

# aocd.submit(ans, part="a", day=12, year=2021)

def can_visit(node, visited):
    if node.upper() == node:
        return True

    if node not in visited:
        return True

    lower_visited = set()
    for v in visited:
        if v.lower() == v:
            if v not in lower_visited:
                lower_visited.add(v)
            else:
                return False

    if node in ["start", "end"]:
        return False
    else:
        return True


conns = {}
tot = 0

for line in data.splitlines():
    c1, c2 = line.split("-")

    if c1 in conns:
        conns[c1].append(c2)
    else:
        conns[c1] = [c2]

    if c2 in conns:
        conns[c2].append(c1)
    else:
        conns[c2] = [c1]

def visit(start, visited):
    global tot
    if start == "end":
        tot += 1

    for c in conns[start]:
        if can_visit(c, visited):
            visit(c, visited + [c])

visit("start", ["start"])
print(tot)

# aocd.submit(ans, part="b", day=12, year=2021)
