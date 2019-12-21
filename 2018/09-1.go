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
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	input, _ := ioutil.ReadFile("09-input.txt")
	inputString := string(input)
	pieces := strings.Split(inputString, " ")
	players, _ := strconv.Atoi(pieces[0])
	marbles, _ := strconv.Atoi(pieces[6])

	circle := []int{0}
	currentMarble := 0
	scores := make([]int, players)
	currentPlayer := 0
	maxScore := 0

	for marble := 1; marble <= marbles; marble++ {
		if marble%23 == 0 {
			currentMarble = (currentMarble + len(circle) - 7) % len(circle)
			scores[currentPlayer] += marble + circle[currentMarble]
			if scores[currentPlayer] > maxScore {
				maxScore = scores[currentPlayer]
			}

			copy(circle[currentMarble:], circle[currentMarble+1:])
			circle = circle[:len(circle)-1]
		} else {
			currentMarble = (currentMarble + 2) % len(circle)

			circle = append(circle, 0)
			copy(circle[currentMarble+1:], circle[currentMarble:])
			circle[currentMarble] = marble
		}
		currentPlayer = (currentPlayer + 1) % players
	}
	fmt.Println(maxScore)
}
