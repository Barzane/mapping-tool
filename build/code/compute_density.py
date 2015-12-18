# -*- coding: utf-8 -*-

import cPickle, numpy, sys

src_network_measures = '..\\..\\..\\network-data\\build\\code\\'

#http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
sys.path.append(src_network_measures)

from list_of_airlines import list_of_airlines
from list_of_airports import list_of_airports
from map_airports_code import map_airports_code
from adjacency_matrix import adjacency_matrix
from remove_zeros import remove_zeros
from invert_dict import invert_dict
from distance_matrix import distance_matrix
from degree_centrality import degree_centrality
from closeness_centrality import closeness_centrality
from centrality_betweenness import all_centrality_betweenness
from centrality_eigenvector import centrality_eigenvector
from density_degree_distribution import density_degree_distribution
from route_level_g import route_level_g
#from connected import connected

import other_carrier_centrality

def density(year, quarter, carrier):

    src = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    all_airlines = list_of_airlines(data)
    
    assert (carrier in all_airlines    ), 'carrier not found'
    
    all_airports = list_of_airports(data)
    
    N = map_airports_code(all_airports)  
    g = adjacency_matrix(data, N, carrier)
    network = (N, g)
    
    Nbar, gbar = remove_zeros(N, g)
    network_bar = (Nbar, gbar)
    
#    D, average_path_length = distance_matrix(gbar)
      
    density, Pd = density_degree_distribution(network)      
#    density, Pd = density_degree_distribution(network_bar)
    
    return density
