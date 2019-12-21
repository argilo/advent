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

script1 = """
NOT C J
AND D J
NOT A T
OR T J
""".strip()

script2 = """
NOT T J
AND B J
AND C J
NOT J J
OR E T
OR H T
AND T J
AND D J
NOT A T
OR T J
""".strip()


def read_output(machine):
    s = ""
    for char in machine:
        if char is None:
            break
        if char >= 256:
            return char
        s += chr(char)
    return s


def input_string(machine, string):
    for c in string:
        machine.send(ord(c))
    machine.send(10)


with open("21-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

machine = intcode.execute(prog)
read_output(machine)
input_string(machine, script1)
input_string(machine, "WALK")
print(read_output(machine))

machine = intcode.execute(prog)
read_output(machine)
input_string(machine, script2)
input_string(machine, "RUN")
print(read_output(machine))
