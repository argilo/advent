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

import intcode
import itertools

with open("07-input.txt") as f:
    prog = [int(n) for n in f.read().rstrip().split(",")]

max_signal = 0
for phases in itertools.permutations(range(5)):
    signal = 0
    for phase in phases:
        amp = intcode.execute(prog)
        next(amp)
        amp.send(phase)
        signal = amp.send(signal)
    if signal > max_signal:
        max_signal = signal
print(max_signal)

max_signal = 0
for phases in itertools.permutations(range(5, 10)):
    amps = [intcode.execute(prog) for _ in range(5)]
    for amp, phase in zip(amps, phases):
        next(amp)
        amp.send(phase)

    signal = 0
    halt = False
    while not halt:
        for amp in amps:
            signal = amp.send(signal)
            try:
                next(amp)
            except StopIteration:
                halt = True

    if signal > max_signal:
        max_signal = signal
print(max_signal)
