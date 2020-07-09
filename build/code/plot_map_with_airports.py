# -*- coding: utf-8 -*-

import cPickle, imp, matplotlib, matplotlib.pyplot

list_of_airlines = imp.load_source('list_of_airlines', '../../../network_data/build/code/list_of_airlines.py')

import nodes_for_illustrations

#http://stackoverflow.com/questions/4142151/python-how-to-import-the-class-within-the-same-directory-or-sub-directory

from airport_classes import Airport

matplotlib.pyplot.ioff()
        
def plot(src, year, quarter, highlight_nodes=False):

    matplotlib.pyplot.close('all')
    
    src_blank_map = '..\\..\\data\\borders\\blank_map.bin'
    
    dst_png = '..\\temp\\map_' + str(year) + '_' + str(quarter) + '.png'
    dst_bin = '..\\temp\\map_' + str(year) + '_' + str(quarter) + '.bin'
        
    f = open(src_blank_map, 'rb')
        
    fig = cPickle.load(f)
    f.close()
    
    f = open(src, 'r')
    data = cPickle.load(f)
    f.close()
    
    all_airlines = list_of_airlines.list_of_airlines(data)    
    
    airport_dict = {}
    
    for key in data:
        
        list_v = key.split('_')
        origin = list_v[0]
        destination = list_v[1]
        
        if origin not in airport_dict:
            
            airport_dict[origin] = Airport(data[key]['originLongitude'],\
                data[key]['originLatitude'], origin)
        
        if destination not in airport_dict:
            
            airport_dict[destination] = Airport(data[key]['destinationLongitude'],\
                data[key]['destinationLatitude'], destination)   
    
    all_airports = list()  
    
    for airport in Airport:
        
        all_airports.append([airport.name, airport])
        
        matplotlib.pyplot.plot(airport.x, airport.y, 'ro')
        matplotlib.pyplot.annotate(airport.name, ([airport.x, airport.y]))
        
        f = open('..\\temp\\airport_' + airport.name + '.bin', 'wb')
        cPickle.dump(airport, f)
        f.close()        
    
    all_airports.sort()
    
    matplotlib.pyplot.title(str(year) + 'Q' + str(quarter))
    
    if highlight_nodes and year == 2013 and quarter == 4:
        
        nodes_for_illustrations.example_nodes('', fig)
    
    f = open(dst_bin, 'w')
    cPickle.dump(fig, f)
    f.close()    
    
    matplotlib.pyplot.savefig(dst_png, bbox_inches='tight')
    matplotlib.pyplot.close(fig)
    
    return all_airports, all_airlines
