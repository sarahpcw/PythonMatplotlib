import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
############### import the excel data into a dataframe
path     = 'C:\\Users\\u\\.spyder-py3\\3W-Webinar\\'
filename = path + 'MLBPlayerSalaries.xlsx'
df = pd.read_excel(filename)

############### extract the data to plot from the dataframe
sumOfSalaries = df.groupby(["Position"]).sum().loc[:,'Salary']
rowcount = sumOfSalaries.shape[0]+1
yAxisLables = df["Position"].unique()
y_ticks = np.arange(1,rowcount,1) # generates a list: 1,2,3,4,5,6,7,8,9

############### print the info ( delete, this is just for testing)
print(y_ticks)
print (df.columns)
print('\nSum all the number columns, by Job Title --------------\n',sumOfSalaries)
print(rowcount)

############### create the bar chart
plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh( y_ticks ,sumOfSalaries,align='center')
ax.set_yticks(y_ticks)
ax.set_yticklabels(yAxisLables)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Sum of Salaries per Position')
ax.set_title('How fast do you want to go today?')

plt.show()