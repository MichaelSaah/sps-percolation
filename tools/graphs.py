import networkx as nx
import numpy as np

class BondGraph(nx.Graph):
    
    def __init__(self, size, p):
        super().__init__()

        # generate grid graph with random edges
        self.add_nodes_from(self.gen_nodes(size))
        self.add_edges_from(self.gen_edges(size, p))
    
        # find wet nodes (assume percolation from bottom)
        wet_nodes = set()
        for k in range(size):
            wet_nodes = wet_nodes | nx.node_connected_component(self, (k,0)) # set union
        self.wet_nodes = wet_nodes

        # find dry nodes
        self.dry_nodes = {node for node in self.nodes if node not in self.wet_nodes}


    def get_dry_lines(self):
        edges = self.subgraph(self.dry_nodes).edges
        
        return self.edges_as_lines(edges)


    def get_wet_lines(self):
        edges = self.subgraph(self.wet_nodes).edges

        return self.edges_as_lines(edges)


    @staticmethod
    def gen_nodes(n):
        """
        Generate nodes on the nxn integer grid
        """
    
        for i in range(n):
            for j in range(n):
                yield (i,j)
    

    @staticmethod
    def gen_edges(n,p):
        """
        Generate edges between nodes on the nxn integer grid with probability p
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
    

    @staticmethod
    def edges_as_lines(edges):
        """
        Helper fct for plotting edges    
        """

        return [((e[0][0], e[1][0]), (e[0][1], e[1][1])) for e in edges]    
