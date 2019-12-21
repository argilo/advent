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

func equal(a, b []int) bool {
	flag := true
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			flag = false
			break
		}
	}
	return flag
}

func main() {
	input := []int{7, 9, 3, 0, 3, 1}

	recipes := []int{3, 7}
	e1 := 0
	e2 := 1

	for {
		sum := recipes[e1] + recipes[e2]
		if sum >= 10 {
			recipes = append(recipes, 1)
		}
		recipes = append(recipes, sum%10)
		e1 = (e1 + recipes[e1] + 1) % len(recipes)
		e2 = (e2 + recipes[e2] + 1) % len(recipes)

		if len(recipes) > len(input)+1 {
			if equal(recipes[len(recipes)-len(input)-1:len(recipes)-1], input) {
				fmt.Println(len(recipes) - len(input) - 1)
				break
			}
		}
		if len(recipes) > len(input) {
			if equal(recipes[len(recipes)-len(input):len(recipes)], input) {
				fmt.Println(len(recipes) - len(input))
				break
			}
		}
	}
}
