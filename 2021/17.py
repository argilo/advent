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

data = aocd.get_data(day=17, year=2021)
#data = "target area: x=20..30, y=-10..-5"

print(data)

x1, x2 = [int(n) for n in data.split()[2][2:-1].split("..")]
y1, y2 = [int(n) for n in data.split()[3][2:].split("..")]

def fire(xv, yv):
    global x1, x2, y1, y2

    x, y = 0, 0
    max_y = 0
    while True:
        if y > max_y:
            max_y = y

        if x1 <= x <= x2 and y1 <= y <= y2:
            return True, max_y
        x += xv
        y += yv
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1

        if y < y1:
            return False, max_y

good_values = 0
for yv in range(-500, 500):
    for xv in range(0, 500):
        hit, max_y = fire(xv, yv)
        if hit:
            good_values += 1
            print(good_values, max_y, xv, yv)
