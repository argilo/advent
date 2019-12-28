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

blueprint = {}
with open("25-input.txt") as f:
    state = f.readline().split()[3][:-1]
    steps = int(f.readline().split()[5])
    while len(f.readline()) != 0:
        current_state = f.readline().split()[2][:-1]
        blueprint[current_state] = {}
        for _ in range(2):
            current_value = int(f.readline().split()[5][:-1])
            write = int(f.readline().split()[4][:-1])
            direction = 1 if f.readline().split()[6][:-1] == "right" else -1
            new_state = f.readline().split()[4][:-1]
            blueprint[current_state][current_value] = (write, direction, new_state)

position = 0
tape = {}
for _ in range(steps):
    current_value = tape.get(position, 0)
    write, direction, new_state = blueprint[state][current_value]
    tape[position] = write
    position += direction
    state = new_state
print(sum(tape.values()))
