#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx

DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75), (1, 4, 0.3)])
"""print(DG.out_degree(1, weight='weight'))
print(DG.degree(1, weight='weight'))
print(list(DG.successors(1))) # = neighbors
print(list(DG.neighbors(1)))"""


MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
#print(dict(MG.degree(weight='weight')))


ws = nx.watts_strogatz_graph(30, 3, 0.1)
nx.write_graphml(ws, "watts_strogatz.graphml")
# https://www.yworks.com/yed-live/