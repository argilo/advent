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

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func neighbours(curr [][]rune, row, col int) []rune {
	var result []rune

	for r := max(row-1, 0); r < min(row+2, len(curr)); r++ {
		for c := max(col-1, 0); c < min(col+2, len(curr[r])); c++ {
			if r == row && c == col {
				continue
			}
			result = append(result, curr[r][c])
		}
	}

	return result
}

func main() {
	file, _ := os.Open("18-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var curr, next [][]rune
	for scanner.Scan() {
		line := scanner.Text()
		curr = append(curr, []rune(line))
		next = append(next, make([]rune, len(line)))
	}

	for i := 0; i < 10; i++ {
		for r := range curr {
			for c := range curr[r] {
				var trees, lumberyards int
				for _, char := range neighbours(curr, r, c) {
					if char == '|' {
						trees++
					}
					if char == '#' {
						lumberyards++
					}

					next[r][c] = curr[r][c]

					if curr[r][c] == '.' && trees >= 3 {
						next[r][c] = '|'
					}
					if curr[r][c] == '|' && lumberyards >= 3 {
						next[r][c] = '#'
					}
					if curr[r][c] == '#' && (lumberyards == 0 || trees == 0) {
						next[r][c] = '.'
					}
				}
			}
		}

		var trees, lumberyards int
		for r := range curr {
			for c := range curr[r] {
				curr[r][c] = next[r][c]

				if curr[r][c] == '|' {
					trees++
				}
				if curr[r][c] == '#' {
					lumberyards++
				}
				fmt.Printf("%c", curr[r][c])
			}
			fmt.Println()
		}
		fmt.Println(trees * lumberyards)
	}
}
