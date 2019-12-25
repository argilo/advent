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
import itertools

script = """
east
take loom
south
take ornament
west
north
take candy cane
south
east
north
east
take fixed point
north
take spool of cat6
north
take weather machine
south
west
take shell
east
south
west
west
north
take wreath
north
east
inv
""".strip().split("\n")

items = [
  "ornament",
  "loom",
  "spool of cat6",
  "wreath",
  "fixed point",
  "shell",
  "candy cane",
  "weather machine",
]


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


with open("25-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

machine = intcode.execute(prog)
for line in script:
    print(read_output(machine))
    input_string(machine, line)
try:
    for bits in itertools.product(range(2), repeat=8):
        for bit, item in zip(bits, items):
            if bit == 0:
                print(read_output(machine))
                input_string(machine, f"drop {item}")
        print(read_output(machine))
        input_string(machine, "south")
        for bit, item in zip(bits, items):
            if bit == 0:
                print(read_output(machine))
                input_string(machine, f"take {item}")
except StopIteration:
    pass
