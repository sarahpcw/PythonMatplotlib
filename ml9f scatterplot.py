# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:43:26 2021

price_data = (cbook.get_sample_data('goog.npz', np_load=True)['price_data']
              .view(np.recarray))
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#################### create 2 sets of random numbers
data1 = np.linspace(0,2,256)  #256 numbers between 0 and2 
data2 = np.random.rand(256)

####################  create a list of colours
frame = pd.read_csv('C:\\Users\\u\\.spyder-py3\\MatPlotLib\\colors.txt',encoding="ISO-8859-1")
colours = frame[0:256]
cols = np.array (colours.iloc[:])
print(frame.shape)
print (colours)
print(cols)
#################### create a scatter chart from the sample random numbers
fig, ax = plt.subplots()
ax.scatter(data1, data2, c="blue",alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()

#################### import excel data into a dataframe
df1 = pd.read_csv('C:\\Users\\u\\.spyder-py3\\ManchesterFeb\\TradeClients.csv',encoding="ISO-8859-1")

#################### extract the data from the data frame
sumOfCoTurnOver = df1.groupby(["Area"]).sum().loc[:,'Company TurnOver']
rowcount = sumOfCoTurnOver.shape[0]+1

countCoPerArea = df1.groupby(["Area"]).size() 
ycount = countCoPerArea.shape[0]+1

colours = frame[0:19]
cols = np.array (colours.iloc[:])

si = round((countCoPerArea / 10),0) +10  # size per dot ( related to co per area)

#################### print for testing
print(df1.shape)

print(si)

print (cols, len(cols))
print (sumOfCoTurnOver)

print(sumOfCoTurnOver.index.values, len(sumOfCoTurnOver), rowcount)
print ( 'Column names:      ', df1.columns.values)  # print the column names
print (countCoPerArea)
print (ycount)

#################### create the scatter chart
fig, ax = plt.subplots()
ax.scatter(sumOfCoTurnOver, countCoPerArea, s=si, c="blue",alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Company Count per Area vs Company Turnover per Area')

ax.grid(True)
fig.tight_layout()

plt.show()
