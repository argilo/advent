#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=21, year=2021)
lines = data.splitlines()

last_roll = 100
num_rolls = 0
def die_roll_1():
    global last_roll, num_rolls
    num_rolls += 1
    last_roll += 1
    if last_roll > 100:
        last_roll -= 100
    return last_roll

p_loc = [None, None]
p_loc[0] = int(lines[0].split()[4])
p_loc[1] = int(lines[1].split()[4])
# p_loc = [4, 8]

p_score = [0, 0]

player = 0
while max(p_score) < 1000:
    rolls = [die_roll_1(), die_roll_1(), die_roll_1()]
    p_loc[player] += sum(rolls)
    while p_loc[player] > 10:
        p_loc[player] -= 10
    p_score[player] += p_loc[player]
    player = (player + 1) % 2


ans = num_rolls * min(p_score)
print(ans)

# aocd.submit(ans, part="a", day=21, year=2021)

die_roll_2 = [0]*10

for d1 in (1, 2, 3):
    for d2 in (1, 2, 3):
        for d3 in (1, 2, 3):
            die_roll_2[d1+d2+d3] += 1

dic = {}
def play(player, p_loc, p_score):
    tp = (player, tuple(p_loc), tuple(p_score))
    if tp in dic:
        return dic[tp]
    wins = [0, 0]
    for d_sum in range(3, 10):
        d_paths = die_roll_2[d_sum]

        new_p_loc = p_loc.copy()
        new_p_loc[player] += d_sum
        while new_p_loc[player] > 10:
            new_p_loc[player] -= 10

        new_p_score = p_score.copy()
        new_p_score[player] += new_p_loc[player]

        if new_p_score[player] >= 21:
            wins[player] += d_paths
        else:
            new_player = (player + 1) % 2
            new_wins = play(new_player, new_p_loc, new_p_score)

            wins[0] += d_paths * new_wins[0]
            wins[1] += d_paths * new_wins[1]

    dic[tp] = wins
    return wins

p_loc = [None, None]
p_loc[0] = int(lines[0].split()[4])
p_loc[1] = int(lines[1].split()[4])

wins = play(0, p_loc, [0, 0])
ans = max(wins)
print(ans)

# aocd.submit(ans, part="b", day=21, year=2021)
