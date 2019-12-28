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


def build(start, components, sofar, all):
    if len(sofar) > 0:
        all.append(sofar)
    for i, component in enumerate(components):
        if start in component:
            new_components = components.copy()
            del new_components[i]
            if start == component[0]:
                new_start = component[1]
            else:
                new_start = component[0]
            build(new_start, new_components, sofar + [component], bridges)


components = []
for line in open("24-input.txt"):
    ports = tuple(int(n) for n in line.rstrip().split("/"))
    components.append(ports)

bridges = []
build(0, components, [], bridges)

max_strength = 0
max_len = 0
max_len_strength = 0
for bridge in bridges:
    strength = sum(sum(component) for component in bridge)
    if strength > max_strength:
        max_strength = strength
    if len(bridge) > max_len:
        max_len = len(bridge)
        max_len_strength = strength
    if len(bridge) == max_len and strength > max_len_strength:
        max_len_strength = strength
print(max_strength)
print(max_len_strength)
