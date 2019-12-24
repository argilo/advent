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

import dijkstar
import itertools

elevator_start = 1
microchips_start = (1, 3, 3, 3, 3)  # + (1, 1)
generators_start = (1, 2, 2, 2, 2)  # + (1, 1)
objects_start = microchips_start + generators_start
n_microchips = len(microchips_start)


def valid(elevator, objects):
    if elevator not in objects:
        return False
    for i in range(n_microchips):
        if objects[i] != objects[i + n_microchips] and objects[i] in objects[n_microchips:]:
            return False
    return True


def valid_up_moves(elevator, objects):
    objects_avail = [i for i in range(len(objects)) if objects[i] == elevator]
    for obj_indices in itertools.chain(itertools.combinations(objects_avail, 1), itertools.combinations(objects_avail, 2)):
        objects_next = list(objects)
        for i in obj_indices:
            objects_next[i] += 1
        objects_next = tuple(objects_next)
        if valid(elevator+1, objects_next):
            yield (elevator+1, objects_next)


graph = dijkstar.Graph()

for elevator in range(1, 4):
    for objects in itertools.product(range(1, 5), repeat=n_microchips*2):
        if valid(elevator, objects):
            for elevator_next, objects_next in valid_up_moves(elevator, objects):
                graph.add_edge((elevator, objects), (elevator_next, objects_next), 1)
                graph.add_edge((elevator_next, objects_next), (elevator, objects), 1)

print(dijkstar.find_path(graph, (elevator_start, objects_start), (4, (4,)*n_microchips*2)).total_cost)
