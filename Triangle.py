# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:02:15 2021

@author: WINDOWS10
"""

Totalrows=eval(input("How many rows: "))
for Rows in range(Totalrows):        
    for Spaces in range ((Totalrows-Rows)+1):
        print(" ",end=" ")    
    for Stars in range(Rows+1):
        print("*",end=" ")            
    print("")

    



            
    
            

   