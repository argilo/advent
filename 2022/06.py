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

data = aocd.get_data(day=6, year=2022)
data = list(data)

for x in range(len(data)):
    s = set(data[x:x+4])
    if len(s) == 4:
        ans = x+4
        break
print(ans)

# aocd.submit(ans, part="a", day=6, year=2022)

for x in range(len(data)):
    s = set(data[x:x+14])
    if len(s) == 14:
        ans = x+14
        break
print(ans)

# aocd.submit(ans, part="b", day=6, year=2022)
