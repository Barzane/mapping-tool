# -*- coding: utf-8 -*-

import cPickle

def route(year, quarter, carrier, test, constant_weight, erdos_renyi, all_airports, Nbar, highlight_nodes, g=None):
    
    carrier_airports = Nbar.keys()
    carrier_airports.sort()    
    
    if test:
        
#        node_list = ['DAY', 'DEN', 'MCO']
#        node_list = ['ABQ', 'DAL', 'HOU', 'MCI']
        node_list = ['BNA', 'BWI', 'DEN', 'HOU', 'LAS', 'MCI',\
                    'MDW', 'MSY', 'PHX', 'STL', 'TPA']
        
        route_list = []
        
        for i in range(len(node_list)-1):
            
            for j in range(i+1, len(node_list)):
                
                route_list.append(([node_list[i], node_list[j]], 1))
        
#        route_list = [(['DAY','DEN'], 1),\
#                    (['DEN','MCO'], 1),\
#                    (['MCO','DAY'], 1)]

#        route_list = [(['ABQ','DAL'], 1),\
#                    (['DAL','HOU'], 1),\
#                    (['HOU','MCI'], 1),\
#                    (['MCI','ABQ'], 1),\
#                    (['ABQ','HOU'], 1),\
#                    (['DAL','MCI'], 1)]
                    
#        route_list = [(['JFK','SFO'], 1),\
#                    (['JFK','ORD'], 1),\
#                    (['ORD','SFO'], 1)]    
    
#        route_list = [(['LGA','DFW'], 0.5),\
#                    (['DFW','MSP'], 0.5),\
#                    (['LGA','MIA'], 0.5),\
#                    (['MIA','MSP'], 0.5),\
#                    (['LGA','ORD'], 0.5),\
#                    (['ORD','MSP'], 0.5)] 

#        route_list = [(['LGA','DFW'], 1),\
#                    (['DFW','MSP'], 1)]

#        route_list = [(['LGA','MIA'], 1),\
#                    (['MIA','MSP'], 1)]

#        route_list = [(['LGA','ORD'], 1),\
#                    (['ORD','MSP'], 1)] 
   
        src = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'    
        
        f = open(src, 'r')
        data = cPickle.load(f)
        f.close()
        
        origin_dest_list = []
        pax_list = []
        
        for key in data:
            
            key_v = key.split('_')
            car = key_v[2]
            
            if car == carrier:
                
                origin = key_v[0]
                dest = key_v[1]
                
                origin_dest_list.append([origin, dest])
                
                pax = float(data[key]['pax'])
                pax_list.append(pax)
                
            else:
                
                pass
        
        if pax_list == []:
            
            raise IndexError('no carrier ' + carrier + ' in data')
        
        max_pax = max(pax_list)
        
#        route_list = []
        
        for element_number in range(len(origin_dest_list)):
                
            route_list.append((origin_dest_list[element_number], 0.05))
   
    elif erdos_renyi:
        
        route_list = []

        for i in range(len(g)):
            
            for j in range(i, len(g)):
                
                if g[i][j] == 1:
                    
                    origin = carrier_airports[i]
                    dest = carrier_airports[j]
                    
                    route_list.append(([origin, dest], 0.1)) #constant line-width
    
    else:
        
        src = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'    
        
        f = open(src, 'r')
        data = cPickle.load(f)
        f.close()
        
        origin_dest_list = []
        pax_list = []
        
        for key in data:
            
            key_v = key.split('_')
            car = key_v[2]
            
            if car == carrier:
                
                origin = key_v[0]
                dest = key_v[1]
                
                origin_dest_list.append([origin, dest])
                
                pax = float(data[key]['pax'])
                pax_list.append(pax)
                
            else:
                
                pass
        
        if pax_list == []:
            
            raise IndexError('no carrier ' + carrier + ' in data')
        
        max_pax = max(pax_list)
        
        route_list = []
        
        for element_number in range(len(origin_dest_list)):
            
            if constant_weight:
                
                route_list.append((origin_dest_list[element_number], 1.0))
                
            else:
                
                if highlight_nodes:
                
                    route_list.append((origin_dest_list[element_number], 0.1))
                    
                else:
                    
                    route_list.append((origin_dest_list[element_number], pax_list[element_number] / max_pax))

    return route_list