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
	serialNumber := 6042

	var grid [301][301]int

	for y := 1; y <= 300; y++ {
		for x := 1; x <= 300; x++ {
			rackID := x + 10
			power := rackID * y
			power += serialNumber
			power *= rackID
			power = (power % 1000) / 100
			power -= 5
			grid[x][y] = power
		}
	}

	var bestX, bestY, bestPower int
	for y := 1; y <= 298; y++ {
		for x := 1; x <= 298; x++ {
			sum := 0
			for offsetY := 0; offsetY < 3; offsetY++ {
				for offsetX := 0; offsetX < 3; offsetX++ {
					sum += grid[x+offsetX][y+offsetY]
				}
			}
			if sum > bestPower {
				bestX = x
				bestY = y
				bestPower = sum
			}
		}
	}

	fmt.Printf("%d,%d\n", bestX, bestY)
}
