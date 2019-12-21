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
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("04-input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	sort.Strings(lines)

	guardSleepTimes := make(map[int][]int)
	var currentGuard, sleepTime, wakeTime int
	for _, line := range lines {
		if line[19:24] == "Guard" {
			currentGuard, _ = strconv.Atoi(strings.Split(line[26:], " ")[0])
			if guardSleepTimes[currentGuard] == nil {
				guardSleepTimes[currentGuard] = make([]int, 60)
			}
		} else if line[19:] == "falls asleep" {
			sleepTime, _ = strconv.Atoi(line[15:17])
		} else if line[19:] == "wakes up" {
			wakeTime, _ = strconv.Atoi(line[15:17])
			for min := sleepTime; min < wakeTime; min++ {
				guardSleepTimes[currentGuard][min]++
			}
		}
	}

	maxGuard := -1
	maxSleepMins := 0
	maxSleepMin := -1
	for guard, sleepTimes := range guardSleepTimes {
		sleepMins := 0
		maxNights := 0
		maxMin := -1
		for min, nights := range sleepTimes {
			sleepMins += nights
			if nights > maxNights {
				maxNights = nights
				maxMin = min
			}
		}
		if sleepMins > maxSleepMins {
			maxSleepMins = sleepMins
			maxSleepMin = maxMin
			maxGuard = guard
		}
	}

	fmt.Println(maxGuard * maxSleepMin)
}
