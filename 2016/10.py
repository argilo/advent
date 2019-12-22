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


def give(type, num, value):
    if type == "bot":
        if num not in bots:
            bots[num] = []
        bots[num].append(value)
        bots[num].sort()
    elif type == "output":
        outputs[num] = value


bots = {}
bot_gives = {}
for line in open("10-input.txt"):
    parts = line.rstrip().split()
    if parts[0] == "value":
        value, bot = int(parts[1]), int(parts[5])
        give("bot", bot, value)
    elif parts[0] == "bot":
        in_bot = int(parts[1])
        type1, type2 = parts[5], parts[10]
        out1, out2 = int(parts[6]), int(parts[11])
        bot_gives[in_bot] = (type1, out1, type2, out2)

outputs = {}
while True:
    for bot, values in bots.items():
        if len(values) == 2:
            if values == [17, 61]:
                print(bot)
            gives = bot_gives[bot]
            give(gives[0], gives[1], values[0])
            give(gives[2], gives[3], values[1])
            bots[bot] = []
            break
    else:
        break

print(outputs[0] * outputs[1] * outputs[2])
