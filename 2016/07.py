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

count = 0
for line in open("07-input.txt"):
    ip = line.rstrip()
    hypernet = False
    good = False
    bad = False
    for i in range(len(ip) - 3):
        if ip[i] == "[":
            hypernet = True
        elif ip[i] == "]":
            hypernet = False

        if ip[i+3] == ip[i] != ip[i+1] == ip[i+2]:
            if hypernet:
                bad = True
            else:
                good = True
    if good and not bad:
        count += 1
print(count)

count = 0
for line in open("07-input.txt"):
    ip = line.rstrip()
    sup = ""
    hyp = ""
    hypernet = False
    good = False
    for char in ip:
        if char == "[":
            hypernet = True
            sup += " "
        elif char == "]":
            hypernet = False
            hyp += " "
        else:
            if hypernet:
                hyp += char
            else:
                sup += char
    for i in range(len(sup) - 2):
        if sup[i] == sup[i+2] != sup[i+1]:
            if f"{sup[i+1]}{sup[i]}{sup[i+1]}" in hyp:
                good = True
    if good:
        count += 1
print(count)
