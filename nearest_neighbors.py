#! /usr/bin/env python
# -*- coding utf-8 -*-
# author: elsuizo
"""
calculation of nearest neighbors with fancy indexing, element-wise operation, 
A naive approach requires three nested loops 
D_{i,j}^2 = (x_i - x_j)^2 + (y_i - y_j)^2

"""
#*************************************************************************
# imports
#*************************************************************************
import numpy as np
import matplotlib.pyplot as plt
#*************************************************************************
N = 1000
X = np.random.random((N,3)) # N points in three dimensions

# Broadcasting to find pairwise differences

diff = X.reshape(N,1,3) - X

# Agregate to find pairwise distances

D = (diff ** 2 ).sum(2)

# set the diagonal to infinity to skip self-neighbors

i = np.arange(N)
D[i, i] = np.inf

# print the indices of the nearest neighbors

i = np.argmin(D, 1)
print(i[:10])
