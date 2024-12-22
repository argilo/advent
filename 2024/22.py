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
import collections

data = aocd.get_data(day=22, year=2024)

# data = """1
# 10
# 100
# 2024"""


def next_secret(secret):
    secret = (secret ^ (secret << 6)) & 0xffffff
    secret = (secret ^ (secret >> 5)) & 0xffffff
    secret = (secret ^ (secret << 11)) & 0xffffff
    return secret


ans = 0
for line in data.splitlines():
    secret = int(line)
    for _ in range(2000):
        secret = next_secret(secret)
    ans += secret

print(ans)
# aocd.submit(ans, part="a", day=22, year=2024)


# data = """1
# 2
# 3
# 2024"""

awards = collections.defaultdict(int)
for line in data.splitlines():
    secret = int(line)
    changes = []
    seen_changes = set()
    for _ in range(2000):
        secret2 = next_secret(secret)
        changes.append((secret2 % 10) - (secret % 10))
        if len(changes) >= 4:
            last_changes = tuple(changes[-4:])
            if last_changes not in seen_changes:
                awards[last_changes] += (secret2 % 10)
                seen_changes.add(last_changes)
        secret = secret2

ans = max(awards.values())

print(ans)
# aocd.submit(ans, part="b", day=22, year=2024)
