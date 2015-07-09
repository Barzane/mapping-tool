# -*- coding: utf-8 -*-

import cPickle, matplotlib

matplotlib.pyplot.ioff()

class IterRegistry(type):

#    http://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python
    
    def __iter__(cls):
        return iter(cls._registry)
        
class Airport:
    
    __metaclass__ = IterRegistry
    _registry = []

    def __init__(self, x, y, name):
        
        self._registry.append(self)
        
#        longitude (x) and latitude (y), in degrees
        
        self.x = float(x)
        self.y = float(y)
        
        self.name = name
        
def plot(src, year, quarter):
    
    src_blank_map = '..\\..\\data\\borders\\blank_map.bin'
    
    dst = '..\\output\\map_' + str(year) + '_' + str(quarter) + '.png'

    f = open(src_blank_map, 'r')
    fig = cPickle.load(f)
    f.close()    
    
    f = open(src, 'r')
    data = cPickle.load(f)
    f.close()
    
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
            
    for airport in Airport:
        
        matplotlib.pyplot.plot(airport.x, airport.y, 'ro')
        matplotlib.pyplot.annotate(airport.name, ([airport.x, airport.y]))
    
    matplotlib.pyplot.title('AIRPORTS IN DATASET: ' + str(year) + 'Q' +\
        str(quarter))    
    
    matplotlib.pyplot.savefig(dst, bbox_inches='tight')
    matplotlib.pyplot.close(fig)
    
    return None
