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

data = aocd.get_data(day=9, year=2024)

# data = "2333133121414131402"

disk = []

is_len = True
file_id = 0
for digit in data:
    n = int(digit)
    if is_len:
        for _ in range(n):
            disk.append(file_id)
        file_id += 1
    else:
        for _ in range(n):
            disk.append(-1)
    is_len = not is_len

l_pos = 0
r_pos = len(disk) - 1

while True:
    while disk[l_pos] != -1:
        l_pos += 1
    while disk[r_pos] == -1:
        r_pos -= 1
    if r_pos <= l_pos:
        break
    disk[l_pos] = disk[r_pos]
    disk[r_pos] = -1

l_pos = 0
ans = 0
while disk[l_pos] != -1:
    ans += l_pos * disk[l_pos]
    l_pos += 1

print(ans)
# aocd.submit(ans, part="a", day=9, year=2024)


disk = []

is_len = True
file_id = 0
for digit in data:
    n = int(digit)
    if is_len:
        for _ in range(n):
            disk.append(file_id)
        file_id += 1
    else:
        for _ in range(n):
            disk.append(-1)
    is_len = not is_len

r_pos = len(disk) - 1
while True:
    while disk[r_pos] == -1:
        r_pos -= 1
    if disk[r_pos] == 0:
        break
    file_id = disk[r_pos]
    r_pos2 = r_pos
    while disk[r_pos2 - 1] == file_id:
        r_pos2 -= 1

    run = 0
    for l_pos in range(0, r_pos2):
        if disk[l_pos] == -1:
            run += 1
            if run == (r_pos - r_pos2 + 1):
                # found space
                disk[l_pos-run + 1:l_pos + 1] = [file_id] * run
                disk[r_pos2:r_pos+1] = [-1] * run
                break
        else:
            run = 0

    r_pos = r_pos2 - 1

ans = 0
for l_pos, file_id in enumerate(disk):
    if file_id != -1:
        ans += l_pos * file_id

print(ans)
# aocd.submit(ans, part="b", day=9, year=2024)
