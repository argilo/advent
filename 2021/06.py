#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=6, year=2021)
#data = "3,4,3,1,2"

states = [0] * 9
fish = [int(n) for n in data.split(",")]

for f in fish:
    states[f] += 1

for day in range(256):
    new_states = states[1:] + [0]
    new_states[6] += states[0]
    new_states[8] += states[0]
    states = new_states
    print(day+1, sum(states))
