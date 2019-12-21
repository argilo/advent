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
	"regexp"
	"strconv"
)

func main() {
	for time := 10001; time <= 10050; time++ {
		file, _ := os.Open("10-input.txt")
		defer file.Close()

		const width = 400
		const height = 300

		var board [width][height]rune
		for y := 0; y < height; y++ {
			for x := 0; x < width; x++ {
				board[x][y] = rune('.')
			}
		}

		scanner := bufio.NewScanner(file)
		minx := 1000000
		maxx := -1000000
		miny := 1000000
		maxy := -1000000
		for scanner.Scan() {
			line := scanner.Text()
			pieces := regexp.MustCompile("[<>,] *").Split(line, -1)
			startx, _ := strconv.Atoi(pieces[1])
			starty, _ := strconv.Atoi(pieces[2])
			vx, _ := strconv.Atoi(pieces[4])
			vy, _ := strconv.Atoi(pieces[5])
			x := startx + time*vx
			y := starty + time*vy
			board[x][y] = rune('#')
			if x < minx {
				minx = x
			}
			if x > maxx {
				maxx = x
			}
			if y < miny {
				miny = y
			}
			if y > maxy {
				maxy = y
			}
		}

		if maxy-miny <= 10 {
			for y := miny; y <= maxy; y++ {
				for x := minx; x <= maxx; x++ {
					fmt.Printf("%c", board[x][y])
				}
				fmt.Println()
			}
			fmt.Println(time)
		}
	}
}
