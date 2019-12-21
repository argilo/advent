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
	"fmt"
)

func main() {
	input := 793031

	recipes := []int{3, 7}
	e1 := 0
	e2 := 1

	for len(recipes) < input+10 {
		sum := recipes[e1] + recipes[e2]
		if sum >= 10 {
			recipes = append(recipes, 1)
		}
		recipes = append(recipes, sum%10)
		e1 = (e1 + recipes[e1] + 1) % len(recipes)
		e2 = (e2 + recipes[e2] + 1) % len(recipes)
	}

	for i := input; i < input+10; i++ {
		fmt.Print(recipes[i])
	}
	fmt.Println()
}
