#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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

data = aocd.get_data(day=13, year=2024)

# data = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

ans = 0
for machine in data.split("\n\n"):
    lines = machine.split("\n")
    ax, ay = [int(piece[2:]) for piece in lines[0][10:].split(", ")]
    bx, by = [int(piece[2:]) for piece in lines[1][10:].split(", ")]
    px, py = [int(piece[2:]) for piece in lines[2][7:].split(", ")]

    best_cost = 1000000
    for a_presses in range(0, 100):
        b_presses = (px - ax * a_presses) // bx
        if (ax * a_presses + bx * b_presses == px) and (ay * a_presses + by * b_presses == py) and (b_presses >= 0):
            cost = a_presses * 3 + b_presses
            if cost < best_cost:
                best_cost = cost
    if best_cost < 1000000:
        ans += best_cost

print(ans)
# aocd.submit(ans, part="a", day=13, year=2024)


ans = 0
for machine in data.split("\n\n"):
    lines = machine.split("\n")
    ax, ay = [int(piece[2:]) for piece in lines[0][10:].split(", ")]
    bx, by = [int(piece[2:]) for piece in lines[1][10:].split(", ")]
    px, py = [int(piece[2:]) for piece in lines[2][7:].split(", ")]
    px += 10000000000000
    py += 10000000000000

    n1 = -(bx * py - by * px)
    n2 = -(px * ay - py * ax)
    den = (by * ax - bx * ay)
    if n1 % den == 0 and n2 % den == 0:
        a_presses = n1 // den
        b_presses = n2 // den
        ans += a_presses * 3 + b_presses

print(ans)
# aocd.submit(ans, part="b", day=13, year=2024)
