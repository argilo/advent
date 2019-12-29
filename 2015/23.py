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

import re

program = []
num = re.compile(r"^[+-]?\d+$")
for line in open("23-input.txt"):
    line = line.rstrip().replace(",", "")
    ins = [int(s) if num.match(s) else s for s in line.split()]
    program.append(ins)


def execute(program, registers):
    ip = 0
    while ip < len(program):
        ins = program[ip]
        if ins[0] == "hlf":
            registers[ins[1]] //= 2
        elif ins[0] == "tpl":
            registers[ins[1]] *= 3
        elif ins[0] == "inc":
            registers[ins[1]] += 1
        elif ins[0] == "jmp":
            ip += ins[1]
            continue
        elif ins[0] == "jie":
            if registers[ins[1]] % 2 == 0:
                ip += ins[2]
                continue
        elif ins[0] == "jio":
            if registers[ins[1]] == 1:
                ip += ins[2]
                continue
        ip += 1


registers = {"a": 0, "b": 0}
execute(program, registers)
print(registers["b"])

registers = {"a": 1, "b": 0}
execute(program, registers)
print(registers["b"])
