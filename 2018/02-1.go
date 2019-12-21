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
)

func main() {
	file, _ := os.Open("02-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sum2 := 0
	sum3 := 0
	for scanner.Scan() {
		m := make(map[rune]int)
		for _, char := range scanner.Text() {
			m[char]++
		}
		var flag2, flag3 bool
		for _, num := range m {
			if num == 2 {
				flag2 = true
			} else if num == 3 {
				flag3 = true
			}
		}
		if flag2 {
			sum2++
		}
		if flag3 {
			sum3++
		}
	}

	fmt.Println(sum2 * sum3)
}
