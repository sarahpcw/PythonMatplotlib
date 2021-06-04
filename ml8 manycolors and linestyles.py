# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:25:33 2021

@author: u
"""

from matplotlib.lines import Line2D  
import matplotlib.pyplot as pl
import numpy as np

colors = ('b', 'g','b', 'g', 'r', 'c', 'm', 'y', 'k','b', 'g', 'r', 'c', 'm', 'y', 'k','b', 'g', 'r', 'c', 'm', 'y', 'k','b', 'g', 'r', 'c', 'm', 'y', 'k')
print ('colors',len(colors))    #there are 30 colors

markerlist = []
for m in Line2D.markers:
    try:
        if len(m) == 1 and m != ' ':
            markerlist.append(m)
    except TypeError:
        pass
markerlist = markerlist + ['.', ',', 'o', 'v', '^',]
print ('markers',len(markerlist),'\n',markerlist)  #there are 25 markers


t = np.arange(0.0, 1.0, 0.1)
counter = 0
print (t)
##change the colours
for s in colors: 
    counter += 1
#    print(counter)
    pl.figure(figsize=(3,3))
    pl.plot(t, color=colors[counter], linewidth=1.5, linestyle=" ", marker=markerlist[counter], markersize=10) 

#stars
pl.figure(figsize=(3,3))
pl.plot(t, color=colors[counter],  linestyle=" ", marker=markerlist[14], markersize=10) 
