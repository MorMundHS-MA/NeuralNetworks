# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import nnwplot

def neuron(X, W = [-0.3,1], threshold = 2):
    if W == None:
        W = [-0.3,1]
    if threshold == None:
        threshold = 2
    net = np.zeros(X.shape[1])
    for i in range(0, X.shape[1]):
        net[i] = (X[:,i] * W).sum()
    return net > threshold

def stats(result):
    stats = {}
    stats['correct'] = result[:50].sum(where=True)
    stats['false negative'] = 50 - stats['correct']
    stats['false positives'] = result[50:].sum(where=True)
    return stats

data = np.loadtxt(fname='iris.csv', delimiter=',')
X = data[:,0:4].T
T = data[:,4].T

plt.scatter(X[0,:], X[1,:], c=T, cmap=plt.cm.prism)
res = neuron(X[:2,:]) # Few corret detections,no false positives
nnwplot.plotTwoFeatures(X[:2,:] , T ,neuron)
# Variation of Threshold
res1 = neuron(X[:2,:], threshold = 1) # More detections, vastly more false positives
res2 = neuron(X[:2,:], threshold = 3) # No detections
# Variation of Weigths
resA = neuron(X[:2,:], W = [-0.2,1]) # Almost perfect detection for first type, a few false positives
resB = neuron(X[:2,:], W = [-0.1,1]) # Almost everything falsely assigned to 1 type
resC = neuron(X[:2,:], W = [0,1]) # Nearly identical to resultB