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

data = aocd.get_data(day=14, year=2022)
# data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9"""

board = {}
max_r = 0
min_c = 1000000
max_c = -1000000
for line in data.split("\n"):
    parts = []
    for part in line.split(" -> "):
        c, r = [int(n) for n in part.split(",")]
        if r > max_r:
            max_r = r
        if c < min_c:
            min_c = c
        if c > max_c:
            max_c = c
        parts.append((c, r))

    for n in range(len(parts) - 1):
        sc, sr = parts[n]
        ec, er = parts[n+1]
        if sc == ec:
            if sr > er:
                sr, er = er, sr
            assert(sr < er)
            for r in range(sr, er+1):
                board[(sc, r)] = "#"
        if sr == er:
            if sc > ec:
                sc, ec = ec, sc
            assert(sc < ec)
            for c in range(sc, ec+1):
                board[(c, sr)] = "#"

done = False
ans = 0
while not done:
    sandc, sandr = 500, 0
    while True:
        if sandr == max_r:
            done = True
            break
        if (sandc, sandr + 1) not in board:
            sandr += 1
        elif (sandc - 1, sandr + 1) not in board:
            sandc -= 1
            sandr += 1
        elif (sandc + 1, sandr + 1) not in board:
            sandc += 1
            sandr += 1
        else:
            board[(sandc, sandr)] = "o"
            ans += 1
            break

for r in range(0, max_r + 1):
    for c in range(min_c, max_c + 1):
        if (c, r) in board:
            print(board[c, r], end="")
        else:
            print(".", end="")
    print()

print(ans)

# aocd.submit(ans, part="a", day=14, year=2022)

board = {}
max_r = 0
min_c = 1000000
max_c = -1000000
for line in data.split("\n"):
    parts = []
    for part in line.split(" -> "):
        c, r = [int(n) for n in part.split(",")]
        if r > max_r:
            max_r = r
        if c < min_c:
            min_c = c
        if c > max_c:
            max_c = c
        parts.append((c, r))

    for n in range(len(parts) - 1):
        sc, sr = parts[n]
        ec, er = parts[n+1]
        if sc == ec:
            if sr > er:
                sr, er = er, sr
            assert(sr < er)
            for r in range(sr, er+1):
                board[(sc, r)] = "#"
        if sr == er:
            if sc > ec:
                sc, ec = ec, sc
            assert(sc < ec)
            for c in range(sc, ec+1):
                board[(c, sr)] = "#"

max_r += 2
min_c = min(min_c, 500 - max_r)
max_c = max(max_c, 500 + max_r)

for c in range(min_c, max_c + 1):
    board[(c, max_r)] = "#"

done = False
ans = 0
while not done:
    sandc, sandr = 500, 0
    while True:
        if (sandc, sandr) in board:
            done = True
            break
        if (sandc, sandr + 1) not in board:
            sandr += 1
        elif (sandc - 1, sandr + 1) not in board:
            sandc -= 1
            sandr += 1
        elif (sandc + 1, sandr + 1) not in board:
            sandc += 1
            sandr += 1
        else:
            board[(sandc, sandr)] = "o"
            ans += 1
            break

for r in range(0, max_r + 1):
    for c in range(min_c, max_c + 1):
        if (c, r) in board:
            print(board[c, r], end="")
        else:
            print(".", end="")
    print()

print(ans)

# aocd.submit(ans, part="b", day=14, year=2022)
