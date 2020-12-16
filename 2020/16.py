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

data = aocd.get_data(day=16, year=2020)


lines = data.splitlines()
i1 = lines.index("")
range_lines = lines[:i1]

dic = {}
for range_line in range_lines:
    field, rest = range_line.split(": ")
    range1, _, range2 = rest.split()
    a, b = [int(n) for n in range1.split("-")]
    c, d = [int(n) for n in range2.split("-")]
    dic[field] = [range(a, b+1), range(c, d+1)]

valid_tickets = []

total = 0
for ticket_line in lines[i1+5:]:
    nums = [int(n) for n in ticket_line.split(",")]

    ticket_valid = True
    for num in nums:
        flag = False
        for k, v in dic.items():
            for r in v:
                if num in r:
                    flag = True
        if not flag:
            ticket_valid = False
            total += num
    if ticket_valid:
        valid_tickets.append(nums)

print(total)

my_ticket = [int(n) for n in lines[i1+2].split(",")]

product = 1
possible = []
for n in range(len(my_ticket)):
    choices = []
    for k, v in dic.items():
        correct = True
        for t in valid_tickets:
            if t[n] not in v[0] and t[n] not in v[1]:
                correct = False
        if correct:
            choices.append(k)
    possible.append(choices)

for _ in range(len(my_ticket)):
    for n in range(len(my_ticket)):
        if len(possible[n]) == 1:
            if possible[n][0].startswith("departure"):
                product *= my_ticket[n]
            break
    chosen = possible[n][0]
    for n in range(len(my_ticket)):
        if chosen in possible[n]:
            possible[n].remove(chosen)
print(product)
