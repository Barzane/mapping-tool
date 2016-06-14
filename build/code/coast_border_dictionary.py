# -*- coding: utf-8 -*-

import cPickle

def build_dict():
    
    src = '..\\..\\data\\borders\\coastl_usa.json'
    dst = '..\\input\\coast_border_dict.bin'    
    
    border_dict = {}

    f = open(src, 'r')

    count = 0
        
    for line in f:
        
        try:
            
            a = eval(line.split('coordinates":')[1].strip().split('}')[0].strip())
            
            xx = []
            yy = []
            
            for item in a:
                
                xx.append(item[0])
                yy.append(item[1])
                
            count += 1
            border_dict[count]=[xx, yy]
            
        except IndexError:
            
            pass
    
    f.close()
    
    f = open(dst, 'wb')
    cPickle.dump(border_dict, f)
    f.close()
    
    return None