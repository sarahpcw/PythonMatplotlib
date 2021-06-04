# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:27:31 2021

@author: u
"""

from matplotlib.lines import Line2D  
import matplotlib.pyplot as plt
import numpy as np


# build an array with marker styles
markers = []
for m in Line2D.markers:
    try:
        if len(m) == 1 and m != ' ':
            markers.append(m)
    except TypeError:
        pass
print(markers, len(markers))

# add styles to the end of the markers array , transfer all to styles array
styles = markers + [
r'$\lambda$',
r'$\bowtie$',
r'$\circlearrowleft$',
r'$\clubsuit$',
r'$\checkmark$',
r'$\lambda$',
r'$\bowtie$'  ]

print ('\n',styles, len(styles))

colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
print ('\n',colors, len(colors))
linestyles = ['_', '-', '--', ':']

t = np.arange(0.0, 1.0, 0.1)
s = np.sin(2*np.pi*t)

plt.figure(figsize=(8,8))
# in the loop, creates all the plots, sets the position of the plot and for everyone
#, creates the plot with linestyle and color

for axisNum in range (1,36):                   		  
    ax = plt.subplot(7, 5, axisNum)        	     # identify the position of the plot 
    colour = colors[axisNum % len(colors)]  	     # extracts the next color from the color array
    if axisNum < len(linestyles):                
# chooses the line styles, makes sure there is one, if not then use no linestyle but only a marker
        	plt.plot(t, s, linestyles[axisNum], color=colour, markersize=10) 	#changes linestyle and color
    else:
        	style = styles[(axisNum - len(linestyles)) % len(styles)] #chooses the marker, puts it into style
        	plt.plot(t, s, linestyle='None', marker=style, color=colour, markersize=10)  


######  simplified
linestyles = ['v', ',', 'o', 'v']
styles = styles + linestyles
print (styles , len(styles))
plt.figure(figsize=(8,8))
for axisNum in range (1,36):                   		  
    ax = plt.subplot(7, 5, axisNum)        	     # identify the position of the plot 
    colour = colors[axisNum % len(colors)]  	     # extracts the next color from the color array
    style = styles[(axisNum)] #chooses the marker, puts it into style
    plt.plot(t, s, linestyle='None', marker=style, color=colour, markersize=10)  