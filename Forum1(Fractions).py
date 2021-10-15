# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:26:57 2021

@author: WINDOWS10
"""

print("Please input a positive numerator and denominator!!")
n=int(input("Numerator:"))
while n<0:
    n=int(input("Please enter a positive number:"))
    if n<0:
        continue
    if n>0:
        break    
d=int(input("Denominator:"))
while d<0:
    d=int(input("Please enter a positive number:"))
    if d<0:
        continue
    if d>0:
        break
import math
from fractions import Fraction
x=math.gcd(n,d)
if n<d:
    print("")
    print(f"{n}/{d}","is a proper fraction")
    if x>=1:
        print("")
        print("This fraction can be simplified into",Fraction(n,d))
elif n>d:
    print("")
    print(f"{n}/{d}","is an improper fraction")
    if x>1:
        print("")
        print("This fraction can be simplified into",Fraction(n,d))
    else:
        print("")
        print("This fraction cannot be further simplified")
    if n%d==0:
        print("")
        print("The whole number is",n//d)
    if n%d !=0:
        print("")
        print("The mixed number is",n//d,"and",Fraction((n%d),d))
        
    


    