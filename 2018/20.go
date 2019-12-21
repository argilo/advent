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
	"github.com/RyanCarrier/dijkstra"
	"os"
)

type coord struct {
	x, y int
}

type data struct {
	n, s, w, e bool
	num        int
}

func main() {
	file, _ := os.Open("20-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	regex := scanner.Text()

	posStack := []coord{coord{0, 0}}
	posData := make(map[coord]data)
	posData[coord{0, 0}] = data{false, false, false, false, 0}

	for _, c := range regex {
		pos := posStack[len(posStack)-1]
		oldData := posData[pos]
		switch c {
		case '^':
			continue
		case '$':
			continue
		case 'N':
			newPos := coord{pos.x, pos.y - 1}
			newData := posData[newPos]
			oldData.n = true
			newData.s = true
			posData[pos] = oldData
			posData[newPos] = newData
			posStack[len(posStack)-1] = newPos
		case 'S':
			newPos := coord{pos.x, pos.y + 1}
			newData := posData[newPos]
			oldData.s = true
			newData.n = true
			posData[pos] = oldData
			posData[newPos] = newData
			posStack[len(posStack)-1] = newPos
		case 'W':
			newPos := coord{pos.x - 1, pos.y}
			newData := posData[newPos]
			oldData.w = true
			newData.e = true
			posData[pos] = oldData
			posData[newPos] = newData
			posStack[len(posStack)-1] = newPos
		case 'E':
			newPos := coord{pos.x + 1, pos.y}
			newData := posData[newPos]
			oldData.e = true
			newData.w = true
			posData[pos] = oldData
			posData[newPos] = newData
			posStack[len(posStack)-1] = newPos
		case '(':
			posStack = append(posStack, posStack[len(posStack)-1])
		case '|':
			posStack[len(posStack)-1] = posStack[len(posStack)-2]
		case ')':
			posStack = posStack[0 : len(posStack)-1]
		}
	}

	i := 0
	for pos, dat := range posData {
		dat.num = i
		i++
		posData[pos] = dat
	}

	graph := dijkstra.NewGraph()
	for _, dat := range posData {
		graph.AddVertex(dat.num)
	}
	for pos, dat := range posData {
		if dat.n {
			graph.AddArc(dat.num, posData[coord{pos.x, pos.y - 1}].num, 1)
		}
		if dat.s {
			graph.AddArc(dat.num, posData[coord{pos.x, pos.y + 1}].num, 1)
		}
		if dat.w {
			graph.AddArc(dat.num, posData[coord{pos.x - 1, pos.y}].num, 1)
		}
		if dat.e {
			graph.AddArc(dat.num, posData[coord{pos.x + 1, pos.y}].num, 1)
		}
	}

	var top int64
	num1000 := 0
	for _, dat := range posData {
		best, _ := graph.Shortest(posData[coord{0, 0}].num, dat.num)
		if best.Distance > top {
			top = best.Distance
		}
		if best.Distance >= 1000 {
			num1000++
		}
	}
	fmt.Println(top)
	fmt.Println(num1000)
}
