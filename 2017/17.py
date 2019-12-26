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

with open("17-input.txt") as f:
    steps = int(f.read().rstrip())

state = [0]
pos = 0
for i in range(1, 2017+1):
    pos = (pos + steps) % len(state)
    pos += 1
    state.insert(pos, i)
print(state[(pos+1) % len(state)])

pos = 0
after_zero = None
for i in range(1, 50000000+1):
    pos = (pos + steps) % i
    pos += 1
    if pos == 1:
        after_zero = i
print(after_zero)
