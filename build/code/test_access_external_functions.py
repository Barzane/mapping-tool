# -*- coding: utf-8 -*-

import os, sys, inspect, re

def set_path():

    print 'setting access to external functions'

    #http://stackoverflow.com/questions/2817264/how-to-get-the-parent-dir-location
    #it would be cleaner to code the relative imports by using packages --- not to be implemented
    
    #give access to functions in network-data
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
    externaldir = uppath(currentdir, 3) + '\\network_data\\build\\code'
    
    def check_duplicate_names():

        def searcher(all_files):
            
            python_files = list()
            
            for file in all_files:
            
            #    https://developers.google.com/edu/python/regular-expressions#basic-examples
                
                lookup_py = re.search(r'.py', file)
                lookup_pyc = re.search(r'.pyc', file)
                
            #    http://stackoverflow.com/questions/23086383/how-to-test-nonetype-in-python
                
                if (lookup_py is not None and lookup_pyc is None):
                    
                    python_files.append(file)        
            
            return python_files
        
        list_current_files = os.listdir(currentdir)        
        list_current_python_files = searcher(list_current_files)
        
        list_external_files = os.listdir(externaldir)
        list_external_python_files = searcher(list_external_files)
        
        for file in list_current_python_files:
            
            if file in list_external_python_files:
                
                if file != 'rundirectory.py':
                    
                    return True
                    
        return False
    
    if check_duplicate_names():
        
        raise Exception('repeated module name in:', currentdir, externaldir)
    
    else:
    
        sys.path.insert(0, externaldir)
        
        print '\nexternaldir', externaldir
        
        #remove duplicates from sys.path --- be careful when changing sys.path
        
        sys.path = list(set(sys.path))

    return None
