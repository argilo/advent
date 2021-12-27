# Copyright 2018 Clayton Smith
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

# https://twitter.com/rundavidrun/status/1071673260469702656

pp = []

for p in Primes():
    if p < 10000:
        continue
    if p >= 100000:
        break
    pp.append(str(p))

best_n = 0
best_i = 0
for i in range(100):
    i_str = "{:02}".format(i)
    n = 0
    for p in pp:
        if i_str in p:
            n += p.count(i_str)
    if n > best_n:
        best_n = n
        best_i = i_str

zeroes = 0
sum = 0
for d in pi.n(digits=50000).str():
    if d == "0":
        zeroes += 1
        if zeroes == 3435:
            break
    if d == "4":
        sum += 2
    if d == "3":
        sum += 17

print("51" + best_i + "0-af1" + str(sum))
