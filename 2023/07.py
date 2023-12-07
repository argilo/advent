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
import collections
import itertools

data = aocd.get_data(day=7, year=2023)

Hand = collections.namedtuple("Hand", ["cards", "bid"])
hands = []
for line in data.splitlines():
    cards, bid = line.split()
    hands.append(Hand(list(cards), int(bid)))

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


def hand_type(cards):
    shape = sorted(collections.Counter(cards).values())

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
    if shape == [1, 1, 1, 1, 1]:
        return 1


def sort_key(hand):
    return hand_type(hand.cards), [card_rank[card] for card in hand.cards]


ans = sum(i * hand.bid for i, hand in enumerate(sorted(hands, key=sort_key), 1))
print(ans)

# aocd.submit(ans, part="a", day=7, year=2023)


card_rank["J"] = 1


def hand_type_jokers(cards):
    joker_offsets = [i for i, card in enumerate(cards) if card == "J"]

    if len(joker_offsets) in (0, 5):
        return hand_type(cards)

    best_type = 0
    for vals in itertools.product(card_rank.keys(), repeat=len(joker_offsets)):
        new_cards = cards.copy()
        for i, val in zip(joker_offsets, vals):
            new_cards[i] = val
            new_type = hand_type(new_cards)
            best_type = max(best_type, new_type)
    return best_type


def sort_key_jokers(hand):
    return hand_type_jokers(hand.cards), [card_rank[card] for card in hand.cards]


ans = sum(i * hand.bid for i, hand in enumerate(sorted(hands, key=sort_key_jokers), 1))
print(ans)

# aocd.submit(ans, part="b", day=7, year=2023)
