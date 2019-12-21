/*
Copyright 2018 Clayton Smith

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

type group struct {
	id           int
	army         int
	units        int
	hitPoints    int
	attackDamage int
	attackType   string
	initiative   int
	weaknesses   map[string]bool
	immunities   map[string]bool
	targeted     bool
	target       int
}

func (g group) effectivePower() int {
	return g.units * g.attackDamage
}

func damage(attacker, defender group) int {
	damage := attacker.effectivePower()
	if defender.weaknesses[attacker.attackType] {
		return damage * 2
	} else if defender.immunities[attacker.attackType] {
		return damage * 0
	} else {
		return damage
	}
}

func main() {
	for boost := 0; ; boost++ {
		file, _ := os.Open("24-input.txt")
		defer file.Close()

		scanner := bufio.NewScanner(file)
		groups := make([]group, 0)
		army := 0
		id := 0
		for scanner.Scan() {
			line := scanner.Text()

			if line == "" {
				// do nothing
			} else if line == "Immune System:" {
				army = 0
			} else if line == "Infection:" {
				army = 1
			} else {
				re := regexp.MustCompile("^(\\d+) units each with (\\d+) hit points (\\(.*\\) )?with an attack that does (\\d+) (.*) damage at initiative (\\d+)$")
				match := re.FindStringSubmatch(line)

				units, _ := strconv.Atoi(match[1])
				hitPoints, _ := strconv.Atoi(match[2])
				attackDamage, _ := strconv.Atoi(match[4])
				if army == 0 {
					attackDamage += boost
				}
				attackType := match[5]
				initiative, _ := strconv.Atoi(match[6])

				group := group{id, army, units, hitPoints, attackDamage, attackType, initiative, make(map[string]bool), make(map[string]bool), false, -1}
				id++

				if match[3] != "" {
					for _, part := range strings.Split(match[3][1:len(match[3])-2], "; ") {
						re := regexp.MustCompile("^(weak|immune) to (.*)$")
						match := re.FindStringSubmatch(part)
						for _, thing := range strings.Split(match[2], ", ") {
							switch match[1] {
							case "weak":
								group.weaknesses[thing] = true
							case "immune":
								group.immunities[thing] = true
							}
						}
					}
				}

				groups = append(groups, group)
			}
		}

		for {
			sort.Slice(groups, func(i, j int) bool {
				if groups[i].effectivePower() > groups[j].effectivePower() {
					return true
				} else if groups[i].effectivePower() < groups[j].effectivePower() {
					return false
				} else {
					return groups[i].initiative > groups[j].initiative
				}
			})

			for i, attacker := range groups {
				groups[i].target = -1
				bestDamage := 0
				bestEffectivePower := 0
				bestInitiative := 0
				bestJ := -1
				for j, defender := range groups {
					if attacker.army == defender.army {
						continue
					}
					if defender.targeted {
						continue
					}
					d := damage(attacker, defender)
					if d == 0 {
						continue
					}
					if d > bestDamage ||
						d == bestDamage && defender.effectivePower() > bestEffectivePower ||
						d == bestDamage && defender.effectivePower() == bestEffectivePower && defender.initiative > bestInitiative {
						groups[i].target = defender.id
						bestDamage = d
						bestEffectivePower = defender.effectivePower()
						bestInitiative = defender.initiative
						bestJ = j
					}
				}
				if bestJ != -1 {
					groups[bestJ].targeted = true
				}
			}

			sort.Slice(groups, func(i, j int) bool {
				return groups[i].initiative > groups[j].initiative
			})

			done := true
			for i, attacker := range groups {
				groups[i].targeted = false

				for j, defender := range groups {
					if defender.id == attacker.target {
						d := damage(attacker, defender)
						if (d / defender.hitPoints) > 0 {
							done = false
						}
						groups[j].units -= (d / defender.hitPoints)
					}
				}
			}
			if done {
				break
			}

			newGroups := make([]group, 0)
			armies := make([]int, 2)
			for _, g := range groups {
				if g.units > 0 {
					newGroups = append(newGroups, g)
					armies[g.army]++
				}
			}
			groups = newGroups

			if armies[0] == 0 || armies[1] == 0 {
				break
			}
		}

		sum := 0
		done := true
		for _, g := range groups {
			sum += g.units
			if g.army != 0 {
				done = false
			}
		}
		if done {
			fmt.Println(sum)
			break
		}
	}
}
