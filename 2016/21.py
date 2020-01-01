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

import itertools


def scramble(str, rules):
    chars = list(str)
    for rule in rules:
        if rule[0] == "swap":
            if rule[1] == "position":
                a, b = int(rule[2]), int(rule[5])
            elif rule[1] == "letter":
                a, b = chars.index(rule[2]), chars.index(rule[5])
            chars[a], chars[b] = chars[b], chars[a]
        elif rule[0] == "rotate":
            if rule[1] == "left":
                amt = len(chars) - int(rule[2])
            elif rule[1] == "right":
                amt = int(rule[2])
            elif rule[1] == "based":
                index = chars.index(rule[6])
                amt = 1 + index + (index >= 4)
            amt %= len(chars)
            chars = chars[-amt:] + chars[:-amt]
        elif rule[0] == "reverse":
            start, end = int(rule[2]), int(rule[4])
            chars = chars[:start] + chars[start:end+1][::-1] + chars[end+1:]
        elif rule[0] == "move":
            a, b = int(rule[2]), int(rule[5])
            tmp = chars[a]
            del chars[a]
            chars.insert(b, tmp)
    return "".join(chars)


def unscramble(str, rules):
    for p in itertools.permutations(str):
        inp = "".join(p)
        if scramble(inp, rules) == str:
            return inp


rules = []
for line in open("21-input.txt"):
    rules.append(line.split())

print(scramble("abcdefgh", rules))
print(unscramble("fbgdceah", rules))
