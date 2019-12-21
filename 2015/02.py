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

paper = 0
ribbon = 0
for line in open("02-input.txt"):
    l, w, h = [int(n) for n in line.rstrip().split("x")]
    sides = l*w, w*h, h*l
    perimeters = 2*(l+w), 2*(w+h), 2*(h+l)
    paper += 2*sum(sides) + min(sides)
    ribbon += min(perimeters) + l*w*h
print(paper)
print(ribbon)
