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

tree = {}

for line in open("06-input.txt"):
    a, b = line.rstrip().split(")")
    tree[b] = a


def path(tree, a):
    path = []
    while True:
        path.append(a)
        if tree[a] == "COM":
            break
        a = tree[a]
    return path


count = 0
for k, v in tree.items():
    p = path(tree, k)
    count += len(p)
print(count)

p1 = path(tree, "YOU")
p2 = path(tree, "SAN")
while p1[-1] == p2[-1]:
    p1 = p1[:-1]
    p2 = p2[:-1]
print(len(p1) + len(p2) - 2)
