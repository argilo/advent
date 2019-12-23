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

import intcode
import queue

with open("23-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

machines = [intcode.execute(prog) for _ in range(50)]
outs = [None] * 50
queues = [queue.Queue() for _ in range(50)]

for i, machine in enumerate(machines):
    next(machine)
    outs[i] = machine.send(i)

nat_x, nat_y = None, None
last_nat_y = None

while True:
    active = False
    new_packets = [None] * 50
    for i, machine, que in zip(range(50), machines, queues):
        if outs[i] is None:
            if not que.empty():
                active = True
                x, y = que.get()
                machine.send(x)
                outs[i] = machine.send(y)
            else:
                outs[i] = machine.send(-1)
        else:
            active = True
            dest = outs[i]
            x = next(machine)
            y = next(machine)
            if dest == 255:
                nat_x, nat_y = x, y
            else:
                new_packets[i] = (x, y)
                queues[dest].put((x, y))
            outs[i] = next(machine)

    if not active and nat_x is not None:
        if last_nat_y is None:
            print(nat_y)
        if last_nat_y == nat_y:
            print(nat_y)
            exit()
        last_nat_y = nat_y
        queues[0].put((nat_x, nat_y))
