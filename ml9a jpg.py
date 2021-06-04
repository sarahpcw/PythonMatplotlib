# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:28:39 2021

@author: u
"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
 
y = [2,4,6,8,10,12,14,16,18,20]
x = np.arange(10)
fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.plot(x, y, label='$y = numbers')
plt.title('Legend inside')
ax.legend()
plt.show()
 
fig.savefig('C:/Users/u/testPlot.pdf')
fig.savefig('C:/Users/u/testPlot.png')
fig.savefig('C:/Users/u/testPlot.jpg')
