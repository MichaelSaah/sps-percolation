from tools.graphs import BondGraph, HexGraph
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
import numpy as np

n = 100 # number of trials
size = 20 # size of domain (size*size)
p_range = np.linspace(0.05, 0.95, 30) # range of Bernoulli probabilities to test over
full_perc_count = np.zeros((len(p_range), 1)) # count number of fully percolated graphs

for i,p in enumerate(p_range):
    for _ in range(n):
        G = BondGraph(size,p)
        if G.is_fully_percolated():
            full_perc_count[i] += 1

percent_perc = full_perc_count / n

plt.plot(p_range, percent_perc, 'b.')
plt.xlabel('probility of edge closure')
plt.ylabel('porportion fully percolated')
plt.title('Bond percolation, ' + str(n) + ' samples, ' + str(size) + 'x' + str(size) + ' domain')
plt.show()
