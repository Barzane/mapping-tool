# -*- coding: utf-8 -*-

import cPickle, matplotlib, glob, numpy

from airport_classes import *

matplotlib.pyplot.ioff()

def radian(degree):
    return (numpy.pi / 180.0) * degree
    
def degree(radian):
    return (180.0 / numpy.pi) * radian
        
def add_routes(year, quarter, route_list, line_type):
    
    src = '..\\temp\\map_' + str(year) + '_' + str(quarter) + '.bin'
    
    dst_png = '..\\output\\map_with_routes_' + str(year) + '_' + str(quarter) + '.png'
    
    f = open(src, 'r')
    fig = cPickle.load(f)
    f.close()
    
    folder_contents = glob.glob('..\\temp\\airport*.bin')

    for filepath in folder_contents:
        
        f = open(filepath, 'r')
        airport = cPickle.load(f)
        f.close()
    
    def add_route_to_plot(routes, col='k', lwd=3.0):
            
        for route in routes:
            
            x = []
            y = []
            
            for airport in Airport:
                
                for node in route:
                    
                    if airport.name == node:
                        x.append(airport.x)
                        y.append(airport.y)
                        
            if len(x) != 2:
                raise Exception('missing node')
                
            matplotlib.pyplot.plot(x, y, color=col, linestyle='-', linewidth=lwd)
        
        return None
    
    def add_geodesic_to_plot(routes, col='k', lwd=3.0):
            
        for route in routes:
            
            end1 = route[0]
            end2 = route[1]
            
#            for UA 2013Q4 geodesic, not needed in general (error in list construction)
            end1 = end1.strip()
            end2 = end2.strip() 
            
            for airport in Airport:
                
                if airport.name == end1:
                    l1 = radian(airport.x)
                    p1 = radian(airport.y)
            
                if airport.name == end2:
                    l2 = radian(airport.x)
                    p2 = radian(airport.y)
                    
#            need error trap if endpoints not found
        
            if l1 > l2:
                l1, l2 = l2, l1
                p1, p2 = p2, p1
            
            l12 = l2 - l1
            
            a1 = numpy.arctan2(numpy.sin(l12), (numpy.cos(p1) * numpy.tan(p2) - numpy.sin(p1) * numpy.cos(l12)))
            a0 = numpy.arcsin(numpy.sin(a1) * numpy.cos(p1))    
            
            if p1 == 0 and a1 == numpy.pi / 2:
                s01 = 0
            else:
                s01 = numpy.arctan2(numpy.tan(p1), numpy.cos(a1))
            
            l01 = numpy.arctan2(numpy.sin(a0) * numpy.sin(s01), numpy.cos(s01))    
            l0 = l1 - l01    
            
            lX = numpy.linspace(l1, l2, num=10)
            
            pY = numpy.arctan2(numpy.sin(lX - l0), numpy.tan(a0))
            
            lX = degree(lX)
            pY = degree(pY)
            
            matplotlib.pyplot.plot(lX, pY, color=col, linestyle='-', linewidth=lwd)
        
        return None    
    
    if line_type == 'linear':
        add_route_to_plot(route_list)
    elif line_type == 'geodesic':
        add_geodesic_to_plot(route_list)
    else:
        raise NotImplementedError('line type must be linear or geodesic')
    
    matplotlib.pyplot.savefig(dst_png, bbox_inches='tight')
        
    return None