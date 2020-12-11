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
import copy

data = aocd.get_data(day=11, year=2020)

seats = []
for line in data.splitlines():
    seats.append(list("." + line + "."))
seats.append(["."] * len(seats[0]))
seats.insert(0, ["."] * len(seats[0]))

while True:
    new_seats = copy.deepcopy(seats)
    for row in range(1, len(seats) - 1):
        for col in range(1, len(seats[row]) - 1):
            adjacent = [
                seats[row-1][col-1],
                seats[row-1][col],
                seats[row-1][col+1],
                seats[row][col-1],
                seats[row][col+1],
                seats[row+1][col-1],
                seats[row+1][col],
                seats[row+1][col+1],
            ]
            if seats[row][col] == "L":
                if "#" not in adjacent:
                    new_seats[row][col] = "#"
            elif seats[row][col] == "#":
                if adjacent.count("#") >= 4:
                    new_seats[row][col] = "L"
    if seats == new_seats:
        break
    seats = new_seats

ans = 0
for row in range(1, len(seats) - 1):
    for col in range(1, len(seats[row]) - 1):
        if new_seats[row][col] == "#":
            ans += 1

print(ans)
# aocd.submit(ans, part="a", day=11, year=2020)


data = aocd.get_data(day=11, year=2020)

seats = []
for line in data.splitlines():
    seats.append(list("." + line + "."))
seats.append(["."] * len(seats[0]))
seats.insert(0, ["."] * len(seats[0]))

while True:
    new_seats = copy.deepcopy(seats)
    for row in range(1, len(seats) - 1):
        for col in range(1, len(seats[row]) - 1):
            dir = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
            adjacent = []
            for dr, dc in dir:
                dist = 0
                try:
                    while True:
                        dist += 1
                        r1, c1 = row + dr*dist, col + dc*dist
                        if r1 < 0 or c1 < 0:
                            adjacent.append(".")
                            break
                        if seats[r1][c1] == "#":
                            adjacent.append("#")
                            break
                        if seats[r1][c1] == "L":
                            adjacent.append("L")
                            break
                except IndexError:
                    adjacent.append(".")

            if seats[row][col] == "L":
                if "#" not in adjacent:
                    new_seats[row][col] = "#"
            elif seats[row][col] == "#":
                if adjacent.count("#") >= 5:
                    new_seats[row][col] = "L"
    if seats == new_seats:
        break
    seats = new_seats

ans = 0
for row in range(1, len(seats) - 1):
    for col in range(1, len(seats[row]) - 1):
        if new_seats[row][col] == "#":
            ans += 1

print(ans)
# aocd.submit(ans, part="b", day=11, year=2020)
