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
)

type coord struct {
	r, c int
}

type square struct {
	char     rune
	played   bool
	points   int
	distance int
}

func neighbours(r, c int) []coord {
	result := make([]coord, 4)
	result[0] = coord{r - 1, c}
	result[1] = coord{r, c - 1}
	result[2] = coord{r, c + 1}
	result[3] = coord{r + 1, c}
	return result
}

func calcDist(r int, c int, board [][]square) {
	for r := 0; r < len(board); r++ {
		for c := 0; c < len(board[r]); c++ {
			board[r][c].distance = -1
		}
	}

	board[r][c].distance = 0

	for dist, done := 0, false; !done; dist++ {
		done = true
		for r := 1; r < len(board)-1; r++ {
			for c := 1; c < len(board[r])-1; c++ {
				if board[r][c].char == '.' && board[r][c].distance == -1 {
					for _, place := range neighbours(r, c) {
						if board[place.r][place.c].distance == dist {
							board[r][c].distance = dist + 1
							done = false
							break
						}
					}
				}
			}
		}
	}
}

func clearPlayed(board [][]square) {
	for r := 0; r < len(board); r++ {
		for c := 0; c < len(board[r]); c++ {
			board[r][c].played = false
		}
	}
}

func move(r int, c int, target rune, board [][]square) (int, int) {
	calcDist(r, c, board)

	bestDistance := 1000000
	bestR := 0
	bestC := 0
	for r := 1; r < len(board)-1; r++ {
		for c := 1; c < len(board[r])-1; c++ {
			if board[r][c].char == '.' && board[r][c].distance != -1 {
				for _, place := range neighbours(r, c) {
					if board[place.r][place.c].char == target && board[r][c].distance < bestDistance {
						bestDistance = board[r][c].distance
						bestR = r
						bestC = c
					}
				}
			}
		}
	}
	if bestDistance == 1000000 {
		return r, c
	}

	calcDist(bestR, bestC, board)
	bestDistance = 1000000
	for _, place := range neighbours(r, c) {
		dist := board[place.r][place.c].distance
		if dist >= 0 && dist < bestDistance {
			bestDistance = dist
			bestR = place.r
			bestC = place.c
		}
	}
	if bestDistance == 1000000 {
		return r, c
	}

	return bestR, bestC
}

func attack(r int, c int, target rune, board [][]square, elfAttackPoints int) {
	bestPoints := 1000000
	bestR := 0
	bestC := 0
	for _, place := range neighbours(r, c) {
		if board[place.r][place.c].char == target {
			points := board[place.r][place.c].points
			if points < bestPoints {
				bestPoints = points
				bestR = place.r
				bestC = place.c
			}
		}
	}

	if bestPoints == 1000000 {
		return
	}

	attackPower := 3
	if board[r][c].char == 'E' {
		attackPower = elfAttackPoints
	}

	board[bestR][bestC].points -= attackPower
	if board[bestR][bestC].points <= 0 {
		board[bestR][bestC].char = '.'
		board[bestR][bestC].points = 0
	}
}

func play(r int, c int, board [][]square, elfAttackPoints int) bool {
	target := 'E'
	if board[r][c].char == 'E' {
		target = 'G'
	}

	hasTargets := false
	for r := 1; r < len(board)-1; r++ {
		for c := 1; c < len(board[r])-1; c++ {
			if board[r][c].char == target {
				hasTargets = true
			}
		}
	}
	if hasTargets == false {
		return false
	}

	inRange := false
	for _, place := range neighbours(r, c) {
		if board[place.r][place.c].char == target {
			inRange = true
		}
	}

	if !inRange {
		newR, newC := move(r, c, target, board)
		if newR != r || newC != c {
			board[newR][newC].char = board[r][c].char
			board[newR][newC].points = board[r][c].points

			board[r][c].char = '.'
			board[r][c].points = 0
		}
		r = newR
		c = newC
	}

	attack(r, c, target, board, elfAttackPoints)

	board[r][c].played = true
	return true
}

func main() {
	for elfAttackPoints := 4; ; elfAttackPoints++ {
		file, _ := os.Open("15-input.txt")
		defer file.Close()

		scanner := bufio.NewScanner(file)
		var board [][]square
		startElves := 0
		for scanner.Scan() {
			row := make([]square, 0)
			for _, char := range scanner.Text() {
				sq := square{char, false, 0, -1}
				if char == 'E' || char == 'G' {
					sq.points = 200
				}
				if char == 'E' {
					startElves++
				}
				row = append(row, sq)
			}
			board = append(board, row)
		}

		endElves := 0
		ans := 0
		for i := 0; ; i++ {
			cont := true
			for r := 1; cont && r < len(board)-1; r++ {
				for c := 1; cont && c < len(board[r])-1; c++ {
					char := board[r][c].char
					if board[r][c].played == false && (char == 'E' || char == 'G') {
						cont = play(r, c, board, elfAttackPoints)
					}
				}
			}
			clearPlayed(board)

			if !cont {
				sum := 0
				for r := 1; r < len(board)-1; r++ {
					for c := 1; c < len(board[r])-1; c++ {
						sum += board[r][c].points
						if board[r][c].char == 'E' {
							endElves++
						}
					}
				}
				ans = i * sum
				break
			}
		}
		if startElves == endElves {
			fmt.Println(ans)
			break
		}
	}
}
