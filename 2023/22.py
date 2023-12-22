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
import copy

data = aocd.get_data(day=22, year=2023)
# data = """1,0,1~1,2,1
# 0,0,2~2,0,2
# 0,2,3~2,2,3
# 0,0,4~0,2,4
# 2,0,5~2,2,5
# 0,1,6~2,1,6
# 1,1,8~1,1,9"""

height = 400

vol = [[[None]*height for _ in range(10)] for _ in range(10)]
for x in range(10):
    for y in range(10):
        vol[x][y][0] = "-"


blocks = []
for i, line in enumerate(data.splitlines()):
    parts = line.split("~")
    x1, y1, z1 = [int(n) for n in parts[0].split(",")]
    x2, y2, z2 = [int(n) for n in parts[1].split(",")]
    block = []
    if x1 < x2:
        for x in range(x1, x2+1):
            block.append([x, y1, z1])
            vol[x][y1][z1] = i
    elif y1 < y2:
        for y in range(y1, y2+1):
            block.append([x1, y, z1])
            vol[x1][y][z1] = i
    else:
        for z in range(z1, z2+1):
            block.append([x1, y1, z])
            vol[x1][y1][z] = i
    blocks.append(block)


def drop(vol, blocks):
    while True:
        changed = False
        for i, block in enumerate(blocks):
            for x, y, z in block:
                if vol[x][y][z-1] not in (None, i):
                    break
            else:
                changed = True
                for x, y, z in block:
                    vol[x][y][z-1] = i
                    vol[x][y][z] = None
                for i in range(len(block)):
                    block[i][2] -= 1
        if not changed:
            break


def could_drop(vol, blocks, without):
    for i, block in enumerate(blocks):
        for x, y, z in block:
            if vol[x][y][z-1] not in (None, i, without):
                break
        else:
            return True
    return False


drop(vol, blocks)


ans = 0
for i in range(len(blocks)):
    if not could_drop(vol, blocks, i):
        ans += 1
print(ans)

# aocd.submit(ans, part="a", day=22, year=2023)


def drop_without(vol, blocks, without):
    for x, y, z in blocks[without]:
        vol[x][y][z] = None

    while True:
        changed = False
        for i, block in enumerate(blocks):
            if i == without:
                continue

            for x, y, z in block:
                if vol[x][y][z-1] not in (None, i):
                    break
            else:
                changed = True
                for x, y, z in block:
                    vol[x][y][z-1] = i
                    vol[x][y][z] = None
                for i in range(len(block)):
                    block[i][2] -= 1
        if not changed:
            break


ans = 0
for i in range(len(blocks)):
    new_vol = copy.deepcopy(vol)
    new_blocks = copy.deepcopy(blocks)
    drop_without(new_vol, new_blocks, i)

    for j in range(len(blocks)):
        if blocks[j] != new_blocks[j]:
            ans += 1
print(ans)

# aocd.submit(ans, part="b", day=22, year=2023)
