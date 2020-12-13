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


def mul_inv(a, b):
    """Compute the multiplicative inverse of a modulo b"""
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def crt(a, b, m, n):
    """
    Compute a number that is congruent to a modulo m, and b modulo n.

    By the Chinese Remainder Theorem, such a number must exist, as long
    as m and n are coprime.
    """
    return ((a * n * mul_inv(n, m)) + (b * m * mul_inv(m, n))) % (m * n)


data = aocd.get_data(day=13, year=2020)

earliest, buses = data.splitlines()
earliest = int(earliest)
buses = [int(n) for n in buses.split(",") if n != "x"]

times = []
for bus in buses:
    first = (earliest // bus) * bus
    if first < earliest:
        first += bus
    times.append((first - earliest, bus))
times.sort()
print(times[0][0] * times[0][1])

data = aocd.get_data(day=13, year=2020)

a = 0
m = 1
for i, bus in enumerate(data.splitlines()[1].split(",")):
    if bus == "x":
        continue
    bus = int(bus)
    a = crt(a, bus-i, m, bus)
    m *= bus
print(a)
