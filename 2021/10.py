#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=10, year=2021)
# data = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]"""

pair = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

points2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

tot = 0
scores = []
for line in data.splitlines():
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        elif c in [")", "]", "}", ">"]:
            if stack[-1] != pair[c]:
                tot += points[c]
                break
            else:
                stack.pop()
    else:
        score = 0
        for c in stack[::-1]:
            score *= 5
            score += points2[c]
        scores.append(score)
print(tot)
# aocd.submit(tot, part="a", day=10, year=2021)

scores.sort()
ans = scores[len(scores)//2]
print(ans)
# aocd.submit(ans, part="b", day=10, year=2021)
