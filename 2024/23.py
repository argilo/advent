#!/usr/bin/env python3

# Copyright 2024 Clayton Smith
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
import networkx as nx

data = aocd.get_data(day=23, year=2024)

# data = """kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn"""

graph = nx.Graph()
for line in data.splitlines():
    c1, c2 = line.split("-")
    graph.add_edge(c1, c2)

ans = 0
for c1, c2, c3 in itertools.combinations(graph.nodes(), 3):
    if c1.startswith("t") or c2.startswith("t") or c3.startswith("t"):
        if graph.has_edge(c1, c2) and graph.has_edge(c2, c3) and graph.has_edge(c3, c1):
            # print(c1, c2, c3)
            ans += 1

print(ans)
# aocd.submit(ans, part="a", day=23, year=2024)

clique = nx.max_weight_clique(graph, weight=None)[0]
ans = ",".join(sorted(clique))

print(ans)
# aocd.submit(ans, part="b", day=23, year=2024)
