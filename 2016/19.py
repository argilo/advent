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

with open("19-input.txt") as f:
    n_elves = int(f.read().rstrip())

elves = list(range(1, 1+n_elves))
while len(elves) > 1:
    if len(elves) % 2 == 0:
        elves = elves[::2]
    else:
        elves = elves[-1:] + elves[:-1:2]
print(elves[0])

elves = list(range(1, 1+n_elves))
while len(elves) > 1:
    start = len(elves) // 2
    if len(elves) % 2 == 0:
        keep = elves[start+2::3]
    else:
        keep = elves[start+1::3]
    skip = len(elves) - start - len(keep)
    elves = elves[skip:start] + keep + elves[:skip]
print(elves[0])
