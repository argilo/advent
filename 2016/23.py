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
num = re.compile(r"^-?\d+$")
for line in open("23-input.txt"):
    ins = [int(s) if num.match(s) else s for s in line.rstrip().split()]
    program.append(ins)

tgl_target = {
    "inc": "dec",
    "dec": "inc",
    "tgl": "inc",
    "jnz": "cpy",
    "cpy": "jnz",
}


def execute(program, registers):
    ip = 0
    while ip < len(program):
        ins = program[ip]
        if ins[0] == "cpy":
            inp = ins[1] if isinstance(ins[1], int) else registers[ins[1]]
            registers[ins[2]] = inp
        elif ins[0] == "inc":
            registers[ins[1]] += 1
        elif ins[0] == "dec":
            registers[ins[1]] -= 1
        elif ins[0] == "jnz":
            inp = ins[1] if isinstance(ins[1], int) else registers[ins[1]]
            offset = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            if inp != 0:
                ip += offset
                continue
        elif ins[0] == "tgl":
            offset = ins[1] if isinstance(ins[1], int) else registers[ins[1]]
            if 0 <= ip+offset < len(program):
                program[ip+offset][0] = tgl_target[program[ip+offset][0]]
        ip += 1


registers = {"a": 7, "b": 0, "c": 0, "d": 0}
execute(program, registers)
print(registers["a"])

factorial = 1
for n in range(1, 12+1):
    factorial *= n
print(factorial + 84*75)
