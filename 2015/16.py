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

analysis = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for line in open("16-input.txt"):
    parts = line.split()
    n = int(parts[1].rstrip(":"))
    things = [s.rstrip(":") for s in parts[2::2]]
    amounts = [int(n.rstrip(",")) for n in parts[3::2]]
    props = {thing: amount for thing, amount in zip(things, amounts)}

    for thing, amount in props.items():
        if analysis[thing] != amount:
            break
    else:
        print(n)

for line in open("16-input.txt"):
    parts = line.split()
    n = int(parts[1].rstrip(":"))
    things = [s.rstrip(":") for s in parts[2::2]]
    amounts = [int(n.rstrip(",")) for n in parts[3::2]]
    props = {thing: amount for thing, amount in zip(things, amounts)}

    for thing, amount in props.items():
        if thing in ["cats", "trees"]:
            if analysis[thing] >= amount:
                break
        elif thing in ["pomeranians", "goldfish"]:
            if analysis[thing] <= amount:
                break
        else:
            if analysis[thing] != amount:
                break
    else:
        print(n)
