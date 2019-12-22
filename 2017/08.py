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

registers = {}
highest = 0
for line in open("08-input.txt"):
    parts = line.rstrip().split()
    inc_var = parts[0]
    inc = int(parts[2])
    if parts[1] == "dec":
        inc = -inc
    comp_var = parts[4]
    comp = parts[5]
    comp_val = int(parts[6])
    bool = False
    if comp == "==":
        bool = registers.get(comp_var, 0) == comp_val
    elif comp == "!=":
        bool = registers.get(comp_var, 0) != comp_val
    elif comp == ">":
        bool = registers.get(comp_var, 0) > comp_val
    elif comp == "<":
        bool = registers.get(comp_var, 0) < comp_val
    elif comp == ">=":
        bool = registers.get(comp_var, 0) >= comp_val
    elif comp == "<=":
        bool = registers.get(comp_var, 0) <= comp_val
    if bool:
        registers[inc_var] = registers.get(inc_var, 0) + inc
    highest = max(highest, max(registers.values()))
print(max(registers.values()))
print(highest)
