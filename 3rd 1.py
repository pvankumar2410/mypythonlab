# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:32:55 2021

@author: Alien10
"""

def alphabet_wars(war):
    count=0
    left={'w' : 4,'p' : 3,'b' : 2,'s' : 1}
    right={'m' : 4,'q' : 3,'d' : 2,'z' : 1}
    
    for i in war:
        if i in left:
            count = left[i] + count 
            
        elif i in right:
            count = right[i] - count
            
            
    if count < 0:
         return "Right side wins"
        
    if count > 0:
         return "left side wins"
        
    if count == 0:
        return "Lets fight again"
        
   
        
print (alphabet_wars("z"))


    

