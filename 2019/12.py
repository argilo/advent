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

import math
import re

poss = []
vels = []

for line in open("12-input.txt"):
    m = re.match(r"<x=(.*), y=(.*), z=(.*)>", line)
    poss.append([int(m[1]), int(m[2]), int(m[3])])
    vels.append([0, 0, 0])

for _ in range(1000):
    for i in range(len(poss) - 1):
        for j in range(i+1, len(poss)):
            if j == i:
                continue
            for coord in range(3):
                if poss[i][coord] < poss[j][coord]:
                    vels[i][coord] += 1
                    vels[j][coord] -= 1
                elif poss[i][coord] > poss[j][coord]:
                    vels[i][coord] -= 1
                    vels[j][coord] += 1

    for i in range(len(poss)):
        for coord in range(3):
            poss[i][coord] += vels[i][coord]

    energy = 0
    for pos, vel in zip(poss, vels):
        energy += sum([abs(n) for n in pos]) * sum([abs(n) for n in vel])
print(energy)


seen_x = {}
seen_y = {}
seen_z = {}
x_period = None
y_period = None
z_period = None
step = 0
while True:
    for i in range(len(poss) - 1):
        for j in range(i+1, len(poss)):
            if j == i:
                continue
            for coord in range(3):
                if poss[i][coord] < poss[j][coord]:
                    vels[i][coord] += 1
                    vels[j][coord] -= 1
                elif poss[i][coord] > poss[j][coord]:
                    vels[i][coord] -= 1
                    vels[j][coord] += 1

    for i in range(len(poss)):
        for coord in range(3):
            poss[i][coord] += vels[i][coord]

    xs = tuple([pos[0] for pos in poss] + [vel[0] for vel in vels])
    ys = tuple([pos[1] for pos in poss] + [vel[1] for vel in vels])
    zs = tuple([pos[2] for pos in poss] + [vel[2] for vel in vels])

    if x_period is None and xs in seen_x:
        x_period = step
    else:
        seen_x[xs] = step

    if y_period is None and ys in seen_y:
        y_period = step
    else:
        seen_y[ys] = step

    if z_period is None and zs in seen_z:
        z_period = step
    else:
        seen_z[zs] = step

    if x_period is not None and y_period is not None and z_period is not None:
        break

    step += 1


def lcm(a, b):
    return a * b // math.gcd(a, b)


print(lcm(lcm(x_period, y_period), z_period))
