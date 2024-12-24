#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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
import random

data = aocd.get_data(day=24, year=2024)

# data = """x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0

# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02"""

# data = """x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1

# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj"""

wire_list, gate_list = data.split("\n\n")

wires = {}
for line in wire_list.splitlines():
    name, value = line.split(": ")
    value = int(value)
    wires[name] = value

gates = []
for line in gate_list.splitlines():
    w1, typ, w2, _, w3 = line.split()
    if w1 not in wires:
        wires[w1] = None
    if w2 not in wires:
        wires[w2] = None
    if w3 not in wires:
        wires[w3] = None
    gates.append((typ, w1, w2, w3))

while list(wires.values()).count(None) > 0:
    for typ, w1, w2, w3 in gates:
        # print(typ, w1, wires[w1], w2, wires[w2], w3, wires[w3])
        if wires[w3] is None:
            if (wires[w1] is not None) and (wires[w2] is not None):
                if typ == "AND":
                    wires[w3] = wires[w1] & wires[w2]
                elif typ == "OR":
                    wires[w3] = wires[w1] | wires[w2]
                elif typ == "XOR":
                    wires[w3] = wires[w1] ^ wires[w2]

bit = 0
ans = 0
while f"z{bit:02}" in wires:
    ans |= (wires[f"z{bit:02}"] << bit)
    bit += 1

print(ans)
# aocd.submit(ans, part="a", day=24, year=2024)


# print(data)


swaps = [
    "z07", "swt",
    "z13", "pqc",
    "rjm", "wsv",
    "z31", "bgs"
]
print(",".join(sorted(swaps)))
exit()


def rename(a, b):
    wires[b] = wires[a]
    del wires[a]

    for i in range(len(gates)):
        typ, w1, w2, w3 = gates[i]
        if w1 == a:
            w1 = b
        if w2 == a:
            w2 = b
        if w3 == a:
            w3 = b
        gates[i] = (typ, w1, w2, w3)


def add(x, y):
    for wire in wires:
        if wire.startswith("x"):
            bit = int(wire[1:])
            wires[wire] = (x >> bit) & 1
        elif wire.startswith("y"):
            bit = int(wire[1:])
            wires[wire] = (y >> bit) & 1
        else:
            wires[wire] = None

    while list(wires.values()).count(None) > 0:
        good = False
        for typ, w1, w2, w3 in gates:
            # print(typ, w1, wires[w1], w2, wires[w2], w3, wires[w3])
            if wires[w3] is None:
                if (wires[w1] is not None) and (wires[w2] is not None):
                    good = True
                    if typ == "AND":
                        wires[w3] = wires[w1] & wires[w2]
                    elif typ == "OR":
                        wires[w3] = wires[w1] | wires[w2]
                    elif typ == "XOR":
                        wires[w3] = wires[w1] ^ wires[w2]
        if not good:
            return None

    bit = 0
    result = 0
    while f"z{bit:02}" in wires:
        result |= (wires[f"z{bit:02}"] << bit)
        bit += 1

    return result


# for g1 in range(0, len(gates)-1):
#     print(g1)
#     for g2 in range(g1+1, len(gates)):
#         gates[g1], gates[g2] = gates[g1][:3] + gates[g2][3:], gates[g2][:3] + gates[g1][3:]

#         bits = 2
#         correct = 0
#         for x in range(1 << bits):
#             for y in range(1 << bits):
#                 if add(x, y) == (x+y):
#                     correct += 1
#                 # print(x, y, add(x, y), add(x, y) == (x+y))
#         print(correct)
#         if correct == (1 << (2*bits)):
#             print(g1, g2)

#         gates[g1], gates[g2] = gates[g1][:3] + gates[g2][3:], gates[g2][:3] + gates[g1][3:]


# for typ, w1, w2, w3 in gates:
#     if not w3.startswith("z"):
#         if typ == "XOR" and w1.startswith("x") and w2.startswith("y") and w1[1:] == w2[1:]:
#             rename(w3, f"sum{w1[1:]}")

#         if typ == "XOR" and w1.startswith("y") and w2.startswith("x") and w1[1:] == w2[1:]:
#             rename(w3, f"sum{w1[1:]}")

#         if typ == "AND" and w1.startswith("x") and w2.startswith("y") and w1[1:] == w2[1:]:
#             rename(w3, f"and{w1[1:]}")

#         if typ == "AND" and w1.startswith("y") and w2.startswith("x") and w1[1:] == w2[1:]:
#             rename(w3, f"and{w1[1:]}")

# rename("brj", "c00")
# rename("and00", "c00")

# rename("thc", "sum1")
# rename("hhp", "sum2")


seen = set()


def back(out):
    count = 0
    todo = [out]
    while todo:
        next_todo = []
        for output in todo:
            for typ, w1, w2, w3 in gates:
                if w3 == output:
                    if (typ, w1, w2, w3) not in seen:
                        # if out == "z07":
                        print(w1, typ, w2, "->", w3)
                        count += 1
                        seen.add((typ, w1, w2, w3))
                    if not w1.startswith("x") and not w1.startswith("y"):
                        next_todo.append(w1)
                    if not w2.startswith("x") and not w2.startswith("y"):
                        next_todo.append(w2)
        todo = next_todo
    # if count == 5:
    #     exit()


def swapout(out1, out2):
    for i in range(len(gates)):
        if gates[i][3] == out1:
            i1 = i
        if gates[i][3] == out2:
            i2 = i

    gates[i1] = gates[i1][:3] + (out2,)
    gates[i2] = gates[i2][:3] + (out1,)


def is_good(bits):
    for _ in range(1000):
        x = random.randrange(0, (1 << bits))
        y = random.randrange(0, (1 << bits))
        sm = add(x, y)
        if sm is None:
            return False
        sm = sm & ((1 << bits) - 1)
        if sm != (x+y) & ((1 << bits) - 1):
            # print(x, y, sm)
            return False
    return True


swapout("z07", "swt")
swapout("z13", "pqc")
swapout("rjm", "wsv")
swapout("z31", "bgs")

print(is_good(45))

for _, _, _, w3 in gates:
    swapout("z31", w3)
    if is_good(32):
        print(w3)
    swapout("z31", w3)

exit()

seen.clear()
back("z00")
print()
back("z01")
print()
back("z02")
print()
back("z03")
print()
back("z04")
print()
back("z05")
print()
back("z06")
print()
back("z07")
print()
back("z08")
print()
back("z09")
print()
back("z10")
print()
back("z11")
print()
back("z12")
print()
back("z13")
print()
back("z14")
print()
back("z15")
print()
back("z16")
print()
back("z17")
print()
back("z18")
print()
back("z19")
print()
back("z20")
print()
back("z21")
print()
back("z22")
print()
back("z23")
print()
back("z24")
print()
back("z25")
print()
back("z26")
print()
back("z27")
print()
back("z28")
print()
back("z29")
print()
back("z30")
print()
back("z31")
print()

for gate in gates:
    if gate not in seen:
        print(gate)


# for _, _, _, w3 in gates:
#     print(w3)
#     swapout("z07", w3)

#     seen.clear()
#     back("z00")
#     print()
#     back("z01")
#     print()
#     back("z02")
#     print()
#     back("z03")
#     print()
#     back("z04")
#     print()
#     back("z05")
#     print()
#     back("z06")
#     print()
#     back("z07")
#     print()

#     swapout("z07", w3)


# aocd.submit(ans, part="b", day=24, year=2024)
