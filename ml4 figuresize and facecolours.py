# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:19:57 2021

@author: u
"""

import numpy as np
import matplotlib.pyplot as pl
# adding a legend
# change the plot size
x = np.linspace(-np.pi,np.pi,256,endpoint=True) #generate 256 numbers between -3.14 and +3.14
cp = np.cos(x)
sp = np.sin(x)

# change the plot face color to blue
pl.figure(figsize=(10,6), dpi=40, facecolor='blue') 
 # change the plot size : experiment: dpi= 40 or 60 or 80 or 100 9 width, height and dpi
pl.plot(x,cp,color="pink",linewidth=2.5,linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-", label="sine")
pl.legend(loc='upper left', frameon=False)
pl.show()

# change the plot face color to yellow
pl.figure(figsize=(10,6), dpi=40, facecolor='yellow') 
pl.plot(x,cp,color="pink",linewidth=2.5,linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-", label="sine")
pl.legend(loc='upper left', frameon=False)
pl.show()

## change the plot edge color to red
pl.figure(figsize=(10,6), dpi=40, edgecolor='red')  #edgecolor makes no difference
pl.plot(x,cp,color="pink",linewidth=2.5,linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-", label="sine")
pl.legend(loc='upper left', frameon=False)
pl.show()

##framon  & edgecolormakes no difference
pl.figure(figsize=(10,6), dpi=40, edgecolor='red', frameon=False)  
#framon  & edgecolormakes no difference
pl.plot(x,cp,color="pink",linewidth=2.5,linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-", label="sine")
pl.legend(loc='upper left', frameon=True)
pl.show()