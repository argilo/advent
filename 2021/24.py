#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=24, year=2021)
lines = data.splitlines()


def calc(input):
    reg = [0, 0, 0, 0]
    reg_name = ["w", "x", "y", "z"]

    for line in lines:
        parts = line.split()
        ins = parts[0]
        reg_index = reg_name.index(parts[1])

        if ins == "inp":
            reg[reg_index] = input.pop(0)
        else:
            arg = parts[2]
            if arg in reg_name:
                arg = reg[reg_name.index(arg)]
            else:
                arg = int(arg)

            if ins == "add":
                reg[reg_index] += arg
            elif ins == "mul":
                reg[reg_index] *= arg
            elif ins == "div":
                reg[reg_index] //= arg
            elif ins == "mod":
                reg[reg_index] %= arg
            elif ins == "eql":
                reg[reg_index] = (1 if arg == reg[reg_index] else 0)
    return reg[3]


for d0 in range(1, 6):
    d13 = d0 + 4

    for d1 in (1,):
        d12 = d1 + 8

        for d2 in (7, 8, 9):
            d5 = d2 - 6

            for d3 in (1, 2, 3):
                d4 = d3 + 6

                for d6 in range(3, 10):
                    d7 = d6 - 2

                    for d8 in range(2, 10):
                        d9 = d8-1

                        for d10 in range(1, 10):
                            d11 = d10

                            input = [None]*14
                            input[0] = d0
                            input[1] = d1
                            input[2] = d2
                            input[3] = d3
                            input[4] = d4
                            input[5] = d5
                            input[6] = d6
                            input[7] = d7
                            input[8] = d8
                            input[9] = d9
                            input[10] = d10
                            input[11] = d11
                            input[12] = d12
                            input[13] = d13
                            input_str = "".join(str(n) for n in input)
                            result = calc(input)
                            print(input_str, result)
