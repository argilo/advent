#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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

data = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
data = aocd.get_data(day=22, year=2020)

a = []
b = []
player = -1
for line in data.splitlines():
    if line == "Player 1:":
        player = 1
    elif line == "Player 2:":
        player = 2
    elif line == "":
        continue
    else:
        if player == 1:
            a.append(int(line))
        else:
            b.append(int(line))

while len(a) > 0 and len(b) > 0:
    if a[0] > b[0]:
        a = a[1:] + [a[0], b[0]]
        b = b[1:]
    else:
        b = b[1:] + [b[0], a[0]]
        a = a[1:]

if len(a) > 0:
    win = a
else:
    win = b

total = 0
for i, n in enumerate(win):
    total += (len(win) - i) * n
print(total)


a = []
b = []
player = -1
for line in data.splitlines():
    if line == "Player 1:":
        player = 1
    elif line == "Player 2:":
        player = 2
    elif line == "":
        continue
    else:
        if player == 1:
            a.append(int(line))
        else:
            b.append(int(line))


def play(a, b):
    prev = set()

    while len(a) > 0 and len(b) > 0:
        config = (tuple(a), tuple(b))
        if config in prev:
            return 1, a, b
        prev.add(config)

        if len(a) >= a[0] + 1 and len(b) >= b[0] + 1:
            winner = play(a[1:1+a[0]], b[1:1+b[0]])[0]
        else:
            winner = 1 if a[0] > b[0] else 2

        if winner == 1:
            a = a[1:] + [a[0], b[0]]
            b = b[1:]
        else:
            b = b[1:] + [b[0], a[0]]
            a = a[1:]

    if len(a) > 0:
        return 1, a, b
    else:
        return 2, a, b


winner, a, b = play(a, b)
if winner == 1:
    win = a
else:
    win = b

total = 0
for i, n in enumerate(win):
    total += (len(win) - i) * n
print(total)
