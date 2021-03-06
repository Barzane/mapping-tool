# -*- coding: utf-8 -*-

import matplotlib, matplotlib.pyplot

from airport_classes import Airport

def example_nodes(carrier, fig):
    
    ax = fig.gca()

    def plot_circle(airport_list):
        
        for airport in Airport:
            
            if airport.name in airport_list:
                
                circle = matplotlib.pyplot.Circle((airport.x, airport.y), 2, color='b', fill=False, linewidth=3)
                ax.add_artist(circle)
        
        return None

    carrier_airport_list = dict()
    carrier_airport_list['AA'] = ['DFW', 'ORD', 'OKC', 'AUS']
    carrier_airport_list['AS'] = ['SEA', 'PDX', 'GEG']
    carrier_airport_list['B6'] = ['JFK', 'BOS', 'FLL', 'IAD']
    carrier_airport_list['DL'] = ['ATL', 'MSP', 'DTW', 'BNA', 'CLT']
    carrier_airport_list['F9'] = ['DEN', 'ABQ', 'SLC', 'OMA']
    carrier_airport_list['WN'] = ['MDW', 'LAS', 'BWI', 'PHX', 'STL', 'DEN', 'HOU']
    
#    highlight nodes on blank map with airports (no routes)
    
#    carrier_airport_list[''] = ['ATL', 'DFW', 'SEA', 'JFK', 'DEN', 'MSP',\
#                                'ORD', 'PHX', 'CLT', 'SFO', 'LAX', 'MDW', 'STL']
                                
    carrier_airport_list[''] = ['ATL', 'DFW', 'SEA', 'JFK', 'DEN', 'MSP',\
                                'ORD', 'PHX', 'SFO', 'MDW']
    
    if carrier in carrier_airport_list:
        
        plot_circle(carrier_airport_list[carrier])
        
    else:
        
        pass
        
    return None
