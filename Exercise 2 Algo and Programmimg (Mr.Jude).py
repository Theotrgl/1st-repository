# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:51:42 2021

@author: WINDOWS10
"""
#Number 1

m=eval(input("Enter mass of Block (in Kg):"))
if int or float:
    print("")
    f=eval(input("Next, please enter the force (in N):"))
else:
    print("Please input a number!")
    if int or float:
        import math
        a=math.degrees(eval("math.asin(f/(m*9.8))"))
        a2=round(a,1)
        print("")
        print("")
        print("The angle of the ramp is",a2)
    else:
        print("Please input a number!")

#%%

#Number 2

T1 = eval( input("Enter lenght of T1:"))
T2 = eval( input("Enter lenght of T2:"))
T3 = eval( input("Enter lenght of T3:"))

if T1+T2>T3 and T2+T3>T1 and T3+T1>T2:
    print("The Perimeter is", round(T1+T2+T3,1))

else:
    print("perimeter is Invalid, please try another combination!")

#%%

#Number 3

x=eval(input("Please enter temperature in Farenheit:"))

while x<-58 or x>41:
    x=eval(input("Number must be between -58 and 41, please re-enter:"))
    if x<-58 or x>41:
        continue
    if x>=-58 and x<=41:        
        break
y=eval(input("Enter wind speed:"))
while y < 2:
    y=eval(input("Number must be greater than or equal to 2, please re-enter:"))
    if y < 2:
        continue
    if y>=2 :
        break        
z=eval("35.74+0.6215*x-35.75*(y**(0.16))+0.4275*x*(y**(0.16))")
z2=format(z,".3f")
print("")
print("The wind-chill speed is",z2)

#%%

#Number 4

a=int(input("How many packages are you going to buy?:"))


if a>=10 and a<=19:
    l=10
    b=(10/100)*99
    b2=format((b),".2f")
    print("")
    print(f"Discount at {l}%:$",b2)
    b3=format((99*a-b),".2f")
    print("")
    print("Total amount:$",b3)
   
elif a>=20 and a<=49:
    l=20
    c=(20/100)*99
    c2=format((c),".2f")
    print("")
    print(f"Discount at {l}%:$",c2)
    c3=format((99*a-c),".2f")
    print("")
    print("Total amount:$",c3)
elif a>=50 and a<=99:
    l=30
    d=(30/100)*99
    d2=format((d),".2f")
    print("")
    print(f"Discount at {l}%:$",d2)
    d3=format((99*a-d),".2f")
    print("")
    print("Total amount:$",d3)
elif a>100:
    l=40
    e=(40/100)*99
    e2=format((e),".2f")
    print("")
    print(f"Discount at {l}%:$",e2)
    e3=format((99*a-e),".2f")
    print("")
    print("Total amount:$",e3)
else:
    l=0
    f=(0)*99
    f2=format((f),".2f")
    print("")
    print(f"Discount at {l}%:$",f2)
    f3=format((99*a-f),".2f")
    print("")
    print("Total amount:$",f3)
    
#%%
        
               

               
               
               
    

    
    
        
      
    
    
    
