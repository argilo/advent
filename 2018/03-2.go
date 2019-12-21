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

type rectangle struct {
	n, x, y, w, h int
}

func main() {
	file, _ := os.Open("03-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var cloth [1000][1000]int
	for scanner.Scan() {
		rect := parseRectangle(scanner.Text())
		for x := rect.x; x < rect.x+rect.w; x++ {
			for y := rect.y; y < rect.y+rect.h; y++ {
				cloth[x][y]++
			}
		}
	}

	file.Seek(0, 0)
	scanner = bufio.NewScanner(file)

	for scanner.Scan() {
		rect := parseRectangle(scanner.Text())
		flag := true
		for x := rect.x; x < rect.x+rect.w; x++ {
			for y := rect.y; y < rect.y+rect.h; y++ {
				if cloth[x][y] > 1 {
					flag = false
				}
			}
		}
		if flag {
			fmt.Println(rect.n)
		}
	}
}

func parseRectangle(line string) rectangle {
	var rect rectangle

	pieces := strings.Split(line, " @ ")
	rect.n, _ = strconv.Atoi(pieces[0][1:])
	pieces = strings.Split(pieces[1], ":")
	xy := strings.Split(pieces[0], ",")
	rect.x, _ = strconv.Atoi(xy[0])
	rect.y, _ = strconv.Atoi(xy[1])
	wh := strings.Split(pieces[1][1:], "x")
	rect.w, _ = strconv.Atoi(wh[0])
	rect.h, _ = strconv.Atoi(wh[1])

	return rect
}
