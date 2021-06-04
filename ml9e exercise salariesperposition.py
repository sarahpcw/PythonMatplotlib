# -*- coding: utf-8 -*-
"""

get a list of salaries per postion
draw 9 plots: 
    plot the salaries per position


"""
import pandas as pd
import matplotlib as pl
import matplotlib.pyplot as plt
path     = 'C:\\Users\\u\\.spyder-py3\\3W-Webinar\\'
filename = path + 'MLBPlayerSalaries.xlsx'
fcsv     = path + 'MLBPlayerSalaries.csv'
df = pd.read_excel(filename)
print (df.columns)
colors = ["brown","orange","red","tan","#ccad60","maroon","olive","#ad900d","orange"]
print ('Unique Positions' , df["Position"].unique() )
positions = df["Position"].unique()
print (positions, len(positions))

### do 9 times : for i in range (len(positions))
for axisNum in range (1, 10, 1):     # 1,2,3,4,5,6,7,8,9    
    df2 = df[  (df['Position'] == positions[0] )  ]  
    data = df2.loc[:,'Salary']
## plot data          		  
    ax = plt.subplot(9, 1, axisNum) 
    plt.plot(data,color=colors[axisNum],linestyle="-", label="cosine")

########
