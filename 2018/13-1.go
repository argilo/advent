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

func main() {
	file, _ := os.Open("13-input.txt")
	defer file.Close()

	var tracks [][]rune
	var carts [][]rune
	var cartStates [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		trackRow := []rune(scanner.Text())
		cartRow := make([]rune, len(trackRow))
		cartStateRow := make([]int, len(trackRow))
		for col, trackChar := range trackRow {
			switch trackChar {
			case '>':
				cartRow[col] = trackRow[col]
				trackRow[col] = '-'
			case '<':
				cartRow[col] = trackRow[col]
				trackRow[col] = '-'
			case '^':
				cartRow[col] = trackRow[col]
				trackRow[col] = '|'
			case 'v':
				cartRow[col] = trackRow[col]
				trackRow[col] = '|'
			}
		}
		tracks = append(tracks, trackRow)
		carts = append(carts, cartRow)
		cartStates = append(cartStates, cartStateRow)
	}

	for {
		for row, trackRow := range tracks {
			for col := range trackRow {
				cartChar := carts[row][col]
				cartState := cartStates[row][col]
				if cartChar != 0 && cartState < 100 {
					newRow := row
					newCol := col
					newCartChar := cartChar
					switch cartChar {
					case '>':
						newCol++
						if tracks[newRow][newCol] == '\\' {
							newCartChar = 'v'
						} else if tracks[newRow][newCol] == '/' {
							newCartChar = '^'
						}
					case '<':
						newCol--
						if tracks[newRow][newCol] == '\\' {
							newCartChar = '^'
						} else if tracks[newRow][newCol] == '/' {
							newCartChar = 'v'
						}
					case '^':
						newRow--
						if tracks[newRow][newCol] == '\\' {
							newCartChar = '<'
						} else if tracks[newRow][newCol] == '/' {
							newCartChar = '>'
						}
					case 'v':
						newRow++
						if tracks[newRow][newCol] == '\\' {
							newCartChar = '>'
						} else if tracks[newRow][newCol] == '/' {
							newCartChar = '<'
						}
					}

					newCartState := cartState
					if tracks[newRow][newCol] == '+' {
						if cartState == 0 {
							switch newCartChar {
							case '>':
								newCartChar = '^'
							case '<':
								newCartChar = 'v'
							case '^':
								newCartChar = '<'
							case 'v':
								newCartChar = '>'
							}
						} else if cartState == 2 {
							switch newCartChar {
							case '>':
								newCartChar = 'v'
							case '<':
								newCartChar = '^'
							case '^':
								newCartChar = '>'
							case 'v':
								newCartChar = '<'
							}
						}
						newCartState = (cartState + 1) % 3
					}

					if carts[newRow][newCol] != 0 {
						fmt.Printf("%d,%d\n", newCol, newRow)
						os.Exit(0)
					}
					carts[newRow][newCol] = newCartChar
					carts[row][col] = 0

					cartStates[newRow][newCol] = newCartState + 100
					cartStates[row][col] = 0
				}
			}
		}
		for row, cartStateRow := range cartStates {
			for col := range cartStateRow {
				if cartStates[row][col] >= 100 {
					cartStates[row][col] -= 100
				}
			}
		}
	}
}
