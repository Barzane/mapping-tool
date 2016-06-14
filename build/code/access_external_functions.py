# -*- coding: utf-8 -*-

import os, sys, inspect

def set_path():

    print 'setting access to external functions'

    #http://stackoverflow.com/questions/2817264/how-to-get-the-parent-dir-location
    #it would be cleaner to code the relative imports by using packages --- not to be implemented
    
    #give access to functions in network-data
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
    externaldir = uppath(currentdir, 3) + '\\network-data\\build\\code'
    sys.path.insert(0, externaldir)
    
    print '\nexternaldir', externaldir
    
    #remove duplicates from sys.path --- be careful when changing sys.path
    
    sys.path = list(set(sys.path))

    return None
