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

data = aocd.get_data(day=8, year=2020)

lines = data.splitlines()

prog = []
for line in lines:
    op, num = line.split()
    num = int(num)
    prog.append((op, num))

acc = 0
ip = 0
visited = set()
while True:
    if ip in visited:
        break
    visited.add(ip)
    op, num = prog[ip]
    if op == "acc":
        acc += num
        ip += 1
    elif op == "jmp":
        ip += num
    elif op == "nop":
        ip += 1
print(acc)
#aocd.submit(acc, part="a", day=8, year=2020)

orig_prog = prog.copy()
for i in range(len(prog)):
    prog = orig_prog.copy()
    op = prog[i][0]
    if op == "acc":
        continue
    elif op == "nop":
        prog[i] = ("jmp", prog[i][1])
    elif op == "jmp":
        prog[i] = ("nop", prog[i][1])

    acc = 0
    ip = 0
    visited = set()
    while True:
        if ip in visited:
            break
        if ip == len(prog):
            print(acc)
            #aocd.submit(acc, part="b", day=8, year=2020)
            break
        visited.add(ip)
        op, num = prog[ip]
        if op == "acc":
            acc += num
            ip += 1
        elif op == "jmp":
            ip += num
        elif op == "nop":
            ip += 1
