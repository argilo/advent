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

WIDTH = 25
HEIGHT = 6

with open("08-input.txt") as f:
    data = f.read().rstrip()


image = [["2" for _ in range(WIDTH)] for _ in range(HEIGHT)]
lowest = 100
for offset in range(0, len(data), WIDTH * HEIGHT):
    layer = data[offset:offset + WIDTH*HEIGHT]
    zeroes, ones, twos = layer.count("0"), layer.count("1"), layer.count("2")
    if zeroes < lowest:
        lowest = zeroes
        product = ones * twos

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[y][x] == "2":
                image[y][x] = layer[y * WIDTH + x]
print(product)

for y in range(HEIGHT):
    for x in range(WIDTH):
        print("█" if image[y][x] == "1" else " ", end="")
    print()
