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
	"strconv"
)

func main() {
	sum := 0
	m := make(map[int]bool)

	for {
		file, _ := os.Open("01-input.txt")
		defer file.Close()

		scanner := bufio.NewScanner(file)
		m[0] = true
		for scanner.Scan() {
			n, _ := strconv.Atoi(scanner.Text())
			sum += n
			if m[sum] {
				fmt.Println(sum)
				os.Exit(0)
			}
			m[sum] = true
		}
	}
}
