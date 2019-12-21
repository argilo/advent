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
	"strings"
)

func main() {
	file, _ := os.Open("12-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	plants := strings.Split(scanner.Text(), ": ")[1]
	scanner.Scan()

	rules := make(map[string]string)
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), " => ")
		rules[parts[0]] = parts[1]
	}

	for gen := 1; gen <= 20; gen++ {
		plants = "...." + plants + "...."

		newPlants := ""
		for offset := 0; offset <= len(plants)-5; offset++ {
			if rule, ok := rules[plants[offset:offset+5]]; ok {
				newPlants += rule
			} else {
				newPlants += "."
			}
		}

		plants = newPlants
	}

	sum := 0
	for i := 0; i < len(plants); i++ {
		if plants[i] == '#' {
			sum += i - 40
		}
	}
	fmt.Println(sum)
}
