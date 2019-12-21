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
	"strings"
)

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func dist(a, b [4]int) int {
	return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3])
}

func visit(v int, edges map[int][]int, visited []bool) {
	visited[v] = true
	for _, u := range edges[v] {
		if !visited[u] {
			visit(u, edges, visited)
		}
	}
}

func main() {
	file, _ := os.Open("25-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	points := make([][4]int, 0)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ",")
		var point [4]int
		for i, part := range parts {
			point[i], _ = strconv.Atoi(part)
		}

		points = append(points, point)
	}

	edges := make(map[int][]int)
	for i, pointI := range points {
		for j, pointJ := range points {
			if i != j && dist(pointI, pointJ) <= 3 {
				edges[i] = append(edges[i], j)
			}
		}
	}

	visited := make([]bool, len(points))
	clusters := 0
	for i := range visited {
		if !visited[i] {
			visit(i, edges, visited)
			clusters++
		}
	}
	fmt.Println(clusters)
}
