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

func processNode(nums []int) (int, int) {
	nodes := nums[0]
	entries := nums[1]
	sum := 0
	used := 2
	for i := 0; i < nodes; i++ {
		newSum, newUsed := processNode(nums[used:])
		sum += newSum
		used += newUsed
	}
	for i := 0; i < entries; i++ {
		sum += nums[used]
		used++
	}
	return sum, used
}

func main() {
	input, _ := ioutil.ReadFile("08-input.txt")
	inputString := string(input)[:len(input)-1]
	var inputNums []int
	for _, s := range strings.Split(inputString, " ") {
		n, _ := strconv.Atoi(s)
		inputNums = append(inputNums, n)
	}
	sum, _ := processNode(inputNums)
	fmt.Println(sum)
}
