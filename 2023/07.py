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
import functools
from collections import Counter
import itertools


data = aocd.get_data(day=7, year=2023)
# data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""


card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def hand_type(hand):
    counts = Counter(hand)
    shape = sorted(counts.values())

    if shape == [5]:
        return 7
    if shape == [1, 4]:
        return 6
    if shape == [2, 3]:
        return 5
    if shape == [1, 1, 3]:
        return 4
    if shape == [1, 2, 2]:
        return 3
    if shape == [1, 1, 1, 2]:
        return 2
    return 1


def compare(first, second):
    first_type = hand_type(first[0])
    first_ranks = [card_rank[c] for c in first[0]]
    second_type = hand_type(second[0])
    second_ranks = [card_rank[c] for c in second[0]]

    if ([first_type] + first_ranks) > ([second_type] + second_ranks):
        return 1
    elif ([first_type] + first_ranks) < ([second_type] + second_ranks):
        return -1
    else:
        return 0

hands = []
for line in data.splitlines():
    hand = line.split()
    hand[1] = int(hand[1])
    hands.append(hand)

hands = sorted(hands, key=functools.cmp_to_key(compare))

ans = 0
for i, hand in enumerate(hands, 1):
    ans += i * hand[1]
print(ans)

# aocd.submit(ans, part="a", day=7, year=2023)


card_rank2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


@functools.cache
def hand_type2(hand):
    joker_offsets = []
    for i, c in enumerate(hand):
        if c == "J":
            joker_offsets.append(i)

    if len(joker_offsets) == 0:
        return hand_type(hand)

    best_type = 0
    for vals in itertools.product(card_rank.keys(), repeat=len(joker_offsets)):
        new_hand = list(hand)
        for i, v in zip(joker_offsets, vals):
            new_hand[i] = v
            typ = hand_type("".join(new_hand))
            best_type = max(best_type, typ)
    return best_type


def compare2(first, second):
    first_type = hand_type2(first[0])
    first_ranks = [card_rank2[c] for c in first[0]]
    second_type = hand_type2(second[0])
    second_ranks = [card_rank2[c] for c in second[0]]

    if ([first_type] + first_ranks) > ([second_type] + second_ranks):
        return 1
    elif ([first_type] + first_ranks) < ([second_type] + second_ranks):
        return -1
    else:
        return 0


hands = []
for line in data.splitlines():
    hand = line.split()
    hand[1] = int(hand[1])
    hands.append(hand)

hands = sorted(hands, key=functools.cmp_to_key(compare2))

ans = 0
for i, hand in enumerate(hands, 1):
    ans += i * hand[1]
print(ans)

# aocd.submit(ans, part="b", day=7, year=2023)
