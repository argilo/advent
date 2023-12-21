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


data = aocd.get_data(day=21, year=2023)
# data = """...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ..........."""

board = []
occupied = set()
for r, row in enumerate(data.splitlines()):
    for c, cell in enumerate(row):
        if cell == "S":
            occupied.add((r, c))
    board.append(row.replace("S", "."))


def step(board, occupied):
    height = len(board)
    width = len(board[0])
    new_occupied = set()
    for r in range(height):
        for c in range(width):
            if board[r][c] == ".":
                adjacent = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for adj in adjacent:
                    if adj in occupied:
                        new_occupied.add((r, c))
                        break
    return new_occupied


for _ in range(64):
    occupied = step(board, occupied)

ans = len(occupied)
print(ans)

# aocd.submit(ans, part="a", day=21, year=2023)

board = []
occupied = set()
for r, row in enumerate(data.splitlines()):
    for c, cell in enumerate(row):
        if cell == "S":
            occupied.add((r, c))
    board.append(row.replace("S", "."))


def step(board, occupied):
    height = len(board)
    width = len(board[0])
    new_occupied = set()

    for r, c in occupied:
        for a_r, a_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if board[a_r % height][a_c % width] == ".":
                new_occupied.add((a_r, a_c))
    return new_occupied


# n = 0
# height = len(board)
# width = len(board[0])
# for _ in range(500):
#     occupied = step(board, occupied)
#     n += 1
#     num_occ = len(occupied)
#     print(n, num_occ)

#     min_r, max_r = 1000000, -1000000
#     min_c, max_c = 1000000, -1000000
#     for r, c in occupied:
#         min_r = min(r, min_r)
#         max_r = max(r, max_r)
#         min_c = min(c, min_c)
#         max_c = max(c, max_c)

#     for r in range(min_r, max_r+1):
#         for c in range(min_c, max_c+1):
#             if (r, c) in occupied:
#                 print("O", end="")
#             else:
#                 print(board[r % height][c % width], end="")
#         print()
#     print()


n = 0
height = len(board)
width = len(board[0])

dic = {}
for rr in range(-2, 3):
    for cc in range(-2, 3):
        dic[(rr, cc)] = [0]

for _ in range(400):
    occupied = step(board, occupied)
    n += 1
    n_occ = len(occupied)
    print(f"{n:>3} {n_occ:>6}", end="  ")

    for rr in range(-2, 3):
        for cc in range(-2, 3):
            filled = 0
            for r in range(rr * height, (rr+1) * height):
                for c in range(cc * width, (cc+1) * width):
                    if (r, c) in occupied:
                        filled += 1
            print(f"{filled:>5}", end=" ")
            dic[(rr, cc)].append(filled)
    print()


for rr in range(-2, 3):
    for cc in range(-2, 3):
        seq = dic[(rr, cc)]
        for i, s in enumerate(seq):
            if s > 0:
                print(f"{i:>3}", end=" ")
                break
    print()


def start_n(rr, cc):
    a, b = sorted([abs(rr), abs(cc)])
    if b == 0:
        return 1
    elif a == 0:
        return b * 131 - 65
    else:
        return (a + b - 1) * 131 + 1


def num_in(n, rr, cc, dic):
    st = start_n(rr, cc)
    diff = n - st
    if diff < 0:
        return 0

    if diff >= 262:
        diff = 262 + (diff % 2)

    if rr == cc == 0:
        return dic[(0, 0)][1+diff]
    elif rr == 0 and cc > 0:
        return dic[(0, 1)][66+diff]
    elif rr == 0 and cc < 0:
        return dic[(0, -1)][66+diff]
    elif rr > 0 and cc == 0:
        return dic[(1, 0)][66+diff]
    elif rr < 0 and cc == 0:
        return dic[(-1, 0)][66+diff]
    elif rr > 0 and cc > 0:
        return dic[(1, 1)][132+diff]
    elif rr > 0 and cc < 0:
        return dic[(1, -1)][132+diff]
    elif rr < 0 and cc > 0:
        return dic[(-1, 1)][132+diff]
    elif rr < 0 and cc < 0:
        return dic[(-1, -1)][132+diff]




def calc(n, dic):
    tot = 0
    for rr in range(-3, 4):
        for cc in range(-3, 4):
            tot += num_in(n, rr, cc, dic)
    return tot


for n in range(1, 400):
    print(n, calc(n, dic))


target = 26501365
target_div = 202300

ans = 0
ans += num_in(target, 0, target_div, dic)
ans += num_in(target, 0, -target_div, dic)
ans += num_in(target, target_div, 0, dic)
ans += num_in(target, -target_div, 0, dic)
ans += (target_div-1) * num_in(target, 1, target_div-1, dic)
ans += (target_div-1) * num_in(target, -1, target_div-1, dic)
ans += (target_div-1) * num_in(target, 1, 1-target_div, dic)
ans += (target_div-1) * num_in(target, -1, 1-target_div, dic)
ans += (target_div) * num_in(target, 1, target_div, dic)
ans += (target_div) * num_in(target, -1, target_div, dic)
ans += (target_div) * num_in(target, 1, -target_div, dic)
ans += (target_div) * num_in(target, -1, -target_div, dic)

ans += num_in(target, 0, 0, dic)

for n in range(1, target_div):
    ans += (4*n) * num_in(target, 0, n%2, dic)

print("ans=", ans)


# after 129 steps, reach steady state in 131x131 cell.


# aocd.submit(ans, part="b", day=21, year=2023)
