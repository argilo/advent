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

import sys

ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJ_REL_BASE = 9
HALT = 99

NUM_BYTES = {
    ADD: 4,
    MULTIPLY: 4,
    INPUT: 2,
    OUTPUT: 2,
    JUMP_IF_TRUE: 3,
    JUMP_IF_FALSE: 3,
    LESS_THAN: 4,
    EQUALS: 4,
    ADJ_REL_BASE: 2,
    HALT: 1,
}


def execute(prog):
    prog = prog.copy()

    ip = 0
    rel_base = 0
    while True:
        opcode = prog[ip] % 100
        ins_len = NUM_BYTES[opcode]

        addrs = []
        args = []
        for i in range(1, ins_len):
            param_mode = (prog[ip] // (10**(i+1))) % 10
            if param_mode == 0:
                addr = prog[ip + i]
                if addr >= len(prog):
                    prog.extend([0] * (addr + 1 - len(prog)))
                addrs.append(addr)
                args.append(prog[addr])
            elif param_mode == 1:
                addrs.append(None)
                args.append(prog[ip + i])
            elif param_mode == 2:
                addr = rel_base + prog[ip + i]
                if addr >= len(prog):
                    prog.extend([0] * (addr + 1 - len(prog)))
                addrs.append(addr)
                args.append(prog[addr])
            else:
                print(f"Invalid parameter mode: {param_mode}")
        jumped = False

        if opcode == ADD:
            prog[addrs[2]] = args[0] + args[1]
        elif opcode == MULTIPLY:
            prog[addrs[2]] = args[0] * args[1]
        elif opcode == INPUT:
            inp = yield
            if inp is None:
                raise Exception("no input given to input instruction")
            prog[addrs[0]] = inp
        elif opcode == OUTPUT:
            inp = yield args[0]
            if inp is not None:
                raise Exception(f"input {inp} given to output instruction")
        elif opcode == JUMP_IF_TRUE:
            if args[0] != 0:
                ip = args[1]
                jumped = True
        elif opcode == JUMP_IF_FALSE:
            if args[0] == 0:
                ip = args[1]
                jumped = True
        elif opcode == LESS_THAN:
            prog[addrs[2]] = int(args[0] < args[1])
        elif opcode == EQUALS:
            prog[addrs[2]] = int(args[0] == args[1])
        elif opcode == ADJ_REL_BASE:
            rel_base += args[0]
        elif opcode == HALT:
            break
        else:
            print(f"Invalid opcode: {opcode}")

        if not jumped:
            ip += ins_len

    return prog
