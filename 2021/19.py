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
import itertools

# from part 1
ans1 = [[0, 0, 0], [-1250, -3, 1250], [-1200, -59, 128], [1153, -188, 125], [-150, 4, 1292], [1054, -1224, 3645], [-1, 8, 2512], [1034, -2418, 1317], [1162, -148, 1277], [-1328, -124, -1155], [-29, -2478, 1235], [1081, 1192, 2368], [1231, -84, 2356], [1222, -2393, 61], [1215, -29, 4902], [1153, -1309, 2500], [1169, -1293, 1321], [24, -2428, -32], [-16, -51, -1141], [-152, 1133, 1178], [2313, -1342, 1280], [3599, -2502, 1336], [-1236, -2499, 1249], [-123, -1208, 1270], [-1240, -2442, 2467], [14, -1321, 2436], [2314, -2564, 1273], [26, -1207, 140], [1163, -123, 3669], [1223, -184, 6096]]

best = 0
for i in range(0, len(ans1)-1):
    for j in range(i, len(ans1)):
        dist = abs(ans1[i][0] - ans1[j][0]) + abs(ans1[i][1] - ans1[j][1]) + abs(ans1[i][2] - ans1[j][2])
        if dist > best:
            best = dist
print(best)


data = aocd.get_data(day=19, year=2021)
# data = """--- scanner 0 ---
# 404,-588,-901
# 528,-643,409
# -838,591,734
# 390,-675,-793
# -537,-823,-458
# -485,-357,347
# -345,-311,381
# -661,-816,-575
# -876,649,763
# -618,-824,-621
# 553,345,-567
# 474,580,667
# -447,-329,318
# -584,868,-557
# 544,-627,-890
# 564,392,-477
# 455,729,728
# -892,524,684
# -689,845,-530
# 423,-701,434
# 7,-33,-71
# 630,319,-379
# 443,580,662
# -789,900,-551
# 459,-707,401
#
# --- scanner 1 ---
# 686,422,578
# 605,423,415
# 515,917,-361
# -336,658,858
# 95,138,22
# -476,619,847
# -340,-569,-846
# 567,-361,727
# -460,603,-452
# 669,-402,600
# 729,430,532
# -500,-761,534
# -322,571,750
# -466,-666,-811
# -429,-592,574
# -355,545,-477
# 703,-491,-529
# -328,-685,520
# 413,935,-424
# -391,539,-444
# 586,-435,557
# -364,-763,-893
# 807,-499,-711
# 755,-354,-619
# 553,889,-390
#
# --- scanner 2 ---
# 649,640,665
# 682,-795,504
# -784,533,-524
# -644,584,-595
# -588,-843,648
# -30,6,44
# -674,560,763
# 500,723,-460
# 609,671,-379
# -555,-800,653
# -675,-892,-343
# 697,-426,-610
# 578,704,681
# 493,664,-388
# -671,-858,530
# -667,343,800
# 571,-461,-707
# -138,-166,112
# -889,563,-600
# 646,-828,498
# 640,759,510
# -630,509,768
# -681,-892,-333
# 673,-379,-804
# -742,-814,-386
# 577,-820,562
#
# --- scanner 3 ---
# -589,542,597
# 605,-692,669
# -500,565,-823
# -660,373,557
# -458,-679,-417
# -488,449,543
# -626,468,-788
# 338,-750,-386
# 528,-832,-391
# 562,-778,733
# -938,-730,414
# 543,643,-506
# -524,371,-870
# 407,773,750
# -104,29,83
# 378,-903,-323
# -778,-728,485
# 426,699,580
# -438,-605,-362
# -469,-447,-387
# 509,732,623
# 647,635,-688
# -868,-804,481
# 614,-800,639
# 595,780,-596
#
# --- scanner 4 ---
# 727,592,562
# -293,-554,779
# 441,611,-461
# -714,465,-776
# -743,427,-804
# -660,-479,-426
# 832,-632,460
# 927,-485,-438
# 408,393,-506
# 466,436,-512
# 110,16,151
# -258,-428,682
# -393,719,612
# -211,-452,876
# 808,-476,-593
# -575,615,604
# -485,667,467
# -680,325,-822
# -627,-443,-432
# 872,-547,-609
# 833,512,582
# 807,604,487
# 839,-516,451
# 891,-625,532
# -652,-548,-490
# 30,-46,-14"""

scanners = []

for line in data.splitlines():
    if line.startswith("---"):
        scanner = []
    elif line == "":
        scanner.sort()
        scanners.append(scanner)
    else:
        scanner.append([int(n) for n in line.split(",")])
scanner.sort()
scanners.append(scanner)

