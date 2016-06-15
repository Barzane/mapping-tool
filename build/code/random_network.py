# -*- coding: utf-8 -*-

import numpy

def random_network(nodes, density):
    
    p = density / 2.0
    
    edge_matrix = numpy.random.choice([1,0], size=(len(nodes), len(nodes)), replace=True, p=[p, 1-p])
    edge_matrix = edge_matrix + edge_matrix.T
    numpy.fill_diagonal(edge_matrix, 0)
    
#    print 'edge_matrix will contains values 0, 1, 2'
#    print 'map 0 to 0, 1 to 1, 2 to 1'
    
    g = numpy.round(edge_matrix * 0.6)
    
    assert numpy.array_equal(g, g.T), 'g not symmetric'
    
    g = g.astype(int)
    
    return g
