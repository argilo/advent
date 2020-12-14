#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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
import itertools

mem = [0]*65536
data = aocd.get_data(day=14, year=2020)
for line in data.splitlines():
    if line.startswith("mask = "):
        mask = line[7:]
        a = 0
        o = 0
        for i, c in enumerate(mask):
            if c == "1":
                o |= (1 << (35-i))
            if c != "0":
                a |= (1 << (35-i))
    else:
        addr = int(line.split("[")[1].split("]")[0])
        val = int(line.split(" = ")[1])
        mem[addr] = (val | o) & a
print(sum(mem))


mem = {}
data = aocd.get_data(day=14, year=2020)
for line in data.splitlines():
    if line.startswith("mask = "):
        mask = line[7:]
    else:
        addr = int(line.split("[")[1].split("]")[0])
        val = int(line.split(" = ")[1])

        xes = []
        a = 0
        for i, c in enumerate(mask):
            if c == "X":
                xes.append(1 << (35-i))
            else:
                a |= (1 << (35-i))

            if c == "1":
                addr |= (1 << (35-i))

        for n in range(len(xes)+1):
            for comb in itertools.combinations(xes, n):
                new_addr = (addr & a) | sum(comb)
                mem[new_addr] = val

total = 0
for k, v in mem.items():
    total += v
print(total)
