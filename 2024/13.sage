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

    A = Matrix([
        [int(piece[2:]) for piece in lines[0][10:].split(", ")],
        [int(piece[2:]) for piece in lines[1][10:].split(", ")]
    ]).transpose()
    Y = vector([int(piece[2:]) for piece in lines[2][7:].split(", ")])

    X = A.solve_right(Y)
    if X[0] in ZZ and X[1] in ZZ:
        ans += X * vector([3, 1])

print(ans)
# aocd.submit(ans, part="a", day=13, year=2024)


ans = 0
for machine in data.split("\n\n"):
    lines = machine.split("\n")

    A = Matrix([
        [int(piece[2:]) for piece in lines[0][10:].split(", ")],
        [int(piece[2:]) for piece in lines[1][10:].split(", ")]
    ]).transpose()
    Y = vector([int(piece[2:]) for piece in lines[2][7:].split(", ")])
    Y += vector([10000000000000, 10000000000000])

    X = A.solve_right(Y)
    if X[0] in ZZ and X[1] in ZZ:
        ans += X * vector([3, 1])

print(ans)
# aocd.submit(ans, part="b", day=13, year=2024)
