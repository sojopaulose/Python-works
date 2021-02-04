# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:53:00 2021

@author: Sojo
"""
def zero_exception():
   try:
      a=5
      b=0
      print(a/b)
   except(ZeroDivisionError,ValueError)as e:
       print('dividing by zero')
   finally:
       print('executed')
zero_exception()
      
