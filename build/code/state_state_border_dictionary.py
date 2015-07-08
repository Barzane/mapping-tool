# -*- coding: utf-8 -*-

import cPickle

def build_dict():
    
    src = '..\\..\\data\\borders\\bordpnts.asc'
    dst = '..\\input\\border_dict.bin'    
    
    border_dict = {}

    f = open(src, 'r')

    for header in f:
        break
    
    for line in f:
        
        line_v = line.split(',')
        border_num = int(line_v[0])
        
        if border_num not in border_dict:
            
            border_dict[border_num] = [[-float(line_v[4])], [float(line_v[3])]]
        
        else:
        
            border_dict[border_num][0].append(-float(line_v[4]))
            border_dict[border_num][1].append(float(line_v[3]))
    
    f.close()
    
    f = open(dst, 'wb')
    cPickle.dump(border_dict, f)
    f.close()
    
    return None