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


def diag(row, col):
    rc = row + col - 1
    return col + (rc-1) * rc // 2


def code(n):
    value = 20151125
    for _ in range(n-1):
        value = (value * 252533) % 33554393
    return value


with open("25-input.txt") as f:
    data = f.read().split()
    row, col = int(data[15][:-1]), int(data[17][:-1])

print(code(diag(row, col)))
