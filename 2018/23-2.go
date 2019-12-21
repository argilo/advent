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
	"sort"
	"strconv"
)

type nanobot struct {
	x, y, z, r int
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func numInRange(nanobots []nanobot, x, y, z int) int {
	num := 0
	for _, bot := range nanobots {
		if abs(x-bot.x)+abs(y-bot.y)+abs(z-bot.z) <= bot.r {
			num++
		}
	}
	return num
}

func main() {
	file, _ := os.Open("23-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	nanobots := make([]nanobot, 0)
	for scanner.Scan() {
		line := scanner.Text()
		pieces := regexp.MustCompile("(pos=<|,|>, r=)").Split(line, -1)
		x, _ := strconv.Atoi(pieces[1])
		y, _ := strconv.Atoi(pieces[2])
		z, _ := strconv.Atoi(pieces[3])
		r, _ := strconv.Atoi(pieces[4])
		nanobots = append(nanobots, nanobot{x, y, z, r})
	}

	best := 0
	for x := 50876000; x < 50877000; x++ {
		for y := 30960900; y < 30961000; y++ {
			starts := make([]int, 0)
			ends := make([]int, 0)

			for _, bot := range nanobots {
				left := bot.r - abs(x-bot.x) - abs(y-bot.y)
				if left >= 0 {
					starts = append(starts, bot.z-left)
					ends = append(ends, bot.z+left+1)
				}
			}
			sort.Ints(starts)
			sort.Ints(ends)

			i := 0
			j := 0
			n := len(starts)
			num := 0
			max := 0
			maxZ := 0
			for i < n && j < n {
				if starts[i] < ends[j] {
					num++
					if num > max {
						max = num
						maxZ = starts[i]
					}
					i++
				} else {
					num--
					j++
				}
			}

			if max > best {
				fmt.Println(max, x, y, maxZ, x+y+maxZ)
				best = max
			}
		}
	}
}
