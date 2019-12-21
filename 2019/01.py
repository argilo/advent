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

total_fuel = 0
total_extra_fuel = 0

for line in open("01-input.txt"):
    mass = int(line)
    fuel = (mass // 3) - 2
    total_fuel += fuel

    while (fuel // 3) - 2 > 0:
        fuel = (fuel // 3) - 2
        total_extra_fuel += fuel

print(total_fuel)
print(total_fuel + total_extra_fuel)
