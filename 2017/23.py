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

import queue
import re

program = []
num = re.compile(r"^-?\d+$")
for line in open("23-input.txt"):
    ins = [int(s) if num.match(s) else s for s in line.rstrip().split()]
    program.append(ins)


def execute(program, registers):
    ip = 0
    muls = 0
    while ip < len(program):
        ins = program[ip]
        if ins[0] == "set":
            inp = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            registers[ins[1]] = inp
        elif ins[0] == "sub":
            inp = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            registers[ins[1]] -= inp
        elif ins[0] == "mul":
            inp = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            registers[ins[1]] *= inp
            muls += 1
        elif ins[0] == "jnz":
            inp = ins[1] if isinstance(ins[1], int) else registers[ins[1]]
            offset = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            if inp != 0:
                ip += offset
                continue
        ip += 1
    return muls


registers = {chr(97+i): 0 for i in range(8)}
print(execute(program, registers))

sum = 0
b = 65*100 + 100000
c = b + 17000
for n in range(b, c+1, 17):
    f = 1
    for d in range(2, n):
        if d * d > n:
            break
        if n % d == 0:
            f = 0
    if f == 0:
        sum += 1
print(sum)
