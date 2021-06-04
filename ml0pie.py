# -*- coding: utf-8 -*-
"""
plot pie charts
"""

#################### pie chart with sample data
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

#################### create a pie chart from the MLBPlayers
import matplotlib.pyplot as plt
import pandas as pd
#################### import the excel data to a dataframe
path     = 'C:\\Users\\u\\.spyder-py3\\3W-Webinar\\'
filename = path + 'MLBPlayerSalaries.xlsx'
df = pd.read_excel(filename)
#################### extract the data to plot from the dataframe
labels = df["Position"].unique()
sizes = df.groupby(["Position"]).sum().loc[:,'Salary']
colors = ["brown","orange","red","tan","#ccad60","maroon","olive","#ad900d","orange"]
explode = (0, 0.1, 0, 0,0,0,0,0,0)
####################  print ( testing only, can delete the prints )
print (df.columns)
print (labels, len(labels))
print('\nSum all the number columns, by Job Title --------------\n',sizes)
print(type(sizes))
#################### create the pie chart
plt.figure(figsize=(12,12))
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()