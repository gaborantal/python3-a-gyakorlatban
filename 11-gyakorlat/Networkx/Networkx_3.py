import networkx as nx

# opciok: https://networkx.github.io/documentation/stable/reference/index.html

G = nx.connected_caveman_graph(4,7)
print(nx.number_of_cliques(G))
for clique in nx.find_cliques(G):
	print(clique)
print("\n")

print(nx.degree_centrality(G))
print("\n")
print(nx.edge_betweenness_centrality(G))
print("\n")

degree_sequence=sorted(nx.degree(G).values(),reverse=True)
print(degree_sequence)