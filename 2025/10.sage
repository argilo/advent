#!/usr/bin/env python3

# Copyright 2025 Clayton Smith
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

YEAR = 2025
DAY = 10

data = aocd.get_data(day=DAY, year=YEAR)
# data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

ans = 0
for line in data.splitlines():
    i1 = line.index("]")
    i2 = line.index("{")

    buttons = [[int(n) for n in piece[1:-1].split(",")] for piece in line[i1+2:i2-1].split()]
    joltage = [int(n) for n in line[i2+1:-1].split(",")]

    p = MixedIntegerLinearProgram()
    v = p.new_variable(integer=True, nonnegative=True)
    x_vars = list(v[f"x_{i}"] for i in range(len(buttons)))
    p.set_objective(-sum(x_vars))
    for i, n in enumerate(joltage):
        sm = sum(x_vars[j] for j, button in enumerate(buttons) if i in button)
        p.add_constraint(sm == n)
    ans += int(-p.solve())

print(ans)
# aocd.submit(ans, part="b", day=DAY, year=YEAR)
