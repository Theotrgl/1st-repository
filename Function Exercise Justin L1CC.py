# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:12:36 2021

@author: WINDOWS10
"""
#Number 1

def get_days(h,m,s):
    return h/24+m/(60*24)+s/(24*3600)
 
def convert_to_days():
    h=eval(input("Please enter number of hours:"))
    m=eval(input("Please enter number of minutes:"))
    s=eval(input("Please enter number of seconds:"))
    c=format(get_days(h,m,s),".4f")
    print(c)

#%%

#Number 2

def calc_weight_on_planet(w,g=23.1):
    x=w/9.8*g
    print(x)



   
#%%  

#Number 3

def num_atoms(g,Ar= 196.97):
    A=g/Ar*6.022*(10**(23))
    print(A)
    
#%%

#Number 4

def calc_new_height():
    from fractions import Fraction
    w=eval(input("Enter current width:"))
    h=eval(input("Enter current height:"))
    w2=eval(input("Enter desired width:"))
    r1=Fraction(w,h)
    h2=w2/r1
    print("Your new height is:",h2)

#%%

#Number 5

def convert_celcius(F):
    return 5/9*(F-32)


def convert_kelvin(C):
    return C+273.15


def convert_temp():
    F=eval(input("Enter a temperature in Farenheit:"))
    C=convert_celcius(F)
    K=convert_kelvin(C)
    print("The temperature in Farenheit is:",F)
    print("The temperature in Celcius is:",C)
    print("The temperature in Kelvin is:",K)


    

    

    
    

        
# %%
