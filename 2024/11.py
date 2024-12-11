#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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
import functools

orig_data = aocd.get_data(day=11, year=2024)

# data = "0 1 10 99 999"
# data = "125 17"

data = [int(n) for n in orig_data.split()]


def evolve(stones):
    next_stones = []
    for stone in stones:
        digits = str(stone)
        if stone == 0:
            next_stones.append(1)
        elif len(digits) % 2 == 0:
            num_digits = len(digits)
            next_stones.append(int(digits[:len(digits) // 2]))
            next_stones.append(int(digits[len(digits) // 2:]))
        else:
            next_stones.append(stone * 2024)
    return next_stones


for _ in range(25):
    data = evolve(data)
ans = len(data)

print(ans)
# aocd.submit(ans, part="a", day=11, year=2024)

data = [int(n) for n in orig_data.split()]


@functools.cache
def evolve(stone, n):
    if n == 75:
        return 1

    next_stones = []

    digits = str(stone)
    if stone == 0:
        next_stones.append(1)
    elif len(digits) % 2 == 0:
        num_digits = len(digits)
        next_stones.append(int(digits[:len(digits) // 2]))
        next_stones.append(int(digits[len(digits) // 2:]))
    else:
        next_stones.append(stone * 2024)

    return sum(evolve(next_stone, n+1) for next_stone in next_stones)


ans = sum(evolve(stone, 0) for stone in data)

print(ans)
# aocd.submit(ans, part="b", day=11, year=2024)
