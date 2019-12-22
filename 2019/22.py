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


def mul_inv(a, b):
    """Compute the multiplicative inverse of a modulo b"""
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


deck_len = 10007
deck = list(range(deck_len))

for line in open("22-input.txt"):
    line = line.rstrip()
    if line == "deal into new stack":
        deck = deck[::-1]
    elif line.startswith("deal with increment"):
        increment = int(line.split()[3])
        new_deck = [0] * deck_len
        for i, card in enumerate(deck):
            new_deck[(i * increment) % deck_len] = card
        deck = new_deck
    elif line.startswith("cut"):
        cut = int(line.split()[1])
        deck = deck[cut:] + deck[:cut]

print(deck.index(2019))


deck_len = 119315717514047
deck_start = 0
deck_inc = 1
repeat = 101741582076661

for line in open("22-input.txt"):
    line = line.rstrip()
    if line == "deal into new stack":
        deck_start = (deck_start - deck_inc) % deck_len
        deck_inc = (-deck_inc) % deck_len
    elif line.startswith("deal with increment"):
        increment = int(line.split()[3])
        deck_inc = (deck_inc * mul_inv(increment, deck_len)) % deck_len
    elif line.startswith("cut"):
        cut = int(line.split()[1])
        deck_start = (deck_start + cut * deck_inc) % deck_len

deck_start = (deck_start * (pow(deck_inc, repeat, deck_len) - 1) * mul_inv(deck_inc - 1, deck_len)) % deck_len
deck_inc = pow(deck_inc, repeat, deck_len)
print((deck_start + 2020*deck_inc) % deck_len)
