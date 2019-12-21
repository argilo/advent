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


def execute_prog(prog):
    machine = intcode.execute(prog)
    try:
        next(machine)
    except StopIteration as e:
        return e.value


with open("02-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

prog[1] = 12
prog[2] = 2

output = execute_prog(prog)
print(output[0])

for noun in range(100):
    prog[1] = noun
    for verb in range(100):
        prog[2] = verb

        output = execute_prog(prog)
        if output[0] == 19690720:
            print(noun * 100 + verb)
