#!/usr/bin/env python3

# Copyright 2021 Clayton Smith
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

data = aocd.get_data(day=16, year=2021)
# data = "8A004A801A8002F478"
# data = "620080001611562C8802118E34"
# data = "C0015000016115A2E0802F182340"
# data = "A0016C880162017C3686B18A3D4780"

# data = "C200B40A82"
# data = "04005AC33890"
# data = "880086C3E88112"
# data = "CE00C43D881120"
# data = "D8005AC2A8F0"
# data = "F600BC2D8F"
# data = "9C005AC2F8F0"
# data = "9C0141080250320F1802104A08"


bits = []
for digit in data:
    bits += [int(b) for b in "{:04b}".format(int(digit, 16))]

def read_int(bits):
    return int("".join(str(b) for b in bits), 2)

def parse(bits, offset):
    global ans

    orig_offset = offset

    version = read_int(bits[offset:offset+3])
    offset += 3
    type_id = read_int(bits[offset:offset+3])
    offset += 3


    if type_id == 4:
        int_bits = []
        while bits[offset] == 1:
            int_bits += bits[offset+1:offset+5]
            offset += 5
        int_bits += bits[offset+1:offset+5]
        offset += 5
        int_value = int("".join(str(b) for b in int_bits), 2)
        result = int_value
    else:
        if bits[offset] == 0:
            length = read_int(bits[offset+1:offset+16])
            offset += 16

            total_read_bits = 0
            sub_results = []
            while total_read_bits < length:
                sub_result, read_bits = parse(bits, offset)
                offset += read_bits
                sub_results.append(sub_result)
                total_read_bits += read_bits
        else:
            num_packets = read_int(bits[offset+1:offset+12])
            offset += 12

            total_read_packets = 0
            sub_results = []
            while total_read_packets < num_packets:
                sub_result, read_bits = parse(bits, offset)
                offset += read_bits
                sub_results.append(sub_result)
                total_read_packets += 1

        if type_id == 0:
            result = sum(sub_results)
        elif type_id == 1:
            prod = 1
            for sr in sub_results:
                prod *= sr
            result = prod
        elif type_id == 2:
            result = min(sub_results)
        elif type_id == 3:
            result = max(sub_results)
        elif type_id == 5:
            result = 1 if sub_results[0] > sub_results[1] else 0
        elif type_id == 6:
            result = 1 if sub_results[0] < sub_results[1] else 0
        elif type_id == 7:
            result = 1 if sub_results[0] == sub_results[1] else 0

    ans += version
    return result, offset - orig_offset


ans = 0
final_result, bits = parse(bits, 0)

print(ans)
print(final_result)
