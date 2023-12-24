#!/usr/bin/env python3

# Copyright 2023 Clayton Smith
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
import itertools
import geomdl.ray

data = aocd.get_data(day=24, year=2023)

stones = []
for line in data.splitlines():
    part1, part2 = line.split(" @ ")
    x, y, z = [int(n) for n in part1.split(", ")]
    vx, vy, vz = [int(n) for n in part2.split(", ")]
    stone = (x, y, z, vx, vy, vz)
    stones.append(stone)

t_low, t_high = 200000000000000, 400000000000000

ans = 0
for a, b in itertools.combinations(stones, 2):
    ra = geomdl.ray.Ray((a[0], a[1]), (a[0] + a[3], a[1] + a[4]))
    rb = geomdl.ray.Ray((b[0], b[1]), (b[0] + b[3], b[1] + b[4]))
    ia, ib, res = geomdl.ray.intersect(ra, rb)
    if res in (1, 3) and ia >= 0 and ib >= 0:
        x, y = ra.eval(ia)
        if t_low <= x <= t_high and t_low <= y <= t_high:
            ans += 1
print(ans)


print()
print('x, y, z, a, b, c = var("x y z a b c")')
print("solve([")
for x, y, z, a, b, c in stones[:4]:
    print(f"({x}-x)/({a}-a)==({y}-y)/({b}-b), ({y}-y)/({b}-b)==({z}-z)/({c}-c), ")
print("], x, y, z, a, b, c)")

# And put that into Sage! ^^
