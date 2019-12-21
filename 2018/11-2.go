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

	var grid [301][301][301]int

	for y := 1; y <= 300; y++ {
		for x := 1; x <= 300; x++ {
			rackID := x + 10
			power := rackID * y
			power += serialNumber
			power *= rackID
			power = (power % 1000) / 100
			power -= 5
			grid[1][x][y] = power
		}
	}

	var bestX, bestY, bestSize, bestPower int
	for size := 1; size < 300; size++ {
		for y := 1; y <= 301-size; y++ {
			for x := 1; x <= 301-size; x++ {
				if size > 1 {
					grid[size][x][y] = grid[size-1][x][y] + grid[size-1][x+1][y+1] +
						grid[1][x-1+size][y] + grid[1][x][y-1+size] -
						grid[size-2][x+1][y+1]
				}
				if grid[size][x][y] > bestPower {
					bestX = x
					bestY = y
					bestSize = size
					bestPower = grid[size][x][y]
				}
			}
		}
	}

	fmt.Printf("%d,%d,%d\n", bestX, bestY, bestSize)
}
