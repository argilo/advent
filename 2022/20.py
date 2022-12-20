#!/usr/bin/env python3

# Copyright 2022 Clayton Smith
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

data = aocd.get_data(day=20, year=2022)


class Node:
    def __init__(self, n):
        self.n = n
        self.next = None
        self.prev = None

    def __repr__(self):
        return repr(self.n)


# els = [Node(int(n)) for n in data.split("\n")]
els = [Node(int(n) * 811589153) for n in data.split("\n")]

for i in range(len(els)):
    els[i].next = els[(i+1) % len(els)]
    els[i].prev = els[(i+len(els)-1) % len(els)]

# for _ in range(1):
for _ in range(10):
    for el in els:
        num = el.n % (len(els) - 1)
        if num == 0:
            continue

        el.next.prev, el.prev.next = el.prev, el.next
        if num > 0:
            target = el.next
            for _ in range(num - 1):
                target = target.next

        target_next = target.next
        el.prev, el.next, target.next, target_next.prev = target, target_next, el, el


el = els[0]
while True:
    if el.n == 0:
        break
    el = el.next

ans = 0
for _ in range(1000):
    el = el.next
ans += el.n
for _ in range(1000):
    el = el.next
ans += el.n
for _ in range(1000):
    el = el.next
ans += el.n

print(ans)
