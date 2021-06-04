# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:22:54 2021

@author: u
"""

import matplotlib.pyplot as pl
import numpy as np
pl.figure(figsize=(10,12), dpi=80)  # 10 width and 12 height
x = np.linspace(-np.pi,np.pi,256,endpoint=True) #generate 256 numbers between -3.14 and +3.14
cp = np.cos(x)
sp = np.sin(x)

for axisNum in range (1, 10, 1):     # 1,2,3,4,5,6,7,8,9              		  
    ax = pl.subplot(9, 3, axisNum) 
    pl.plot(x,cp,color="pink",linestyle="-", label="cosine")
    pl.plot(x,sp,color="red",linestyle="-", label="sine")

