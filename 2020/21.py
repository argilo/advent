#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
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

data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
data = aocd.get_data(day=21, year=2020)

pairs = []
all_allergens = set()
all_ingredients = set()
for line in data.splitlines():
    ingredients = line.split(" (contains ")[0].split()
    allergens = line.split(" (contains ")[1][:-1].split(", ")
    pairs.append((ingredients, allergens))
    for allergen in allergens:
        all_allergens.add(allergen)
    for ingredient in ingredients:
        all_ingredients.add(ingredient)

allergen_map = {}
while True:
    for allergen in all_allergens:
        if allergen in allergen_map:
            continue
        common = all_ingredients.copy()
        for v in allergen_map.values():
            common.remove(v)

        for ingredients, allergens in pairs:
            if allergen in allergens:
                ingredient_set = set(ingredients)
                common = common.intersection(ingredient_set)
        if len(common) == 1:
            allergen_map[allergen] = list(common)[0]
    if len(allergen_map) == len(all_allergens):
        break

total = 0
excluded_ingredients = set(allergen_map.values())
for ingredients, _ in pairs:
    for ingredient in ingredients:
        if ingredient not in excluded_ingredients:
            total += 1
print(total)

lst = sorted([(k, v) for k, v in allergen_map.items()])
lst = [v for (k, v) in lst]
print(",".join(lst))
