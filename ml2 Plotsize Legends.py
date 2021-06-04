# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:18:29 2021

@author: u
"""

import numpy as np
import matplotlib.pyplot as pl
# adding a legend
# change the plot size
x = np.linspace(-np.pi,np.pi,256,endpoint=True) 
#generate 256 numbers between -3.14 and +3.14
cp = np.cos(x)
sp = np.sin(x)

# change the plot size : experiment: dpi= 40 or 60 or 80 or 100 9 width, height and dpi
pl.figure(figsize=(6,6), dpi=110)  

pl.xlim(x.min()*1.5,x.max()*1.5)
pl.ylim(cp.min()*1.5,cp.max()*1.5)
pl.xticks([-np.pi,-np.pi/2, 0, np.pi/2, np.pi], 
[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])  		#show pi
pl.yticks([-1, 0, 1], [r'$-1$',r'$0$',r'$+1$']) 

axs = pl.gca()
axs.spines['right'].set_color('none')
axs.spines['top'].set_color('none')

axs.xaxis.set_ticks_position('bottom')
axs.spines['bottom'].set_position(('data',0))	#put the x axis on the centre

axs.yaxis.set_ticks_position('left') 
axs.spines['left'].set_position(('data',0)) 	#put the y axis on the centre

pl.plot(x,cp,color="blue",linewidth=2.5,linestyle="-", label="cosine")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-", label="sine")

#add legend : upper or lower
pl.legend(loc='lower right', frameon=False) 
# frameon is for the frame around legend only

pl.show()
