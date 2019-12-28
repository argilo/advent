#!/usr/bin/env python3

# Copyright 2019 Clayton Smith
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


def to_2d(s):
    return tuple(tuple(row) for row in s.split("/"))


def transpose(pat):
    return tuple(tuple(pat[col][row] for col in range(len(pat))) for row in range(len(pat)))


def flip_rows(pat):
    return pat[::-1]


def flip_cols(pat):
    return tuple(row[::-1] for row in pat)


def variants(pat):
    return (
        pat,
        flip_cols(pat),
        flip_rows(pat),
        flip_rows(flip_cols(pat)),
        transpose(pat),
        transpose(flip_cols(pat)),
        transpose(flip_rows(pat)),
        transpose(flip_rows(flip_cols(pat)))
    )


replace = {}
for line in open("21-input.txt"):
    parts = line.rstrip().split(" => ")
    pattern, output = to_2d(parts[0]), to_2d(parts[1])
    for variant in variants(pattern):
        replace[variant] = output

image = [
    [".", "#", "."],
    [".", ".", "#"],
    ["#", "#", "#"]
]

for n in range(18):
    if len(image) % 2 == 0:
        pat_size = 2
        out_size = 3
    else:
        pat_size = 3
        out_size = 4
    new_size = len(image) // pat_size * out_size
    new_image = [[None for _ in range(new_size)] for _ in range(new_size)]
    for y in range(0, len(image), pat_size):
        y_out = y // pat_size * out_size
        for x in range(0, len(image), pat_size):
            x_out = x // pat_size * out_size
            pat = tuple(tuple(image[yy][xx] for xx in range(x, x+pat_size)) for yy in range(y, y+pat_size))
            out = replace[pat]
            for yy_out in range(out_size):
                for xx_out in range(out_size):
                    new_image[y_out+yy_out][x_out+xx_out] = out[yy_out][xx_out]
    image = new_image

    if n in (5-1, 18-1):
        count = 0
        for y in range(len(image)):
            for x in range(len(image)):
                if image[y][x] == "#":
                    count += 1
        print(count)
