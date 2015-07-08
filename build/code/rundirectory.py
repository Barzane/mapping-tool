# -*- coding: utf-8 -*-

import os, glob, shutil

import state_state_border_dictionary

print

print 'clear contents of \output and \\temp and \input'

for folder in ['..\\output\\*', '..\\temp\\*', '..\\input\\*']:

    folder_contents = glob.glob(folder)

    for filename in folder_contents:
        os.remove(filename)

print 'build state-state border dictionary, save to \\input'

state_state_border_dictionary.build_dict()

#    
#    print 'copy data_year_quarter.bin datafile from ..\data to \input'
#    
#    src = '..\\..\\data\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    dst = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    
#    shutil.copyfile(src, dst)
#  
  
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
