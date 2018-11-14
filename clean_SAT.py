#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:22:03 2018

@author: josiewilliams
"""

def clean_SAT():
    file = '2012_SAT_Results.csv'
    try:
        source = open(file,'r')
    except Exception as e:
        print('Error: file cannot be opened')
        print(e)
    else:
        output_name = file[0:4] + '_out.csv'
        text_file = open(output_name, 'w')
    
    line_counter = 0;
    
    for line in source:
        line_counter += 1
        if (line_counter == 1):
            continue
        new_line=''  
        values = line.split(',')
        
        for i in range (len(values)):
            if (i != 0 and i != 2):
                if (i == 1):
                    s = values[1].replace('"','')
                    values[1] = s
                
                new_line += values[i] + '\t'
                    
            
        if (len(new_line)) > 0:
            text_file.write(new_line + '\n')


clean_SAT()
