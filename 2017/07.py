#!/usr/bin/env python3

# Copyright 2019 Clayton Smith
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

parents = {}
tree = {}
for line in open("07-input.txt"):
    parts = line.rstrip().split(" -> ")
    left_parts = parts[0].split()
    name = left_parts[0]
    weight = int(left_parts[1][1:-1])
    children = []
    if len(parts) > 1:
        for name2 in parts[1].split(", "):
            parents[name2] = name
            children.append(name2)
    tree[name] = (weight, children)

while name in parents:
    name = parents[name]
print(name)


def walk(name):
    weight, children = tree[name]
    if len(children) > 0:
        child_weights = [walk(child) for child in children]
        if min(child_weights) != max(child_weights):
            print(child_weights, children)
        weight += sum(child_weights)
    return weight


walk(name)
print(tree["rfkvap"][0]-9)
