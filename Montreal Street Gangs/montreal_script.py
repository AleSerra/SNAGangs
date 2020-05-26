import pandas as pd
import networkx as nx
import numpy as np
input_data = pd.read_csv('MONTREALGANG.csv', index_col=0)
G = nx.from_numpy_matrix(input_data.values)

print(input_data)
print(input_data.values)

print(nx.info(G))

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
dmax = max(degree_sequence)
dmin= min(degree_sequence)

print("Maximum degree: ",dmax)
print("Minimum degree: ",dmin)
print("Average degree: ",sum(degree_sequence)/len(degree_sequence))
print("Average degree centrality: ", sum(nx.degree_centrality(G).values())/len(nx.degree_centrality(G)))

from networkx.algorithms.community import greedy_modularity_communities
c = list(greedy_modularity_communities(G))
print("Number of communities: ",len(c))

print("Transitivity: ", nx.transitivity(G))

from networkx.algorithms.approximation import clique
print("Maximum clique number: ", len(clique.max_clique(G)))

print("Max k-core: ",max(nx.core_number(G).values()))

print("Number of triangles: ",sum(list(nx.triangles(G).values())))
print("Degree of assortativity: ", nx.degree_assortativity_coefficient(G))