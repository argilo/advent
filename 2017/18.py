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
for line in open("18-input.txt"):
    ins = [int(s) if num.match(s) else s for s in line.rstrip().split()]
    program.append(ins)


def execute(program, registers):
    ip = 0
    while ip < len(program):
        ins = program[ip]
        if ins[0] == "snd":
            result = ins[1] if isinstance(ins[1], int) else registers[ins[1]]
            inp = yield result
            if inp is not None:
                raise Exception(f"input {inp} given to snd instruction")
        elif ins[0] == "set":
            inp = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            registers[ins[1]] = inp
        elif ins[0] == "add":
            inp = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            registers[ins[1]] += inp
        elif ins[0] == "mul":
            inp = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            registers[ins[1]] *= inp
        elif ins[0] == "mod":
            inp = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            registers[ins[1]] %= inp
        elif ins[0] == "rcv":
            inp = yield
            if inp is None:
                raise Exception("no input given to input instruction")
            registers[ins[1]] = inp
        elif ins[0] == "jgz":
            inp = ins[1] if isinstance(ins[1], int) else registers[ins[1]]
            offset = ins[2] if isinstance(ins[2], int) else registers[ins[2]]
            if inp > 0:
                ip += offset
                continue
        ip += 1


registers = {}
for i in range(26):
    registers[chr(97+i)] = 0
machine = execute(program, registers)
while True:
    output = next(machine)
    if output is None:
        break
    else:
        last = output
print(last)


count = 0
registers = [{}, {}]
for i in range(26):
    registers[0][chr(97+i)] = 0
    registers[1][chr(97+i)] = 0
registers[1]["p"] = 1
machines = [execute(program, reg) for reg in registers]
queues = [queue.Queue() for _ in registers]
outputs = [0 for _ in registers]
done = False
while not done:
    done = True
    for i, machine in enumerate(machines):
        if outputs[i] is None:
            if not queues[i ^ 1].empty():
                outputs[i] = machine.send(queues[i ^ 1].get())
                done = False
            else:
                continue
        else:
            done = False
            outputs[i] = next(machine)

        if outputs[i] is not None:
            queues[i].put(outputs[i])
            if i == 1:
                count += 1
print(count)
