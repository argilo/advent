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


def pos(reindeer, now):
    speed, time, rest = reindeer
    dist = (now // (time+rest)) * (speed * time)
    now = now % (time+rest)
    if now > time:
        dist += speed * time
    else:
        dist += speed * now
    return dist


reindeers = []
for line in open("14-input.txt"):
    parts = line.split()
    speed, time, rest = int(parts[3]), int(parts[6]), int(parts[13])
    reindeers.append((speed, time, rest))

best = 0
for reindeer in reindeers:
    dist = pos(reindeer, 2503)
    if dist > best:
        best = dist
print(best)

scores = [0] * len(reindeers)
for time in range(1, 2503+1):
    dists = [pos(reindeer, time) for reindeer in reindeers]
    for i in range(len(reindeers)):
        if dists[i] == max(dists):
            scores[i] += 1
print(max(scores))
