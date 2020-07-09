# -*- coding: utf-8 -*-

import cPickle, glob, matplotlib, matplotlib.pyplot, numpy

from airport_classes import Airport

import nodes_for_illustrations

matplotlib.pyplot.ioff()

def radian(degree):
    
    return (numpy.pi / 180.0) * degree
    
def degree(radian):
    
    return (180.0 / numpy.pi) * radian
        
def add_routes(carrier, year, quarter, route_list, erdos_renyi, line_type, highlight_nodes, call_num=None):
    
    src = '..\\temp\\map_' + str(year) + '_' + str(quarter) + '.bin'

    if not erdos_renyi:
        
        if highlight_nodes:

            dst_png = '..\\output\\map_with_routes_' + carrier + '_' + str(year) + '_' + str(quarter) + '_circle_nodes.png'
            
        else:
            
            dst_png = '..\\output\\map_with_routes_' + carrier + '_' + str(year) + '_' + str(quarter) + '.png'
        
    else:
        
        dst_png = '..\\output\\map_with_routes_' + carrier + '(ErdosRenyi)_' + str(year) + '_' + str(quarter) + '.png'
       
    f = open(src, 'r')
    fig = cPickle.load(f)
    f.close()
    
    folder_contents = glob.glob('..\\temp\\airport*.bin')

    for filepath in folder_contents:
        
        f = open(filepath, 'r')
        airport = cPickle.load(f)
        f.close()
    
    def add_route_to_plot(routes, col='k', lwd=5.0):
            
        for route in routes:
            
            x = []
            y = []
            
            for airport in Airport:
                
                for node in route[0]:
                    
                    if airport.name == node:
                        x.append(airport.x)
                        y.append(airport.y)
                        
            if len(x) != 2:
                
                raise Exception('missing node')
                
            matplotlib.pyplot.plot(x, y, color=col, linestyle='-', linewidth=route[1]*lwd)
        
        return None
    
    def add_geodesic_to_plot(routes, col='k', lwd=5.0):
            
        for route in routes:
            
            end1 = route[0][0]
            end2 = route[0][1]
            
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
            
            matplotlib.pyplot.plot(lX, pY, color=col, linestyle='-', linewidth=route[1]*lwd)
        
        return None    
    
    if line_type == 'linear':
        
        add_route_to_plot(route_list)
        
    elif line_type == 'geodesic':
        
        add_geodesic_to_plot(route_list)
        
    else:
        
        raise NotImplementedError('line type must be linear or geodesic')
    
    if highlight_nodes and year == 2013 and quarter == 4:
        
        nodes_for_illustrations.example_nodes(carrier, fig)
    
    matplotlib.pyplot.savefig(dst_png, bbox_inches='tight')
    matplotlib.pyplot.close(fig)
    
    return None
