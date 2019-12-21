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
	"sort"
	"strconv"
	"strings"
)

type point struct {
	x, y int
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func uniqMin(values []int) int {
	min := 1000000
	index := -1
	for i, n := range values {
		if n < min {
			min = n
			index = i
		} else if n == min {
			index = -1
		}
	}
	return index
}

func main() {
	file, _ := os.Open("06-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var points []point
	for scanner.Scan() {
		pieces := strings.Split(scanner.Text(), ", ")
		var p point
		p.x, _ = strconv.Atoi(pieces[0])
		p.y, _ = strconv.Atoi(pieces[1])
		points = append(points, p)
	}

	distances := make([]int, len(points))
	closestTimes := make([]int, len(points))
	numCloseEnough := 0
	for y := -2000; y < 2400; y++ {
		for x := -2000; x < 2400; x++ {
			totalDist := 0
			for i, p := range points {
				distances[i] = abs(x-p.x) + abs(y-p.y)
				totalDist += distances[i]
			}
			if totalDist < 10000 {
				numCloseEnough++
			}
			closest := uniqMin(distances)
			if closest != -1 {
				closestTimes[closest]++
			}
		}
	}

	sort.Ints(closestTimes)
	for i, n := range closestTimes {
		if n > 10000 {
			fmt.Println(closestTimes[i-1])
			break
		}
	}
	fmt.Println(numCloseEnough)
}
