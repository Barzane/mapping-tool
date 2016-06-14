# -*- coding: utf-8 -*-

import cPickle

def build_dict():
    
    src_mexico_us = '..\\..\\data\\borders\\mexicoUSBorder.txt'
    src_canada_us = '..\\..\\data\\borders\\canadaUSBorder.txt'

    dst = '..\\input\\mexico_us_canada_us_border_dict.bin'    
    
    border_dict = {}

    for src in [src_mexico_us, src_canada_us]:

        border = []
    
        f = open(src, 'r')
        
        for line in f:
            
            line_v = line.split()
            
            if border == []:
                
                border = [[float(line_v[1])], [float(line_v[0])]]
            else:
                
                border[0].append(float(line_v[1]))
                border[1].append(float(line_v[0]))
        
        f.close()
        
        border_key = src.split('\\')[-1].split('.')[0]     
        
        border_dict[border_key] = border
    
    f = open(dst, 'wb')
    cPickle.dump(border_dict, f)
    f.close()
    
    return None