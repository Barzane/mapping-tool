#Erdos-Renyi random network generator
#input: (list of nodes, p)
#output: adjacency matrix g

import numpy as np

def random_network(nodes, p):
    
    p = p/2.0
    edge_matrix = np.random.choice([1,0], size=(len(nodes), len(nodes)), replace=True, p=[p, 1-p])
    edge_matrix = edge_matrix + edge_matrix.T
    np.fill_diagonal(edge_matrix, 0)
    g = np.round(edge_matrix * 0.6)
    
    assert np.array_equal(g, g.T), 'g not symmetric' # g symmetric
    
    return g

#test case

#edges = random_network([0 for x in range(10)], 0.25)
#print edges
