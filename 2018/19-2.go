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

type instruction struct {
	opcode string
	op1    int
	op2    int
	dest   int
}

func sumOfDivisors(n int) int {
	sum := 0
	d := 1
	for ; d*d < n; d++ {
		if n%d == 0 {
			sum += d
			sum += (n / d)
		}
	}
	if d*d == n {
		sum += d
	}
	return sum
}

func execute(ip int, regIn [6]int, opcode string, op1, op2, dest int) [6]int {
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
	regOut[ip]++
	return regOut
}

func main() {
	var reg [6]int
	var program []instruction

	file, _ := os.Open("19-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	ip, _ := strconv.Atoi(strings.Split(scanner.Text(), " ")[1])

	for scanner.Scan() {
		var inst instruction
		line := scanner.Text()
		parts := strings.Split(line, " ")
		inst.opcode = parts[0]
		inst.op1, _ = strconv.Atoi(parts[1])
		inst.op2, _ = strconv.Atoi(parts[2])
		inst.dest, _ = strconv.Atoi(parts[3])
		program = append(program, inst)
	}

	reg[0] = 1
	for {
		if reg[ip] < 0 || reg[ip] >= len(program) {
			break
		}
		if reg[ip] == 1 {
			break
		}
		inst := program[reg[ip]]
		reg = execute(ip, reg, inst.opcode, inst.op1, inst.op2, inst.dest)
	}
	fmt.Println(sumOfDivisors(reg[3]))
}
