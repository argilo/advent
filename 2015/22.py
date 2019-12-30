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

spells = [
    ("Magic Missile", 53, 0),
    ("Drain",         73, 0),
    ("Shield",       113, 6),
    ("Poison",       173, 6),
    ("Recharge",     229, 5),
]


def play_me(state):
    global best, hard_mode

    if state in cache:
        return
    else:
        cache.add(state)

    mana, mana_spent, hp, boss_hp = state[5:9]

    if hard_mode:
        hp -= 1
        if hp <= 0:
            # lost
            return

    if state[3] > 0:
        boss_hp -= 3
    if state[4] > 0:
        mana += 101
    state = tuple(max(time-1, 0) for time in state[0:5]) \
        + (mana, mana_spent, hp, boss_hp)
    if boss_hp <= 0:
        if mana_spent < best:
            # won
            best = mana_spent
        return

    cast_something = False
    for i, spell in enumerate(spells):
        times = list(state[0:5])
        mana, mana_spent, hp, boss_hp = state[5:9]
        if times[i] == 0 and spell[1] <= mana:
            cast_something = True
            times[i] = spell[2]
            mana -= spell[1]
            mana_spent += spell[1]
            if spell[0] == "Magic Missile":
                boss_hp -= 4
            elif spell[0] == "Drain":
                boss_hp -= 2
                hp += 2
            new_state = tuple(times) + (mana, mana_spent, hp, boss_hp)
            if boss_hp <= 0:
                if mana_spent < best:
                    # won
                    best = mana_spent
            else:
                play_boss(new_state)
    if not cast_something:
        # lost
        return


def play_boss(state):
    global best

    mana, mana_spent, hp, boss_hp = state[5:9]
    if state[3] > 0:
        boss_hp -= 3
    if state[4] > 0:
        mana += 101
    state = tuple(max(time-1, 0) for time in state[0:5]) \
        + (mana, mana_spent, hp, boss_hp)
    if boss_hp <= 0:
        if mana_spent < best:
            # won
            best = mana_spent
        return

    damage = boss_dam
    if state[2] > 0:
        damage = max(damage-7, 1)
    hp -= damage

    new_state = state[0:5] + (mana, mana_spent, hp, boss_hp)
    if hp <= 0:
        # lost
        return
    play_me(new_state)


with open("22-input.txt") as f:
    boss_hp = int(f.readline().split()[2])
    boss_dam = int(f.readline().split()[1])

state = (0, 0, 0, 0, 0, 500, 0, 50, boss_hp)

best = 1000000
hard_mode = False
cache = set()
play_me(state)
print(best)

best = 1000000
hard_mode = True
cache = set()
play_me(state)
print(best)
