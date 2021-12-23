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
import copy

data = aocd.get_data(day=23, year=2021)
# data = """#############
# #...........#
# ###B#C#B#D###
#   #A#D#C#A#
#   #########"""

lines = data.splitlines()
lines.insert(3, "  #D#C#B#A#")
lines.insert(4, "  #D#B#A#C#")
depth = len(lines) - 3
depth_rows = list(range(2, 2+depth))

for line in lines:
    print(line)

cost = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

hall_targets = [
    (1, 1),
    (1, 2),
    (1, 4),
    (1, 6),
    (1, 8),
    (1, 10),
    (1, 11),
]

pod_targets = []
win_state = []
for col in (3, 5, 7, 9):
    for row in depth_rows:
        pod_targets.append((row, col))
        win_state.append(row)
        win_state.append(col)
win_state = tuple(win_state)

pod_loc = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
}

for target_row, target_col in pod_targets:
    pod_type = lines[target_row][target_col]
    pod_loc[pod_type].append([target_row, target_col])


def path_cost(pod_type, occupied, start, end):
    start_row, start_col = start
    current_row, current_col = start
    end_row, end_col = end

    total_cost = 0
    while True:
        if start_row == 1:
            if current_col < end_col:
                dir = (0, 1)
            elif current_col > end_col:
                dir = (0, -1)
            else:
                dir = (1, 0)
        else:
            if current_row > 1:
                dir = (-1, 0)
            else:
                if current_col < end_col:
                    dir = (0, 1)
                elif current_col > end_col:
                    dir = (0, -1)

        current_row += dir[0]
        current_col += dir[1]

        if (current_row, current_col) in occupied:
            return -1
        else:
            total_cost += cost[pod_type]
            if (current_row, current_col) == (end_row, end_col):
                return total_cost


def contents_of(pod_loc, square):
    target_row, target_col = square
    for pod_type, locs in pod_loc.items():
        for row, col in locs:
            if row == target_row and col == target_col:
                return pod_type
    return None


def pod_target(pod_type, pod_loc, this_loc):
    if pod_type == "A":
        target_col = 3
    elif pod_type == "B":
        target_col = 5
    elif pod_type == "C":
        target_col = 7
    elif pod_type == "D":
        target_col = 9

    column = [contents_of(pod_loc, (row, target_col)) for row in depth_rows]

    for row in depth_rows:
        if column == [None]*(row-1) + [pod_type]*(depth - (row-1)):
            return (row, target_col)
    return None


def valid_moves(pod_loc):
    moves = []

    occupied = set()
    for pod_type, locs in pod_loc.items():
        for row, col in locs:
            occupied.add((row, col))
    for pod_type, locs in pod_loc.items():
        for row, col in locs:
            if row in depth_rows:

                if pod_type == "A":
                    target_col = 3
                elif pod_type == "B":
                    target_col = 5
                elif pod_type == "C":
                    target_col = 7
                elif pod_type == "D":
                    target_col = 9

                if col == target_col:
                    ok_below = True
                    for row2 in range(row+1, 2+depth):
                        if [row2, col] not in pod_loc[pod_type]:
                            ok_below = False
                            break
                    if ok_below:
                        continue

                for target in hall_targets:
                    pc = path_cost(pod_type, occupied, (row, col), target)
                    if pc > 0:
                        moves.append((pod_type, pc, [row, col], list(target)))
            else:
                target = pod_target(pod_type, pod_loc, (row, col))
                if target:
                    pc = path_cost(pod_type, occupied, (row, col), target)
                    if pc > 0:
                        moves.append((pod_type, pc, [row, col], list(target)))
    return moves


def uniq_state(pod_loc):
    lst = []
    for pod_type in ["A", "B", "C", "D"]:
        locs = sorted(pod_loc[pod_type])
        for loc in locs:
            lst.append(loc[0])
            lst.append(loc[1])
    return tuple(lst)


dic = {}


def explore(pod_loc, depth):
    us1 = uniq_state(pod_loc)

    if us1 == win_state:
        return 0

    if us1 in dic:
        return dic[us1]

    best_cost = 1000000

    moves = valid_moves(pod_loc)
    for pod_type, new_cost, start, end in moves:
        index = pod_loc[pod_type].index(start)
        new_pod_loc = copy.deepcopy(pod_loc)
        new_pod_loc[pod_type][index] = end
        us = uniq_state(new_pod_loc)

        explore_cost = explore(new_pod_loc, depth+1)
        if new_cost + explore_cost < best_cost:
            best_cost = new_cost + explore_cost

    dic[us1] = best_cost
    return best_cost


print(explore(pod_loc, 0))
