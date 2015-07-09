# -*- coding: utf-8 -*-

import cPickle, matplotlib

#matplotlib.pyplot.ioff()

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
    
    f = open(src, 'r')
    data = cPickle.load(f)
    f.close()
    
    src_coast = '..\\input\\coast_border_dict.bin'
    src_mexico_canada = '..\\input\\mexico_us_canada_us_border_dict.bin'
    src_state_state = '..\\input\\state_state_border_dict.bin'
    
    f = open(src_state_state, 'r')
    border_dict = cPickle.load(f)
    f.close()
    
    f = open(src_mexico_canada, 'r')
    mexico_canada_dict = cPickle.load(f)
    f.close()

    mexico_dict = mexico_canada_dict['mexicoUSBorder']
    canada_dict = mexico_canada_dict['canadaUSBorder']

    f = open(src_coast, 'r')
    coast_dict = cPickle.load(f)
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
    
    fig = matplotlib.pyplot.figure()
        
    for airport in Airport:
        
        matplotlib.pyplot.plot(airport.x, airport.y, 'ro')
        matplotlib.pyplot.annotate(airport.name, ([airport.x, airport.y]))
    
    for border in border_dict:
        matplotlib.pyplot.plot(border_dict[border][0], border_dict[border][1],\
            color='b', linestyle='-')
    
    matplotlib.pyplot.plot(mexico_dict[0], mexico_dict[1], color='g',\
        linestyle='-')
        
    matplotlib.pyplot.plot(canada_dict[0], canada_dict[1], color='g',\
        linestyle='-')
        
    matplotlib.pyplot.title('AIRPORTS IN DATASET: ' + str(year) + 'Q' +\
        str(quarter))
    matplotlib.pyplot.xlabel('LONGITUDE')
    matplotlib.pyplot.ylabel('LATITUDE')
    matplotlib.pyplot.xlim((-130, -65))
    matplotlib.pyplot.ylim((22.5, 52.5))
    matplotlib.pyplot.grid(True)
    
    for coast in coast_dict:
            matplotlib.pyplot.plot(coast_dict[coast][0], coast_dict[coast][1],\
                color='b', linestyle='-')    
    
    matplotlib.pyplot.show()
    
#    f = open('..\\temp\\test.bin', 'w')
#    cPickle.dump(fig, f)
#    f.close()
    
#    f = open('..\\temp\\test.bin', 'r')
#    ffig = cPickle.load(f)
#    f.close()
    
    return None
