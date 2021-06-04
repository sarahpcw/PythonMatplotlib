# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:33:17 2021

@author: u
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#matplotlib.style.use('ggplot')

df4 = pd.DataFrame(
        {
          'a':np.random.randn(100)+1,
          'b':np.random.randn(100),
          'c':np.random.randn(100)-1,
          'd':np.random.randn(100)-2,                
                }, columns=['a','b','c','d'])

plt.figure()
df4.plot.hist(alpha=0.5)
df4.plot.hist(stacked=True, bins=20)
df4.plot.hist(stacked=True, bins=10)
plt.show()
