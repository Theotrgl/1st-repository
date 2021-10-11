# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:57:53 2021

@author: WINDOWS10
"""
#%%
#Number 1
print("Please Enter Coordinates")
x1=eval(input("X-Axis:"))
if x1==int or float:
    y1=eval(input("Y-Axis:"))
    if y1==int or float:
        print ("(",x1,",",y1,")")
        print("")
        print("Enter Second Coordinates")
x2=eval(input("X-Axis:"))
if x2==int or float:
    y2=eval(input("Y-Axis:"))
    if y2==int or float:
        print ("(",x2,",",y2,")")
        print("")
Semifinal=eval("(y2-y1)/(x2-x1)")
final=round(Semifinal,5)
print(f"The slope for the line that connects two points ({x1} , {y1} ) and ( {x2} , {y2} ) is:",final)
#%%

#Number 2

v=eval(input("Please enter velocity (m/s):"))
a=eval(input("Next, please enter the acceleration (m/s\u00b2):"))
R=eval("(v*v)/(2*a)")
RL=round(R,4)
if R >= 0:
    print("")
    print("The minimum runway length needed is:",RL,"meters")       
else:
    print("")
    print("Please Enter a positive number!!")
#%%

#Number 3

s=float(input("Enter Subtotal:$"))
tp=eval(input("Enter tip ammount in %:"))
print("")
s2=format(s, '.2f')
print("Subtotal:""$",s2)
t=eval("(tp/100)*s")
t2=format(t,".2f")
print("")
print("Tip:""$",t2)
Tot=eval("s-t")
Total=format(Tot,".2f")
print("")
print("Total:""$",Total)
#%%

#Number 4

l=eval(input("Enter the length of the sides of the hexagon:"))

if l>=0:
    l2=eval("((3**(1/3))/2)*(l*l)")
    l3=round(l2,3)
    print("")
    print("The Area of Your Hexagon is:", l3)















    
    
    







# %%
