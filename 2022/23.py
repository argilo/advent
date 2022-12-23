#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=23, year=2022)

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
dir_checks = (
    ((-1, -1), (-1, 0), (-1, 1)),
    ((1, -1), (1, 0), (1, 1)),
    ((-1, -1), (0, -1), (1, -1)),
    ((-1, 1), (0, 1), (1, 1)),
)


def draw(elves):
    min_r, max_r = 1000000, -1000000
    min_c, max_c = 1000000, -1000000
    for r, c in elves:
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
    cnt = 0
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if (r, c) in elves:
                print("#", end="")
            else:
                cnt += 1
                print(".", end="")
        print()
    print(cnt)
    return cnt


elves = set()
for r, row in enumerate(data.split("\n")):
    for c, chr in enumerate(row):
        if chr == "#":
            elves.add((r, c))


start = 0
round = 0
while True:
    round += 1
    elf_prop = {}
    dupe_check = {}
    for r, c in elves:
        num_adj = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (r+dr, c+dc) in elves:
                    num_adj += 1
        if num_adj == 1:
            elf_prop[(r, c)] = (r, c)
        else:
            for d in range(4):
                dir_idx = (start + d) % 4
                dir_r, dir_c = dirs[dir_idx]
                dir_chk = dir_checks[dir_idx]

                for dr, dc in dir_chk:
                    if (r+dr, c+dc) in elves:
                        break
                else:
                    elf_prop[(r, c)] = (r+dir_r, c+dir_c)
                    break
            else:
                elf_prop[(r, c)] = (r, c)

    for elf in elf_prop:
        new_elf = elf_prop[elf]
        if new_elf in dupe_check:
            other_elf = dupe_check[new_elf]
            elf_prop[elf] = elf
            elf_prop[other_elf] = other_elf
        else:
            dupe_check[new_elf] = elf

    new_elves = set(elf_prop.values())
    draw(new_elves)
    print(round)

    if new_elves == elves:
        break

    elves = new_elves

    start = (start + 1) % 4
