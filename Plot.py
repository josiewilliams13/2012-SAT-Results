#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:21:40 2018

@author: josiewilliams
"""

import pylab #matplotlib

def data_prep():
    source = open('2012_out.csv')
    
    x_temp =[]
    y_temp =[]
    z_temp =[]  
    for line in source:        
        
        values = line.split('\t')
        line_counter = 0
        
        #if(line_counter == 5):
         #   break
            
        line_counter+=1
                      
        if (len(line) != 2): 
            x_temp.append(values[1])
            y_temp.append(values[2])
            z_temp.append(values[3])      
       
    x=[]
    y=[]
    z=[]
    
    for i in range(3):
       x.append(x_temp[i])
       y.append(y_temp[i])
       z.append(z_temp[i])
    
    return x,y,z
        

def graph():
    
    x=[]
    y=[]
    z=[]
    
    x,y,z = data_prep()
    
    pylab.bar(1 - 0.2, x[0],width=0.15,color='b',align='center',
              label='HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES')
    pylab.bar(2 - 0.2, y[0],width=0.15,color='b',align='center')
    pylab.bar(3 - 0.2, z[0],width=0.15,color='b',align='center')
    
    
    pylab.bar(1, x[1],width=0.15,color='r',align='center')
    pylab.bar(2, y[1],width=0.15,color='r',align='center',
              label='UNIVERSITY NEIGHBORHOOD HIGH SCHOOL')
    pylab.bar(3, z[1],width=0.15,color='r',align='center')
    
    
    pylab.bar(1 + 0.2, x[2],width=0.15,color='g',align='center')
    pylab.bar(2 + 0.2, y[2],width=0.15,color='g',align='center')
    pylab.bar(3 + 0.2, z[2],width=0.15,color='g',align='center',
              label='EAST SIDE COMMUNITY SCHOOL')    

    pylab.ylim(0,700)
    pylab.axis([0, 3.5, 0, 800])
    
    
    s = list(range(1,5)) #turn data into list, which converts them into integers.
    SAT_sections = 'Critical Reading,Math,Writing'
    m = SAT_sections.split(',')
    pylab.xticks(s,m) #will produce the sections at the bottom.
        
    pylab.xlabel('SAT Sections')
    pylab.ylabel('Scores')
    pylab.title('2012 SAT Result')
    
    pylab.legend(loc= "upper left") #creates a legend in the upper left corner
    pylab.show
    

graph()

def graph2():
    line = [29,91,70]
    
    pylab.plot(1- 0.2,line[0],'bo') #Henry St school
    pylab.plot(2- 0.2,line[1],'ro') #University neighborhood
    pylab.plot(3- 0.2,line[2],'go') #East side community
  
    pylab.show    


graph2()
