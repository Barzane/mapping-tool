# -*- coding: utf-8 -*-

import matplotlib

from airport_classes import Airport

def example_nodes(carrier, fig):
    
    ax = fig.gca()

    if carrier == 'AA':
        
        for airport in Airport:
        
            if airport.name in ['DFW', 'ORD', 'OKC', 'AUS']:
                    
                circle = matplotlib.pyplot.Circle((airport.x, airport.y), 2, color='b', fill=False, linewidth=3)
                ax.add_artist(circle)
                
    elif carrier == 'AS':
    
        for airport in Airport:
            
            if airport.name in ['SEA', 'PDX', 'GEG']:
                
                circle = matplotlib.pyplot.Circle((airport.x, airport.y), 2, color='b', fill=False, linewidth=3)
                ax.add_artist(circle)
                
    elif carrier == 'B6':
    
        for airport in Airport:
            
            if airport.name in ['JFK', 'BOS', 'FLL', 'IAD']:
                
                circle = matplotlib.pyplot.Circle((airport.x, airport.y), 2, color='b', fill=False, linewidth=3)
                ax.add_artist(circle)
                
    elif carrier == 'DL':
    
        for airport in Airport:
            
            if airport.name in ['ATL', 'MSP', 'DTW', 'BNA', 'CLT']:
                
                circle = matplotlib.pyplot.Circle((airport.x, airport.y), 2, color='b', fill=False, linewidth=3)
                ax.add_artist(circle)
                
    elif carrier == 'F9':
    
        for airport in Airport:
            
            if airport.name in ['DEN', 'ABQ', 'SLC', 'OMA']:
                
                circle = matplotlib.pyplot.Circle((airport.x, airport.y), 2, color='b', fill=False, linewidth=3)
                ax.add_artist(circle)
    
    else:

        pass
        
    return None
