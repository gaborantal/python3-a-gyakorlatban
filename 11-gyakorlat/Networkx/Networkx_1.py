#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_node("node_1")
G.add_nodes_from([2, 3, 5, 15, "node_15"])

#print(G.number_of_nodes())
#print(G.nodes())
G.remove_node("node_15")
#print(G.nodes())


G.add_edge(1,2)
e=(5,15)
G.add_edge(*e) # !!!! * !!!!
G.add_edges_from([(1,2),(1,3), (3,5)])
#print(G.number_of_edges())
#print(G.edges())
G.remove_edge(1,2)
#print(G.edges())

#print(G.neighbors(3))
#print(G[3])
G[1][3]['color'] = "blue"
#print(G[3])
#print(G.degree(3))