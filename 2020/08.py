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
import console

data = aocd.get_data(day=8, year=2020)
prog = console.parse(data)

c = console.Console(prog)
visited = set()
while True:
    if c.ip in visited:
        break
    visited.add(c.ip)
    c.exec()
print(c.acc)
# aocd.submit(c.acc, part="a", day=8, year=2020)

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

    c = console.Console(prog)
    visited = set()
    while True:
        if c.ip in visited:
            break
        if c.ip == len(prog):
            print(c.acc)
            # aocd.submit(c.acc, part="b", day=8, year=2020)
            break
        visited.add(c.ip)
        c.exec()
