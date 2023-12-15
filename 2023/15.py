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

data = aocd.get_data(day=15, year=2023)
#data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

data = data.strip()

def hsh(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val

ans = 0
for part in data.split(","):
    ans += hsh(part)
print(ans)

# aocd.submit(ans, part="a", day=15, year=2023)

hshmap = [[] for _ in range(256)]
for part in data.split(","):
    if "-" in part:
        label = part[:-1]
        h = hsh(label)
        lst = hshmap[h]
        for i, lens in enumerate(lst):
            if lens[0] == label:
                del lst[i]
                break
    elif "=" in part:
        label, fl = part.split("=")
        h = hsh(label)
        fl = int(fl)
        lst = hshmap[h]
        for i, lens in enumerate(lst):
            if lens[0] == label:
                lens[1] = fl
                break
        else:
            lst.append([label, fl])

ans = 0
for i, lst in enumerate(hshmap):
    for j, lens in enumerate(lst):
        ans += (i+1) * (j+1) * lens[1]
print(ans)

# aocd.submit(ans, part="b", day=15, year=2023)
