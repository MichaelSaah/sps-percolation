import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def gen_grid(n):
    """
    Generate coorinates on the nxn grid
    """

    for i in range(n):
        for j in range(n):
            yield (i,j)


def gen_edges(n,p):
    """
    Generate edges between coordinates on the nxn grid with probability p
    """

    # horizontal edges
    for i in range(n):
        for j in range(n-1):
            if np.random.rand() < p:
                yield ((i, j), (i, j+1))

    # vertical edges
    for j in range(n):
        for i in range(n-1):
            if np.random.rand() < p:
                yield ((i, j), (i+1, j))


def edges_to_lines(edges):
    """
    Helper fct for plotting edges    
    """

    return [((e[0][0], e[1][0]), (e[0][1], e[1][1])) for e in edges]


# setup
fig, ax = plt.subplots(3, 2, sharex='col', sharey='row')
fig.suptitle('Bond Percolation For Six Probabilities')
ax = ax.flat
p_vals = [2/10, 3/10, 4/10, 5/10, 6/10, 7/10]
n = 30

for i in range(len(p_vals)):
    # generate grid graph with random edges
    G = nx.Graph()
    G.add_nodes_from(gen_grid(n))
    G.add_edges_from(gen_edges(n, p_vals[i]))
    
    # split graph into wet and dry parts (assume percolation from bottom)
    wet_nodes = set()
    for k in range(n):
        wet_nodes = wet_nodes | nx.node_connected_component(G, (k,0)) # set union
    wet_graph = G.subgraph(wet_nodes)
    wet_edges = wet_graph.edges
    
    dry_nodes = {node for node in G.nodes if node not in wet_nodes}
    dry_graph = G.subgraph(dry_nodes)
    dry_edges = dry_graph.edges
    
    # plot wet edges in blue
    for edge in edges_to_lines(wet_edges):
        ax[i].plot(*edge, 'b-')
    
    # plot dry edges in black
    for edge in edges_to_lines(dry_edges):
        ax[i].plot(*edge, 'k-')
    
    ax[i].set_title('p = ' + "%.2f" % round(p_vals[i],2))

plt.show()
