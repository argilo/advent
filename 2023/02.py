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

data = aocd.get_data(day=2, year=2023)
# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

have = [12, 13, 14]
ans = 0
for line in data.splitlines():
    game_no, games = line.split(": ")
    game_no = int(game_no.split(" ")[1])

    good = True
    for game in games.split("; "):
        drawn = [0, 0, 0]
        for piece in game.split(", "):
            num, color = piece.split(" ")
            num = int(num)
            if color == "red":
                drawn[0] += num
            elif color == "green":
                drawn[1] += num
            elif color == "blue":
                drawn[2] += num
        if drawn[0] > have[0] or drawn[1] > have[1] or drawn[2] > have[2]:
            good = False

    if good:
        ans += game_no

print(ans)
# aocd.submit(ans, part="a", day=2, year=2023)

ans = 0
for line in data.splitlines():
    fewest = [0, 0, 0]
    game_no, games = line.split(": ")
    game_no = int(game_no.split(" ")[1])

    for game in games.split("; "):
        drawn = [0, 0, 0]
        for piece in game.split(", "):
            num, color = piece.split(" ")
            num = int(num)
            if color == "red":
                drawn[0] += num
            elif color == "green":
                drawn[1] += num
            elif color == "blue":
                drawn[2] += num
        fewest[0] = max(fewest[0], drawn[0])
        fewest[1] = max(fewest[1], drawn[1])
        fewest[2] = max(fewest[2], drawn[2])

    ans += fewest[0] * fewest[1] * fewest[2]

print(ans)
# aocd.submit(ans, part="b", day=2, year=2023)
