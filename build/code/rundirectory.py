# -*- coding: utf-8 -*-

import os, glob, shutil, os.path, sys

import state_state_border_dictionary
import mexico_us_canada_us_border_dictionary
import coast_border_dictionary
import plot_map_with_airports
import plot_blank_map
import add_routes_to_map
import make_route_list
import random_network
import compute_density

print
print 'clear contents of \output and \\temp and \input'

for folder in ['..\\output\\*', '..\\temp\\*', '..\\input\\*']:

    folder_contents = glob.glob(folder)

    for filename in folder_contents:
        os.remove(filename)

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
        route_options['erdos_renyi'] = True
        route_options['all_airports'] = all_airports
        
        assert not (route_options['test'] and route_options['erdos_renyi'])
        
        if route_options['erdos_renyi']:
            
            density, Nbar, gbar = compute_density.density(year, quarter, carrier) 
            print 'density for carrier', carrier, 'is', density
            
        if route_options['erdos_renyi']:
            
            g = random_network.random_network(gbar, density)
            
        else:
            
            g = None
            
        route_options['Nbar'] = Nbar
        route_options['g'] = g
        
        try:
            
            route_list = make_route_list.route(**route_options)
            
        except IndexError:
            
            print '\n' + carrier + ' not found in ' + str(year) + 'Q' + str(quarter)
            
            continue
                
        add_routes_to_map.add_routes(carrier, year, quarter, route_list, route_options['erdos_renyi'], line_type='geodesic')
        
        print '[warning] \\temp airport instances must be regenerated for other periods'

print 'move pyc files (byte code) from \code to \\temp'

src = '.\\'
dst = '..\\temp\\'

for folder in [src + '*.pyc']:
    
    folder_contents = glob.glob(folder)
    
    for filename in folder_contents:
        
        filename_split = filename.split('\\')[-1]
        shutil.move(filename, dst + filename_split)
     