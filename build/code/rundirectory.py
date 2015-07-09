# -*- coding: utf-8 -*-

import os, glob, shutil

import state_state_border_dictionary
import mexico_us_canada_us_border_dictionary
import coast_border_dictionary
import plot_map_with_airports

print

print 'clear contents of \output and \\temp and \input'

for folder in ['..\\output\\*', '..\\temp\\*', '..\\input\\*']:

    folder_contents = glob.glob(folder)

    for filename in folder_contents:
        os.remove(filename)

print 'build state-state border dictionary, save to \\input'

state_state_border_dictionary.build_dict()

print 'build US-Mexico and US-Canada border dictionary, save to \\input'

mexico_us_canada_us_border_dictionary.build_dict()

print 'US coast border dictionary, save to \\input'

coast_border_dictionary.build_dict()

year = 2013
quarter = 4
  
print 'copy data_year_quarter.bin datafile from ..\data to \input'

src = '..\\..\\data\\data_' + str(year) + '_' + str(quarter) + '.bin'
dst = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'

shutil.copyfile(src, dst)

print 'plot map with airports for ' + dst

plot_map_with_airports.plot(dst, year, quarter)
  
print 'move pyc files (byte code) from \code to \\temp'

src = '.\\'
dst = '..\\temp\\'

for folder in [src + '*.pyc']:
    
    folder_contents = glob.glob(folder)
    
    for filename in folder_contents:
        
        filename_split = filename.split('\\')[-1]
        shutil.move(filename, dst + filename_split)
           
#    
#    print 'move bin from \\temp to \output'
#    
#    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    dst = '..\\output\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    
#    shutil.move(src, dst)
