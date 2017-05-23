# -*- coding: utf-8 -*-

import os, glob, shutil, os.path, numpy, sys

import state_state_border_dictionary
import mexico_us_canada_us_border_dictionary
import coast_border_dictionary

def horizontal():
    
    print
    print '-'*90
    print
    
    return None

import access_external_functions

horizontal()

access_external_functions.set_path()

import plot_map_with_airports
import plot_blank_map
import compute_density
import connected
import density_degree_distribution
import degree_centrality
import closeness_centrality
import distance_matrix
import centrality_betweenness
import invert_dict
import random_network
import centrality_eigenvector
import add_routes_to_map
import make_route_list

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

horizontal()

full_sample = False

if full_sample:
    
    year_range = range(1999, 2014)
    quarter_range = range(1, 5)
    
else:
    
    year_range = [2013]
    quarter_range = [4]
    
for year in year_range:
    
    for quarter in quarter_range:
          
        print 'copy data_year_quarter.bin datafile from ..\data to \input'
        
        src = '..\\..\\data\\data_' + str(year) + '_' + str(quarter) + '.bin'
        dst = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
        
        shutil.copyfile(src, dst)
        
        print '\nplot map with airports for ' + dst + ', save .png to \output, .bin to \\temp'
        
        horizontal()        
        
        nodes_on_blank_map = False
        
        if not nodes_on_blank_map:
            
            all_airports, all_airlines = plot_map_with_airports.plot(dst, year, quarter)

        else:
            
            if year == 2013 and quarter == 4:
            
                all_airports, all_airlines = plot_map_with_airports.plot(dst, year, quarter, True)
             
                print 'Copy map_2013_4.png illustrative plot from ..\\temp to \output'
                 
                src_png = '..\\temp\\map_' + str(year) + '_' + str(quarter) + '.png'
                dst_png = '..\\output\\map_dominant_hubs_' + str(year) + '_' + str(quarter) + '.png'
                 
                shutil.copyfile(src_png, dst_png)

                print '\nExit code'
                 
                horizontal()
                 
                raise SystemError
                 
            else:
                
                raise NotImplementedError('set nodes_on_blank_map = False if not 2013Q4')
            
        for carrier in all_airlines:
        
            print 'add routes to map with airports, carrier', carrier
            
            #https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
            
            route_options = dict()
                    
            route_options['year'] = year
            route_options['quarter'] = quarter
            route_options['carrier'] = carrier
            route_options['test'] = False
            route_options['constant_weight'] = False        
            route_options['erdos_renyi'] = False
            route_options['all_airports'] = all_airports
            route_options['highlight_nodes'] = False
            
            assert not (route_options['test'] and route_options['erdos_renyi'])

            density, Nbar, gbar = compute_density.density(year, quarter, carrier)
            
            if route_options['erdos_renyi']:
                                                
                print 'Erdos-Renyi',
                print 'density for carrier', carrier, 'is %.3f'%density
    
                inv_d = invert_dict.invert_dict(Nbar)
                
                horizontal()
            
            if route_options['erdos_renyi']:
                
                g = random_network.random_network(gbar, density)
            
            else:
                
                g = None
    
            route_options['Nbar'] = Nbar
            route_options['g'] = g
            
            if route_options['erdos_renyi']:
                
                number_nodes = len(g)
                number_edges = sum(sum(g)) / 2
                diameter_g = connected.connected(g)
                density, Pd = density_degree_distribution.density_degree_distribution((Nbar, g))
                DC = degree_centrality.degree_centrality((Nbar, g))
                CC = closeness_centrality.closeness_centrality(g)
                eigenvector_map = centrality_eigenvector.centrality_eigenvector(g)
                D, average_path_length = distance_matrix.distance_matrix(g)
                
                if len(Nbar) > 2 and not numpy.isinf(average_path_length):
                    
                    BC = centrality_betweenness.all_centrality_betweenness(D)
                
                print 'Erdos-Renyi'
                print '# nodes', number_nodes
                print '# edges', number_edges
                print 'diameter', diameter_g
                print 'density', density
                
                print '\nBC'
                
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
    
                horizontal()
                        
    #        animation - conflict with single call of route_list?
    #        
    #        counter = 0        
    #
    #        for route_list in route_list_fullsize:
    #            
    #            add_routes_to_map.add_routes(carrier, year, quarter, route_list, route_options['erdos_renyi'], route_options['pref_attachment'], 'geodesic', counter)
    #            
    #            counter += 1
            
            try:
                
                route_list = make_route_list.route(**route_options)
                
            except IndexError:
                
                print '\n' + carrier + ' not found in ' + str(year) + 'Q' + str(quarter)
                
                continue
            
            highlight_nodes = False
            
            add_routes_to_map.add_routes(carrier, year, quarter, route_list, route_options['erdos_renyi'], 'geodesic', highlight_nodes)
            
            horizontal()
            
            if route_options['test']:
                
                break
            
print '[warning] \\temp airport instances must be regenerated for other periods'
    
horizontal()

print 'move pyc files (byte code) from \code to \\temp'

src = '.\\'
dst = '..\\temp\\'

for folder in [src + '*.pyc']:
    
    folder_contents = glob.glob(folder)
    
    for filename in folder_contents:
        
        filename_split = filename.split('\\')[-1]
        shutil.move(filename, dst + filename_split)
     