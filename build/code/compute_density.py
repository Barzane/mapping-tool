# -*- coding: utf-8 -*-

import cPickle, imp

list_of_airlines = imp.load_source('list_of_airlines', '../../../network_data/build/code/list_of_airlines.py')
list_of_airports = imp.load_source('list_of_airports', '../../../network_data/build/code/list_of_airports.py')
map_airports_code = imp.load_source('map_airports_code', '../../../network_data/build/code/map_airports_code.py')
adjacency_matrix = imp.load_source('adjacency_matrix', '../../../network_data/build/code/adjacency_matrix.py')
remove_zeros = imp.load_source('remove_zeros', '../../../network_data/build/code/remove_zeros.py')
density_degree_distribution = imp.load_source('density_degree_distribution', '../../../network_data/build/code/density_degree_distribution.py')

def density(year, quarter, carrier):

    src = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    all_airlines = list_of_airlines.list_of_airlines(data)
    
    assert (carrier in all_airlines), 'carrier not found'
    
    all_airports = list_of_airports.list_of_airports(data)
    
    N = map_airports_code.map_airports_code(all_airports)
    
    g = adjacency_matrix.adjacency_matrix(data, N, carrier)
    
    Nbar, gbar = remove_zeros.remove_zeros(N, g)
    network_bar = (Nbar, gbar)
        
    density, Pd = density_degree_distribution.density_degree_distribution(network_bar)      
    
    return density, Nbar, gbar
