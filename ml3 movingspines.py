# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:19:04 2021
Moving spines and color
@author: u
"""

import numpy as np
import matplotlib.pyplot as pl
# adding a legend
# change the plot size
x = np.linspace(-np.pi,np.pi,256,endpoint=True)  #generate 256 numbers between -3.14 and +3.14
cp = np.cos(x)
sp = np.sin(x)

pl.figure(figsize=(10,6), dpi=60)               		#change the plot size : experiment: dpi= 40, 60, 80 or 100

pl.xlim(x.min()*1.5,x.max()*1.5)
pl.ylim(cp.min()*1.5,cp.max()*1.5)
pl.xticks([-np.pi,-np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])  #show pi 
pl.yticks([-1, 0, 1], [r'$-1$',r'$0$',r'$+1$']) 

axs = pl.gca()
axs.spines['right'].set_color('pink')           	#experiment with red, blue, black, right border
axs.spines['top'].set_color('green')          		#left  border
axs.spines['left'].set_color('blue')            		#this is the y axis
axs.spines['bottom'].set_color('red')       		# this is the x-axis

axs.xaxis.set_ticks_position('bottom')
axs.spines['bottom'].set_position(('data',-0))  	#experiment 0, -1, 1 , 2, -2, move the x axis up and down
axs.yaxis.set_ticks_position('left') 
axs.spines['left'].set_position(('data',0))         	#experiment 0, -1, 1 , 2, -2 move the y axis left andright

pl.plot(x,cp,color="blue",linewidth=2.5,linestyle='-', label="cosine")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-", label="sine")
pl.legend(loc='upper left', frameon=False)

pl.show()
