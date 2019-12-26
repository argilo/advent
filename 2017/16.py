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

with open("16-input.txt") as f:
    moves = f.read().rstrip().split(",")

programs = [chr(97 + n) for n in range(16)]

for i in range(1000000000 % 60):
    for move in moves:
        if move[0] == "s":
            n = int(move[1:])
            programs = programs[-n:] + programs[:-n]
        elif move[0] == "x":
            a, b = [int(n) for n in move[1:].split("/")]
            temp = programs[a]
            programs[a] = programs[b]
            programs[b] = temp
        elif move[0] == "p":
            a, b = [programs.index(n) for n in move[1:].split("/")]
            temp = programs[a]
            programs[a] = programs[b]
            programs[b] = temp
    if i == 0:
        print("".join(programs))
print("".join(programs))
