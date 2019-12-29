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

import json


def total(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    elif isinstance(obj, list):
        return sum(total(a) for a in obj)
    elif isinstance(obj, dict):
        return sum(total(a) for a in obj.keys()) \
            + sum(total(a) for a in obj.values())


def total_red(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    elif isinstance(obj, list):
        return sum(total_red(a) for a in obj)
    elif isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(total_red(a) for a in obj.keys()) \
            + sum(total_red(a) for a in obj.values())


with open("12-input.txt") as f:
    data = json.loads(f.read().rstrip())

print(total(data))
print(total_red(data))
