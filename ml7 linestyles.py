# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:23:25 2021

@author: u
"""

import matplotlib.pyplot as pl
#from pylab import *
import numpy as np
# line styles

x = np.linspace(-np.pi,np.pi,256,endpoint=True) #generate 256 numbers between -3.14 and +3.14
cp = np.cos(x)
pl.figure(figsize=(10,12), dpi=60) 
				

pl.subplot(4,1,1) 			# 4 vertical plots, first one
pl.plot(x,cp,color="pink",linestyle="-", label="cosine")
pl.plot() 				# delfault size 

pl.subplot(4,1,2)			# 4 vertical plots, second one
pl.plot(x,cp,color="blue",linestyle="--", label="cosine")
pl.plot() 				# delfault size 

pl.subplot(4,1,3)			# 4 vertical plots, third one
pl.plot(x,cp,color="blue",linestyle="-.", label="cosine")
pl.plot() 		

pl.subplot(4,1,4)			# 4 vertical plots, fourth one
pl.plot(x,cp,color="blue",linestyle=":", label="cosine")
pl.plot()

