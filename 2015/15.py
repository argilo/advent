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


results = []
results_500 = []


def foo(ingredients, amounts):
    if len(amounts) == len(ingredients)-1:
        prod = 1
        for attr in range(5):
            summ = 0
            for ing, amt in zip(ingredients, amounts + [100-sum(amounts)]):
                summ += ing[attr] * amt
            if attr == 4:
                cals = summ
            else:
                if summ > 0:
                    prod *= summ
                else:
                    prod = 0
        results.append(prod)
        if cals == 500:
            results_500.append(prod)
    else:
        for amt in range(0, 100-sum(amounts)+1):
            foo(ingredients, amounts + [amt])


ingredients = []
for line in open("15-input.txt"):
    values = [int(n.rstrip(",")) for n in line.split()[2::2]]
    ingredients.append(values)


foo(ingredients, [])
print(max(results))
print(max(results_500))
