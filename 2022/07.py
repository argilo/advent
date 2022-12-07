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

data = aocd.get_data(day=7, year=2022)

current_dir = []
tree = dict()
pointer = tree
for line in data.split("\n"):
    if line.startswith("$ cd "):
        dir = line[5:]
        if dir == "/":
            current_dir = []
        elif dir == "..":
            current_dir.pop()
        else:
            current_dir.append(dir)
        pointer = tree
        for x in current_dir:
            pointer = pointer[x]
    elif line.startswith("$ ls"):
        pass
    else:
        size, name = line.split(" ")
        if size == "dir":
            pointer[name] = dict()
        else:
            size = int(size)
            pointer[name] = size

lessthan = 0


def weight(dir, subtree):
    global lessthan
    tot = 0
    for name, subsubtree in subtree.items():
        if isinstance(subsubtree, int):
            tot += subsubtree
        else:
            tot += weight(dir + [name], subsubtree)
    if tot <= 100000:
        lessthan += tot
    return tot


weight([], tree)
print(lessthan)


sizes = []


def weight(dir, subtree):
    global sizes
    tot = 0
    for name, subsubtree in subtree.items():
        if isinstance(subsubtree, int):
            tot += subsubtree
        else:
            tot += weight(dir + [name], subsubtree)
    sizes.append((tot, dir))
    return tot


used = weight([], tree)
sizes.sort()

unused = 70000000 - used
needed = 30000000 - unused

for a, b in sizes:
    if a >= needed:
        print(a)
        break
