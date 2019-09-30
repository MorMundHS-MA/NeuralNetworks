# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(fname='iris.csv', delimiter=',')
X = data[:,0:4].T
T = data[:,4].T

plt.scatter(X[0,:], X[1,:], c=T, cmap=plt.cm.prism)