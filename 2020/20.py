#!/usr/bin/env python3

# Copyright 2020 Clayton Smith
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import aocd
import dijkstar

data = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
dim = 3

data = aocd.get_data(day=20, year=2020)
dim = 12

tiles = []
tile_dict = {}
num = 0
for line in data.splitlines():
    if line == "":
        continue
    elif line.startswith("Tile"):
        num = int(line[5:-1])
        rows = []
    else:
        rows.append(list(line))
        if len(rows) == 10:
            tiles.append((num, rows))
            tile_dict[num] = rows


def edges(tile):
    e = []
    data = tile[1]
    e.append(data[0])
    e.append(data[0][::-1])
    e.append(data[9])
    e.append(data[9][::-1])
    left = []
    right = []
    for r in range(10):
        left.append(data[r][0])
        right.append(data[r][9])
    e.append(left)
    e.append(left[::-1])
    e.append(right)
    e.append(right[::-1])
    return [tuple(edge) for edge in e]


edge_dict = {}
times_seen = {}
for tile in tiles:
    times_seen[tile[0]] = 0
    for i, edge in enumerate(edges(tile)):
        if edge in edge_dict:
            edge_dict[edge].append((tile[0], i))
        else:
            edge_dict[edge] = [(tile[0], i)]


for edge in edge_dict:
    if len(edge_dict[edge]) > 1:
        for tile_num, _ in edge_dict[edge]:
            times_seen[tile_num] += 1

prod = 1
corners = []
for tile_num in times_seen:
    if times_seen[tile_num] == 4:
        corners.append(tile_num)
        prod *= tile_num

print(prod)


def flip(tile):
    return [row[::-1] for row in tile]


def rotate(tile):
    d = len(tile)
    new_tile = [[None] * d for _ in range(d)]
    for r in range(d):
        for c in range(d):
            new_tile[r][c] = tile[d-1-c][r]
    return new_tile


def rotate_n(tile, n):
    if n >= 4:
        tile = flip(tile)
        n -= 4
    for _ in range(n):
        tile = rotate(tile)
    return tile


def print_tile(tile):
    d = len(tile)
    for r in range(d):
        for c in range(d):
            print(tile[r][c], end="")
        print()
    print()


graph = dijkstar.Graph()

for edge in edge_dict:
    conn = edge_dict[edge]
    if len(conn) == 2:
        graph.add_edge(conn[0][0], conn[1][0], 1)
        graph.add_edge(conn[1][0], conn[0][0], 1)

cost = dijkstar.find_path(graph, corners[0], corners[1]).total_cost
if cost == (dim-1)*2:
    corners = [corners[0], corners[2], corners[3], corners[1]]

grid = [[None] * dim for _ in range(dim)]

for tile_num in tile_dict:
    cost0 = dijkstar.find_path(graph, corners[0], tile_num).total_cost
    cost1 = dijkstar.find_path(graph, corners[1], tile_num).total_cost
    row = (cost0 + cost1 - (dim - 1)) // 2
    col = cost0 - row
    grid[row][col] = tile_num

for r1 in range(8):
    tile1 = rotate_n(tile_dict[grid[0][0]], r1)
    for r2 in range(8):
        tile2 = rotate_n(tile_dict[grid[0][1]], r2)
        for r3 in range(8):
            tile3 = rotate_n(tile_dict[grid[1][0]], r3)

            flag = True
            for r in range(10):
                if tile1[r][9] != tile2[r][0]:
                    flag = False
            for c in range(10):
                if tile1[9][c] != tile3[0][c]:
                    flag = False

            if flag:
                tile_dict[grid[0][0]] = tile1

for r in range(dim):
    for c in range(dim):
        if r == c == 0:
            continue
        elif c > 0:
            tile1 = tile_dict[grid[r][c-1]]
            for rot in range(8):
                tile2 = rotate_n(tile_dict[grid[r][c]], rot)

                flag = True
                for rr in range(10):
                    if tile1[rr][9] != tile2[rr][0]:
                        flag = False
                if flag:
                    tile_dict[grid[r][c]] = tile2
        elif r > 0:
            tile1 = tile_dict[grid[r-1][c]]
            for rot in range(8):
                tile2 = rotate_n(tile_dict[grid[r][c]], rot)

                flag = True
                for cc in range(10):
                    if tile1[9][cc] != tile2[0][cc]:
                        flag = False
                if flag:
                    tile_dict[grid[r][c]] = tile2

big_grid = [[None] * (dim*8) for _ in range(dim*8)]

for rr in range(dim):
    for cc in range(dim):
        for r in range(8):
            for c in range(8):
                big_grid[rr*8 + r][cc*8 + c] = tile_dict[grid[rr][cc]][r+1][c+1]

sea_monster = [
    list("                  # "),
    list("#    ##    ##    ###"),
    list(" #  #  #  #  #  #   "),
]

roughness = 0
for r in range(dim*8):
    for c in range(dim*8):
        if big_grid[r][c] == "#":
            roughness += 1

for rot in range(8):
    new_big_grid = rotate_n(big_grid, rot)
    for r in range(dim*8 - 3 + 1):
        for c in range(dim*8 - 20 + 1):
            flag = True

            for rr in range(3):
                for cc in range(20):
                    if sea_monster[rr][cc] == "#":
                        if new_big_grid[r+rr][c+cc] != "#":
                            flag = False
            if flag:
                roughness -= 15

print(roughness)
# aocd.submit(ans, part="b", day=20, year=2020)
