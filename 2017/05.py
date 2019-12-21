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

message = []
for line in open("05-input.txt"):
    n = int(line.rstrip())
    message.append(n)

offset = 0
steps = 0
while True:
    steps += 1
    new_offset = offset + message[offset]
    if new_offset < 0 or new_offset >= len(message):
        break
    message[offset] += 1
    offset = new_offset
print(steps)


message = []
for line in open("05-input.txt"):
    n = int(line.rstrip())
    message.append(n)

offset = 0
steps = 0
while True:
    steps += 1
    new_offset = offset + message[offset]
    if new_offset < 0 or new_offset >= len(message):
        break
    if message[offset] >= 3:
        message[offset] -= 1
    else:
        message[offset] += 1
    offset = new_offset
print(steps)
