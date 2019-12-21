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

import intcode

with open("17-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

machine = intcode.execute(prog)
map = []
current_row = ""
for char in machine:
    if char == 10 and len(current_row) > 0:
        map.append(current_row)
        current_row = ""
    else:
        current_row += chr(char)

sum = 0
for r in range(1, len(map) - 1):
    for c in range(1, len(map[r]) - 1):
        if map[r][c-1:c+2] == "###" and map[r-1][c] == map[r+1][c] == "#":
            sum += r * c
print(sum)


def discard_output(machine):
    for char in machine:
        if char is None:
            break


def input_string(machine, string):
    for c in string:
        machine.send(ord(c))
    machine.send(10)


prog[0] = 2
machine = intcode.execute(prog)

discard_output(machine)
input_string(machine, "A,A,B,B,C,B,C,B,C,A")
discard_output(machine)
input_string(machine, "L,10,L,10,R,6")
discard_output(machine)
input_string(machine, "R,12,L,12,L,12")
discard_output(machine)
input_string(machine, "L,6,L,10,R,12,R,12")
discard_output(machine)
input_string(machine, "n")

for char in machine:
    pass
print(char)
