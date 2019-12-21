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
	"io/ioutil"
)

func reduce(input []byte) int {
	var stack []byte
	for _, b := range input {
		if len(stack) > 0 && stack[len(stack)-1] == b^0x20 {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, b)
		}
	}
	return len(stack)
}

func main() {
	input, _ := ioutil.ReadFile("05-input.txt")
	input = input[:len(input)-1]
	fmt.Println(reduce(input))

	min := len(input)
	for removeChar := byte('A'); removeChar <= byte('Z'); removeChar++ {
		var newInput []byte
		for _, char := range input {
			if char != removeChar && (char^0x20) != removeChar {
				newInput = append(newInput, char)
			}
		}
		newLength := reduce(newInput)
		if newLength < min {
			min = newLength
		}
	}
	fmt.Println(min)
}
