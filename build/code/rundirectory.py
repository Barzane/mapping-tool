# -*- coding: utf-8 -*-

import os, glob, shutil, os.path, numpy

import state_state_border_dictionary
import mexico_us_canada_us_border_dictionary
import coast_border_dictionary
import plot_map_with_airports
import plot_blank_map
import add_routes_to_map
import make_route_list
import random_network
import compute_density
from connected import connected
from density_degree_distribution import density_degree_distribution
from degree_centrality import degree_centrality
from invert_dict import invert_dict
from closeness_centrality import closeness_centrality
from centrality_eigenvector import centrality_eigenvector
from distance_matrix import distance_matrix
from centrality_betweenness import all_centrality_betweenness
import pure_pref_att_network

def horizontal():
    
    print
    print '-'*90
    print
    
    return None

def manual_transfer_reminder():

    print 'manually transfer data_yyyy_q.bin datafiles (output from network-data) to data\\ before run'
    print
    print '** DISK SPACE REQUIREMENT: ~ 194 MB to store 60 quarterly datafiles (1999_1 to 2013_4) **'
    
#    raw_input('press a key to continue')
    
    return None

def clear_output_temp_input():
    
    print 'clear contents of \output and \\temp and \input'

    for folder in ['..\\output\\*', '..\\temp\\*', '..\\input\\*']:
    
        folder_contents = glob.glob(folder)
    
        for filename in folder_contents:
            
            os.remove(filename)
    
    return None

horizontal()
   
manual_transfer_reminder()

horizontal()
    
clear_output_temp_input()

horizontal()

sss

src_blank_map = '..\\..\\data\\borders\\blank_map.bin'

#http://stackoverflow.com/questions/82831/check-whether-a-file-exists-using-python

if not os.path.isfile(src_blank_map):
    
    print src_blank_map + ' does not exist: rebuild'
    
    print 'build state-state border dictionary, save to \\input'
    
    state_state_border_dictionary.build_dict()
    
    print 'build US-Mexico and US-Canada border dictionary, save to \\input'
    
    mexico_us_canada_us_border_dictionary.build_dict()
    
    print 'US coast border dictionary, save to \\input'
    
    coast_border_dictionary.build_dict()

    print 'plot blank map, save to ..\data\\borders'
    
    plot_blank_map.plot()
    
else:
    
    print src_blank_map + ' already exists: no rebuild'

full_sample = False

if full_sample:
    year_range = range(1999, 2014)
    quarter_range = range(1, 5)
else:
    year_range = [2013]
    quarter_range = [4]
    
for year in year_range:
    for quarter in quarter_range:

        carrier = 'WN'
          
        print 'copy data_year_quarter.bin datafile from ..\data to \input'
        
        src = '..\\..\\data\\data_' + str(year) + '_' + str(quarter) + '.bin'
        dst = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
        
        shutil.copyfile(src, dst)
        
        print 'plot map with airports for ' + dst + ', save .png to \output, .bin to \\temp'
        
        all_airports = plot_map_with_airports.plot(dst, year, quarter)
        
        print 'add routes to map with airports'
        
        #https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
        
        route_options = {}
        route_options['year'] = year
        route_options['quarter'] = quarter
        route_options['carrier'] = carrier
        route_options['test'] = False
        route_options['constant_weight'] = False
        route_options['erdos_renyi'] = False
        route_options['pref_attachment'] = True
        route_options['all_airports'] = all_airports
        
        assert not (route_options['test'] and route_options['erdos_renyi'])
        assert not (route_options['test'] and route_options['pref_attachment'])
        assert not (route_options['erdos_renyi'] and route_options['pref_attachment'])
        
        if route_options['erdos_renyi'] or route_options['pref_attachment']:
            
            density, Nbar, gbar = compute_density.density(year, quarter, carrier) 
            print 'density for carrier', carrier, 'is', density
            inv_d = invert_dict(Nbar)
            
        if route_options['erdos_renyi']:
            
            g = random_network.random_network(gbar, density)
        
        elif route_options['pref_attachment']:
        
            g, g_dynamic = pure_pref_att_network.generate(range(len(gbar)), 6)
        
        else:
            
            g = None
            
        route_options['Nbar'] = Nbar
        route_options['g'] = g
        
        if route_options['erdos_renyi'] or route_options['pref_attachment']:
            
            number_nodes = len(g)
            number_edges = sum(sum(g)) / 2
            diameter_g = connected(g)
            density, Pd = density_degree_distribution((Nbar, g))
            DC = degree_centrality((Nbar, g))
            CC = closeness_centrality(g)
            eigenvector_map = centrality_eigenvector(g)
            D, average_path_length = distance_matrix(g)
            
            if len(Nbar) > 2 and not numpy.isinf(average_path_length):
                BC = all_centrality_betweenness(D)
            
            print '# nodes', number_nodes
            print '# edges', number_edges
            print 'diameter', diameter_g
            print 'density', density
            
            print 'BC'
            if len(Nbar) > 2 and not numpy.isinf(average_path_length):
                for key in BC:
                    if inv_d[key] == 'DEN':
                        print inv_d[key], BC[key],
            
            print '\nCC'
            for key in CC:
                if inv_d[key] == 'DEN':
                    print inv_d[key], CC[key],
            
            print '\nDC'
            for key in DC:
                if inv_d[key] == 'DEN':
                    print inv_d[key], DC[key],
            
            print '\nEC'
            for key in eigenvector_map:
                if inv_d[key] == 'DEN':
                    print inv_d[key], eigenvector_map[key],

            print
        
#        animation - conflict with single call of route_list?
#        if route_options['pref_attachment']:
#            
#            route_list_fullsize = list()
#            
#            for g_dyn in g_dynamic:
#                
#                try:
#            
#                    route_options['g'] = g_dyn
#                    route_list = make_route_list.route(**route_options)
#                    route_list_fullsize.append(route_list[:])
#                    
#                except IndexError:
#                    
#                    print '\n' + carrier + ' not found in ' + str(year) + 'Q' + str(quarter)
#                    
#                    continue
#        
#        counter = 0        
#
#        for route_list in route_list_fullsize:
#            
#            add_routes_to_map.add_routes(carrier, year, quarter, route_list, route_options['erdos_renyi'], route_options['pref_attachment'], 'geodesic', counter)
#            
#            counter += 1
        
#        try:
#            
#            route_list = make_route_list.route(**route_options)
#            
#        except IndexError:
#            
#            print '\n' + carrier + ' not found in ' + str(year) + 'Q' + str(quarter)
#            
#            continue
#                
#        add_routes_to_map.add_routes(carrier, year, quarter, route_list, route_options['erdos_renyi'], route_options['pref_attachment'], 'geodesic')
        
        print '[warning] \\temp airport instances must be regenerated for other periods'

print 'move pyc files (byte code) from \code to \\temp'

src = '.\\'
dst = '..\\temp\\'

for folder in [src + '*.pyc']:
    
    folder_contents = glob.glob(folder)
    
    for filename in folder_contents:
        
        filename_split = filename.split('\\')[-1]
        shutil.move(filename, dst + filename_split)
     