/*
Copyright 2018-2021 Clayton Smith

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
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"time"
)

type privateLeaderboard struct {
	OwnerID string                `json:"owner_id"`
	Event   string                `json:"event"`
	Members map[string]memberData `json:"members"`
}

type memberData struct {
	ID          string                               `json:"id"`
	Name        string                               `json:"name"`
	Stars       int                                  `json:"stars"`
	GlobalScore int                                  `json:"global_score"`
	LocalScore  int                                  `json:"local_score"`
	LastStarTS  interface{}                          `json:"last_star_ts"`
	Days        map[string]map[string]map[string]int `json:"completion_day_level"`
}

func sessionCookie() string {
	homeDir, err := os.UserHomeDir()
	if err != nil {
		log.Fatal(err)
	}
	path := filepath.Join(homeDir, ".config", "aocd", "token")
	content, err := os.ReadFile(path)
	if err != nil {
		log.Fatal(err)
	}
	return strings.TrimSpace(string(content))
}

func fetchJSON(year int) privateLeaderboard {
	yearStr := strconv.Itoa(year)
	url := "https://adventofcode.com/" + yearStr + "/leaderboard/private/view/179752.json"

	client := http.Client{}

	req, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		log.Fatal(err)
	}

	req.Header.Set("Cookie", "session="+sessionCookie())

	res, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}

	var leaderboard privateLeaderboard
	if err := json.Unmarshal(body, &leaderboard); err != nil {
		log.Fatal(err)
	}

	return leaderboard
}

func sortKV(scores map[string]int) []string {
	type kv struct {
		key   string
		value int
	}

	var s []kv
	for k, v := range scores {
		s = append(s, kv{k, v})
	}

	sort.Slice(s, func(a, b int) bool {
		return s[a].value > s[b].value
	})

	var result []string
	for _, kv := range s {
		result = append(result, kv.key)
	}
	return result
}

func main() {
	var year int
	var err error
	if len(os.Args) == 2 {
		year, err = strconv.Atoi(os.Args[1])
		if err != nil {
			log.Fatal(err)
		}
	} else {
		year = time.Now().Year()
	}
	leaderboard := fetchJSON(year)
	members := make([]memberData, 0, len(leaderboard.Members))
	memberScores := make(map[string]int)
	memberPotentialScores := make(map[string]int)
	for _, member := range leaderboard.Members {
		members = append(members, member)
		memberScores[member.ID] = 0
		memberPotentialScores[member.ID] = 0
	}

	for day := 1; day <= 25; day++ {
		dayString := strconv.Itoa(day)
		for part := 1; part <= 2; part++ {
			partString := strconv.Itoa(part)

			solvers := make([]memberData, 0)
			for _, member := range members {
				partData := member.Days[dayString][partString]
				if _, ok := partData["get_star_ts"]; ok {
					solvers = append(solvers, member)
				}
			}

			sort.Slice(solvers, func(a, b int) bool {
				aTS, _ := solvers[a].Days[dayString][partString]["get_star_ts"]
				bTS, _ := solvers[b].Days[dayString][partString]["get_star_ts"]
				if aTS == bTS {
					return solvers[a].ID > solvers[b].ID
				}
				return aTS < bTS
			})

			if len(solvers) > 0 {
				fmt.Printf("Day %d part %d\n", day, part)
				for i, member := range solvers {
					points := len(leaderboard.Members) - i
					ts, _ := member.Days[dayString][partString]["get_star_ts"]
					memberScores[member.ID] += points
					memberPotentialScores[member.ID] += points
					fmt.Println(points, time.Unix(int64(ts), 0).Format("2006-01-02 15:04:05"), member.Name)
				}
				for _, member := range members {
					partData := member.Days[dayString][partString]
					if _, ok := partData["get_star_ts"]; !ok {
						memberPotentialScores[member.ID] += len(leaderboard.Members) - len(solvers)
					}
				}
				fmt.Println()
			}
		}
	}

	myScore := 0
	for _, id := range sortKV(memberPotentialScores) {
		if leaderboard.Members[id].Name == "Clayton Smith" {
			myScore = memberPotentialScores[id]
		}
	}
	for _, id := range sortKV(memberPotentialScores) {
		if memberPotentialScores[id]-myScore > -1338 {
			fmt.Println(memberPotentialScores[id]-myScore, leaderboard.Members[id].Name)
		}
	}
}