permutations = list(itertools.permutations([0, 1, 2]))
def rotate(scanner, n):
    perm = permutations[n // 8]
    x_mult = 1 if (n & 4 == 0) else -1
    y_mult = 1 if (n & 2 == 0) else -1
    z_mult = 1 if (n & 1 == 0) else -1
    #print(perm, x_mult, y_mult, z_mult)
    rotated_scanner = []
    for point in scanner:
        rotated_scanner.append([point[perm[0]] * x_mult, point[perm[1]] * y_mult, point[perm[2]] * z_mult])
    rotated_scanner.sort()
    return rotated_scanner


#def compare(scanner1, scanner2):

# for point in scanners[0]:
#     print(point)
# print()

def check_overlap(scanner1, scanner2):
    x_set = set(point[0] for point in scanner1)
    y_set = set(point[1] for point in scanner1)
    z_set = set(point[2] for point in scanner1)

    valid_x = set()
    valid_y = set()
    valid_z = set()
    x_offsets = set()
    y_offsets = set()
    z_offsets = set()
    for n in range(48):
        rotated_scanner = rotate(scanner2, n)
        for offset in range(-2000, 2000+1):
            rotated_x_set = set(point[0]+offset for point in rotated_scanner)
            overlap = len(x_set & rotated_x_set)
            if overlap >= 10:
                valid_x.add(n)
                x_offsets.add(offset)
        for offset in range(-2000, 2000+1):
            rotated_y_set = set(point[1]+offset for point in rotated_scanner)
            overlap = len(y_set & rotated_y_set)
            if overlap >= 10:
                valid_y.add(n)
                y_offsets.add(offset)
        for offset in range(-2000, 2000+1):
            rotated_z_set = set(point[2]+offset for point in rotated_scanner)
            overlap = len(z_set & rotated_z_set)
            if overlap >= 10:
                valid_z.add(n)
                z_offsets.add(offset)
    rotations = valid_x & valid_y & valid_z
    if len(rotations) == 1 and len(x_offsets) == 1 and len(y_offsets) == 1 and len(z_offsets) == 1:
        rotation = list(rotations)[0]
        x_offset = list(x_offsets)[0]
        y_offset = list(y_offsets)[0]
        z_offset = list(z_offsets)[0]
        return rotation, x_offset, y_offset, z_offset
    else:
        if len(rotations) + len(x_offsets) + len(y_offsets) + len(z_offsets) > 0:
            print("something fishy")
            print(sorted(x_set), sorted(set(point[0] for point in scanner2)))
            print(valid_x, valid_y, valid_z, x_offsets, y_offsets, z_offsets)
        #print(len(rotations), len(x_offsets), len(y_offsets), len(z_offsets))
        return None, None, None, None


# scanners_used = [False] * len(scanners)
#
# scanners_sofar = scanners[0]
# scanners_used[0] = True
#
# while sum(scanners_used) < len(scanners):
#     for i in range(len(scanners)):
#         print(i)
#         if not scanners_used[i]:
#             rotation, x_offset, y_offset, z_offset = check_overlap(scanners_sofar, scanners[i])
#             if rotation:
#                 print(rotation, x_offset, y_offset, z_offset)
#                 scanners_used[i] = True
#                 rotated_scanner = rotate(scanners[i], rotation)
#                 for point in rotated_scanner:
#                     new_point = [point[0] + x_offset, point[1] + y_offset, point[2] + z_offset]
#                     if new_point not in scanners_sofar:
#                         scanners_sofar.append(new_point)
#
# print(len(scanners_sofar))

offsets = [None] * len(scanners)
offsets[0] = [0, 0, 0]
queue = [0]

while len(queue) > 0:
    ii = queue.pop(0)
    for jj in range(len(scanners)):
        if offsets[jj] is not None:
            continue

# for i in range(0, len(scanners)-1):
#     for j in range(i+1, len(scanners)):
        print(ii, jj, offsets[ii], offsets[jj])

        rotation, x_offset, y_offset, z_offset = check_overlap(scanners[ii], scanners[jj])
        if rotation is not None:
            queue.append(jj)
            print(ii, jj, rotation, x_offset, y_offset, z_offset)
            rotated_scanner = rotate(scanners[jj], rotation)
            scanners[jj] = rotated_scanner
            offsets[jj] = [offsets[ii][0] + x_offset, offsets[ii][1] + y_offset, offsets[ii][2] + z_offset]

print(offsets)

points = set()
for i in range(len(scanners)):
    for point in scanners[i]:
        points.add(tuple([point[c] + offsets[i][c] for c in range(3)]))
print(points)
print(len(points))


# aocd.submit(ans, part="a", day=19, year=2021)

# aocd.submit(ans, part="b", day=19, year=2021)
