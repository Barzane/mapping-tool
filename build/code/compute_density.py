# -*- coding: utf-8 -*-

import cPickle

import list_of_airlines
import list_of_airports
import map_airports_code
import adjacency_matrix
import remove_zeros
import density_degree_distribution

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
