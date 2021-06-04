# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:35:51 2021

@author: u
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
t = pd.Series(np.random.randn(100),index=pd.date_range('1/1/2017',periods=100))
t=t.cumsum()
t.plot()
plt.show()

print('======================')
t = pd.Series(np.random.randn(100),index=pd.date_range('1/1/2017',periods=100))
d=pd.DataFrame(np.random.randn(100,4),index=t.index,columns=list('XYZW'))
d=d.cumsum()
plt.figure()
d.plot()
plt.show()
