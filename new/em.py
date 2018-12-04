#!/usr/bin/env python

import numpy as np
import scipy as sp

import seaborn as sbs
import matplotlib.pyplot as plt

# Introduction: Density estimation
# We start by defining a problem in the context of unsupervised learning. Suppose we have 1 dimensional data 


N = 100
mu_arr = np.array([1, 10])
sigma_arr = np.array([1, 1])
x = np.append(np.random.normal(mu_arr[0], sigma_arr[0], N), 
              np.random.normal(mu_arr[1], sigma_arr[1], N))
print(x[:10])
