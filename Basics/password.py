# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:20:26 2021

@author: Sojo
"""

class checkEX:pass
try:
    a=input('enter a username:')
    b=input('enter a password:')
    x='hijk11'
    y='12345'
    if a==x and b==y:
       print('valid login')
    else:
       raise checkEX('invalid login')
except checkEX as e:
   print(e)    
    