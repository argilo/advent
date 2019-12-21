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

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for i := 0; i < len(lines)-1; i++ {
		for j := i + 1; j < len(lines); j++ {
			line1 := lines[i]
			line2 := lines[j]
			diffs := 0
			for c := 0; c < len(line1); c++ {
				if line1[c] != line2[c] {
					diffs++
				}
			}
			if diffs == 1 {
				var output string
				for c := 0; c < len(line1); c++ {
					if line1[c] == line2[c] {
						output += string(line1[c])
					}
				}
				fmt.Println(output)
			}
		}
	}
}
