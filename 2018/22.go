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
	"github.com/RyanCarrier/dijkstra"
)

const (
	depth   = 8103
	targetX = 9
	targetY = 758
)

const (
	rocky = iota
	wet
	narrow
)

const (
	torch = 1 << iota
	climbing
	neither
)

const extra = 100
const mod = 20183

func cavernType(gIndex int) int {
	return ((gIndex + depth) % mod) % 3
}

func tools(cavernType int) (int, int) {
	switch cavernType {
	case rocky:
		return climbing, torch
	case wet:
		return climbing, neither
	case narrow:
		return torch, neither
	default:
		return -1, -1
	}
}

func vertex(x, y, tool int) int {
	const cells = (targetX + extra) * (targetY + extra)
	return tool*cells + y*(targetX+extra) + x
}

func connect(graph *dijkstra.Graph, v1, v2 int, time int64) {
	graph.AddArc(v1, v2, time)
	graph.AddArc(v2, v1, time)
}

func main() {
	risk := 0
	var gIndex [targetX + extra][targetY + extra]int
	graph := dijkstra.NewGraph()

	for y := 0; y < targetY+extra; y++ {
		for x := 0; x < targetX+extra; x++ {
			if x == targetX && y == targetY {
				gIndex[x][y] = 0
			} else if y == 0 {
				gIndex[x][y] = (x * 16807) % mod
			} else if x == 0 {
				gIndex[x][y] = (y * 48271) % mod
			} else {
				gIndex[x][y] = ((gIndex[x-1][y] + depth) * (gIndex[x][y-1] + depth)) % mod
			}

			cType := cavernType(gIndex[x][y])
			tool1, tool2 := tools(cType)

			graph.AddVertex(vertex(x, y, tool1))
			graph.AddVertex(vertex(x, y, tool2))
			connect(graph, vertex(x, y, tool1), vertex(x, y, tool2), 7)

			if x > 0 {
				cTypePrev := cavernType(gIndex[x-1][y])
				tool1Prev, tool2Prev := tools(cTypePrev)
				commonTools := (tool1 | tool2) & (tool1Prev | tool2Prev)

				for _, tool := range []int{torch, climbing, neither} {
					if (tool & commonTools) != 0 {
						connect(graph, vertex(x-1, y, tool), vertex(x, y, tool), 1)
					}
				}
			}
			if y > 0 {
				cTypePrev := cavernType(gIndex[x][y-1])
				tool1Prev, tool2Prev := tools(cTypePrev)
				commonTools := (tool1 | tool2) & (tool1Prev | tool2Prev)

				for _, tool := range []int{torch, climbing, neither} {
					if (tool & commonTools) != 0 {
						connect(graph, vertex(x, y-1, tool), vertex(x, y, tool), 1)
					}
				}
			}

			if x <= targetX && y <= targetY {
				risk += cavernType(gIndex[x][y])
			}
		}
	}

	fmt.Println(risk)

	best, _ := graph.Shortest(vertex(0, 0, torch), vertex(targetX, targetY, torch))
	fmt.Println(best.Distance)
}
