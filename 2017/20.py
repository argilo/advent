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

import re


def position(t, p, v, a):
    return (
        p[0] + t*v[0] + t*(t+1)//2*a[0],
        p[1] + t*v[1] + t*(t+1)//2*a[1],
        p[2] + t*v[2] + t*(t+1)//2*a[2],
    )


min = 1000000000
num = 0
pp = []
vv = []
aa = []
for line in open("20-input.txt"):
    m = re.match(r"p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>, a=<(.*),(.*),(.*)>", line.rstrip())
    p = int(m[1]), int(m[2]), int(m[3])
    pp.append(p)
    v = int(m[4]), int(m[5]), int(m[6])
    vv.append(v)
    a = int(m[7]), int(m[8]), int(m[9])
    aa.append(a)

    late_p = position(1000, p, v, a)
    late_p_dist = abs(late_p[0]) + abs(late_p[1]) + abs(late_p[2])
    if late_p_dist < min:
        min = late_p_dist
        min_n = num
    num += 1
print(min_n)

alive = [True] * len(pp)
for t in range(1000):
    pp_t = {}
    for i, p, v, a in zip(range(len(pp)), pp, vv, aa):
        if not alive[i]:
            continue
        pos = position(t, p, v, a)
        if pos in pp_t:
            alive[pp_t[pos]] = False
            alive[i] = False
        else:
            pp_t[pos] = i
print(sum(alive))
