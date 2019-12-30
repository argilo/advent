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

weapons = [
    ("Dagger",      8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer",  25, 6, 0),
    ("Longsword",  40, 7, 0),
    ("Greataxe",   74, 8, 0),
]

armors = [
    ("Leather",    13, 0, 1),
    ("Chainmail",  31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
]

rings = [
    ("Damage +1",  25, 1, 0),
    ("Damage +2",  50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
]


def fight(a, b):
    damage = max(a[1] - b[2], 1)
    b[0] -= damage


def play(a, b):
    a = a.copy()
    b = b.copy()
    while True:
        fight(a, b)
        if b[0] <= 0:
            return True
        fight(b, a)
        if a[0] <= 0:
            return False


with open("21-input.txt") as f:
    boss_hp = int(f.readline().split()[2])
    boss_damage = int(f.readline().split()[1])
    boss_armor = int(f.readline().split()[1])
    boss = [boss_hp, boss_damage, boss_armor]

iter = itertools.product(
    itertools.combinations(weapons, 1),
    itertools.chain(
        itertools.combinations(armors, 0),
        itertools.combinations(armors, 1)
    ),
    itertools.chain(
        itertools.combinations(rings, 0),
        itertools.combinations(rings, 1),
        itertools.combinations(rings, 2)
    )
)

least = 1000000
most = 0
for w, a, r in iter:
    items = w + a + r
    cost = sum(item[1] for item in items)
    dam = sum(item[2] for item in items)
    arm = sum(item[3] for item in items)
    if play([100, dam, arm], boss):
        if cost < least:
            least = cost
    else:
        if cost > most:
            most = cost
print(least)
print(most)
