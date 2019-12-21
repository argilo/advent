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

type nanobot struct {
	x, y, z, r int
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func main() {
	file, _ := os.Open("23-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	nanobots := make([]nanobot, 0)
	largestR := 0
	var largestBot nanobot
	for scanner.Scan() {
		line := scanner.Text()
		pieces := regexp.MustCompile("(pos=<|,|>, r=)").Split(line, -1)
		x, _ := strconv.Atoi(pieces[1])
		y, _ := strconv.Atoi(pieces[2])
		z, _ := strconv.Atoi(pieces[3])
		r, _ := strconv.Atoi(pieces[4])
		nanobots = append(nanobots, nanobot{x, y, z, r})
		if r > largestR {
			largestR = r
			largestBot = nanobots[len(nanobots)-1]
		}
	}

	num := 0
	for _, bot := range nanobots {
		if abs(largestBot.x-bot.x)+abs(largestBot.y-bot.y)+abs(largestBot.z-bot.z) <= largestBot.r {
			num++
		}
	}

	fmt.Println(num)
}
