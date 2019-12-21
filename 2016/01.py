#!/usr/bin/env python3

# Copyright 2019 Clayton Smith
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

with open("01-input.txt") as f:
    data = f.read().rstrip()

visited = {}
visited_twice = None
direction = 0
x, y = 0, 0
for command in data.split(", "):
    turn, dist = command[0], int(command[1:])
    direction = (direction + (1 if turn == "R" else -1)) % 4

    for _ in range(dist):
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1

        if not visited_twice and (x, y) in visited:
            visited_twice = (x, y)
        else:
            visited[(x, y)] = True

print(abs(x) + abs(y))
print(abs(visited_twice[0]) + abs(visited_twice[1]))
