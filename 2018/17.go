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

func drawSquare(board [][]int, x, y int) [][]int {
	for len(board) < y+1 {
		board = append(board, make([]int, 1000))
	}
	board[y][x] = 3
	return board
}

func dropFrom(board [][]int, x, y int) {
	for ; y+1 < len(board) && board[y][x] <= 1; y++ {
		board[y][x] = 1
	}
	if y+1 == len(board) {
		if board[y][x] <= 1 {
			board[y][x] = 1
			return
		}
	}

	for {
		y--

		leftLim := x
		for board[y+1][leftLim] >= 2 && board[y][leftLim-1] <= 1 {
			leftLim--
		}
		blockedLeft := board[y][leftLim-1] >= 2

		rightLim := x
		for board[y+1][rightLim] >= 2 && board[y][rightLim+1] <= 1 {
			rightLim++
		}
		blockedRight := board[y][rightLim+1] >= 2

		//fmt.Println(leftLim, blockedLeft, rightLim, blockedRight)
		if blockedLeft && blockedRight {
			for xDone := leftLim; xDone <= rightLim; xDone++ {
				board[y][xDone] = 2
			}
		} else {
			for xDone := leftLim; xDone <= rightLim; xDone++ {
				board[y][xDone] = 1
			}
			if !blockedLeft {
				dropFrom(board, leftLim, y)
			}
			if !blockedRight {
				dropFrom(board, rightLim, y)
			}
			break
		}
	}
}

func main() {
	file, _ := os.Open("17-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	board := [][]int{make([]int, 1000)}
	minY := 1000000
	for scanner.Scan() {
		line := scanner.Text()
		pieces := regexp.MustCompile("(=|, |\\.\\.)").Split(line, -1)
		n1, _ := strconv.Atoi(pieces[1])
		n2, _ := strconv.Atoi(pieces[3])
		n3, _ := strconv.Atoi(pieces[4])
		for i := n2; i <= n3; i++ {
			var x, y int
			if pieces[0] == "x" {
				x = n1
				y = i
			} else {
				x = i
				y = n1
			}
			board = drawSquare(board, x, y)
			if y < minY {
				minY = y
			}
		}
	}

	dropFrom(board, 500, 0)

	var sum1, sum2 int
	for y := range board {
		if y < minY {
			continue
		}
		for x := 420; x <= 640; x++ {
			switch board[y][x] {
			case 0:
				fmt.Print(".")
			case 1:
				fmt.Print("|")
				sum1++
			case 2:
				fmt.Print("~")
				sum1++
				sum2++
			case 3:
				fmt.Print("#")
			}
		}
		fmt.Println()
	}
	fmt.Println(sum1)
	fmt.Println(sum2)
}
