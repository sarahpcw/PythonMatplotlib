# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:07:23 2021

@author: u
"""
import numpy as np
#Creating arrays
#Method 1 :
#numpy.arange([start, ]stop, [step, ]dtype=None)

x = np.arange(9,19,1)
print (x)

#Returns an array of evenly spaced values within a given interval.
#Method 2 :
#linspaceEvenly spaced numbers with careful handling of endpoints.
x = np.linspace(1,2,9)  #9 numbers  between 0 and 2 
print(x)
x = np.linspace(1,2,9, endpoint=True)  #9 numbers  between 0 and 2 
print(x)
x = np.linspace(33,1203, 9, endpoint=False)  #9 numbers  between 0 and 2 
print(x)



#Method 3 :
myItem = [ [0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14],[15,16,17,18,19]] #p48

#Method 4 :
x = np.array([0, 1, 2])
print (x)

#Examples
