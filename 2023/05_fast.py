#!/usr/bin/env python3

# Copyright 2023 Clayton Smith
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

data = aocd.get_data(day=5, year=2023)
# data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

first = True
maps = []
map = []
for line in data.splitlines():
    if first:
        seeds = [int(n) for n in line[7:].split()]
        first = False
    else:
        if line == "":
            if map:
                maps.append(map)
            map = []
        elif line.endswith("map:"):
            continue
        else:
            nums = [int(n) for n in line.split()]
            map.append(nums)
maps.append(map)


def forward(n, map):
    for d_start, s_start, num in map:
        if s_start <= n < s_start + num:
            return d_start + (n - s_start)
    return n


least = 1000000000000
for seed in seeds:
    current = seed
    for map in maps:
        current = forward(current, map)
    if current < least:
        least = current

print(least)
# aocd.submit(least, part="a", day=5, year=2023)


def forward_with_room(n, map):
    room = 1000000000000
    for d_start, s_start, num in map:
        if n < s_start:
            room = min(room, s_start - n)
        if s_start <= n < s_start + num:
            return d_start + (n - s_start), (s_start + num) - n
    if room == 1000000000000:
        room = -1
    return n, room


least = 1000000000000
for i in range(0, len(seeds), 2):
    range_start, range_end = seeds[i], seeds[i] + seeds[i+1]
    while range_start < range_end:
        current = range_start
        room = 1000000000000
        for map in maps:
            current, new_room = forward_with_room(current, map)
            room = min(room, new_room)
        if current < least:
            least = current
        if room == -1:
            break
        range_start += room

print(least)
# aocd.submit(ans, part="b", day=5, year=2023)
