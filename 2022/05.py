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

data = aocd.get_data(day=5, year=2022)

lines = data.split("\n")
blank = lines.index("")
cols = len(lines[blank-1]) // 4 + 1

stacks = [list() for _ in range(cols)]
for i in range(blank-2, -1, -1):
    line = lines[i]
    while len(line) < cols * 4 - 1:
        line = line + " "
    for j in range(cols):
        ch = j * 4 + 1
        if line[ch] != " ":
            stacks[j].append(line[ch])

for i in range(blank+1, len(lines)):
    line = lines[i].split()
    num = int(line[1])
    f = int(line[3])
    t = int(line[5])
    for x in range(num):
        tmp = stacks[f-1].pop()
        stacks[t-1].append(tmp)

ans = ""
for stack in stacks:
    if len(stack) > 0:
        ans += stack[-1]
print(ans)

# aocd.submit(ans, part="a", day=5, year=2022)

stacks = [list() for _ in range(cols)]
for i in range(blank-2, -1, -1):
    line = lines[i]
    while len(line) < cols * 4 - 1:
        line = line + " "
    for j in range(cols):
        ch = j * 4 + 1
        if line[ch] != " ":
            stacks[j].append(line[ch])

for i in range(blank+1, len(lines)):
    line = lines[i].split()
    num = int(line[1])
    f = int(line[3])
    t = int(line[5])
    tmp = []
    for x in range(num):
        tmp.append(stacks[f-1].pop())
    for x in range(num):
        stacks[t-1].append(tmp[num-x-1])

ans = ""
for stack in stacks:
    if len(stack) > 0:
        ans += stack[-1]
print(ans)

# aocd.submit(ans, part="b", day=5, year=2022)
