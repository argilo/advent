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

import statistics
import string


def least_common(s):
    counts = [(s.count(char), char) for char in string.ascii_lowercase if s.count(char) > 0]
    counts.sort()
    return(counts[0][1])


cols = [[] for _ in range(8)]
for line in open("06-input.txt"):
    for i, char in enumerate(line.rstrip()):
        cols[i].append(char)
print("".join([statistics.mode(col) for col in cols]))
print("".join([least_common(col) for col in cols]))
