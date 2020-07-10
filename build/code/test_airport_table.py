# -*- coding: utf-8 -*-

import cPickle

year = 2013
quarter = 4

src = '..\\temp\\map_airports_2013_4.bin'

f = open(src, 'r')
data = cPickle.load(f)
f.close()

airports = data.keys()
airports.sort()

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
        
caption = 'Title. List of airports by IATA code in ' + str(year) + 'Q' + str(quarter) + ', all carriers. \
            Also longitude (x) and latitude (y). The identify of the airport corresponding to each \
            IATA code can be found at \url{http://www.iata.org/en/publications/directories/code-search/}. \
            Discussion.' 
                        
output += '\\end{tabular}'
output += '\n\\caption{' + caption + '}'
    
output += '\n\\label{tab:XXX}'
output += '\n\\end{center}'
output += '\n\\end{table}'

dst = '..\\output\\'
output_filename = 'list_of_airports_' + str(year) + 'Q' + str(quarter) + '.tex'

f = open(dst + output_filename, 'w')    
f.write(output)
f.close()

print output
print

print '\\input{' + output_filename + '}\n'
    