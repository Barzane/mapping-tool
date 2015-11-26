# -*- coding: utf-8 -*-

import cPickle

def route(year, quarter, carrier, test, constant_weight):
    
    if test:
        
        route_list = [(['BHM','ATL'], 1.0),\
                    (['BHM','BNA'], 1.0),\
                    (['BHM','LIT'], 1.0),\
                    (['BHM','AUS'], 1.0),\
                    (['BHM','ECP'], 1.0),\
                    (['BHM','MCO'], 1.0),\
                    (['BHM','STL'], 1.0),\
                    (['BHM','GSP'], 1.0),\
                    (['BHM','BLI'], 1.0)]    
    
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
                
                route_list.append((origin_dest_list[element_number], pax_list[element_number] / max_pax))

    return route_list