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


a, m = 0, 1
for line in open("15-input.txt"):
    parts = line.split()
    n, size, pos = int(parts[1][1:]), int(parts[3]), int(parts[11][:-1])
    a, m = crt(a, -(pos+n) % size, m, size), m * size
print(a)

n, size, pos = 7, 11, 0
a, m = crt(a, -(pos+n) % size, m, size), m * size
print(a)
