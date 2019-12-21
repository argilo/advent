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
	const numLetters = 26
	const numWorkers = 5
	file, _ := os.Open("07-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	depends := make([]map[int]bool, numLetters)
	for i := 0; i < numLetters; i++ {
		depends[i] = make(map[int]bool)
	}
	for scanner.Scan() {
		line := scanner.Text()
		a := int(line[5]) - 65
		b := int(line[36]) - 65
		depends[b][a] = true
	}

	workerTasks := make([]int, numWorkers)
	workerTimes := make([]int, numWorkers)
	for w := 0; w < numWorkers; w++ {
		workerTasks[w] = -1
	}

	for t := 0; ; t++ {
		for w := 0; w < numWorkers; w++ {
			if workerTasks[w] != -1 {
				workerTimes[w]--
				if workerTimes[w] == 0 {
					for k := 0; k < numLetters; k++ {
						delete(depends[k], workerTasks[w])
					}
					workerTasks[w] = -1
				}
			}
		}
		for w := 0; w < numWorkers; w++ {
			if workerTasks[w] == -1 {
				for j := 0; j < numLetters; j++ {
					if len(depends[j]) == 0 {
						depends[j][-1] = true
						workerTasks[w] = j
						workerTimes[w] = j + 61
						break
					}
				}
			}
		}

		done := true
		for w := 0; w < numWorkers; w++ {
			if workerTasks[w] != -1 {
				done = false
			}
		}
		if done {
			fmt.Println(t)
			break
		}
	}
}
