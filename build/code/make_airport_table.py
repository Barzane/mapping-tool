# -*- coding: utf-8 -*-

import cPickle

def build(year, quarter, path = ''):

    src = path + '..\\temp\\map_airports_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'r')
    data = cPickle.load(f)
    f.close()
    
    airports = data.keys()
    airports.sort()
    
    output_filename = 'list_of_airports_' + str(year) + '_' + str(quarter)
    
    output = '\\begin{table}'
    output += '\n\\scriptsize'
    output += '\n\\begin{center}'
    
    col_names = ['code', 'x', 'y', ''] * 3
    
    output += '\n\\begin{tabular}{' + 'lrrc' * 3 + '}\n'
        
    for name in col_names:
            
        output += name + ' & '
            
    output += '\\\ \\hline'
    output += '\n ' + '& ' * 12 + '\\\ \n'    
    
    tick = 0
        
    for airport in airports:
            
        output += airport + ' & ' + '%.2f'%(data[airport][0]) + ' & ' + '%.2f'%(data[airport][1]) + ' & ' 
    
        tick += 1
        
        if tick % 3 == 0:
            
            output += '\\\ \n'
            
        else:
            
            output += ' & '
            
    caption = 'List of airports by IATA code in ' + str(year) + 'Q' + str(quarter) + ', all carriers, \
                with their longitude (x) and latitude (y). The identity of the airport corresponding to each \
                IATA code can be found at \\url{http:' + '/' + '/' + 'www.iata.org/en/publications/directories/code-search/}.' 
                            
    output += '\\end{tabular}'
    output += '\n\\caption{' + caption + '}'
        
    output += '\n\\label{tab:' + output_filename + '}'
    output += '\n\\end{center}'
    output += '\n\\end{table}'
    
    dst = '..\\output\\'
        
    f = open(dst + output_filename + '.tex', 'w')    
    f.write(output)
    f.close()
    
    print output
    print
    
    print '\\input{' + output_filename + '.tex}\n'
    
    return None
