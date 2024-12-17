#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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

import aocd

data = aocd.get_data(day=17, year=2024)

# data = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

lines = data.splitlines()

a = int(lines[0][12:])
b = int(lines[1][12:])
c = int(lines[2][12:])

program = [int(n) for n in lines[4][9:].split(",")]


def execute(a, b, c, program):
    output = []
    ip = 0
    while ip < len(program):
        opcode = program[ip]
        literal = program[ip+1]
        if literal < 4:
            combo = literal
        elif literal == 4:
            combo = a
        elif literal == 5:
            combo = b
        elif literal == 6:
            combo = c
        else:
            combo = None

        jump = None
        if opcode == 0:
            a = a >> combo
        elif opcode == 1:
            b = b ^ literal
        elif opcode == 2:
            b = combo % 8
        elif opcode == 3:
            if a != 0:
                jump = literal
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(combo % 8)
        elif opcode == 6:
            b = a >> combo
        elif opcode == 7:
            c = a >> combo

        if jump is not None:
            ip = jump
        else:
            ip += 2

    return output


output = execute(a, b, c, program)
ans = ",".join(str(n) for n in output)
print(ans)
# aocd.submit(ans, part="a", day=17, year=2024)

valid_a = []
for a in range(0o10000):
    output = execute(a, b, c, program)
    if output[0] == 2:
        valid_a.append(a)

for prefix in range(2, len(program) + 1):
    new_valid_a = []
    for end_a in valid_a:
        for begin_a in range(8):
            a = ((begin_a) << ((prefix + 2) * 3)) | end_a
            output = execute(a, b, c, program)
            if output[:prefix] == program[:prefix]:
                new_valid_a.append(a)
    valid_a = new_valid_a
valid_a.sort()
ans = valid_a[0]

print(ans)
# aocd.submit(ans, part="b", day=17, year=2024)


# Program: 2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0
# 2, 4 --> b = a % 8
# 1, 5 --> b = b ^ 5     b = (a%8) ^ 5
# 7, 5 --> c = a >> b    c = a >> ((a%8) ^ 5)
# 0, 3 --> a >>= 3
# 4, 1 --> b = b ^ c     b = (a%8) ^ (a >> ((a%8) ^ 5)) ^ 3
# 1, 6 --> b = b ^ 6
# 5, 5 --> output b % 8
# 3, 0 --> if (a != 0), jump to 0
