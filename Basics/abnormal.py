# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:18:26 2021

@author: Sojo
"""

n=int(input('enter a number:'))
try:
   if n<90 or n>120:
        raise ValueError('abnormal condition')
except ValueError as ve:
        print(ve)
else:
        print(n,'is within 90 and 120')
            