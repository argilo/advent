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

func execute(regIn [4]int, opcode string, op1, op2, dest int) [4]int {
	regOut := regIn
	switch opcode {
	case "addr":
		regOut[dest] = regIn[op1] + regIn[op2]
	case "addi":
		regOut[dest] = regIn[op1] + op2
	case "mulr":
		regOut[dest] = regIn[op1] * regIn[op2]
	case "muli":
		regOut[dest] = regIn[op1] * op2
	case "banr":
		regOut[dest] = regIn[op1] & regIn[op2]
	case "bani":
		regOut[dest] = regIn[op1] & op2
	case "borr":
		regOut[dest] = regIn[op1] | regIn[op2]
	case "bori":
		regOut[dest] = regIn[op1] | op2
	case "setr":
		regOut[dest] = regIn[op1]
	case "seti":
		regOut[dest] = op1
	case "gtir":
		if op1 > regIn[op2] {
			regOut[dest] = 1
		} else {
			regOut[dest] = 0
		}
	case "gtri":
		if regIn[op1] > op2 {
			regOut[dest] = 1
		} else {
			regOut[dest] = 0
		}
	case "gtrr":
		if regIn[op1] > regIn[op2] {
			regOut[dest] = 1
		} else {
			regOut[dest] = 0
		}
	case "eqir":
		if op1 == regIn[op2] {
			regOut[dest] = 1
		} else {
			regOut[dest] = 0
		}
	case "eqri":
		if regIn[op1] == op2 {
			regOut[dest] = 1
		} else {
			regOut[dest] = 0
		}
	case "eqrr":
		if regIn[op1] == regIn[op2] {
			regOut[dest] = 1
		} else {
			regOut[dest] = 0
		}
	}
	return regOut
}

func main() {
	opcodes := []string{
		"addr", "addi",
		"mulr", "muli",
		"banr", "bani",
		"borr", "bori",
		"setr", "seti",
		"gtir", "gtri", "gtrr",
		"eqir", "eqri", "eqrr",
	}

	var reg [4]int

	var opcodePoss []map[string]bool
	for opcode := 0; opcode < len(opcodes); opcode++ {
		set := make(map[string]bool)
		for _, op := range opcodes {
			set[op] = true
		}
		opcodePoss = append(opcodePoss, set)
	}

	file, _ := os.Open("16-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sum := 0
	for scanner.Scan() {
		line := scanner.Text()

		if len(line) >= 7 && line[:7] == "Before:" {
			var regIn, regOut [4]int
			var opcode, op1, op2, dest int

			for i, s := range strings.Split(line[9:len(line)-1], ", ") {
				regIn[i], _ = strconv.Atoi(s)
			}

			scanner.Scan()
			line = scanner.Text()
			parts := strings.Split(line, " ")
			opcode, _ = strconv.Atoi(parts[0])
			op1, _ = strconv.Atoi(parts[1])
			op2, _ = strconv.Atoi(parts[2])
			dest, _ = strconv.Atoi(parts[3])

			scanner.Scan()
			line = scanner.Text()
			for i, s := range strings.Split(line[9:len(line)-1], ", ") {
				regOut[i], _ = strconv.Atoi(s)
			}

			scanner.Scan()

			var validOps []string
			for _, op := range opcodes {
				result := execute(regIn, op, op1, op2, dest)
				match := true
				for r := 0; r < 4; r++ {
					if result[r] != regOut[r] {
						match = false
					}
				}
				if match {
					validOps = append(validOps, op)
				} else {
					delete(opcodePoss[opcode], op)
				}
			}
			if len(validOps) >= 3 {
				sum++
			}
		} else if line == "" {
			scanner.Scan()
			fmt.Println(sum)

			for {
				cont := false
				for opcode := range opcodes {
					if len(opcodePoss[opcode]) == 1 {
						var uniqueOp string
						for op := range opcodePoss[opcode] {
							uniqueOp = op
						}
						opcodes[opcode] = uniqueOp
						for opcode := range opcodes {
							if len(opcodePoss[opcode]) > 1 {
								delete(opcodePoss[opcode], uniqueOp)
							}
						}
					} else {
						cont = true
					}
				}
				if !cont {
					break
				}
			}
		} else {
			parts := strings.Split(line, " ")
			opcode, _ := strconv.Atoi(parts[0])
			op1, _ := strconv.Atoi(parts[1])
			op2, _ := strconv.Atoi(parts[2])
			dest, _ := strconv.Atoi(parts[3])
			reg = execute(reg, opcodes[opcode], op1, op2, dest)
		}
	}
	fmt.Println(reg[0])
}
