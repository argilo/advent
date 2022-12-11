#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=11, year=2022)

lines = [line for line in data.split("\n") if len(line) > 0]
monkeys = []
for line in lines:
    if line.startswith("Monkey"):
        monkey = {"inspected": 0}
    elif line.startswith("  Starting"):
        monkey["items"] = [int(n) for n in line[18:].split(", ")]
    elif line.startswith("  Operation"):
        op_parts = line[23:].split(" ")
        if op_parts[1] != "old":
            op_parts[1] = int(op_parts[1])
        monkey["op"] = op_parts[0]
        monkey["operand"] = op_parts[1]
    elif line.startswith("  Test"):
        monkey["div"] = int(line[21:])
    elif line.startswith("    If true"):
        monkey["true"] = int(line[29:])
    elif line.startswith("    If false"):
        monkey["false"] = int(line[30:])
        monkeys.append(monkey)

for round in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            monkey["inspected"] += 1
            worry = item
            operand = monkey["operand"]
            if operand == "old":
                operand = worry
            op = monkey["op"]
            if op == "*":
                worry = worry * operand
            elif op == "+":
                worry = worry + operand
            worry = worry // 3
            div = monkey["div"]
            if worry % div == 0:
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)
            monkey["items"] = []

insp = [monkey["inspected"] for monkey in monkeys]
insp.sort()
print(insp[-2] * insp[-1])


lines = [line for line in data.split("\n") if len(line) > 0]
monkeys = []
prod = 1
for line in lines:
    if line.startswith("Monkey"):
        monkey = {"inspected": 0}
    elif line.startswith("  Starting"):
        monkey["items"] = [int(n) for n in line[18:].split(", ")]
    elif line.startswith("  Operation"):
        op_parts = line[23:].split(" ")
        if op_parts[1] != "old":
            op_parts[1] = int(op_parts[1])
        monkey["op"] = op_parts[0]
        monkey["operand"] = op_parts[1]
    elif line.startswith("  Test"):
        monkey["div"] = int(line[21:])
        prod *= monkey["div"]
    elif line.startswith("    If true"):
        monkey["true"] = int(line[29:])
    elif line.startswith("    If false"):
        monkey["false"] = int(line[30:])
        monkeys.append(monkey)

for round in range(10000):
    for monkey in monkeys:
        for item in monkey["items"]:
            monkey["inspected"] += 1
            worry = item
            operand = monkey["operand"]
            if operand == "old":
                operand = worry
            op = monkey["op"]
            if op == "*":
                worry = (worry * operand) % prod
            elif op == "+":
                worry = (worry + operand) % prod
            div = monkey["div"]
            if worry % div == 0:
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)
            monkey["items"] = []

insp = [monkey["inspected"] for monkey in monkeys]
insp.sort()
print(insp[-2] * insp[-1])
