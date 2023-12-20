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
import math

data = aocd.get_data(day=20, year=2023)
# data = """broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a"""
# data = """broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output"""

modules = {}
for line in data.splitlines():
    part1, part2 = line.split(" -> ")
    if part1.startswith("%"): # flip-flop
        typ = part1[:1]
        name = part1[1:]
        state = False
    elif part1.startswith("&"): # conjunction
        typ = part1[:1]
        name = part1[1:]
        state = {}
    else:
        typ = None
        name = part1
        state = None
    outputs = part2.split(", ")
    modules[name] = [typ, outputs, state]

to_add = []
for name, parts in modules.items():
    typ, outputs, state = parts
    for output in outputs:
        if output not in modules:
            to_add.append(output)

for name in to_add:
    modules[name] = [None, [], None]

for name, parts in modules.items():
    typ, outputs, state = parts
    for output in outputs:
        output_typ, output_outputs, output_state = modules[output]
        if output_typ == "&":
            output_state[name] = False


def button(modules):
    lows, highs = 0, 0
    q = [("button", "broadcaster", False)]
    while q:
        origin, name, pulse = q[0]
        if pulse:
            highs += 1
        else:
            lows += 1
        del q[0]
        parts = modules[name]
        typ, outputs, state = parts

        if name == "broadcaster":
            for output in outputs:
                q.append((name, output, pulse))
        elif typ == "%":
            if not pulse:
                new_state = not state
                parts[2] = new_state
                for output in outputs:
                    q.append((name, output, new_state))
        elif typ == "&":
            state[origin] = pulse
            if all(state.values()):
                out_pulse = False
            else:
                out_pulse = True
            for output in outputs:
                q.append((name, output, out_pulse))
    return lows, highs

tot_low = 0
tot_high = 0
for _ in range(1000):
    lows, highs = button(modules)
    tot_low += lows
    tot_high += highs
ans = tot_low * tot_high
print(ans)

# aocd.submit(ans, part="a", day=20, year=2023)


modules = {}
for line in data.splitlines():
    part1, part2 = line.split(" -> ")
    if part1.startswith("%"): # flip-flop
        typ = part1[:1]
        name = part1[1:]
        state = False
    elif part1.startswith("&"): # conjunction
        typ = part1[:1]
        name = part1[1:]
        state = {}
    else:
        typ = None
        name = part1
        state = None
    outputs = part2.split(", ")
    modules[name] = [typ, outputs, state]

to_add = []
for name, parts in modules.items():
    typ, outputs, state = parts
    for output in outputs:
        if output not in modules:
            to_add.append(output)

for name in to_add:
    modules[name] = [None, [], None]

for name, parts in modules.items():
    typ, outputs, state = parts
    for output in outputs:
        output_typ, output_outputs, output_state = modules[output]
        if output_typ == "&":
            output_state[name] = False


def button(modules, presses):
    q = [("button", "broadcaster", False)]
    while q:
        origin, name, pulse = q[0]
        del q[0]

        if origin in ["lh", "fk", "ff", "mm"] and pulse:
            print(presses, origin, "-high-" if pulse else "-low-", ">", name)

        parts = modules[name]
        typ, outputs, state = parts

        if name == "broadcaster":
            for output in outputs:
                q.append((name, output, pulse))
        elif typ == "%":
            if not pulse:
                new_state = not state
                parts[2] = new_state
                for output in outputs:
                    q.append((name, output, new_state))
        elif typ == "&":
            state[origin] = pulse
            if all(state.values()):
                out_pulse = False
            else:
                out_pulse = True
            for output in outputs:
                q.append((name, output, out_pulse))


presses = 0
for _ in range(10000):
    presses += 1
    button(modules, presses)

print(math.lcm(3761, 3797, 3919, 4079))
