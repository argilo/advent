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

# times = [7, 15, 30]
# dists = [9, 40, 200]

times = [41, 77, 70, 96]
dists = [249, 1362, 1127, 1011]

prod = 1
for t, d in zip(times, dists):
    sum = 0
    for hold in range(0, t+1):
        new_dist = hold * (t - hold)
        if new_dist > d:
            sum += 1
    prod *= sum

print(prod)

# aocd.submit(prod, part="a", day=6, year=2023)


# times = [71530]
# dists = [940200]

times = [41777096]
dists = [249136211271011]

prod = 1
for t, d in zip(times, dists):
    sum = 0
    for hold in range(0, t+1):
        new_dist = hold * (t - hold)
        if new_dist > d:
            sum += 1
    prod *= sum

print(prod)

# aocd.submit(prod, part="b", day=6, year=2023)
