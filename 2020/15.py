#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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

data = aocd.get_data(day=15, year=2020)
seq = [int(n) for n in data.split(",")]
while len(seq) < 2020:
    last = seq[-1]
    try:
        a = seq[-2::-1]
        i = seq[-2::-1].index(last)
        seq.append(i+1)
    except ValueError:
        seq.append(0)
print(seq[-1])


data = aocd.get_data(day=15, year=2020)
seq = [int(n) for n in data.split(",")]
last_index = {}
for i, n in enumerate(seq[:-1]):
    last_index[n] = i

while len(seq) < 30000000:
    last = seq[-1]
    if last in last_index:
        seq.append(len(seq)-last_index[last]-1)
    else:
        seq.append(0)
    last_index[seq[-2]] = len(seq) - 2
print(seq[-1])
