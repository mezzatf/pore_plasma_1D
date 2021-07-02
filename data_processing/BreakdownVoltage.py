#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:15:00 2019
@author: M.Ezzat
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k, R
import os
import math

m   = 0.3
S   = np.arange(10,300)
U10 = 220
U   = U10 * (S/10)** m

U20 = U[list(S).index(20)]
plt.plot(S,U)
plt.ylim(250,650)
plt.plot
plt.show()
