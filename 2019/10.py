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


def sort_order(x, y):
    if x >= 0 and y < 0:
        quadrant = 0
        angle = x / (-y)
    elif y >= 0 and x > 0:
        quadrant = 1
        angle = y / x
    elif x <= 0 and y > 0:
        quadrant = 2
        angle = (-x) / y
    elif y <= 0 and x < 0:
        quadrant = 3
        angle = (-y) / (-x)
    return quadrant, angle, x, y


asteroids = set()

for y, line in enumerate(open("10-input.txt")):
    for x, char in enumerate(line.rstrip()):
        if char == "#":
            asteroids.add((x, y))

best = 0
for x1, y1 in asteroids:
    visible = set()
    for x2, y2 in asteroids:
        if (x1, y1) == (x2, y2):
            continue
        diff_x, diff_y = x2-x1, y2-y1
        g = math.gcd(diff_x, diff_y)
        step_x, step_y = diff_x // g, diff_y // g

        x, y = x1 + step_x, y1 + step_y
        while (x, y) != (x2, y2):
            if (x, y) in asteroids:
                break
            x += step_x
            y += step_y
        else:
            visible.add((x2, y2))
    if len(visible) > best:
        best = len(visible)
        best_visible = visible.copy()
        best_x, best_y = x1, y1
print(best)

laser_order = []
for x, y in best_visible:
    diff_x, diff_y = x-best_x, y-best_y
    laser_order.append(sort_order(diff_x, diff_y))
laser_order.sort()

two_hundredth = laser_order[199]
print(100 * (two_hundredth[2] + best_x) + (two_hundredth[3] + best_y))
