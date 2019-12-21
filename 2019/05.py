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


def execute_prog(prog, input):
    machine = intcode.execute(prog)
    next(machine)
    output = machine.send(input)
    while True:
        try:
            output = next(machine)
        except StopIteration as e:
            break
    return output


with open("05-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

print(execute_prog(prog, 1))
print(execute_prog(prog, 5))
