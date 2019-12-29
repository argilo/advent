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


def divisors(n):
    d = 1
    while d*d <= n:
        if n % d == 0:
            yield d
            if n // d > d:
                yield n // d
        d += 1


def sum_divisors(n):
    sum = 0
    for d in divisors(n):
        sum += d
    return(sum)


def divisors50(n):
    for d in range(1, 51):
        if n % d == 0:
            yield n // d


def sum_divisors50(n):
    sum = 0
    for d in divisors50(n):
        sum += d
    return(sum)


with open("20-input.txt") as f:
    presents = int(f.read().rstrip())

n = 1
while True:
    if sum_divisors(n) * 10 >= presents:
        print(n)
        break
    n += 1

n = 1
while True:
    if sum_divisors50(n) * 11 >= presents:
        print(n)
        break
    n += 1
