# -*- coding: utf-8 -*-

import cPickle, matplotlib, matplotlib.pyplot

matplotlib.pyplot.ioff()
        
def plot():
    
    src_coast = '..\\input\\coast_border_dict.bin'
    src_mexico_canada = '..\\input\\mexico_us_canada_us_border_dict.bin'
    src_state_state = '..\\input\\state_state_border_dict.bin'
    
    dst = '..\\..\\data\\borders\\blank_map.bin'
    
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
    
    fig = matplotlib.pyplot.figure()
    
    for border in border_dict:
        
        matplotlib.pyplot.plot(border_dict[border][0], border_dict[border][1],\
            color='b', linestyle='-')
    
    matplotlib.pyplot.plot(mexico_dict[0], mexico_dict[1], color='g',\
        linestyle='-')
        
    matplotlib.pyplot.plot(canada_dict[0], canada_dict[1], color='g',\
        linestyle='-')

    matplotlib.pyplot.xlabel('LONGITUDE')
    matplotlib.pyplot.ylabel('LATITUDE')
    matplotlib.pyplot.xlim((-130, -65))
    matplotlib.pyplot.ylim((22.5, 52.5))
    matplotlib.pyplot.grid(True)
    
    for coast in coast_dict:
        
            matplotlib.pyplot.plot(coast_dict[coast][0], coast_dict[coast][1],\
                color='b', linestyle='-')    
    
#    http://stackoverflow.com/questions/7290370/store-and-reload-matplotlib-pyplot-object
    
    fig.set_size_inches(8, 6, forward=True)
    fig.tight_layout()
        
    f = open(dst, 'wb')
    cPickle.dump(fig, f)
    f.close()
    
    print 'test load'
    
    f = open(dst, 'rb')
    test = cPickle.load(f)
    f.close()
    
    sss
    
    return None
