# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:20:28 2021

@author: u
"""

#Draw one plot  ( do the 3 separately)
import matplotlib.pyplot as pl
import numpy as np
from pylab import *
# adding a legend
# change the plot size
x = np.linspace(-np.pi,np.pi,256,endpoint=True) #generate 256 numbers between -3.14 and +3.14
cp = np.cos(x)
sp = np.sin(x)
pl.plot(x,cp,color="pink",linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linestyle="-", label="sine")
pl.plot() 				# default size 
#Draw 2 plots vertically
# give me two plots, VERTICAL(1 in the middle)
pl.subplot(2,1,1) 			# top
pl.plot(x,cp,color="pink",linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linestyle="-", label="sine")
pl.plot() 				# default size 
pl.subplot(2,1,2)			# bottom
pl.plot(x,cp,color="blue",linestyle="-", label="cosine")
pl.plot(x,sp,color="green",linestyle="-", label="sine")
pl.plot() 				# default size 

#Draw 2 plots across
#give me two plots, across(2 in the middle), first one of them
pl.subplot(2,2,1) 			# left
pl.plot(x,cp,color="pink",linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linestyle="-", label="sine")
pl.plot() # delfault size 

# give me two plots, across(2 in the middle), first SECOND of them
pl.subplot(2,2,2) 			# right
pl.plot(x,cp,color="pink",linestyle="-", label="cosine")
pl.plot(x,sp,color="blue",linestyle="-", label="sine")
pl.plot() 				# delfault size


#matplotlib is a plotting library for the Python programming language and its numerical 
#mathematics extension NumPy. It provides an object-oriented API for embedding plots into 
#applications using general-purpose GUI toolkits like wxPython, Qt, or GTK+.
# There is also a procedural "pylab" interface based on a state machine (like OpenGL), 
# designed to closely resemble that of MATLAB.
