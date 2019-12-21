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

import itertools

sum1 = 0
sum2 = 0
for line in open("02-input.txt"):
    data = [int(n) for n in line.rstrip().split()]
    for pair in itertools.combinations(data, 2):
        a, b = sorted(pair)
        if b % a == 0:
            sum2 += (b // a)
    sum1 += (max(data) - min(data))
print(sum1)
print(sum2)
