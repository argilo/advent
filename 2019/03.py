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


def follow(wire, num, coords):
    closest = 1000000
    best = 1000000
    steps = 0
    x, y = 0, 0

    for segment in wire.split(","):
        direction, length = segment[0], int(segment[1:])
        x_step, y_step = 0, 0
        if direction == "R":
            x_step = 1
        elif direction == "L":
            x_step = -1
        elif direction == "U":
            y_step = 1
        elif direction == "D":
            y_step = -1

        for _ in range(length):
            x += x_step
            y += y_step
            steps += 1
            counts = coords.get((x, y), [0, 0])
            if counts[num] == 0:
                counts[num] = steps
                coords[(x, y)] = counts

            if counts[0] > 0 and counts[1] > 0:
                dist = abs(x) + abs(y)
                if dist < closest:
                    closest = dist

                time = counts[0] + counts[1]
                if time < best:
                    best = time

    if num == 1:
        print(closest)
        print(best)


with open("03-input.txt") as f:
    wire1 = f.readline().rstrip()
    wire2 = f.readline().rstrip()

# wire1 = "R8,U5,L5,D3"
# wire2 = "U7,R6,D4,L4"

# wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
# wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"

# wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
# wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

coords = {}

follow(wire1, 0, coords)
follow(wire2, 1, coords)
