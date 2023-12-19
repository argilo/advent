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
import copy

data = aocd.get_data(day=19, year=2023)


def parse_rule(rule):
    if ":" in rule:
        cond, dest = rule.split(":")
        return (cond[0], cond[1], int(cond[2:]), dest)
    else:
        return (None, None, None, rule)


part2 = False
rulebook = {}
ans = 0
for line in data.splitlines():
    if line == "":
        part2 = True

    elif not part2:
        name, rest = line.split("{")
        rules = rest[:-1].split(",")
        rules = [parse_rule(rule) for rule in rules]
        rulebook[name] = rules

    else:
        parts = line[1:-1].split(",")
        vals = {}
        for part in parts:
            var, val = part.split("=")
            val = int(val)
            vals[var] = val

        cur_rule = "in"
        while cur_rule not in ("A", "R"):
            rules = rulebook[cur_rule]
            for var, op, val, dest in rules:
                if op is None:
                    cur_rule = dest
                    break
                elif op == "<":
                    if vals[var] < val:
                        cur_rule = dest
                        break
                elif op == ">":
                    if vals[var] > val:
                        cur_rule = dest
                        break

        if cur_rule == "A":
            for var, val in vals.items():
                ans += val
print(ans)

# aocd.submit(ans, part="a", day=19, year=2023)

final_sum = 0


def explore(start_rule, allowed):
    global final_sum
    if start_rule == "A":
        prod = 1
        for k, v in allowed.items():
            prod *= sum(v)
        final_sum += prod
    elif start_rule == "R":
        pass
    else:
        rules = rulebook[start_rule]
        for var, op, val, dest in rules:
            if op is None:
                explore(dest, allowed)
                break
            elif op == "<":
                new_allowed = copy.deepcopy(allowed)
                for n in range(val, 4001):
                    new_allowed[var][n] = 0
                if sum(new_allowed[var]) > 0:
                    explore(dest, new_allowed)
                for n in range(1, val):
                    allowed[var][n] = 0
            elif op == ">":
                new_allowed = copy.deepcopy(allowed)
                for n in range(1, val+1):
                    new_allowed[var][n] = 0
                if sum(new_allowed[var]) > 0:
                    explore(dest, new_allowed)
                for n in range(val+1, 4001):
                    allowed[var][n] = 0


allowed = {
    "x": [0] + [1] * 4000,
    "m": [0] + [1] * 4000,
    "a": [0] + [1] * 4000,
    "s": [0] + [1] * 4000,
}
explore("in", allowed)

print(final_sum)

# aocd.submit(final_sum, part="b", day=19, year=2023)
