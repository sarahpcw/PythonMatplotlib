# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:06:25 2021

@author: u
"""

import numpy as np
import matplotlib.pyplot as pl
x = np.linspace(-np.pi,np.pi,256,endpoint=True) 
#generate 256 numbers between -3.14 and +3.14
print (x)
cp = np.cos(x)
sp = np.sin(x)
pl.plot(x,cp)
pl.plot(x,sp)
#pl.show()


#Change The Colours 
#one of {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', #'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
#purple
#(#7e1e9c)
# 
# 
#green
#(#15b01a)
# 
# 
#blue
#(#0343df)
# 
# 
#pink
#(#ff81c0)
# 
# 
#brown
#(#653700)
# 
# 
#red
#(#e50000)

pl.plot(x,cp,color="#cb416b",linewidth=2.5,linestyle="--") 
# Line Styles  (# -   --  :   Or Space)
pl.plot(x,sp,color="pink",linewidth=4.5,linestyle="-")
pl.show()


#-- https://xkcd.com/color/rgb/

#Change Where The Axes Starts (Axes Cross Each Other ) Ie Not At 0,0 But -1.5,-1.5
#Change Where The Axes Starts (Axes Cross Each Other ) Ie Not At 0,0 But -1.5,-1.5
# It Gives Distance From The Plot To The Axes  (xlim, ylim)
pl.xlim(x.min()*1.5,x.max()*1.5)
pl.ylim(cp.min()*1.5,cp.max()*1.5)
pl.plot(x,cp,color="blue",linewidth=2.5,linestyle="-")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-")
pl.show()

# Ticks: To Show The +/-Pi And  +/-Pi  For Sine And Cosine
pl.xlim(x.min()*1.5,x.max()*1.5)
pl.ylim(cp.min()*1.5,cp.max()*1.5)
pl.xticks([-np.pi,-np.pi/2, 0, np.pi/2, np.pi])  	
# to show the +/-pi and  +/-pi  for sine and cosine
pl.yticks([-1, 0, 1])  				
pl.plot(x,cp,color="blue",linewidth=2.5,linestyle="-")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-")
pl.show()

# To Show The Pi Symbol, Rather Than The Exact Value (xticks, yticks)
pl.xlim(x.min()*1.5,x.max()*1.5)
pl.ylim(cp.min()*1.5,cp.max()*1.5)

# to show the pi symbol
pl.xticks([-np.pi,-np.pi/2, 0, np.pi/2, np.pi]
, [r'$-\pi$' , r'$-\pi/2$' , r'$0$' , r'$+\pi/2$' , r'$+\pi$'])  
pl.yticks([-1, 0, 1] , [r'$-1$',r'$0$',r'$+1$']) 
                       
pl.plot(x,cp,color="blue",linewidth=2.5,linestyle="-")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-")
pl.show()
# Moving The Spines From The Border Of The Plot To The Centre Of The Plot 
#SPINES:  set top and right borders to no colour
#SPINES: move /left/bottom/ borders 

#•	matplotlib.pyplot.gca(**kwargs)[source]¶
#•	Get the current Axes instance on the current figure matching the given keyword args, or create one.

pl.xlim(x.min()*1.5,x.max()*1.5)
pl.ylim(cp.min()*1.5,cp.max()*1.5)
pl.xticks([-np.pi,-np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$']) 
 # to show the pi symbol
pl.yticks([-1, 0, 1], [r'$-1$',r'$0$',r'$+1$']) 

axes = pl.gca()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')

##tick positions
axes.xaxis.set_ticks_position('bottom') 
# puts ticks of x-axis at the axis rather than at the top border
axes.yaxis.set_ticks_position('left') 
# put ticks of y-axis the axis rather than at the right border

#Spine positions
axes.spines['bottom'].set_position(('data',0))
#put the x axis on the centre
axes.spines['left'].set_position(('data',0)) 
#put the y axis on the centre
pl.plot(x,cp,color="blue",linewidth=2.5,linestyle="-")
pl.plot(x,sp,color="red",linewidth=4.5,linestyle="-")
pl.show()


#Axes¶
#This is what you think of as 'a plot', it is the region of the image with the data space. 
#A given figure can contain many Axes, but a given Axes object can only be in one Figure. 
#The Axes contains two (or three in the case of 3D) Axis which take care of the data limits
# (the data limits can also be controlled via set via the set_xlim() and set_ylim()Axes methods). 
#Each Axes has a title (set via set_title()), an x-label (set via set_xlabel()), 
#and a y-label set via set_ylabel()).
#The Axes class and it's member functions are the primary entry point to working with the OO interface
#objects (be aware of the difference between Axes and Axis)
#
#Actually, gca() is not part of numpy, but of matplotlib, which is usually imported together with 
#numpy to do some plots.
#matplotlib.pyplot.gca(**kwargs)[source]¶
#Get the current Axes instance on the current figure matching the given keyword args, or create one. 
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gca.html
# 

